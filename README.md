# grep
Python Reconstruction of grep (a popular unix command line utility)

# Features:
## Search Functionality:
Search Keyword: Allows users to search for a specified keyword within a file. The keyword is provided as a command-line argument.

## Additional Options:
Line Count: Includes an option to display the line count of matches. Users can add -l in the command line to activate this feature.
Case Insensitivity: Supports case-insensitive searching. Users can specify -i in the command line to perform case-insensitive searches.

## Robustness:
Exception Handling: Handles file non-existence gracefully. If the specified file does not exist, the program will raise an exception and stop execution.


Usage :
```
python3 main.py text file.txt
```

Perform a case-insensitive search for the keyword "Hello" in the file "helloworld.html" and display line counts:

```
python3 main.py text file.txt
python3 main.py -i -l Hello helloworld.html
```
