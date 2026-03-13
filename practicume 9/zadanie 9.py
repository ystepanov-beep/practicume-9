import os

with open('input8.txt', 'r', encoding='utf-8') as inputfile:
    lines = inputfile.readlines()

os.makedirs('simple', exist_ok=True)

with open('simple/output8.txt', 'w', encoding='utf-8') as outputfile:
    start = 0
    for line in lines:
        start += 1
        if start % 2 == 0:
            outputfile.write(line)
