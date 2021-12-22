
massive = []
path_massive = []
result = ''


def make_interval():
    for j in range(params[1]):
        if j == params[1] - 1:
            path_massive.append(massive[0])
        else:
            path_massive.append(massive[0])
            massive.append(massive[0])
            massive.remove(massive[0])


check_input = False
while check_input is False:
    params = input()
    params = list(params.split(" "))
    if len(params) == 2:
        if params[0].isdigit() is True and params[1].isdigit() is True:

            params[0] = int(params[0])
            params[1] = int(params[1])
            if params[0] > 0 and params[1] > 0:

                for i in range(1, params[0] + 1):
                    massive.append(i)

                key_number = massive[0]
                make_interval()
                result += str(path_massive[0])

                while key_number != path_massive[len(path_massive)-1]:
                    path_massive.clear()
                    make_interval()
                    result += str(path_massive[0])

                check_input = True

            else:
                print("Невозможно сделать массив и обход, введите параметры заново")

        else:
            print("Входные данные не являются числом, введите параметры заново")
    else:
        print("Параметров меньше 2 или больше, введите параметры заново")

print(result)
