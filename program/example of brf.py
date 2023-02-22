import random
character = "123456789qwertyuiop[]asdfghjklzxcvbnm,."
character_list = list(character)
password = input("Enter your password: ")
guess=""
while (guess != password):

    guess = random.choices(character_list,k=len(password))
    print(guess)
    guess = "".join(guess)
print("your pasword is " + guess)
#-prikjvskm aw