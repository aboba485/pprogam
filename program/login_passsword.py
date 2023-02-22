import pickle 

base = {"Arseniy": "password123"} #так храним


#загружаем словарь из файла 
with open("dump.dat", 'rb') as dump_in:
    base = pickle.load(dump_in)  

base["Maxim"] =  '123123' #добавить в словарь 

if 'Arseniy' in base: #проверить наличие логина в словаре 
    base["Arseniy"] #взять пароль

#сохраняем словарь в файл
with open('dump.dat', 'wb') as dump_out:
    pickle.dump(base, dump_out)


