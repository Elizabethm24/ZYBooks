# Read binary files
# Prof. O & CPTR-215
# 2023-11-03

with open("SampleFile", "rb") as binary_file:
    contents = binary_file.read()
    print(type(contents))
    for byte in contents:
        print(byte, chr(byte))