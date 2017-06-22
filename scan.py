from os import path, getcwd

def Scan(directory=None):
    """
    Returns a directory tree of the argument directory.
    :param directory: a string defining the top level directory to scan.
    :return: a list
    """

    if directory:
        directory = path.splitdrive(path.expanduser(directory))
    else:
        directory = os.getcwd()

        if path.splitdrive(directory)[0]:
            directory = path.splitdrive(directory)[0]
        else:
            directory = '/'

    return os.walk(directory)
