from os import path

def Scan(directory=''):
    """
    Returns a directory tree of the argument directory.
    :param directory: a string defining the top level directory to scan.
    :return: a list
    """

    if path.splitdrive(path.abspath(directory))[0]:
        print('We\'re on Windows!')
    else:
        print('What? POSIX?')
