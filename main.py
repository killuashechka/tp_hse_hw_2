import func

name_file = input("Введите название файла: ")
f = open(name_file)
line = f.readline()
numbers = list(map(int,line.split()))
action = "1"
while action != "0":
    print("Что вы хотите сделать?")
    print("1 - Найти минимум")
    print("2 - Найти максимум")
    print("3 - Найти сумму всех числел")
    print("4 - Найти произведение всех числел")
    print("0 - Выход")
    action = input("Выберете действие: ")
    if action == "1":
        print("Минимальное число: " + str(func.Arithmetic._min(numbers)))
    elif action == "2":
        print("Максимальное число: " + str(func.Arithmetic._max(numbers)))
    elif action == "3":
        print("Сумма чисел: " + str(func.Arithmetic._sum(numbers)))
    elif action == "4":
        print("Произведение чисел: " + str(func.Arithmetic._mult(numbers)))
    elif action == "0":
        break
    else:
        print("Неизвестная команда")