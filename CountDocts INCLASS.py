# Count Doctests
# Prof. O & CPTR-215
# 2023-10-30 first draft--just count functions & doctests

"""
>>> stuff = "stuff"
>>> stuff += "ies"
>>> stuff
'stuffies'
>>> print("one line\nand another")
one line
and another
"""

count_classes = 0
count_definitions = 0
count_doctests = 0
state = "Normal" # other possible values are "Doctest Setup", "Doctest Output"

filename = input("File to open: ")
# equivalent to input_file = open(filename), then input_file.close() after body
with open(filename, "r") as input_file:
    for line in input_file:
        line = line.strip() # remove leading & trailing whitespace (including \n)
        if line.startswith("class "):
            count_classes += 1
        elif line.startswith("def "): # and line.endswith(":"): # doesn't work for "broken" headers
            count_definitions += 1
        elif state == "Normal" and line.startswith(">>> "):
            state = "Doctest Setup"
        elif state == "Doctest Setup" and not line.startswith(">>> "):
            state = "Doctest Output"
            count_doctests += 1
            state = "Normal"
            
print(f"Found {count_classes} class definition(s)")        
print(f"Found {count_definitions} function/method definition(s)")
print(f"Found {count_doctests} doctest(s)")