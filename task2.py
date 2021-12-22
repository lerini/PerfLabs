data_circle = []
data_points = []
list_points = []
line_count = 0

with open("file1.txt") as file_circle:
    for line in file_circle:
        line = line.replace("\n", "")
        data_circle.append(line)

check_input = False
while check_input is False:
    if len(data_circle) == 2:

        x_0, y_0 = (data_circle[0]).split(' ')
        radius = data_circle[1]

        if x_0.isdigit() is True and y_0.isdigit() is True and radius.isdigit() is True:
            x_0 = int(x_0)
            y_0 = int(y_0)
            radius = int(radius)
            # print(x_0, y_0, radius)
            data_circle.clear()

            data_circle.append(x_0)
            data_circle.append(y_0)
            data_circle.append(radius)
            check_input = True

with open("file2.txt") as file_points:
    for line in file_points:
        line = line.replace("\n", "")
        line_count += 1
        data_points.append(line)

for point in data_points:
    list_points.append(point.split(' '))
# print(list_point)

check_point = False
while check_point is False:
    # print(line_count)
    if 0 < line_count < 100:
        for point in list_points:
            if len(point) == 2:
                if point[0].isdigit() is True and point[1].isdigit() is True:
                    if (int(point[0]) - data_circle[0]) ** 2 + (int(point[1]) - data_circle[1]) ** 2 \
                            < data_circle[2] ** 2:
                        print(1)
                    elif (int(point[0]) - data_circle[0]) ** 2 + (int(point[1]) - data_circle[1]) ** 2 \
                            == data_circle[2] ** 2:
                        print(0)
                    else:
                        print(2)
                    check_point = True
                else:
                    print("Ошибка: параметр не является числом")
            else:
                print("Ошибка: неизвестный параметр")
    else:
        print("Не соблюдено условие: размер файла не подходит")
