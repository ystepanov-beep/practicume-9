def day_of_year(date):
    day, month = map(int, date.split('.'))
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return sum(days_in_month[:month - 1]) + day


with open('input9.txt', 'r', encoding='utf-8') as inputfile:
    lines = [line.strip() for line in inputfile if line.strip()]

current_date = lines[0]
n = int(lines[1])

current_day = day_of_year(current_date)

with open('output9.txt', 'w', encoding='utf-8') as outputfile:
    for i in range(2, 2 + n):
        cell_number, storage_date = lines[i].split()
        storage_day = day_of_year(storage_date)

        if current_day - storage_day > 3:
            outputfile.write(cell_number + '\n')