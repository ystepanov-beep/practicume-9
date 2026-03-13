with open('input3.txt', 'r', encoding = 'utf-8') as inputfile:
    lines = inputfile.readlines()

with open('output3.txt', 'w', encoding = 'utf-8') as outputfile:
    for line in lines:
        if len(line.strip()) > 20:
            outputfile.write(line)
