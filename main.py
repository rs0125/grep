import sys

def open(file_name):
    try:
        file = open(file_name, "r")
    except:
        print("File doesn't exist")
        quit()
    lines = file.readlines()
    return lines

text = sys.argv[1]
file_name = sys.argv[2]

file_lines = open(file_name)
for i in file_lines:
    if text in i:
        print(i)
