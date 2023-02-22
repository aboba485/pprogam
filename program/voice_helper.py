from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
import sys
import webbrowser
import os

#альфия
def listen_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('say:')
        audio = r.listen(source)

    try:
        our_speech = r.recognize_google(audio, language = 'ru')
        print("ВЫ сказали:"+our_speech)
        return our_speech
    except sr.UnknownValueError:
        return "ochibka"
    except sr.RequestError :
        return 'ochibka'
        

    #    elif '' in message:say_message('')     
    #return input('скадите вашу команду: ')
    #input("wads ")

def do_this_command(message):
    message = message.lower()
    if 'вииаааа' in message:
        say_message('daswer')
    
    elif 'привет' in message:
        say_message("привет дорогой")


    elif 'а ты знаешь что такое' in message :
        key = message.split('а ты знаешь что такое')[1]
        print('ваш ключ - ' + key)
        with open("rest.txt", 'r', encoding = 'utf-8') as f:
            for line in f.readlines():
                try:
                    if key in line.split('это')[0]:
                        say_message(line.split('это')[1])
                        break
                except:
                    pass

    elif 'запоминай' in message:
        say_message("Слушаю")
        do_this_command.zapom = True
    elif do_this_command.zapom:
        with open("rest.txt",'a',encoding = 'utf-8') as f:
            f.write('\n' + command)
        do_this_command.zapom = False
        say_message("запомнила")

    

    elif 'когда у меня день рождения' in message:
        say_message('лучший день в году для всего мира 30 декабря!!')     



    elif 'хочу послушать музыку' in message:
        say_message("какую?")
        do_this_command.music = True
        


    elif 'рок' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=-qEla3eow3c")
        do_this_command.music = False
        say_message('наслаждайтесь')

        
    elif 'металик' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=yYnHa1G9_Xc")
        do_this_command.music = False
        say_message('наслаждайтесь')
     

            
    elif 'блюз' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=SH3KlDlqu_k")
        do_this_command.music = False
        say_message('наслаждайся')

            
    elif 'джаз' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=u2EQduP24GE")
        do_this_command.music = False
        say_message('наслаждайтесь')

    elif 'моя любимая' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=67R_uPGIw08")
        do_this_command.music = False
        say_message('наслаждайтесь')

            
    elif 'электронная музыка' in message and do_this_command.music:
        webbrowser.open("https://www.youtube.com/watch?v=-ObdvMkCKws")
        do_this_command.music = False
        say_message('наслаждайтесь')

            
    elif 'как дела' in message:
        say_message('Хорошо, а у вас как?')


        do_this_command.flag = True


    elif 'хорошо' in message and do_this_command.flag:
        say_message ("я очень этому рада!")


        do_this_command.flag = False


    elif 'плохо' in message and do_this_command.flag:
        say_message('Очень, жаль... Думаю следующий день будет лучше!')

        
        do_this_command.flag = False


    elif 'нормально' in message and do_this_command.flag:
        say_message("Не плохо и не хорошо, завтра будет очень круто!")

            
        do_this_command.flag = False


    elif 'пока' in message:
        say_message("пока пока")
        sys.exit()


    elif 'дура' in message :
        say_message("Ай, как неприлично")



    else:
        say_message("Я вас не расслышала, повторите пожалуйcта еще раз")

glebflag = False
do_this_command.flag = False
do_this_command.zapom = False
do_this_command.music = False
def say_message(message):
    voice = gTTS(message, lang='ru')
    file_voice_name = '_audio' + str(time.time()) + '_' + str(random.randint(0, 1000000000))+ '.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
   # print('Голосовой ассистент:' + message)


if __name__ == '__main__':
    while True:
        command = listen_command()
        do_this_command(command)
