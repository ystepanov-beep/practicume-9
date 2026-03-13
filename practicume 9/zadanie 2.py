with open('input1.txt', 'r', encoding = 'utf-8') as inputfile:
    text = inputfile.read()

lines = text.split('\n')

with open('output1.txt', 'w', encoding = 'utf-8') as outputfile:
    for line in lines:
        if line.startswith('A'):
            outputfile.write(line + '\n')
