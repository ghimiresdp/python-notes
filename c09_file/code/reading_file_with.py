# FIXME: please use this path if you run this script from current directory
# file_name = "file_1.txt"

# ! Please create a new file named `file1.txt` in this directory to open the file

# Please use this path if you run this script fromthe project directory
file_name = "c09_file/code/file1.txt"

# ------------------------------------------------------------------------------
# reading line by line

with open(file_name, "r") as file:
    line = 0
    while content := (file.readline()).strip():
        print(f"{line:>3} | {content}")
        line += 1
    print(content)

    # ? output:
    #   0 | This is Line 1
    #   1 | This is Line 2
    #   2 | This is Line 3

    # closing the file is not necessary when using `with` statement
    # file.close()
