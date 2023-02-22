height = float(input("Введите свой рост в сантиметрах: "))
weight = float(input("Введите свой вес в кг: "))

height = height / 100
BMI = weight / (height * height)
print("Ваш индекс массы тела равен: ", BMI)

if BMI > 0:
    if BMI <= 16:
        print("У Вас сильный недостаток веса")
    elif BMI <= 18.5:
        print("У Вас недостаток веса")
    elif BMI <= 25:
        print("Вы здоровы")
    elif BMI <= 30:
        print("У Вас избыточный вес")
    else:
        print("У Вас серьезный избыточный вес")
else:
    print("Введены некорректные данные")