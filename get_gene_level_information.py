"""
This module provides functions to find
and print tissue expression data for a given gene in a given host.

Example usage:

usage: get_gene_level_information.py [-h] [--host HOST] [-g GENE]

The module provides five functions:

* `update_host_name(host_name)`: This function updates the host name
                                 by replacing underscores with spaces.
* `_print_directories_for_hosts()`: This function prints a list of available hosts
                                   by scientific name.
* `_print_host_list(host_keywords, name_type)`: This function prints a list of available hosts
                                                by common name.
* `get_data_for_gene_file(file_path)`: This function extracts tissue expression data
                                       from a gene file.
* `print_host_to_gene_name_output(host, gene, tissues)`: This function prints the list of tissues
                                                          that the gene is expressed in.

"""
import re
import sys
import argparse
from assignment5.config \
    import get_keywords_for_hosts, get_directory_for_unigene, get_extension_for_unigene
from assignment5.io_utils import get_filehandle, is_gene_file_valid


def main():
    """
    Main function that orchestrates the processing of a gene file for a given host and gene.
    """
    host = ARGS.host
    gene = ARGS.gene

    # Function 1: Update host name
    host_name = update_host_name(host)

    # Construct file path
    file_path = "/".join(
        (get_directory_for_unigene(), host_name, gene + "." + get_extension_for_unigene()))

    # Function 2: Check if gene file is valid
    if is_gene_file_valid(file_path):
        host_name = host_name.replace('_', ' ')
        print(f"\nFound Gene {gene} for {host_name}")
        # Function 4: Get data for gene file
        tissues = get_data_for_gene_file(file_path)
        # Function 5: Print tissue expression data
        print_host_to_gene_name_output(host_name, gene, tissues)
    else:
        print("Not found")
        print(f"Gene {gene} does not exist for {host_name}. Exiting now...", file=sys.stderr)
        sys.exit(1)


def update_host_name(host_name):
    """
    updates the provided host name to its corresponding scientific name.

    """
    host_keywords = get_keywords_for_hosts()

    # Check if the provided host name exists in the mapping
    scientific_name = host_keywords.get(host_name.lower())

    if scientific_name is None:
        # If the host does not exist, print available directories and exit
        _print_directories_for_hosts()
        sys.exit(1)

    return scientific_name


def _print_directories_for_hosts():
    """
    Prints available host names and exits the program.
    """
    host_keywords = get_keywords_for_hosts()

    print("\nEither the Host Name you are searching for is not in the database\n")
    print("or If you are trying to use the scientific name please put the name in double quotes:\n")
    print("\"Scientific name\"\n")
    print("Here is a (non-case sensitive) list of available Hosts by scientific name\n")

    # Print the unique scientific names
    scientific_names = sorted(set(value for value in host_keywords.values()))

    for i, scientific_name in enumerate(sorted(scientific_names), start=1):
        print(f"  {i}. {scientific_name}")

    print("\nHere is a (non-case sensitive) list of available Hosts by common name\n")

    _print_host_list(host_keywords, "common_name")

    print("\n")
    sys.exit(1)


def _print_host_list(host_keywords, name_type):
    """
    Prints available host names and exits the program.
    """
    if name_type == "scientific_name":
        # Print only scientific names
        scientific_names_to_print =\
            sorted(set(value.capitalize() for value in host_keywords().values()))
        for i, scientific_name in enumerate(scientific_names_to_print, start=1):
            print(f"  {i}. {scientific_name}")
    elif name_type == "common_name":
        # Print common names excluding "Homo sapiens"
        common_names = sorted([common_name for common_name in host_keywords
                               if common_name.lower() != "homo_sapiens"])
        for i, common_name in enumerate(common_names, start=1):
            if i <= 9:
                print(f"  {i}. {common_name.capitalize()}")
            else:
                print(f" {i}. {common_name.capitalize()}")


def get_data_for_gene_file(file_path):
    """
    Extracts tissue expression data for a gene file

    """
    # Initialize an empty list to store tissues
    tissues = []

    # Open the gene file and read line by line
    with get_filehandle(file_path, 'r') as file:
        for line in file:
            # Use a regular expression to extract tissue expression data
            match = re.search(r'EXPRESS\s+(.*)', line)
            if match:
                tissue_string = match.group(1)
                # Split the string into a list of tissues
                tissues = [t.strip().capitalize() for t in tissue_string.split('|')]

    # Remove any empty strings from the list
    tissues = list(filter(None, tissues))

    # Sort the list of tissues alphabetically
    tissues.sort()

    return tissues


def print_host_to_gene_name_output(host, gene, tissues):
    """
    This function prints the list of tissues that the gene is expressed in

    It takes 3 arguments

    """

    # Check the count of tissues
    tissues_count = len(tissues)
    host = host.replace('_', ' ')

    print(f"In {host}, There are {tissues_count} tissues that {gene} is expressed in:\n")

    # Print the list of tissues
    for i, tissue in enumerate(tissues, start=1):
        if i <= 9:
            print(f"  {i}. {tissue}")
        else:
            print(f" {i}. {tissue}")


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Give the Host and Gene name')

    PARSER.add_argument('--host', dest='host',
                        help='Name of Host', required=False, default='Human')

    PARSER.add_argument('-g', '--gene', dest='gene',
                        help='Name of Gene', required=False, default='TGM1')

    ARGS = PARSER.parse_args()
    main()
