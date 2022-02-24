import os


def parent_directory():
    # Create a relative path to the parent
    cwd = os.getcwd()
    parent = os.path.dirname(cwd)
    os.chdir(parent)
    # of the current working directory
    relative_parent = os.path.join(parent, '/')

    # Return the absolute path of the parent directory
    return os.path.abspath(relative_parent)


print(parent_directory())
