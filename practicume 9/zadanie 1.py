with open('input.txt', 'r', encoding = 'utf-8') as inputfile:
    text = inputfile.read()

with open('output.txt', 'w', encoding = 'utf-8') as outputfile:
    outputfile.write(text.upper())
