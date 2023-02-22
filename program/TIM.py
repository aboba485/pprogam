import random
#==============================================================================
def greater_RSP(L, R):
    return L + R in ('RS','SP','PR')
#==============================================================================
while True:
    while True:
        user = input('Эна-бена-цо! (R,S,P): ')
        if user in ('R','S','P'):
            break
    print(f'Ваш ход        - {"камень" if user == "R" else "ножницы" if user == "S" else "бумага"}.')
    comp = 'RSP'[random.randint(0,2)]
    print(f'Ход компьютера - {"камень" if comp == "R" else "ножницы" if comp == "S" else "бумага"}.')
    if greater_RSP( user, comp ):
        print('Вы победили!')
    elif greater_RSP( comp, user ):
        print('Победил искусственный интеллект!')
    else:
        print('Ничья!')
    cont = input('Для продолжения игры введите любой символ, для выхода - просто нажмите Enter: ')
    if not cont:
        print('До следующей игры!')
        break
    print()          

