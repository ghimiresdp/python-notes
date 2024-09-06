# FIXME: please use this path if you run this script from current directory
# file_name = "file_1.txt"

"""
Please create a new file named `file1.txt` in this directory with content
as follows:

c09_file/code/file1.txt

This is Line 1
This is Line 2
This is Line 3

"""

# Please use this path if you run this script from the project directory
file_name = "c09_file/code/file1.txt"

# ------------------------------------------------------------------------------
# opening the file in append mode
# using with statement
with open(file_name, "a") as file:
    file.write("This is Line 4")

"""
After executing this script, you should be able to see the appended content in
the file which will look like below:

This is Line 1
This is Line 2
This is Line 3
This is Line 4

"""
