import os

with open('hebron.txt', 'r') as file:
    contents = file.read()

print(contents)

print(os.getcwd())
