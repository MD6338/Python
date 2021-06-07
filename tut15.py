# File IO

"""
"r" - Used to read file - default mode
"w" - Used for writing in file
"x" - Used to create file if not exists
"a" - Used for appending content in file 
"t" - Text mode - default mode
"b" - Binary mode
"+" - Read and write
"""

from os import path


f = open("ch.txt")
# co = f.read(6)

# print("haha", co)

# print(co)

# for l in f:
#     print(l)

# print(f.readline())

print(f.readlines())

# print(f.read())
f.close()