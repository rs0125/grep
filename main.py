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

def search(text, file_lines):
    for i in file_lines:
        temp = []
        line_count = 0

        #case sensitiveity via usage of '-i' in CL argument
        if "-i" in sys.argv:
            if text.lower() in i.lower():
                temp.append(i)
                line_count += 1
        else:
            if text in i:
                temp.append(i)
                line_count += 1

        return (temp, line_count)


#text to be searched and file name taken as input from the command line arg
text = sys.argv[-2]
file_name = sys.argv[-1]
file_lines = open(file_name) 

file_stats = search(text, file_lines)

if "-l" in sys.argv:
    print(f"line count of matches: {file_stats[1]}")
else:
    for i in file_stats[0]:
        print(f"{i} at line {file_lines.index(i)}")
