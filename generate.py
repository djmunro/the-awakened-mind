'''
Step 1 - Read
Listing files in a directory, reading files and writing files are most
likely part of the standard library of any high level language - at least I am not aware of one
that does not provide those functions, please correct me if I am wrong.


This step is actually pretty simple - read all files in an directory,
read the file and add it to the SITE directory with the filename, which we will later use as URL,
and its content as value.

Lines: 19 to 23

Do It Yourself
Right now you have to make sure the filename is URL friendly.
Add a function which takes a string as input and returns an URL friendly version of it.
Replacing spaces with dashes and cut of file extensions, for example.
'''
import os


def get_all_file_paths(directory):
    file_names = os.listdir(os.path.join(os.path.dirname(__file__), directory))
    return [os.path.join(directory, file) for file in file_names]


def read_all_posts(directory):
    files = get_all_file_paths(directory)
    content = read_file_content(file)
    return content


def read_file_content(file):
    with open(file, u'r') as file:
        text = file.read()
    return text