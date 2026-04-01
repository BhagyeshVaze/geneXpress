"""

This module provides utility functions related to Unigene data,
 directory paths, host keywords, and error messages.

Functions:
- get_directory_for_unigene(): Returns the directory path
                               for storing Unigene data files.
- get_extension_for_unigene(): Returns the file extension
                               for Unigene data files.
- get_keywords_for_hosts(): Returns a dictionary mapping
                            common host keywords to their standardized names.
- get_error_string_4_exception_type(exception_type): Returns an error string
                                                    for a given exception type.
"""

_DIRECTORY_FOR_UNIGENE = "C:/Users/coco/PycharmProjects/2" \
                         "/assignment5/assignment5_data"
_FILE_ENDING_FOR_UNIGENE = "unigene"


def get_directory_for_unigene():
    """
    Returns the directory path for storing Unigene data files.
    """
    return _DIRECTORY_FOR_UNIGENE


def get_extension_for_unigene():
    """
        Returns the file extension for Unigene data files.
    """
    return _FILE_ENDING_FOR_UNIGENE


def get_keywords_for_hosts():
    """

    Returns a dictionary mapping common host keywords
    to their standardized names.


    """
    bos_taurus = "Bos_taurus"
    homo_sapiens = "Homo_sapiens"
    equus_caballus = "Equus_caballus"
    mus_musculus = "Mus_musculus"
    ovis_aries = "Ovis_aries"
    rattus_norvegicus = "Rattus_norvegicus"

    host_keywords = {
        "bos taurus": bos_taurus,
        "cow": bos_taurus,
        "cows": bos_taurus,
        "homo_sapiens": homo_sapiens,
        "homo sapiens": homo_sapiens,
        "human": homo_sapiens,
        "humans": homo_sapiens,
        "equus caballus": equus_caballus,
        "horse": equus_caballus,
        "horses": equus_caballus,
        "mus musculus": mus_musculus,
        "mouse": mus_musculus,
        "mice": mus_musculus,
        "ovis aries": ovis_aries,
        "sheep": ovis_aries,
        "sheeps": ovis_aries,
        "rattus norvegicus": rattus_norvegicus,
        "rat": rattus_norvegicus,
        "rats": rattus_norvegicus,

        # Add more mappings as needed
    }

    return host_keywords


def get_error_string_4_exception_type(exception_type):
    """
        Returns an error string for a given exception type.

    """

    return f"Error: {exception_type} occurred." \
           f" Please check your code and try again."
