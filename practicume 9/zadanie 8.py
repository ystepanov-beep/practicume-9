with open('input.txt', 'r', encoding='utf-8') as inputfile:
    lines = inputfile.readlines()

steps = [int(line.strip()) for line in lines]

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

with open('output.txt', 'w', encoding='utf-8') as outputfile:
    start = 0
    for i in range(12):
        days = days_in_month[i]
        month_steps = steps[start:start + days]
        average = sum(month_steps) / days
        outputfile.write(months[i] + ': ' + str(average) + '\n')
        start += days
