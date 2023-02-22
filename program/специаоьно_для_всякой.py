import pickle 

# user = input("User name: ")
# password = input("Password")

#загружаем словарь из файла 
with open("dump.dat", 'rb') as dump_in:
    base = pickle.load(dump_in)

#base[user] =  password #добавить в словарь 

# if user in base: #проверить наличие логина в словаре 
#     base[user] #взять пароль

# #сохраняем словарь в файл
# with open('dump.dat', 'wb') as dump_out:
#     pickle.dump(base, dump_out)
login = input("Input your account name: ")
if login in base: #проверить наличие логина в словаре
    passw = input("Input your password: ")
    if base[login] == passw:
        print("Well Done. Now u're in your account: ",login )
    else:
        print("Incorrect password")
else:
    print("incorrect login")
    #