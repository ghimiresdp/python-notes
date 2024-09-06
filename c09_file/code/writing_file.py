# FIXME: please use this path if you run this script from current directory
# file_name = "file_1.txt"

# ! Please create a new file named `file1.txt` in this directory to open the file

# Please use this path if you run this script from the project directory
file_name = "c09_file/code/file2.txt"
binary_file_name = "c09_file/code/binary_file.txt"

content = """This is a content to the written file.
- This is a point 1
- This is a point 2
"""

binary_content = (
    """{
    "name": "Tony Stark 🙂",
    "affiliation": "Avengers",
    "age": 40,
}
"""
).encode("utf-8")

# ------------------------------------------------------------------------------
# opening the file in writing mode
file = open(file_name, "w")

file.write(content)

# we need to close the file once we don't need anymore
file.close()

# ------------------------------------------------------------------------------
# using with statement
with open(file_name, "w") as file:
    file.write(content)

# ------------------------------------------------------------------------------
# writing a binary file
with open(binary_file_name, "wb") as file:
    file.write(binary_content)
