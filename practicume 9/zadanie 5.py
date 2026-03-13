with open('input4.txt', 'r', encoding = 'utf-8') as inputfile:
     text = inputfile.read()

number = text.split('\n')

a = int(number[0])
b = int(number[1])
c = int(number[2])

result = (a / b) + c

with open('output4.txt', 'w', encoding = 'utf-8') as outputfile:
    try:
        outputfile.write(str(result))
    except ValueError:
        outputfile.write('data error')
    except ZeroDivisionError:
        outputfile.write('division by 0')
