import re

"""
Turns all snake_case variables and function names into camelCase, but excludes CONSTANT_VARIABLES.
"""

snake_file = input("What is the file name to read from? ")
camelFile = input("What is the file name to write to? ")

snake_case = open(snake_file)
camelCase = open(camelFile, "w")
for line in snake_case:
    match = re.search(r"_([a-z])", line)
    while match:
        line = line[:match.start()] + match.group(1).upper() + line[match.end():]
        match = re.search(r"_([a-z])", line)
    camelCase.write(line)
snake_case.close()
camelCase.close()
