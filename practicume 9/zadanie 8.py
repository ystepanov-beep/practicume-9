DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

with open('input7.txt', 'r', encoding='utf-8') as inputfile:
    lines = inputfile.readlines()

steps = [int(line.strip()) for line in lines]

with open('output7.txt', 'w', encoding='utf-8') as outputfile:
    start = 0
    for i in range(12):
        days = DAYS_IN_MONTH[i]
        month_steps = steps[start:start + days]
        average = sum(month_steps) / days
        outputfile.write(MONTHS[i] + ': ' + str(average) + '\n')
        start += days
