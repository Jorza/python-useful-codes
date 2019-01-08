"""
Finds the percentage of a code that is comments or documentation.
Must have code saved as a .txt file
"""

comment_chars = "/#*"
total_count = 0
empty_count = 0
comment_count = 0
code_count = 0

file_name = input("What is the file name? ")

code_file = open(file_name)
for line in code_file:
    total_count += 1
    if line == "" or line == "\n":
        empty_count += 1
        continue
    while line[0] == "\t" or line[0] == " ":
        line = line[1:]
    if line[0] in comment_chars:
        comment_count += 1
    else:
        code_count += 1

code_percent = round(code_count / total_count * 100)
comment_percent = round(comment_count / total_count * 100)
empty_percent = round(empty_count / total_count * 100)

out_string = "\n" + str(code_percent) + "% of the file is code.\n" + str(comment_percent) + \
             "% of the file is comments and documentation.\n" + str(empty_percent) + "% of the file is blank lines.\n"\
             + "\nThe file is " + str(total_count) + " lines long."
print(out_string)
