import telebot
import random
bot = telebot.TeleBot('5642136702:AAH8PnJaJE4AB1d_kv7f_iGLZ-hCX7zAJr4')

words = ("школа",'ручка','пенал','мяч','время','дата','число','планета','язык','игра','джойстик','наушники','вода','бутылка','лампа','крокодил','ноутбук','экран','мальчик','девочка','освещение','материал')
letters = []

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Это старая, но всемилюбимая игра - виселица(Сначала надо выбрать, кто станет Палачом,"
                     "а кто сыграет роль Висельника. Затем Палач придумывает слово из 5 или более букв, а Висельник начинает загадывать разные буквы."
                     "Если буква есть в данном слове, Палач ставит ее в пробел в том месте, где она должна быть, а если буквы там нет, он начинает рисовать виселицу). Чтобы начать играть введите команду '/play'")


@bot.message_handler(commands=['play'])
def send_welcome(message):
    global word
    letters.clear()
    bot.send_message(message.chat.id, " Я загадал слово!")
    word=random.choice(words)
    bot.send_message(message.chat.id, len(word)*'X')

#bir
@bot.message_handler(content_types=['text'])
def send_text(message):
    letter = message.text.lower()
    letters.append(letter)
    vis_word = ""
    for i in word:
        if i in letters:
            vis_word += i
        else:
            vis_word += "*"
    bot.send_message(message.chat.id, vis_word)
    



bot.polling()
