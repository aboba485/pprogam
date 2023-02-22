maxch=input("Введите максимальную длину заголовка: ")
maxch=int(maxch)
zagolovki=input('число заголовков: ')
zagolovki=int(zagolovki)
for i in range(zagolovki):
    zagolovok=input('введите заголовок: ')
    dlinaz=len(zagolovok)
    dlinaz=dlinaz+3
    if dlinaz<=maxch:
        print(zagolovok)
    else:
        maxch=maxch-3
        print(zagolovok[0:maxch]+'...')
