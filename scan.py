import os

def Scan(directory=None):
    """
    Returns a directory tree of the argument directory.
    :param directory: a string defining the top level directory to scan.
    :return: a list
    """

    if directory:
        directory = os.path.splitdrive(os.path.expanduser(directory))
    else:
        directory = os.getcwd()

        if os.path.splitdrive(directory)[0]:
            directory = os.path.splitdrive(directory)[0]
        else:
            directory = '/'

    return os.walk(directory)
