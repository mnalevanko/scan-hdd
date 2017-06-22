import os

def Scan(directory=None):
    """
    Returns a directory tree of the argument directory.
    :param directory: a string defining the top level directory to scan.
    :return: a list
    """

    if not directory:
        directory = os.getcwd()
    else:
        directory = os.path.abspath(os.path.expanduser(directory))
        if os.path.splitdrive(directory)[0]:
            directory = os.path.splitdrive(directory)[0]
        else:
            directory = '/'

    return os.walk(directory)

for _ in Scan('/home/gg/'):
    print(_)
