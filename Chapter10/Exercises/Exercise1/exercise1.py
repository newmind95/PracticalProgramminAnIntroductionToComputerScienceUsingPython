import os

"""
Write a program that makes a backup of a file. Your program should
prompt the user for the name of the file to copy and then write a new file
with the same contents but with .bak as the file extension.
"""

# Prompt the user for the name of the file to copy
input_file = input("Enter the name of the file to copy: ")

# Write a new file with the same contents but with .bak
os.rename(os.path.realpath(input_file), os.path.realpath(input_file) + ".bak")

f = open(os.path.realpath(input_file), "w")
f.write("First exercise done!")
f.close()
