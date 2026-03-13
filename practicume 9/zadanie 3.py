with open('input2.txt', 'r', encoding = 'utf-8') as inputfile:
    lines = inputfile.readlines()

result = ''

for line in lines:
    if line != '\n':
        result += line[0]

with open('output2.txt', 'w', encoding='utf-8') as outputfile:
    outputfile.write(result)
