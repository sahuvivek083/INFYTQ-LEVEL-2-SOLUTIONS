"""
Write a python function that creates a new text file in which all the lines from the original
text file are present and numbered from 1 to n
(where n is the number of lines in the file).
"""
#PF-Tryout
def number_lines(file_p
    with open(file_path, "r") as f:
        contents = f.readlines()

    with open("to_file.txt", "w") as f:
        for i in range(len(contents)):
            f.write(str(i + 1) + " " + contents[i])

file_path = "solution-21.py"
number_lines(file_path)
