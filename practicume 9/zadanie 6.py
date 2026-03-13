with open('input5.txt', 'r', encoding='utf-8') as inputfile:
    lines = inputfile.read().split('\n')

n = int(lines[0])
count = len(lines) - 1

with open('output5.txt', 'w', encoding='utf-8') as outputfile:
    try:
        if n == count:
            outputfile.write('YES')
        else:
            outputfile.write('NO')
    except ValueError:
        outputfile.write('ERROR')
