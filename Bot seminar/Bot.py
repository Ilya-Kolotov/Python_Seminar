import telebot
from telebot import types
import datetime
import random
bot = telebot.TeleBot("5839553872:AAFi3Z5o1w-LMX3nJzUug3P-5-1X2xgaSwY")


@bot.message_handler(commands = ["start"])
def start(message):
    bot.send_message(message.chat.id,"Привет! Это Игра с конфетами.\n\
Условия игры следующие:\n\
1) На столе лежит 221 конфета. Вы играете против Меня. Ходите поочередно.\n\
2) Первый ход определяется жеребьёвкой.\n\
3) За один ход можно забрать не более чем 28 конфет, но не меньше 1.\n\
4) Все конфеты оппонента достаются сделавшему последний ход.\n\
Если условия понятны, то для начала игры, напишите команду: /go")


@bot.message_handler(commands = ["go"])
def button(message):
    bot.send_message(message.chat.id,"Начнём игру!")
    player_number = random.randint(1, 2)
    if player_number == 1:
        bot.send_message(message.chat.id,"Первым ходит компьютер.")
    else:
        bot.send_message(message.chat.id,"Первым ходите Вы!")
    start = 221
    count = 0

    while start > 28:
        count += 1
        bot.send_message(message.chat.id,f'{count} ход. На столе сейчас лежит {start} конфет(а).')

        if player_number == 1:
            candies = random.randint(1, 28)
            start -= candies
            bot.send_message(message.chat.id,f'Компьютер взял {candies} конфет(ы).')
            player_number=2

        else:

            user_input = input('Сколько конфет Вы возьмете со стола: ')
            while not user_input.isdigit():
                print(f'{user_input} - не число! Попробуйте снова.')
                user_input = input('Сколько конфет Вы возьмете со стола: ')
            while int(user_input) < 1 or int(user_input) > 28:
                print(f'Вы должны взять хотя бы 1 конфету, но не больше 28. Попробуйте снова.')
                user_input = input('Сколько конфет Вы возьмете со стола: ')
                while not user_input.isdigit():
                    print(f'{user_input} - не число! Попробуйте снова.')
                    user_input = input('Сколько конфет Вы возьмете со стола: ')
            user_input = int(user_input)
            start -= user_input
            player_number = 1

        while start > 0:
            count += 1
            print(f'{count} ход. На столе сейчас лежит {start} конфет(а).')

            if player_number == 1:
                candies = random.randint(1, start)
                start -= candies
                print(f'Компьютер взял {candies} конфет(ы).')
                player_number = 2

            else:
                user_input = input('Сколько конфет Вы возьмете со стола: ')
                while not user_input.isdigit():
                    print(f'{user_input} - не число! Попробуйте снова.')
                    user_input = input('Сколько конфет Вы возьмете со стола: ')
                while int(user_input) < 1 or int(user_input) > start:
                    print(f'Вы должны взять хотя бы 1 конфету, но не больше {start}. Попробуйте снова.')
                    user_input = input('Сколько конфет Вы возьмете со стола: ')
                    while not user_input.isdigit():
                        print(f'{user_input} - не число! Попробуйте снова.')
                        user_input = input('Сколько конфет Вы возьмете со стола: ')
                user_input = int(user_input)
                start -= user_input
                player_number = 1

        if player_number == 1:
            print('Поздравляю! Вы победили!')
        else:
            print('Увы, в этот раз не повезло. Победил компьютер. Попробуйте сыграть снова!')

        @bot.message_handler(content_types="text")
        def controller(message):
            print(message.text)
            if message.text == "Сделать предложение":
                bot.send_message(message.chat.id, "введи фамили и имя")
                bot.register_next_step_handler(message, sentence)
            elif message.text == "узнать время":
                bot.send_message(message.chat.id, f"текущее время - {datetime.datetime.now()}")
                button(message)

        def sentence(message):
            text = message.text
            surname = text.split()[0]
            name = text.split()[1]
            bot.send_message(message.chat.id, f"Вас зовут - {name}, фамилия - {surname}")
            button(message)

        bot.infinity_polling()