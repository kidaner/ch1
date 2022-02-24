import os


def create_python_script(filename):

    comments = "# Start of a new Python program"

    with open(filename, "w") as newscript:
        newscript.write(comments)

    with open(filename, "r"):
        filesize = os.path.getsize(filename)
    return(filesize)


print(create_python_script("program.py"))
