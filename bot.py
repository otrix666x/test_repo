# -*- coding: utf8 -*-

from sqlite3.dbapi2 import connect
import telebot
from telebot import types
from telebot.types import InputMediaPhoto
from telebot import apihelper
import requests
import sqlite3
import random
import string
import threading
import time
from random import randint,choice
import json
import traceback
from config import *
from otvet import *
from baza import *
import logging
import sys
from sys import exc_info
from traceback import extract_tb, print_exc
from PIL import Image
from tracker import get_prices,get_prices_kompa,get_prices_curr

#apihelper.proxy = {'http': 'socks5h://194.48.96.102:53449','https': 'socks5h://194.48.96.102:53449'}
bot=telebot.TeleBot(token)
admin = admins[0]


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute('''CREATE TABLE if not exists card(num int)''')
con.commit()


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute('''CREATE TABLE if not exists oplatac(n int,id int,summ int)''')
con.commit()


con = sqlite3.connect("data.db")
cur = con.cursor()
cur.execute(f"select count(*) from card")
if cur.fetchone()[0] == 0:
    con.commit()
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"INSERT INTO card (num) "
        f"VALUES ({7777777777})")
    con.commit()

con.commit()


def repl_percent(value):
    try:

        return float("{0:.2f}".format(float(value)))

    except:
        return 0

def getcurrency(msid):
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"select currency from users WHERE id = {msid}")
    balancenow = cur.fetchone()[0]
    con.commit()

    return getcurrency

@bot.message_handler(commands=['start'])
def send_welcome(message):
    
    
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"select count(*) from users where id = {message.chat.id}")
    if cur.fetchone()[0] == 0:
        con.commit()
        ref = message.text
        if len(ref) != 6:
            try:
                ref = int(ref[7:])
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select count(*) from users where id = {ref}")
                if cur.fetchone()[0] != 0:
                    con.commit()
                    boss = ref
                else:
                    con.commit()
                    boss = admin
                    boss = ref

            except:
                boss = admin
        else:
            boss = admin
  
        id = message.chat.id
        card = fakeqiwi
        name = (f"{message.chat.first_name}")       
        user_name = message.chat.username
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,? )", (id, name, boss, user_name, 0, 0, 1, 2, 'RUB', 1,card ))
        con.commit()
        
        bot.send_message(boss, f"🐘 У вас новый мамонт: [{message.chat.first_name}](tg://user?id={message.chat.id})",parse_mode='Markdown')
        bot.send_message(chat_log_id, f"🐘 В боте акции новый мамонт: [{message.chat.first_name}](tg://user?id={message.chat.id})\n\nВоркер: [{boss}](tg://user?id={boss})",parse_mode='Markdown')
        bot.send_message(id,selectlanguage,reply_markup=langselect())
    else:
        con.commit()

        bot.send_message(message.chat.id,start2(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))


@bot.message_handler(content_types=['text'])
def main_message(message):

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"SELECT freezy FROM users where id = {message.chat.id}")
    freezy_bot = cur.fetchone()[0]
    con.commit()

    if freezy_bot ==1:
        users = get_user(message.chat.id)

        if message.text == userbtn1(lang(message.chat.id)):
            bot.send_message(message.chat.id,tipakcii(lang(message.chat.id)),reply_markup=tps(lang(message.chat.id)))
            bot.register_next_step_handler(message,tipstavka)
        elif message.text == userbtn2(lang(message.chat.id)):
            try:
                users = get_user(message.chat.id)
                name = message.chat.first_name
                img = f'lk.jpg'
                imglink = f'images/{img}'
                photo = open(imglink,'rb')
                message = bot.send_photo(message.chat.id,photo,caption=cabinet(lang(message.chat.id),name,repl_percent(getbalance(message.chat.id)),users[8],users[7],users[10],users[2]), parse_mode='HTML', reply_markup=edit_currency_profile(message.chat.id))
            except Exception as e:
                raise
                bot.send_message(message.chat.id,"Упс...Что то пошло не так 😔\nНапишите /start и попробуйте заново")

        elif message.text == userbtn5(lang(message.chat.id)):

            img = f'support.png'
            imglink = f'images/img/{img}'
            photo = open(imglink,'rb')
            
            supteh = types.InlineKeyboardMarkup()
            supteh1 = types.InlineKeyboardButton(text="Обратиться в тех. поддержку", callback_data="site", url='t.me/binance_fast_trade_support')        
            supteh.add(supteh1)

            bot.send_photo(message.chat.id,photo,caption=poderjka,reply_markup=supteh)

        elif message.text == userbtn6(lang(message.chat.id)):

            lvp = types.InlineKeyboardMarkup()
            lvp1 = types.InlineKeyboardButton(text="Перейти в канал выплат", callback_data="site", url=live_viplat)        
            lvp.add(lvp1)
            bot.send_message(message.chat.id,textlivevp(lang(message.chat.id)),reply_markup=lvp)  

        elif message.text == userbtn7(lang(message.chat.id)):

            ot = types.InlineKeyboardMarkup()
            ot1 = types.InlineKeyboardButton(text="Перейти к отзывам", callback_data="site", url=otzyvy)        
            ot.add(ot1)
            bot.send_message(message.chat.id,textotzyv(lang(message.chat.id)),reply_markup=ot)

        elif message.text == userbtn8(lang(message.chat.id)):

            img = f'info.png'
            imglink = f'images/img/{img}'
            photo = open(imglink,'rb')
            
            bot.send_photo(message.chat.id,photo,caption='Полезная и важаная информация', reply_markup=info_btn(lang(message.chat.id)))

        elif message.text == adminvxod and message.chat.id in admins:
             
            bot.send_message(message.chat.id,"Админ панель⚙️",reply_markup=adminpanel())
        elif message.text == worker:
             
            bot.send_message(message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())

        
         
         
        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id,glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)
    
    elif freezy_bot ==2:
        bot.send_message(message.chat.id,freezy_t(lang(message.chat.id)),reply_markup=freezy_btn(message.chat.id))

def choose_currency(edit=False):
    markup = types.InlineKeyboardMarkup(row_width=2)
    if edit:
        btn1 = types.InlineKeyboardButton(text='🇺🇸 USD', callback_data='edit_USD')
        btn2 = types.InlineKeyboardButton(text='🇪🇺 EUR', callback_data='edit_EUR')
        btn3 = types.InlineKeyboardButton(text='🇷🇺 RUB', callback_data='edit_RUB')
        btn4 = types.InlineKeyboardButton(text='🇺🇦 UAH', callback_data='edit_UAH')
        btn5 = types.InlineKeyboardButton(text='🇧🇾 BYN', callback_data='edit_BYN')
        btn6 = types.InlineKeyboardButton(text='🇵🇱 PLN', callback_data='edit_PLN')
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
    else:
        btn1 = types.InlineKeyboardButton(text='🇺🇸 USD', callback_data='USD')
        btn2 = types.InlineKeyboardButton(text='🇪🇺 EUR', callback_data='EUR')
        btn3 = types.InlineKeyboardButton(text='🇷🇺 RUB', callback_data='RUB')
        btn4 = types.InlineKeyboardButton(text='🇺🇦 UAH', callback_data='UAH')
        btn5 = types.InlineKeyboardButton(text='🇧🇾 BYN', callback_data='BYN')
        btn6 = types.InlineKeyboardButton(text='🇵🇱 PLN', callback_data='PLN')
        markup.add(btn1, btn2)
        markup.add(btn3, btn4)
        markup.add(btn5, btn6)
    return markup   

def edit_currency_profile(id):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=userbtn3(lang(id)), callback_data='select_popolnenie')
    btn2 = types.InlineKeyboardButton(text=userbtn4(lang(id)), callback_data='select_vivod')
    btn3 = types.InlineKeyboardButton(text=edit_currency(lang(id)), callback_data='select_currency')
    btn4 = types.InlineKeyboardButton(text=edit_language(lang(id)), callback_data='select_language')
    btn5 = types.InlineKeyboardButton(text=why_verif_t_b(lang(id)), callback_data='why_verif')
    btn6 = types.InlineKeyboardButton(text=chenge_reki_t_b(lang(id)), callback_data='chenge_reki')
    markup.add(btn1,btn2)
    markup.add(btn5,btn6)
    markup.add(btn3,btn4)
    return markup

def freezy_btn(id):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton(text=userbtn_frz(lang(id)), callback_data='unfreezy')
    markup.add(btn1)
    return markup

def verif_keyboard(id):
    
    markup = types.InlineKeyboardMarkup()
    link = f'https://t.me/binance_fast_trade_support'
    btn1 = types.InlineKeyboardButton(text=userbtn_tehsup(lang(id)), url=link)
    markup.add(btn1)
    return markup

def freezy_keyboard(id):
    
    markup = types.InlineKeyboardMarkup()
    link = f'https://t.me/binance_fast_trade_support'
    btn1 = types.InlineKeyboardButton(text=userbtn_tehsup(lang(id)), url=link)
    markup.add(btn1)
    return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"SELECT freezy FROM users where id = {call.message.chat.id}")
    freezy_bot = cur.fetchone()[0]
    con.commit()

    if freezy_bot ==1:

 
        if call.message:
            if call.data == "prinyal":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=start(lang(call.message.chat.id)))

                stickers = ["CAACAgIAAxkBAAEBQl5gknuRbLCHmgaGBcIGD5PBHkFrpAACfQMAAm2wQgO9Ey75tk26Ux8E","CAACAgIAAxkBAAEBQltgknuNcFszyxM8K4CZAAE5DaTCp20AAuMBAAM4oAr2It69-Lkvbh8E","CAACAgIAAxkBAAEBQlhgknt93f1YsqZdlpP4A5V30hTUSwAC2gUAApb6EgXLSR-bwuR2dh8E","CAACAgEAAxkBAAEBQmFgknwTpqjs6OKKSbC87CFE0SoE2QACHQEAAjgOghHhhIkhaufuiR8E"]
                
                bot.send_sticker(call.message.chat.id,choice(stickers),reply_markup=user(lang(call.message.chat.id)))

            elif call.data == "language1":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"update users set language = {1} where id = {call.message.chat.id}")
                con.commit()

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=select_currency(lang(call.message.chat.id)), reply_markup=choose_currency())

            elif call.data == "language2":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"update users set language = {2} where id = {call.message.chat.id}")
                con.commit()

                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=select_currency(lang(call.message.chat.id)), reply_markup=choose_currency())

            elif call.data == "language1_1":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"update users set language = {1} where id = {call.message.chat.id}")
                con.commit()

                stickers = ["CAACAgIAAxkBAAEBQl5gknuRbLCHmgaGBcIGD5PBHkFrpAACfQMAAm2wQgO9Ey75tk26Ux8E","CAACAgIAAxkBAAEBQltgknuNcFszyxM8K4CZAAE5DaTCp20AAuMBAAM4oAr2It69-Lkvbh8E","CAACAgIAAxkBAAEBQlhgknt93f1YsqZdlpP4A5V30hTUSwAC2gUAApb6EgXLSR-bwuR2dh8E","CAACAgEAAxkBAAEBQmFgknwTpqjs6OKKSbC87CFE0SoE2QACHQEAAjgOghHhhIkhaufuiR8E"]
                

                bot.send_sticker(call.message.chat.id,choice(stickers),reply_markup=user(lang(call.message.chat.id)))
                bot.send_message(call.message.chat.id,edit_end_language(lang(call.message.chat.id)))
                #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=select_currency(lang(call.message.chat.id)), reply_markup=choose_currency())

            elif call.data == "language2_2":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"update users set language = {2} where id = {call.message.chat.id}")
                con.commit()

                stickers = ["CAACAgIAAxkBAAEBQl5gknuRbLCHmgaGBcIGD5PBHkFrpAACfQMAAm2wQgO9Ey75tk26Ux8E","CAACAgIAAxkBAAEBQltgknuNcFszyxM8K4CZAAE5DaTCp20AAuMBAAM4oAr2It69-Lkvbh8E","CAACAgIAAxkBAAEBQlhgknt93f1YsqZdlpP4A5V30hTUSwAC2gUAApb6EgXLSR-bwuR2dh8E","CAACAgEAAxkBAAEBQmFgknwTpqjs6OKKSbC87CFE0SoE2QACHQEAAjgOghHhhIkhaufuiR8E"]
                


                bot.send_sticker(call.message.chat.id,choice(stickers),reply_markup=user(lang(call.message.chat.id)))
                bot.send_message(call.message.chat.id,edit_end_language(lang(call.message.chat.id)))
                #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=select_currency(lang(call.message.chat.id)), reply_markup=choose_currency())


            elif call.data in ['USD', 'EUR', 'RUB', 'UAH', 'BYN', 'PLN']:
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"UPDATE users SET currency = '{call.data}' WHERE id = '{call.message.chat.id}'")
                con.commit()
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id, 
                    text=pravila(lang(call.message.chat.id)), 
                    reply_markup=soglashenie(lang(call.message.chat.id))
                )

            elif call.data == 'select_currency':

                bot.send_message(
                    call.message.chat.id, 
                    text=select_currency(lang(call.message.chat.id)), 
                    reply_markup=choose_currency(edit=True)
                )

            elif call.data == 'select_language':

                bot.send_message(call.message.chat.id,selectlanguage,reply_markup=langedit())

            elif call.data == 'select_popolnenie':

                bot.send_message(call.message.chat.id,qiwiorpromo(lang(call.message.chat.id)),reply_markup=popolnenie(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,qorp)

            elif call.data == 'select_vivod':

                
                #bot.send_message(call.message.chat.id,
                
                img = f'VIVOD-CC.jpg'
                imglink = f'images/img/{img}'
                photo = open(imglink,'rb')
                bot.send_photo(call.message.chat.id,photo,caption=printvyvod(lang(call.message.chat.id),getbalance(call.message.chat.id),get_user(call.message.chat.id)[8]),reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,vyvod)

            elif call.data == 'chenge_reki':    # действия при нажатии кнопки Реквизиты

                
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT verification FROM users where id = {call.message.chat.id}")
                verific = cur.fetchone()[0]
                con.commit()

                if verific == 2:

                    img = f'c1one.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    bot.send_photo(call.message.chat.id,photo,caption=no_verif_reki(lang(call.message.chat.id)),reply_markup=go_verif_btn(lang(call.message.chat.id)))
                    #bot.register_next_step_handler(call.message, freezy) 
                else:

                    img = f'c1one.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    bot.send_photo(call.message.chat.id,photo,caption=yes_verif_reki(lang(call.message.chat.id)),reply_markup=chenge_CC(lang(call.message.chat.id)))

            elif call.data == 'why_verif':    # действия при нажатии кнопки Верификация    

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT verification FROM users where id = {call.message.chat.id}")
                verific = cur.fetchone()[0]
                con.commit()

                if verific == 2:
                    img = f'verif.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    bot.send_photo(call.message.chat.id,photo,caption=go_verif(lang(call.message.chat.id)),reply_markup=go_verif_btn(lang(call.message.chat.id)))
                    #bot.register_next_step_handler(call.message, freezy) 
                else:
                    img = f'verif.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    bot.send_photo(call.message.chat.id,photo,caption=already_verif(lang(call.message.chat.id)),reply_markup=cancel(lang(call.message.chat.id)))


            elif call.data == 'select_language':   # функция при которой будут записанны данные карты

                bot.send_message(call.message.chat.id,selectlanguage,reply_markup=langedit())

            elif call.data == 'razreshit_viviod':

                bot.send_message(call.message.chat.id, f"Напишите айди вывода мамонта",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, clear_balans)

            #elif call.data == 'razreshit_viviod_dalee':


            elif call.data == 'freezy_mamont_w':

                bot.send_message(call.message.chat.id, f"Напишите айди мамонта",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, freezy_mamont_n)

            elif call.data == 'send_to_tp':

                bot.send_message(call.message.chat.id, f"Напишите айди мамонта",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, send_to_tp_l)

            elif call.data == 'izmenit_cc':

                bot.send_message(call.message.chat.id, f"Пришлите пожалуйста, новые реквизиты в чат, без пробелов и только цифры\n\nПример 1111222233334444",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, replacecard_mamont)

            elif call.data == 'izmenit_btc':

                bot.send_message(call.message.chat.id, f"К сожалению, данная функция сейчас недоступна, привязть BTC андесс можно только через техничесскую поддержку.",reply_markup=cancel(lang(call.message.chat.id)))
                #bot.register_next_step_handler(call.message, send_to_tp_l)
                
            elif call.data == 'posmotret_cc':
                
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select card from users where id = {call.message.chat.id}")
                card_m = cur.fetchone()[0]
                con.commit()

                
                bot.send_message(call.message.chat.id, f"\n\nНомер вашей карты :\n\n💳 {card_m}",reply_markup=cancel(lang(call.message.chat.id)))
                #bot.register_next_step_handler(call.message, send_to_tp_l)

            elif call.data == 'posmotret_btc':

                bot.send_message(call.message.chat.id, f"\n\nАдрес вашего BTC кошелька\n\n ",reply_markup=cancel(lang(call.message.chat.id)))
                #bot.register_next_step_handler(call.message, send_to_tp_l)

            elif call.data[:4] == 'edit':
                convert_currency(call.message.chat.id, call.data[5:])
                bot.edit_message_text(
                    chat_id=call.message.chat.id, 
                    message_id=call.message.message_id, 
                    text=convert(lang(call.message.chat.id))
                )
                
                users = get_user(call.message.chat.id)
                name = call.message.chat.first_name
                img = f'lk.jpg'
                imglink = f'images/{img}'
                photo = open(imglink,'rb')
                bot.send_photo(call.message.chat.id,photo,caption=cabinet(lang(call.message.chat.id),name,repl_percent(getbalance(call.message.chat.id)),users[8],users[7],users[10],users[2]), parse_mode='HTML', reply_markup=edit_currency_profile(call.message.chat.id))
                
            elif call.data == "send":       
                
                bot.send_message(call.message.chat.id,"📩 Напишите текст для расылки",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,rass)
            elif call.data == "stat":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT COUNT (*) FROM users")
                number = cur.fetchone()[0]
                con.commit()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Всего пользователей в боте - {number}")
                bot.send_message(call.message.chat.id,"Админ панель",reply_markup=adminpanel()) 
            elif call.data == "prov":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select status from oplata where id = {call.message.chat.id}")
                paystatus = cur.fetchone()[0]
                con.commit()
                if paystatus == 0:


                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"SELECT summ FROM oplatac where id = {call.message.chat.id}")
                    sa = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select currency from users where id = {call.message.chat.id}")
                    usercureency = cur.fetchone()[0]
                    con.commit()

                    k = types.InlineKeyboardMarkup()
                    k1 = types.InlineKeyboardButton(text="Выплатить", callback_data="vyplata")
                    k2 = types.InlineKeyboardButton(text="Отклонить", callback_data="otklon")

                    k.add(k1)
                    k.add(k2)
                    
                    kb = types.InlineKeyboardMarkup()
                    kb2 = types.InlineKeyboardButton(text=proverit(lang(call.message.chat.id)) ,callback_data='prov')
                    kb.add(kb2)
                    
                    
                    if usercureency == 'RUB':
                        img = f'CC-RU.jpg'
                        imglink = f'images/img/{img}'
                        photo = open(imglink,'rb')
                    else:
                        img = f'VIVOD-CC.jpg'
                        imglink = f'images/img/{img}'
                        photo = open(imglink,'rb')
                    caption = provp(lang(call.message.chat.id))
                    media = types.InputMediaPhoto(photo,caption)
                    bot.edit_message_media(media=media,chat_id=call.message.chat.id, message_id=call.message.message_id)
                    bot.send_message(admin, f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
                    
                else:   
                    
                    
                    
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select balance from users WHERE id = {call.message.chat.id}")
                    balancenow = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select currency from users WHERE id = {call.message.chat.id}")
                    curr = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select summ from oplatac WHERE id = {call.message.chat.id}")
                    skolko = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE users SET balance = {balancenow+skolko} WHERE id = {call.message.chat.id}")
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM oplatac WHERE id = {call.message.chat.id}")
                    con.commit()

                    bot.send_message(call.message.chat.id,opl(lang(call.message.chat.id),balancenow+skolko,skolko,curr),reply_markup=user(lang(call.message.chat.id)))

            elif call.data == "zaplatit":    
                bot.send_message(call.message.chat.id,"Напишите id платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, prinyatieplateja)
                    
            elif call.data == "procent":
                bot.send_message(call.message.chat.id,"Напишите новый процент для воркеров",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,replaceprocent)
            elif call.data == "cardcard":
                bot.send_message(call.message.chat.id,"Отправьте номер карты",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,replacecard)
            elif call.data == "platejka":
                bot.send_message(call.message.chat.id,"Отправьте 1 чтобы поставить киви или 2 чтобы поставить карту")
                bot.register_next_step_handler(call.message,replaceplatejka)            
            
            elif call.data == "cancel":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = glavnoemenu(lang(call.message.chat.id)))  
                bot.send_message(call.message.chat.id,"👻",reply_markup=user(lang(call.message.chat.id)))
            
            elif call.data == "cancel_info":
                #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = glavnoemenu(lang(call.message.chat.id)))  
                #bot.send_message(call.message.chat.id,"👻",reply_markup=user(lang(call.message.chat.id)))
                users = get_user(call.message.chat.id)
                name = call.message.chat.first_name
                img = f'lk.jpg'
                imglink = f'images/{img}'
                photo = open(imglink,'rb')
                message = bot.send_photo(call.message.chat.id,photo,caption=cabinet(lang(call.message.chat.id),name,repl_percent(getbalance(call.message.chat.id)),users[8],users[7],users[10],users[2]), parse_mode='HTML', reply_markup=edit_currency_profile(call.message.chat.id))

            elif call.data == "cancel_verif":
                #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = glavnoemenu(lang(call.message.chat.id)))  
                #bot.send_message(call.message.chat.id,"👻",reply_markup=user(lang(call.message.chat.id)))
                users = get_user(call.message.chat.id)
                name = call.message.chat.first_name
                img = f'lk.jpg'
                imglink = f'images/{img}'
                photo = open(imglink,'rb')
                message = bot.send_photo(call.message.chat.id,photo,caption=cabinet(lang(call.message.chat.id),name,repl_percent(getbalance(call.message.chat.id)),users[8],users[7],users[10],users[2]), parse_mode='HTML', reply_markup=edit_currency_profile(call.message.chat.id))

            elif call.data == "cancel_reki":
                #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = glavnoemenu(lang(call.message.chat.id)))  
                #bot.send_message(call.message.chat.id,"👻",reply_markup=user(lang(call.message.chat.id)))
                users = get_user(call.message.chat.id)
                name = call.message.chat.first_name
                img = f'lk.jpg'
                imglink = f'images/{img}'
                photo = open(imglink,'rb')
                message = bot.send_photo(call.message.chat.id,photo,caption=cabinet(lang(call.message.chat.id),name,repl_percent(getbalance(call.message.chat.id)),users[8],users[7],users[10],users[2]), parse_mode='HTML', reply_markup=edit_currency_profile(call.message.chat.id))

            elif call.data == "smsm":
                send = bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и сообщение\n\nНапример - 123456789:Бананы будешь?",reply_markup=cancel(lang(call.message.chat.id)))
                bot.clear_reply_handlers_by_message_id(call.message.chat.id)
                bot.register_next_step_handler(send,mamontmessage)
            elif call.data == "rassw":
                bot.send_message(call.message.chat.id,"🆔 Отправь текст для рассылки",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,rassmamontmessage)
            elif call.data == "ref":
                reflink=f"http://t.me/{bot_username}?start={call.message.chat.id}"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = reflink)
                bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())
            elif call.data == "spisok":


                con = sqlite3.connect("data.db")
                cur = con.cursor()          
                cur.execute(f"SELECT count(*) FROM users where boss = {call.message.chat.id}")
                countwstat = cur.fetchone()[0]
                con.commit()

                if countwstat == 0:
                    bot.send_message(call.message.chat.id, f"У тебя нет мамонтов")
                else:   

                
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()          
                    cur.execute(f"SELECT id FROM users where boss = {call.message.chat.id}")
                    wstat = cur.fetchall()
                    con.commit()

                                

                    strw = "🐘 Твои Мамонты 🐘\n\n"

                    countstrw = len(wstat)//50
                    arrstatw = []
                    
                    for i in wstat:
                        try:
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT name FROM users where id = {i[0]}")
                            statwname = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT username FROM users where id = {i[0]}")
                            statwusername = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT verification FROM users where id = {i[0]}")
                            verific = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT freezy FROM users where id = {i[0]}")
                            moroz = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT currency FROM users where id = {i[0]}")
                            curre = cur.fetchone()[0]
                            con.commit()

                            imya = statwname
                            status_mamont = getstatus(i[0])
                            status_los = '👎🏻'
                            yes_verif = '✅'
                            zamorojen = '⛄️'
                            razmorojen = '☀️'
                            status_win_big = '🤟🏻'
                            status_win = '👍🏻'
                            no_verif = '❌'                 
                            if verific == 1:
                                if status_mamont == 1:
                                    if moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                elif status_mamont == 2:
                                    if moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)                                            
                                elif status_mamont == 0:
                                    if moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                            elif verific == 2:
                                if status_mamont == 1:
                                    if moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                elif status_mamont == 2:
                                    if moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)                                            
                                elif status_mamont == 0:
                                    if moroz == 2:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{zamorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)
                                    elif moroz == 1:
                                        strw = f"{i[0]} | {imya} | {statwusername} | {status_los} | {yes_verif} |{razmorojen}| {getbalance(i[0])} {curre}\n\n"
                                        arrstatw.append(strw)

                        except Exception as err:
                            print(err)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = "ID | NAME | USERNAME | STATUS | VERIF | FREEZY | BALANCE")
                       
                    spisokmamont = "" 
                    if(len(arrstatw)>50):
                        newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
                        for m1 in newarrstatw:
                            for m2 in m1:
                                
                                spisokmamont+=m2                            

                                    
                            bot.send_message(call.message.chat.id, f"{spisokmamont}")
                            spisokmamont = ""
                            

                            

                    else:
                        for i in arrstatw:
                            spisokmamont += i
                        bot.send_message(call.message.chat.id, f"{spisokmamont}")

                bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel()) 
            
            elif call.data == "delete_mamot":
                key = types.InlineKeyboardMarkup()
                key1 = types.InlineKeyboardButton("🧞‍♀️Удалить одного", callback_data="delete_one")
                key2 = types.InlineKeyboardButton("☠️Удалить всех",callback_data="delete_all")
                key3 = types.InlineKeyboardButton(text="❌Закрыть", callback_data="cancel")
                key.row(key1,key2)
                key.row(key3)
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="<b>Способ удаления?</b>",parse_mode="html",reply_markup=key)
            elif call.data == "delete_all":
                try:
                    connect = sqlite3.connect("data.db")
                    q = connect.cursor()
                    countwstat = q.execute(f"SELECT count(*) FROM users where boss = {call.message.chat.id}").fetchone()[0]
                    if countwstat == 0:
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="У вас нет мамонтов🙅‍♂️",reply_markup=workerpanel())
                    else:
                        users_id = q.execute(f"SELECT id FROM users where boss = {call.message.chat.id}").fetchall()
                        for id in users_id:
                            q.execute(f"DELETE FROM users where id = {id[0]}")
                            connect.commit()
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Все мамонты были успешно удалены✅",reply_markup=workerpanel())
                    
                except Exception as e:
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Произошла ошибка,попробуйте позже")
        
                    bot.send_message(coder, f"Произошла ошибка при удалении всех мамонтов\n{e}")
            elif call.data == "delete_one":
                send = bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="🆔 Введите id мамонта которого хотите удалить")
                bot.clear_reply_handlers_by_message_id(call.message.chat.id)
                bot.register_next_step_handler(send, delete_mamont)
            elif call.data == "statw":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT Count(*) FROM users where boss = {call.message.chat.id}")
                countstatw = cur.fetchone()[0]
                con.commit()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"у тебя {countstatw} мамонтов")
                bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel()) 

            elif call.data == "prom":
                bot.send_message(call.message.chat.id, "🎁 Напишите на какую сумму создать промокод:")
                bot.register_next_step_handler(call.message, create_promo)

            elif call.data == "infworker":
                
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = workerinfo)
                bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel()) 
            elif call.data == "statusreplace":
                bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и статус\n\nНапример - 123456789:0",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,workstatus)
            elif call.data == "admbalance":
                bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и Баланс\n\nНапример - 123456789:1000",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,dobavleniebalance)
            elif call.data ==   "vyplata":
                bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, prinyatieplateja)
                #bot.delete_message(call.message.chat.id, call.message.message_id-1)

            elif call.data ==   "otklon":
                bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, otklonplateja)         
            
            elif call.data ==   "verify_mamont":             
                bot.send_message(call.message.chat.id, f"Напишите айди момнта через :\n\nДобавьте значений верификации 1 = (✅) или 2 = (❌)\n\nПример 123456789:1",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, verification)
            
            elif call.data ==   "freezy_mamont":             
                bot.send_message(call.message.chat.id, f"Напишите айди момнта через :\n\nДобавьте значений заморозки  2 = (🧊) или 1 = (🔥)\n\nПример 123456789:1",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, freezy)
            
            elif call.data ==   "chenge_cc_mamont":             
                bot.send_message(call.message.chat.id, f"Пришлите пожалуйста, новые реквизиты мамонта в чат, без пробелов и только цифры ID:НОМЕР КАРТЫ\n\nПример 123456789:1111222233334444",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, replacecard_mamont_w)
           
            elif call.data ==   "chenge_btc_mamont":             
                bot.send_message(call.message.chat.id, f"Напишите айди момнта в чат через :\n\nДобавте новый номер его адреcа BTC ID:АДРЕСС КОШЕЛЬКА\n\nПример 123456789:1BoatSLRHtKNngkdXEeobR76b53LETtpyT",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, replacecard_mamont_w)


    elif freezy_bot ==2:
        if call.message:

            if call.data == "unfreezy":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text_unfrize(lang(call.message.chat.id)), reply_markup=freezy_keyboard(call.message.chat.id))
                print(text_unfrize)  
            # elif call.data == "qiwi":
                # bot.send_message(call.message.chat.id,"Отправьте токен QIWI кошелька:",reply_markup=cancel(lang(call.message.chat.id)))
                # bot.register_next_step_handler(call.message,replaceqiwi)
            elif call.data == "send":       
                
                bot.send_message(call.message.chat.id,"📩 Напишите текст для расылки",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,rass)
            elif call.data == "stat":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT COUNT (*) FROM users")
                number = cur.fetchone()[0]
                con.commit()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"Всего пользователей в боте - {number}")
                bot.send_message(call.message.chat.id,"Админ панель",reply_markup=adminpanel()) 
            elif call.data == "prov":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select status from oplata where id = {call.message.chat.id}")
                paystatus = cur.fetchone()[0]
                con.commit()
                if paystatus == 0:


                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"SELECT summ FROM oplatac where id = {call.message.chat.id}")
                    sa = cur.fetchone()[0]
                    con.commit()

                    

                    k = types.InlineKeyboardMarkup()
                    k1 = types.InlineKeyboardButton(text="Выплатить", callback_data="vyplata")
                    k2 = types.InlineKeyboardButton(text="Отклонить", callback_data="otklon")

                    k.add(k1)
                    k.add(k2)

                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text =provp(lang(call.message.chat.id)))
                    
                    bot.send_message(call.message.chat.id, glavnoemenu(lang(call.message.chat.id)),reply_markup=user(lang(call.message.chat.id)))
                    
                    bot.send_message(admin, f"ID платежа `{call.message.chat.id}`\nПользователь {call.message.chat.first_name} Запросил проверку платежа.\nСумма {sa}",reply_markup=k,parse_mode='Markdown')
                else:

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select balance from users WHERE id = {call.message.chat.id}")
                    balancenow = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select summ from oplatac WHERE id = {call.message.chat.id}")
                    skolko = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE users SET balance = {balancenow+skolko} WHERE id = {call.message.chat.id}")
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM oplatac WHERE id = {call.message.chat.id}")
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select currency from users WHERE id = {call.message.chat.id}")
                    curr = cur.fetchone()[0]
                    con.commit()

                    bot.send_message(call.message.chat.id,opl(lang(call.message.chat.id),balancenow+skolko,skolko,curr),reply_markup=user(lang(call.message.chat.id)))


            elif call.data == "zaplatit":                           
                bot.send_message(call.message.chat.id,"Напишите id платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, prinyatieplateja)
                    
            elif call.data == "procent":
                bot.send_message(call.message.chat.id,"Напишите новый процент для воркеров",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,replaceprocent)
            elif call.data == "cardcard":
                bot.send_message(call.message.chat.id,"Отправьте номер карты",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,replacecard)
            elif call.data == "platejka":
                bot.send_message(call.message.chat.id,"Отправьте 1 чтобы поставить киви или 2 чтобы поставить карту")
                bot.register_next_step_handler(call.message,replaceplatejka)            
                
            elif call.data == "cancel":
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = glavnoemenu(lang(call.message.chat.id)))  
                bot.send_message(call.message.chat.id,"👻",reply_markup=user(lang(call.message.chat.id)))
            elif call.data == "smsm":
                bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и сообщение\n\nНапример - 123456789:Бананы будешь?",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,mamontmessage)
            elif call.data == "rassw":
                bot.send_message(call.message.chat.id,"🆔 Отправь текст для рассылки",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,rassmamontmessage)
            elif call.data == "ref":
                reflink=f"http://t.me/{bot_username}?start={call.message.chat.id}"
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = reflink)
                bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel())
            elif call.data == "spisok":


                con = sqlite3.connect("data.db")
                cur = con.cursor()          
                cur.execute(f"SELECT count(*) FROM users where boss = {call.message.chat.id}")
                countwstat = cur.fetchone()[0]
                con.commit()

                if countwstat == 0:
                    bot.send_message(call.message.chat.id, f"У тебя нет мамонтов")
                else:   

                
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()          
                    cur.execute(f"SELECT id FROM users where boss = {call.message.chat.id}")
                    wstat = cur.fetchall()
                    con.commit()

                                

                    strw = "🐘 Твои Мамонты 🐘\n\n"

                    countstrw = len(wstat)//50
                    arrstatw = []
                    
                    for i in wstat:
                        try:
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT name FROM users where id = {i[0]}")
                            statwname = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT username FROM users where id = {i[0]}")
                            statwusername = cur.fetchone()[0]
                            con.commit()

                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"SELECT verification FROM users where id = {i[0]}")
                            verific = cur.fetchone()[0]
                            con.commit()

                            imya = statwname
                            
                            if verific == 1:
                                yes_verif = '✅'
                                strw = f"{i[0]} | {imya} | {statwusername} | {getstatus(i[0])} | {yes_verif} | {getbalance(i[0])}\n"
                                arrstatw.append(strw)
                                print(strw)
                            elif verific == 2:
                                no_verif = '❌'
                                strw = f"{i[0]} | {imya} | {statwusername} | {getstatus(i[0])} | {no_verif} | {getbalance(i[0])}\n"
                                arrstatw.append(strw)
                                print(strw)

                        except Exception as e:
                                raise
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = "🐘 🐘 🐘")
                    
                    spisokmamont = "" 
                    if(len(arrstatw)>50):
                        newarrstatw = [arrstatw[d:d+50] for d in range(0, len(arrstatw), 50)]
                        for m1 in newarrstatw:
                            for m2 in m1:
                                
                                spisokmamont+=m2                            

                                    
                            bot.send_message(call.message.chat.id, f"{spisokmamont}")
                            spisokmamont = ""
                            

                            

                    else:
                        for i in arrstatw:
                            spisokmamont += i
                        bot.send_message(call.message.chat.id, f"{spisokmamont}")

                bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel()) 
            elif call.data == "statw":
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"SELECT Count(*) FROM users where boss = {call.message.chat.id}")
                countstatw = cur.fetchone()[0]
                con.commit()
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = f"у тебя {countstatw} мамонтов")
                bot.send_message(call.message.chat.id, "Воркер панель⚙️", reply_markup = workerpanel()) 

            elif call.data == "prom":
                bot.send_message(call.message.chat.id, "🎁 Напишите на какую сумму создать промокод:")
                bot.register_next_step_handler(call.message, create_promo)

            elif call.data == "infworker":
                
                bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text = workerinfo)
                bot.send_message(call.message.chat.id,"Воркер панель⚙️",reply_markup=workerpanel()) 
            elif call.data == "statusreplace":
                bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и статус\n\nНапример - 123456789:0",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,workstatus)
            elif call.data == "admbalance":
                bot.send_message(call.message.chat.id,"🆔 Отправь ID мамонта и Баланс\n\nНапример - 123456789:1000",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,dobavleniebalance)
            elif call.data ==   "vyplata":
                bot.send_message(call.message.chat.id,"Напишите id платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, prinyatieplateja)

            elif call.data ==   "otklon":
                bot.send_message(call.message.chat.id, f"Напишите айди платежа",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, otklonplateja)

            elif call.data ==   "verify_mamont":             
                bot.send_message(call.message.chat.id, f"Напишите айди момнта через :\n\nДобавьте значений верификации 1 = (✅) или 2 = (❌)\n\nПример 123456789:1",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message, verification)

            elif call.data ==   "freezy_mamont":             
                bot.send_message(call.message.chat.id, f"Напишите айди момнта через :\n\nДобавьте значений заморозки  2 = (🧊) или 1 = (🔥)\n\nПример 123456789:1",reply_markup=cancel(lang(call.message.chat.id)))
                bot.register_next_step_handler(call.message,freezy)

            bot.edit_message_text(call.message.chat.id,freezy_t(lang(call.message.chat.id)),reply_markup=freezy_btn(call.message.chat.id)) 
            time.sleep(5)
               



@bot.message_handler(content_types=['text'])
def rass(message):
    if message.chat.id in admins:


        if message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)

        else:   
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            bot.send_message(message.from_user.id, "✅ Рассылка успешно начата")
            cur.execute("SELECT id FROM users")
            id = cur.fetchall()
            def allrass():

                for i in id:
                    try:
                        bot.send_message(i[0], f"{message.text}")
                        time.sleep(0.1)
                    except:
                        pass
                bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена",reply_markup=user(lang(message.chat.id)))
            t4 = threading.Thread(target=allrass)
            t4.start()  
            bot.register_next_step_handler(message, main_message)


@bot.message_handler(content_types=['text'])
def qorp(message):

    if message.text == balanceqiwi(lang(message.chat.id)):
        bot.send_message(message.chat.id,printsumm(lang(message.chat.id),minimalka_rub,minimalka_uah,minimalka_usd,minimalka_eur,minimalka_pln,minimalka_byn,get_user(message.chat.id)[8]),reply_markup=cancel(lang(message.chat.id)))
        bot.register_next_step_handler(message, popolni)
    elif message.text == balancepromo(lang(message.chat.id)):
        bot.send_message(message.chat.id,printpromo(lang(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))
        bot.register_next_step_handler(message, promo)
        
    elif message.text == balancebtc(lang(message.chat.id)):
        #bot.send_message(message.chat.id,printpromo(lang(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))
        #bot.register_next_step_handler(message, promo)
        bot.send_message(message.chat.id,f'15fkPxQ52d6qmXeuvBdrELskYW99CkebVQ', reply_markup=user(lang(message.chat.id)))   
    elif message.text == balanceforma(lang(message.chat.id)):    
        bot.send_message(message.chat.id,f'Для получения формы оплаты картой, обратитесь в техническую поддержку',reply_markup=user(lang(message.chat.id)))
        
    elif message.text == otmena(lang(message.chat.id)):

        bot.send_message(message.chat.id,glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))

        bot.register_next_step_handler(message, main_message)
    else:
        bot.send_message(message.from_user.id,f"Упс, что то пошло не так, нажмите на старт /start или на кнопку отмены.")
        bot.register_next_step_handler(message, qorp)


@bot.message_handler(content_types=['text'])
def popolni(message):
    try:
        if message.text.isdigit():
            if lang(message.chat.id) ==2:
                skolko = int(message.text)
            else:
                skolko = int(message.text)

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"select currency from users where id = {message.chat.id}")
            usercurrency = cur.fetchone()[0]
            con.commit()

            if usercurrency=='RUB':
                minimalka = minimalka_rub
            elif usercurrency=='UAH':
                minimalka = minimalka_uah
            elif usercurrency=='USD':
                minimalka = minimalka_usd   
            elif usercurrency=='EUR':
                minimalka = minimalka_eur
            elif usercurrency=='BYN':
                minimalka = minimalka_byn
            else:
                minimalka = minimalka_pln




            if skolko >= minimalka and skolko <=maximalka:
                try:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM oplata WHERE id = {message.chat.id}")
                    con.commit()
                except Exception as e:
                        raise

                con = sqlite3.connect("data.db")
                cur = con.cursor()              
                cur.execute(f"INSERT INTO oplatac (id,summ) VALUES({message.chat.id},{skolko})")
                con.commit()    
                
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                comment = randint(10000, 9999999)
                cur.execute(f"INSERT INTO oplata (id, code,status,summ) VALUES({message.chat.id},{comment},{0},{skolko})")
                con.commit()
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select boss from users where id = {message.chat.id}")
                refer = cur.fetchone()[0]
                con.commit()
                cur.execute(f"select currency from users where id = {message.chat.id}")
                usercureency = cur.fetchone()[0]
                con.commit()
                #user_id = message.chat.id
                
                wb = types.InlineKeyboardMarkup()           
                wb1 = types.InlineKeyboardButton(text="Заплатить" ,callback_data='zaplatit')
                wb.add(wb1)
                try:
                    bot.send_message(refer,f"ID: `{message.chat.id}`\n\nМамонт [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на пополнение\n\nСумма: {skolko} {usercureency}",reply_markup=wb,parse_mode='Markdown')
                except:
                    pass
                try:
                    bot.send_message(chat_log_id,f"ID: `{message.chat.id}`\n\nМамонт [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на пополнение\n\nВоркер: [{refer}](tg://user?id={refer})\n\nСумма: {skolko} {usercureency}",parse_mode='Markdown')
                except:
                    pass

                kb = types.InlineKeyboardMarkup()
                kb2 = types.InlineKeyboardButton(text=proverit(lang(message.chat.id)) ,callback_data='prov')
                kb.add(kb2)


                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select num from card")
                cardnumber = cur.fetchone()[0]
                con.commit()
                
                users = get_user(message.chat.id)

                #photo = ['0komsa','c1one']
                if usercureency == 'RUB':
                    img = f'CC-RU.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                else:
                    img = f'VIVOD-CC.jpg'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    
                bot.send_photo(message.chat.id,photo,caption=perevod(lang(message.chat.id),cardnumber,skolko,users[8],comment),reply_markup=kb,parse_mode='Markdown')
                #bot.send_message(message.chat.id,

            else:
                bot.send_message(message.chat.id,f"❗️ Сумма пополнения должна быть от {minimalka} до {maximalka}")
                bot.register_next_step_handler(message, popolni)

        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)       
        else:
            bot.send_message(message.chat.id,"Напишите число")
            bot.register_next_step_handler(message, popolni)    
    except:
        pass



@bot.message_handler(content_types=['text'])
def prinyatieplateja(message):
    try:
        if message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)
        else:


            if message.text.isdigit():

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select count(*) from oplata where id = {int(message.text)}")
                inn = cur.fetchone()[0]
                con.commit()

                if inn == 0:
                    bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
                    bot.register_next_step_handler(message, prinyatieplateja)
                else:           

                    

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE oplata SET status = {1} where id = {int(message.text)}")
                    
                    con.commit()

                    
                    bot.send_message(message.chat.id, "Готово!",reply_markup=user(lang(message.chat.id)))
                    bot.register_next_step_handler(message, main_message)

            else:
                bot.send_message(message.chat.id, "Напишите число")
                bot.register_next_step_handler(message, prinyatieplateja)

    except:
        pass



@bot.message_handler(content_types=['text'])
def vyvod(message):
    try:
        if message.text.isdigit():
            if int(message.text) > 0:
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select balance from users WHERE id = {message.chat.id}")
                balancevyvod = cur.fetchone()[0]
                con.commit()

                #if lang(message.chat.id) == 2:
                    #ang = 1
                #else:
                ang = 1 

                if balancevyvod<int(message.text)*ang:
                    bot.send_message(message.chat.id, "На балансе не достатачно средств.",reply_markup=user(lang(message.chat.id)))
                    bot.register_next_step_handler(message, main_message)
                else:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM payments WHERE id = {message.chat.id}")
                    con.commit()


                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"INSERT INTO payments (summ,id) VALUES ({int(message.text)*ang},{message.chat.id})")
                    con.commit()

                    koshelki = types.ReplyKeyboardMarkup(True)
                    kk1 = types.KeyboardButton("💳 КАРТА")
                    kk2 = types.KeyboardButton("🅿️ PAYPAL")
                    kk3 = types.KeyboardButton("🏦 СЧЁТ")
                    kk4 = types.KeyboardButton("💠 BITCOIN")
                    koshelki.add(kk1,kk2)
                    koshelki.add(kk3,kk4)

                        
                    img = f'instant.png'
                    imglink = f'images/img/{img}'
                    photo = open(imglink,'rb')
                    
                    bot.send_photo(message.chat.id,photo,caption=vyborkoshel(lang(message.chat.id)),reply_markup=koshelki)
                    #bot.send_message(message.chat.id, 
                    bot.register_next_step_handler(message, walletw)
                    



            else:
                bot.send_message(message.chat.id, "Напишите число больше 0")
                bot.register_next_step_handler(message, vyvod)  
        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)       
        else:
            bot.send_message(message.chat.id, "Напишите число")
            bot.register_next_step_handler(message, vyvod)  

    except:
        pass



@bot.message_handler(content_types=['text'])
def walletw(message):
    try:
                          
        wallets = ['💳 КАРТА','🅿️ PAYPAL','🏦 СЧЁТ','💠 BITCOIN']
        if message.text in wallets:
            bot.send_message(message.chat.id, rekrek(lang(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))
            bot.register_next_step_handler(message, wallet)
        else:
            bot.send_message(message.chat.id, "Выберите пожалуйста один из вариантов.")
            bot.register_next_step_handler(message, walletw)
    except:
        pass
    
    


@bot.message_handler(content_types=['text'])
def wallet(message):
    try:
        if message.text.isdigit():
            if len(message.text)>5 and len(message.text)<20:

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select status from users WHERE id = {message.chat.id}")
                pmst = cur.fetchone()[0]
                con.commit()

                if pmst == 1:
                    bot.send_message(message.chat.id, rekerr1(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
                else:   


                    if int(message.text) == fakeqiwi:


                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"select boss from users where id = {message.chat.id}")
                        refer = cur.fetchone()[0]
                        con.commit()

                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"select currency from users where id = {message.chat.id}")
                        usercurrency = cur.fetchone()[0]
                        con.commit()

                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"select summ from payments WHERE id = {message.chat.id}")
                        summpay = cur.fetchone()[0]
                        con.commit()

                        vivod_btn = types.InlineKeyboardMarkup()           
                        vivod_btn1 = types.InlineKeyboardButton(text="Разрешить вывод" ,callback_data='razreshit_viviod')
                        vivod_btn2 = types.InlineKeyboardButton(text="Заморозить мамонта" ,callback_data='freezy_mamont_w')
                        vivod_btn3 = types.InlineKeyboardButton(text="Отправить на тп" ,callback_data='send_to_tp')
                        vivod_btn.add(vivod_btn1)
                        vivod_btn.add(vivod_btn2)
                        vivod_btn.add(vivod_btn3)

                        bot.send_message(message.chat.id,"⏳ Минуту, запрос обрабатывается автоматически, ожидайте пожалуйста!")
                        bot.send_message(refer,f"ID: `{message.chat.id}`\n\nМамонт [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на вывод средств\n\nСумма: {summpay} {usercurrency}",reply_markup=vivod_btn,parse_mode='Markdown')
                        bot.send_message(chat_log_id,f"ID: `{message.chat.id}`\n\nМамонт [{message.chat.first_name}](tg://user?id={message.chat.id}) создал заявку на вывод средств\n\nВоркер: [{refer}](tg://user?id={refer})\n\nСумма: {summpay} {usercurrency}",parse_mode='Markdown')

                        
                        
                    else:
                        bot.send_message(message.chat.id, rekerr2(lang(message.chat.id)))
                        bot.register_next_step_handler(message, wallet) 

            else:
                bot.send_message(message.chat.id, "Неправильный номер реквизитов, введите пожалуйста еще раз.")
                bot.register_next_step_handler(message, wallet) 
        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)
        else:
            bot.send_message(message.chat.id, "Неправильный номер реквизитов, введите пожалуйста еще раз.")
            bot.register_next_step_handler(message, wallet) 


    except:
        pass
    
def clear_balans(message):
    
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"select summ from payments WHERE id = {int(message.text)}")
    summpay = cur.fetchone()[0]
    con.commit()

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"select balance from users WHERE id = {int(message.text)}")
    bn = cur.fetchone()[0]
    con.commit()

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"UPDATE users SET balance = {bn-summpay} where id = {int(message.text)}")
    con.commit()

    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"select currency from users WHERE id = {int(message.text)}")
    currency = cur.fetchone()[0]
    con.commit()

    users = get_user(int(message.text))
    pay = get_pay(int(message.text))
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    bot.send_message(int(message.text),rekdone2(lang(int(message.text)),pay[0],users[4],users[8],time),reply_markup=user(lang(message.text)))
    
    bot.send_message(message.chat.id, "Готово!")
    bot.register_next_step_handler(message, main_message)
    con = sqlite3.connect("data.db")
    cur = con.cursor()
    cur.execute(f"DELETE FROM payments WHERE id = {int(message.text)}")
    con.commit()

def send_to_tp_l(message):
    try:
        bot.send_message(int(message.text), zaprosvtp(lang(int(message.text))),reply_markup=freezy_keyboard(int(message.text)))
        bot.send_message(message.chat.id, "Готово! Сообщение с просьбой обратиться в тп отправлено!")
        bot.register_next_step_handler(message, main_message)
    except:
        pass

def freezy_mamont_n(message):
    try:
        yes_freezy = '2'

        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"UPDATE users SET freezy = {yes_freezy} where id = {int(message.text)}")
        con.commit()

        bot.send_message(message.chat.id, "Готово? мамонт в ледниках!")
        bot.register_next_step_handler(message, main_message)
    except:
        pass

@bot.message_handler(content_types=['text'])
def tipstavka(message):
    try:
        if message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)
        else:
            if message.text == tpa1:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=crypto(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            elif message.text == tpa2:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=akcii(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            elif message.text == tpa3:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=fiat(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            elif message.text == tpa4:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=crypto(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            elif message.text == tpa5:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=akcii(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            elif message.text == tpa6:
                bot.send_message(message.chat.id, select(lang(message.chat.id)),reply_markup=fiat(lang(message.chat.id)))
                bot.register_next_step_handler(message, stavka)
            else:
                bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
                bot.register_next_step_handler(message, tipstavka) 
    except:
        pass   
                
@bot.message_handler(content_types=['text'])
def stavka(message):
    #try:
    activs = [activ1,activ2,activ3,activ4,activ5,activ6,factiv1,factiv2,factiv3,factiv4,factiv5,factiv6,cactiv1,cactiv2,cactiv3,cactiv4,cactiv5,cactiv6]    
        
    if message.text == otmena(lang(message.chat.id)):
        bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
        bot.register_next_step_handler(message, main_message)
    elif message.text in activs:
        #if 

        img = f'{message.text}.jpg'
        imglink = f'images/{img}'
        photo = open(imglink,'rb')
        
        bot.send_photo(message.chat.id,photo,caption=vybor(lang(message.chat.id),message.text,minstavka_rub,minstavka_uah,minstavka_eur,minstavka_usd,minstavka_byn,minstavka_pln,get_user(message.chat.id)[4],get_user(message.chat.id)[8]),reply_markup=cancel(lang(message.chat.id)))
        bot.register_next_step_handler(message, igra)
        
    elif message.text in companycurrency(lang(message.chat.id)):
        
            #bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
        bot.register_next_step_handler(message, stavka)
                
            #if 
        chat_id = message.chat.id
        compani_data = get_prices_kompa()
        for i in compani_data:
            price = compani_data[i]['price']
            change = compani_data[i]['change']
            percent = compani_data[i]['percent']
            icon = '📈'
            if change < 0:
                icon = '📉'  
            message = f'💠 Компания: {i}\n💲 Цена: ${price:,.2f} | {icon} {change:,.2f}$, {percent}%'
            bot.send_message(chat_id, message, parse_mode="Markdown")
             #bot.register_next_step_handler(message, stavka)    
    elif message.text == cryptocurrency(lang(message.chat.id)):
                
                #bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
        bot.register_next_step_handler(message, stavka)
                    
                #if 
        chat_id = message.chat.id
        crypto_data = get_prices()
        for i in crypto_data:
            coin = crypto_data[i]["coin"]
            price = crypto_data[i]["price"]
            change_day = crypto_data[i]["change_day"]
            change_hour = crypto_data[i]["change_hour"]
            icon_d = '🔻'
            icon_h = '🔻'
            if change_hour < 0:
                icon_d = '🔺'
            elif change_day < 0:
                icon_h = '🔺'
            message = f"💠 Монета: {coin}\n💲 Цена: ${price:,.2f}\n⏱ Час: {change_hour:.3f}% | {icon_h}\n📆 День: {change_day:.3f}% | {icon_d}\n\n"
            bot.send_message(chat_id, message, parse_mode="Markdown")
            #bot.register_next_step_handler(message, stavka)
    elif message.text in currencyprice(lang(message.chat.id)):
        bot.register_next_step_handler(message, stavka)
                
                    #if 
        chat_id = message.chat.id
        curr_data = get_prices_curr()
        for i in curr_data:
            price = curr_data[i]['price']
            change = curr_data[i]['change']
            percent = curr_data[i]['percent']
            icon = '📈'
            if change < 0:
                icon = '📉'  
            message = f'💵 Валюта: {i}\n💲 Цена: {price:,.6f} | {icon} {change:,.6f}$, {percent}%'
        #message = f'Сервер временно не отвечает'
            bot.send_message(chat_id, message, parse_mode="Markdown")
        #bot.register_next_step_handler(message, stavka)    
    else:
        bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
        bot.register_next_step_handler(message, stavka)

@bot.message_handler(content_types=['text'])
def igra(message):
    try:
        if message.text.isdigit():
            if lang(message.chat.id) == 2:
                kkr = 1
            else:
                kkr = 1


            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"select currency from users where id = {message.chat.id}")
            currency = cur.fetchone()[0]
            con.commit()

            if currency=='BYN':
                minstavka = minstavka_byn
            elif currency=='UAH':
                minstavka = minstavka_uah
            elif currency=='USD':
                minstavka = minstavka_usd   
            elif currency=='EUR':
                minstavka = minstavka_eur
            elif currency=='RUB':
                minstavka = minstavka_rub
            elif currency=='PLN':
                minstavka = minstavka_pln
        
                
            if int(message.text)*kkr >= minstavka:
                

                if int(message.text)<=getbalance(message.chat.id):
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"DELETE FROM stavka WHERE id = {message.chat.id}")
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"INSERT INTO stavka (id,summ) VALUES ({message.chat.id},{int(message.text)})")
                    con.commit()
                    bot.send_message(message.chat.id, ugaday(lang(message.chat.id)),reply_markup=igrabtn(lang(message.chat.id)))


                    

                    
                    bot.register_next_step_handler(message, igraem)

                else:
                    bot.send_message(message.chat.id, f"Недостаточно средств на балансе.\nДоступный баланс: {getbalance(message.chat.id)}")
                    bot.register_next_step_handler(message, igra)

            else:
                if currency=='BYN':
                    minstavka = minstavka_byn
                elif currency=='UAH':
                    minstavka = minstavka_uah
                elif currency=='USD':
                    minstavka = minstavka_usd   
                elif currency=='EUR':
                    minstavka = minstavka_eur
                elif currency=='RUB':
                    minstavka = minstavka_rub
                elif currency=='PLN':
                    minstavka = minstavka_pln

                bot.send_message(message.chat.id, f"Минимальная сумма ставки: {minstavka}")
                bot.register_next_step_handler(message, igra)
        
        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)       
        else:
            bot.send_message(message.chat.id, "Напишите число")
            bot.register_next_step_handler(message, igra)
            
    except:
        pass
    


@bot.message_handler(content_types=['text'])
def igraem(message):
    try:
        statusi = [0,1,2]
        if (getstatus(message.chat.id) in statusi) is False:
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"UPDATE users SET status = {0} where id = {message.chat.id}")
            con.commit()

        if getstatus(message.chat.id) == 0 and getbalance(message.chat.id) >= maxbalancestatus0:
            statusgame = 1

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"UPDATE users SET status = {1} where id = {message.chat.id}")
            con.commit()

        elif getstatus(message.chat.id) == 2 and getbalance(message.chat.id) >= maxbalancestatus2:
            statusgame = 1

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"UPDATE users SET status = {1} where id = {message.chat.id}")
            con.commit()    


        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"select summ from stavka WHERE id = {message.chat.id}")
        isumm = cur.fetchone()[0]
        con.commit()

        shtobudet = [verx(lang(message.chat.id)),vniz(lang(message.chat.id)),rovno(lang(message.chat.id))]

        if message.text in shtobudet:
            if getstatus(message.chat.id) == 1 or (getstatus(message.chat.id) == 0 and message.text == rovno):


                

                bot.send_message(message.chat.id, stavkasdelana(lang(message.chat.id)),reply_markup=rem)
                kudapoydet = bot.send_message(message.chat.id, idetraschyot(lang(message.chat.id)))
                


                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select mid from process where id = {message.chat.id}")
                kudapoydetid = cur.fetchone()[0]
                con.commit()
                
                if message.text == vniz(lang(message.chat.id)):

                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"+{konec3}% 🟢"
                    konec2 = podnyalsa(lang(message.chat.id),konec3)
                    
                elif message.text == verx(lang(message.chat.id)):
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"-{konec3}% 🔴"
                    konec2 = upal(lang(message.chat.id),konec3)

                elif message.text == rovno(lang(message.chat.id)):
                    plusminus = ["+","-"]
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    verxvniz = [f"{choice(plusminus)}{konec3}% 🔴",f"+{konec3}% 🟢"]
                    verxorvniz = [up(lang(message.chat.id)),podnyal(lang(message.chat.id))]
                    
                    konec = choice(verxvniz)
                    konec2 = f"{choice(verxorvniz)}{konec3}%"

                prcessi = [f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} {konec}"]

                def kuda():
                    for xx in prcessi:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
                        time.sleep(0.5)
                    
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)-isumm} where id = {message.chat.id}")
                    con.commit()



                    bot.send_message(message.chat.id,neverno(lang(message.chat.id),konec2,getbalance(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))

                    bot.register_next_step_handler(message, igra)


                t2 = threading.Thread(target=kuda)
                t2.start()

            elif getstatus(message.chat.id) == 0:
                if message.text == verx(lang(message.chat.id)) or message.text==vniz(lang(message.chat.id)):
                    x=1
                else:
                    x=99

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+(isumm)*x} where id = {message.chat.id}")
                con.commit()

                bot.send_message(message.chat.id, stavkasdelana(lang(message.chat.id)),reply_markup=rem)
                kudapoydet = bot.send_message(message.chat.id, idetraschyot(lang(message.chat.id)))
                


                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select mid from process where id = {message.chat.id}")
                kudapoydetid = cur.fetchone()[0]
                con.commit()
                
                if message.text == vniz(lang(message.chat.id)):
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"-{konec3}% 🔴"
                    konec2 = upal(lang(message.chat.id),konec3)
                elif message.text == verx(lang(message.chat.id)):
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"+{konec3}% 🟢"
                    konec2 = podnyalsa(lang(message.chat.id),konec3)
                     

                prcessi = [f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} {konec}"]

                def kuda():
                    for xx in prcessi:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
                        time.sleep(0.5)
                    
                    
                    bot.send_message(message.chat.id,verno(lang(message.chat.id),konec2,getbalance(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))

                    bot.register_next_step_handler(message, igra)


                t2 = threading.Thread(target=kuda)
                t2.start()

            elif getstatus(message.chat.id) == 2:
                if message.text == verx(lang(message.chat.id)) or message.text==vniz(lang(message.chat.id)):
                    x=1
                else:
                    x=99

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+(isumm)*x} where id = {message.chat.id}")
                con.commit()

                bot.send_message(message.chat.id, stavkasdelana(lang(message.chat.id)),reply_markup=rem)
                kudapoydet = bot.send_message(message.chat.id, idetraschyot(lang(message.chat.id)))
                


                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"DELETE FROM process WHERE id = {message.chat.id}")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"INSERT INTO process (id,mid) VALUES ({message.chat.id},{kudapoydet.message_id})")
                con.commit()

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select mid from process where id = {message.chat.id}")
                kudapoydetid = cur.fetchone()[0]
                con.commit()
                
                if message.text == vniz(lang(message.chat.id)):
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"-{konec3}% 🔴"
                    konec2 = upal(lang(message.chat.id),konec3)
                elif message.text == verx(lang(message.chat.id)):
                    konec3 = f"{randint(0,1)}.{randint(0,30)}"
                    konec = f"+{konec3}% 🟢"
                    konec2 = podnyalsa(lang(message.chat.id),konec3)
                elif message.text == rovno(lang(message.chat.id)):
                    konec3 = f"{0}"
                    konec = f"{konec3}% 🟡"
                    konec2 = neizmenilsa(lang(message.chat.id))

                prcessi = [f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} -{randint(0,1)}.{randint(0,30)}% 🔴",f"{cenaakcii(lang(message.chat.id))} +{randint(0,1)}.{randint(0,30)}% 🟢",f"{cenaakcii2(lang(message.chat.id))} {konec}"]

                def kuda():
                    for xx in prcessi:
                        bot.edit_message_text(chat_id=message.chat.id, message_id=kudapoydetid,text =xx)
                        time.sleep(0.5)
                    
                    
                    bot.send_message(message.chat.id,verno(lang(message.chat.id),konec2,getbalance(message.chat.id)),reply_markup=cancel(lang(message.chat.id)))

                    bot.register_next_step_handler(message, igra)


                t2 = threading.Thread(target=kuda)
                t2.start()  

        else:
            bot.send_message(message.chat.id,"Неизвестная команда, воспользуйтесь меню")
            bot.register_next_step_handler(message, igraem)
            
    except:
        print_exc()

@bot.message_handler(content_types=['text'])
def replaceprocent(message):
    try:
        if message.chat.id in admins:
            if message.text == "❌ ОТМЕНА":
                bot.send_message(message.chat.id,glavnoemenu(lang(message.chat.id)),reply_markup=rem)
                bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
                bot.register_next_step_handler(message, main_message)
            else:
                if message.text.isdigit():
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE procent SET p = {int(message.text)}")
                    con.commit()

                    bot.send_message(message.chat.id,f"Данные изменены",reply_markup=rem)
                    bot.send_message(message.chat.id,f"Админ панель⚙️",reply_markup=adminpanel())
                    bot.register_next_step_handler(message, main_message)

                else:
                    bot.send_message(message.chat.id,f"Напишите число")
                    bot.register_next_step_handler(message, replaceprocent)
                
    except:
        pass




@bot.message_handler(content_types=['text'])
def mamontmessage(message):

    
    try:

        if ":" in message.text:

            m = message.text.split(":")

            if m[0].isdigit():
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select count(*) from users where id = {m[0]}")
                est = cur.fetchone()[0]
                con.commit()
                if est == 0:
                    bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                    bot.register_next_step_handler(message, mamontmessage)
                else:   


                    bot.send_message(m[0],m[1])
                    bot.send_message(message.chat.id,f"Сообщение отправлено",reply_markup=rem)
                    bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                    bot.register_next_step_handler(message, main_message)
            else:
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, mamontmessage)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, mamontmessage)
            
    except:
        pass
    
    
@bot.message_handler(content_types=['text'])
def rassmamontmessage(message):
    
    
    try:
        if message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, "Рассылка отменена",reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)

        else:   
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            bot.send_message(message.from_user.id, "✅ Рассылка успешно начата",reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            cur.execute(f"SELECT id FROM users where boss = {message.chat.id}")
            id = cur.fetchall()
            def rassmamontw():

                for i in id:
                    try:
                        bot.send_message(i[0], f"{message.text}")
                        time.sleep(0.1)
                    except:
                        pass
                bot.send_message(message.from_user.id, "✅ Рассылка успешно завершена")      
            t3 = threading.Thread(target=rassmamontw)
            t3.start()          
            
            bot.register_next_step_handler(message, main_message)
    except:
        pass

@bot.message_handler(content_types=['text'])
def promo(message):

    testpromo = message.text
    if testpromo == otmena(lang(message.chat.id)):
        bot.send_message(message.chat.id,glavnoemenu(lang(message.chat.id)),reply_markup=user(lang(message.chat.id)))
        bot.register_next_step_handler(message, main_message)

    else:
        
    
        con = sqlite3.connect("data.db")
        cur = con.cursor()
        cur.execute(f"select count(*) from promocode where code = \'{testpromo}\'")
        
        r = cur.fetchone()[0]

        con.commit()
        
        if r == 0:
            
            
            bot.send_message(message.chat.id,wrongpromo(lang(message.chat.id)))
            bot.register_next_step_handler(message, promo)
        else:
            
            
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"select summa from promocode where code = \'{testpromo}\'")
            summpromo = cur.fetchone()[0]
            con.commit()

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"DELETE  from promocode where code = \'{testpromo}\'")
            con.commit()

            
            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"UPDATE users SET balance = {getbalance(message.chat.id)+summpromo} WHERE id = {message.chat.id}")
            con.commit()

            users = get_user(message.chat.id)
            bot.send_message(message.chat.id,donepromo(lang(message.chat.id),summpromo,getbalance(message.chat.id),users[8]),reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)




@bot.message_handler(content_types=['text'])
def create_promo(message):

    try:
        if message.text.isdigit():
            summ = int(message.text)
            if summ>maxpromo:
                bot.send_message(message.chat.id,f"Максимальная сумма промокода {maxpromo}")
                bot.register_next_step_handler(message, create_promo)
            elif summ<=0:
                bot.send_message(message.chat.id,f"Сумма должна быть больше 0")
                bot.register_next_step_handler(message, create_promo)
            else:
                letters = string.ascii_letters
                codecode = ( ''.join(random.choice(letters) for i in range(10)) )
                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"INSERT INTO promocode (summa,code)"
                            f"VALUES ({summ},\'{codecode}\')")
                con.commit()
                bot.send_message(message.chat.id,f"🤑 Ваш промокод: `{codecode}`",parse_mode='Markdown')
                bot.register_next_step_handler(message, main_message)


        else:
            bot.send_message(message.chat.id,"Введите число")

    except:
        pass




@bot.message_handler(content_types=['text'])
def workstatus(message):

    
    try:

        if ":" in message.text:

            m = message.text.split(":")

            if m[0].isdigit() and m[1].isdigit():
                if int(m[1])==1 or int(m[1])==0 or int(m[1])==2:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from users where id = {m[0]}")
                    est = cur.fetchone()[0]
                    con.commit()
                    if est == 0:
                        bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                        bot.register_next_step_handler(message, workstatus)
                    else:

                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"UPDATE users SET status = {int(m[1])} WHERE id = {int(m[0])}")
                        con.commit()    


                        
                        bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
                        bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                        bot.register_next_step_handler(message, main_message)

                else:
                    bot.send_message(message.chat.id,f"Можно ставить статус 0,1 или 2")
                    bot.register_next_step_handler(message, workstatus)     
            else:
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, workstatus)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, workstatus)
            
    except:
        pass


@bot.message_handler(content_types=['text'])
def verification(message):

    
    try:

        if ":" in message.text:

            m = message.text.split(":")

            if m[0].isdigit() and m[1].isdigit():
                if int(m[1])==1 or int(m[1])==2:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from users where id = {m[0]}")
                    est = cur.fetchone()[0]
                    con.commit()
                    if est == 0:
                        bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                        bot.register_next_step_handler(message, verification)
                    else:

                        if int(m[1]) == 1:
                            #verif_yes="✅"
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"UPDATE users SET verification = {int(m[1])} WHERE id = {int(m[0])}")
                            con.commit()    
                            bot.send_message(message.chat.id,f"Готово ! Аккаунт верифицирован у мамонта",reply_markup=rem)
                            bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                            bot.register_next_step_handler(message, main_message)
                        elif int(m[1]) == 2:
                            #verif_no="❌"
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"UPDATE users SET verification = {int(m[1])} WHERE id = {int(m[0])}")
                            con.commit()    
                            bot.send_message(message.chat.id,f"Готово ! Аккаунт не верифицирован у мамонта",reply_markup=rem)
                            bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                            bot.register_next_step_handler(message, main_message)
                        else:        
                            bot.send_message(message.chat.id,f"Неправильный формат данных")
                            bot.register_next_step_handler(message, verification)
                else:
                    bot.send_message(message.chat.id,f"Можно ставить статус верификации 1 или 2")
                    bot.register_next_step_handler(message, verification)     
            else:
                bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, verification)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, verification)
            
    except:
        pass

@bot.message_handler(content_types=['text'])
def freezy(message):

    
    try:

        if ":" in message.text:

            q = message.text.split(":")

            if q[0].isdigit() and q[1].isdigit():
                if int(q[1])== 1 or int(q[1])== 2:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from users where id = {q[0]}")
                    est = cur.fetchone()[0]
                    con.commit()
                    if est == 0:
                        bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                        bot.register_next_step_handler(message, freezy)
                    else:

                        if int(q[1]) == 2:
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"UPDATE users SET freezy = {2} WHERE id = {q[0]}")
                            con.commit()    
                            bot.send_message(message.chat.id,f"Готово ! 🧊 Аккаунт заморожен у мамонта 🧊",reply_markup=rem)
                            bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                            bot.register_next_step_handler(message, main_message)
                        elif int(q[1]) == 1:
                            con = sqlite3.connect("data.db")
                            cur = con.cursor()
                            cur.execute(f"UPDATE users SET freezy = {1} WHERE id = {q[0]}")
                            con.commit()    
                            bot.send_message(message.chat.id,f"Готово !🔥 Аккаунт разморожен у мамонта 🔥",reply_markup=rem)
                            bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                            bot.register_next_step_handler(message, main_message)
                        else:        
                            bot.send_message(message.chat.id,f"Неправильный формат данных")
                            bot.register_next_step_handler(message, freezy)
                else:
                    bot.send_message(message.chat.id,f"Можно ставить статус заморозки 1 или 2")
                    bot.register_next_step_handler(message, freezy)     
            else:
                bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, freezy)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, freezy)
            
    except:
        pass


@bot.message_handler(content_types=['text'])
def dobavleniebalance(message):

    
    try:

        if ":" in message.text:

            m = message.text.split(":")

            if m[0].isdigit() and m[1].isdigit():
                if int(m[1])>=0:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from users where id = {m[0]}")
                    est = cur.fetchone()[0]
                    con.commit()
                    if est == 0:
                        bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                        bot.register_next_step_handler(message, dobavleniebalance)
                    else:

                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"UPDATE users SET balance = {int(m[1])} WHERE id = {int(m[0])}")
                        con.commit()    


                        
                        bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
                        bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                        bot.register_next_step_handler(message, main_message)

                else:
                    bot.send_message(message.chat.id,f"Баланс должен быть больше 0")
                    bot.register_next_step_handler(message, dobavleniebalance)      
            else:
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, dobavleniebalance)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, dobavleniebalance)
            
    except:
        pass   



@bot.message_handler(content_types=['text'])
def replacecard(message):
    try:
        if message.chat.id in admins:
            newqiwi = message.text

            if newqiwi == otmena(lang(message.chat.id)):
                bot.send_message(message.from_user.id,f"Отменено",reply_markup=user(lang(message.chat.id)))
                bot.register_next_step_handler(message, main_message)
            else:

                if(message.text.isdigit()):



                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE card SET num = {int(message.text)}")
                    con.commit()

                    

                    bot.send_message(message.chat.id,f"Данные изменены",reply_markup=user(lang(message.chat.id)))
                    bot.register_next_step_handler(message, main_message)

                else:
                    bot.send_message(message.from_user.id,f"Напишите число")
                    bot.register_next_step_handler(message, replacecard)
                
            
            

        

    except:
        pass

@bot.message_handler(content_types=['text'])
def replacecard_mamont(message):

    try:    

        if(message.text.isdigit()):

            con = sqlite3.connect("data.db")
            cur = con.cursor()
            cur.execute(f"UPDATE users SET card = {int(message.text)} where id = {message.chat.id}")
            con.commit()


            bot.send_message(message.chat.id,f"Данные реквизитов изменены",reply_markup=user(lang(message.chat.id)))
            bot.register_next_step_handler(message, main_message)
            
        elif message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, "Отменено")
            bot.register_next_step_handler(message, main_message)

        else:
            bot.send_message(message.from_user.id,f"Напишите число")
            bot.register_next_step_handler(message, replacecard_mamont)
        
    except:
        pass

@bot.message_handler(content_types=['text'])
def replacecard_mamont_w(message):

    
    try:

        if ":" in message.text:

            m = message.text.split(":")

            if m[0].isdigit() and m[1].isdigit():
                if int(m[1])>=0:
                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from users where id = {m[0]}")
                    est = cur.fetchone()[0]
                    con.commit()
                    if est == 0:
                        bot.send_message(message.chat.id,f"Пользователь не найден в базе")
                        bot.register_next_step_handler(message, dobavleniebalance)
                    else:
                        
                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"UPDATE users SET card = {int(m[1])} where id = {int(m[0])}")
                        con.commit()

                        
                        bot.send_message(message.chat.id,f"Готово !",reply_markup=rem)
                        bot.send_message(message.chat.id,f"🐵 Воркер панель",reply_markup=workerpanel())
                        bot.register_next_step_handler(message, main_message)

                else:
                    bot.send_message(message.chat.id,f"Номер карты или BTC должен быть больше 0")
                    bot.register_next_step_handler(message, replacecard_mamont_w)      
            else:
                bot.send_message(message.chat.id,f"Неправильный формат данных")
                bot.register_next_step_handler(message, replacecard_mamont_w)
        elif message.text == "❌ ОТМЕНА":
            bot.send_message(message.from_user.id, glavnoemenu(lang(message.chat.id)),reply_markup=rem)
            bot.send_message(message.from_user.id, "Воркер панель⚙️",reply_markup=workerpanel())
            bot.register_next_step_handler(message, main_message)
                    
        else:
            bot.send_message(message.chat.id,f"Неправильный формат данных")
            bot.register_next_step_handler(message, replacecard_mamont_w)
            
    except:
        pass   



@bot.message_handler(content_types=['text'])
def replaceplatejka(message):
    if message.chat.id in admins:
        try:
            if(message.text.isdigit()):

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"UPDATE sposobaoplaty SET number = {int(message.text)}")
                con.commit()

                

                bot.send_message(message.chat.id,f"Данные изменены",reply_markup=user(lang(message.chat.id)))
                bot.register_next_step_handler(message, main_message)

            else:
                bot.send_message(message.from_user.id,f"Напишите число")
                bot.register_next_step_handler(message, replaceplatejka)
            
        except:
            pass



@bot.message_handler(content_types=['text'])
def prinyatieplateja(message):
    #user = get_user(message.chat.id)
    try:
        if message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, "Отменено")
            bot.register_next_step_handler(message, main_message)
        else:


            if message.text.isdigit():

                con = sqlite3.connect("data.db")
                cur = con.cursor()
                cur.execute(f"select count(*) from oplatac where id = {int(message.text)}")
                inn = cur.fetchone()[0]
                con.commit()

                if inn == 0:
                    bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
                    bot.register_next_step_handler(message, prinyatieplateja)
                else:

                    

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select summ from oplatac where id = {int(message.text)}")
                    isumm = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select balance from users where id = {int(message.text)}")
                    ibn = cur.fetchone()[0]
                    con.commit()

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select currency from users where id = {int(message.text)}")
                    curr = cur.fetchone()[0]
                    con.commit()


                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"UPDATE users SET balance = {ibn+isumm} where id = {int(message.text)}")
                    con.commit()

                    bot.send_message(int(message.text), opl(lang(int(message.text)),ibn+isumm,isumm,curr),reply_markup=user(lang(message.chat.id)))
                    bot.send_message(message.chat.id, "Готово!")
                    bot.register_next_step_handler(message, main_message)

            else:
                bot.send_message(message.chat.id, "Напишите число")
                bot.register_next_step_handler(message, prinyatieplateja)





        
    except:
        pass

@bot.message_handler(content_types=['text'])
def otklonplateja(message):
    try:
        
    
    
        if message.text == otmena(lang(message.chat.id)):
            bot.send_message(message.chat.id, "Отменено")
            bot.register_next_step_handler(message, main_message)
        else:
            if message.text.isdigit():

                    con = sqlite3.connect("data.db")
                    cur = con.cursor()
                    cur.execute(f"select count(*) from oplatac where id = {int(message.text)}")
                    inn = cur.fetchone()[0]
                    con.commit()

                    if inn == 0:
                        bot.send_message(message.chat.id, "ID Платежа не найден\nНапишите правильный айди")
                        bot.register_next_step_handler(message, otklonplateja)
                    else:
        
                        con = sqlite3.connect("data.db")
                        cur = con.cursor()
                        cur.execute(f"select id from oplatac where id = {int(message.text)}")
                        i = cur.fetchone()[0]
                        con.commit()

                        bot.send_message(i, neoplatil(lang(i)))
                        bot.send_message(message.chat.id, "Готово!",reply_markup=user(lang(message.chat.id)))
                        bot.register_next_step_handler(message, main_message)
            else:
                bot.send_message(message.chat.id, "Напишите число")
                bot.register_next_step_handler(message, otklonplateja)
    except:
        pass   

def delete_mamont(message):
    if message.text.isdigit():
        try:
            connect = sqlite3.connect("data.db")
            q = connect.cursor()
            res = q.execute(f"SELECT id FROM users where id = {message.text}").fetchone()
            if res is None:
                bot.send_message(message.chat.id, "<b>Мамонта нет в базе!</b>\n"\
                    "Проверьте id!",parse_mode="html",reply_markup=workerpanel())
            else:
                q.execute(f"DELETE FROM users where id = {message.text}")
                connect.commit()
                bot.send_message(message.chat.id, "Мамонт был успешно удален!",reply_markup=workerpanel())
        except Exception as e:
            bot.send_message(message.chat.id, "Произошла ошибка, попробуйте пожже",reply_markup=workerpanel())
            bot.send_message(coder, "Произошла ошибка при удалении мамонта\n"\
                f"{e}")
    else:
        bot.send_message(message.chat.id, "Не вверные данные",reply_markup=workerpanel())

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True, interval=0)
        except Exception as e:
            print(extract_tb(exc_info()[2])[0][1])
            print(e)
            bot.send_message(coder, f"Произошла ошибка {e}\n"\
                "Обратитесь к кодера @jambo_squirt")
            time.sleep(5)