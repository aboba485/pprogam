billet = input("Введите ваш бт: ")
dlina_bileta = len(billet)
dlina_bileta = int(dlina_bileta)
nomer_chicla = 0
chet = 0
nechet = 0
for i in billet:
    nomer_chicla+=1
    i = int(i)
    nomer=nomer_chicla//2
    if nomer<nomer_chicla:
        chet = i
    else:
        nechet += i
if nechet == chet:
    print("Это питерский бт")
elif nechet!=chet:
    print("Это не питерский бт")