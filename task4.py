list_data = []

with open('data.txt') as data_file:
    for line in data_file:
        line = line.replace("\n", "")
        if line.isdigit() is True:
            line = int(line)
            list_data.append(line)

sum_data = sum(list_data)

a = sum_data / len(list_data)

if str(a)[-1] == '5':
    a -= 0.5
a = round(a)

i = 0
for number in list_data:
    while number > a:
        number = number - 1
        i += 1
    while number < a:
        number = number + 1
        i += 1
print(i)
