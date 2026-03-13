with open('input6.txt', 'r', encoding='utf-8') as inputfile:
    lines = inputfile.readlines()

result = [line for line in lines if line.strip() != '100']

with open('output6.txt', 'w', encoding='utf-8') as outputfile:
    outputfile.write(''.join(result))
