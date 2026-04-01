"""

This module provides utility functions for gene files.

Functions:
- is_gene_file_valid(file_name): Check if a specified file exists.
- get_filehandle(file, mode): Open a file and return its file handle.


"""


import sys
import os


def is_gene_file_valid(file_name):
    """
    This function checks if the path specified exists or not
    """
    return os.path.exists(file_name)


def get_filehandle(file=None, mode=None):
    """

    Takes : 2 arguments file name and mode
    This function opens the file based on the mode passed in
    the argument and returns filehandle.

    """

    try:
        fobj = open(file, mode)
        return fobj
    except OSError:
        print(f"Could not open the file: {file}"
              f" for type '{mode}'", file=sys.stderr)
        raise
    except ValueError:
        print(f"Could not open the file: {file}"
              f" for type '{mode}'", file=sys.stderr)
        raise


if __name__ == '__main__':
    # You can keep the code here for execution if needed
    pass
