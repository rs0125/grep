import sys
import re

def open(file_name):
    #opens file, ends the program if the file does not exist
    try:
        file = open(file_name, "r")
    except:
        print("File doesn't exist")
        quit()
    lines = file.readlines()
    #content of file dumped in different lines
    return lines

text = sys.argv[-2]
file_name = sys.argv[-1]
file_lines = open(file_name) 

for i in file_lines:
    if sys.argv[-3] == "-i":
        if text.lower() in i.lower():
            print(f"{i} at line {file_lines.index(i)}")
    else:
        if text in i:
            print(f"{i} at line {file_lines.index(i)}")
