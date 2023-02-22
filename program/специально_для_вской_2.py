stroka = input("Введи строку: ")
slova = len(stroka)
if slova%2==0:
    razdelitel = slova//2
    first_part = stroka[0:razdelitel]
    second_part = stroka[razdelitel:]
    print(second_part,first_part)
else:
    razdelitel = slova//2+1
    first_part = stroka[0:razdelitel-1]
    second_part = stroka[razdelitel-1:]
    print(second_part+first_part)