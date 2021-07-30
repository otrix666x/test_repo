# -*- coding: utf8 -*-
import telebot
from telebot import types
import json
from config import maxbalancestatus0,maxbalancestatus2
from baza import lang
from baza import *
from datetime import datetime
from random import randint
#kursrublya2 = 73

selectlanguage = "Выберите язык 🇷🇺\n\nSelect language 🇺🇸"

def langselect():
    langs = types.InlineKeyboardMarkup()
    lang1 = types.InlineKeyboardButton(text="🇷🇺 Rus", callback_data="language1")
    lang2 = types.InlineKeyboardButton(text="🇺🇸 Eng", callback_data="language2")

    langs.add(lang1)
    langs.add(lang2)

    return langs

def langedit():
    langs = types.InlineKeyboardMarkup()
    lang1 = types.InlineKeyboardButton(text="🇷🇺 Rus", callback_data="language1_1")
    lang2 = types.InlineKeyboardButton(text="🇺🇸 Eng", callback_data="language2_2")

    langs.add(lang1)
    langs.add(lang2)

    return langs

def perevod(l,card,summa,currency,comm):
    if l == 1:
        textp = f"Переведите {summa} {currency} на карту\n\nНомер: {card}\nКомментарий: {comm}\n\nВнимание, если нет возможности оставить комментарий к платёжу, пришлите чек об успешной оплате в тех.поддержку, это ускорит зачисление средств на ваш баланс, а так же, платежи без комментариев зачисленны не будут, сверяйте пожалуйста реквизиты, спасибо!"
    else:
        textp = f"Transfer {summa} {currency} to card\n\nNumber: {card}\nComment: {comm}\n\nAttention, if it is not possible to leave a comment on the payment, send a check of successful payment to technical support, this will speed up the crediting of funds to your balance, and also, payments without comments will not be credited, please check the details, thank you!"
    return textp    


def opl(l,summ,skolko,currency):
	if l == 1:
		oplt = f"Ваш баланс успешно пополнен\n\nСумма пополнения : {skolko} {currency}\nВаш текущий баланс {summ} {currency}"
	else:
		oplt = f"Your balance has been successfully replenished \n\nTop amount: {skolko} {currency} \nYour current balance is {summ} {currency}"
	return oplt	

def provp(l):
    if l ==1:
        provt = "⏳ Ваш платеж проверяется,подождите..."
    else:
        provt = "Your payment is being verified, please wait..."
    
    return provt
    
# def provp2(l):
    # if l ==1:
        # provt2 = "⏳ Ваш платеж проверяется,подождите..."
    # else:
        # provt2 = "Your payment is being verified, please wait..."
    
    # return provt2
    

def tipakcii(l):
    if l ==1:
        tpa = "Выберите тип акции"
    else:
        tpa = "Select the type of promotion"

    return tpa

tpa1 = '🌕 КРИПТОВАЛЮТА'
tpa2 = '📈 АКЦИИ'
tpa3 = '💶 ФИАТ'

tpa4 = '🌕 CRYPTOCURRENCY'
tpa5 = '📈 PROMOTIONS'
tpa6 = '💶 FIAT'

        



def tps(l):

    if l ==1:
        
        ft = types.ReplyKeyboardMarkup(True)
        f1 = types.KeyboardButton(tpa1)
        f2 = types.KeyboardButton(tpa2)
        f3 = types.KeyboardButton(tpa3)
        f7 = types.KeyboardButton(otmena(l))

        ft.add(f1)    
        #ft.add()
        ft.add(f3,f2)
        
        ft.add(f7)

    else:

        ft = types.ReplyKeyboardMarkup(True)
        f1 = types.KeyboardButton(tpa4)
        f2 = types.KeyboardButton(tpa5)
        f3 = types.KeyboardButton(tpa6)
        f7 = types.KeyboardButton(otmena(l))

        ft.add(f1)    
        ft.add(f2)
        ft.add(f3)   
        
        ft.add(f7)
    return ft

activ1 = "AMAZON"
activ2 = "APPLE"
activ3 = "NEWMONT"
activ4 = "NEXTERA ENERGY"
activ5 = "TESLA"
activ6 = "BROADCOM"


factiv1 = "RUB"
factiv2 = "USD"
factiv3 = "EUR"
factiv4 = "UAH"
factiv5 = "KZT"
factiv6 = "PLN"

#cactiv0 = "Cryptocurrency"
cactiv1 = "BITCOIN"
cactiv2 = "CARDANO"
cactiv3 = "DOGE"
cactiv4 = "ETHEREUM"
cactiv5 = "LITECOIN"
cactiv6 = "VERTCOIN"    


def fiat(l):
    fact = types.ReplyKeyboardMarkup(True)
    factiv_btn0 = types.KeyboardButton(currencyprice(l))
    factiv_btn1 = types.KeyboardButton(factiv1)
    factiv_btn2 = types.KeyboardButton(factiv2)
    factiv_btn3 = types.KeyboardButton(factiv3)
    factiv_btn4 = types.KeyboardButton(factiv4)
    factiv_btn5 = types.KeyboardButton(factiv5)
    factiv_btn6 = types.KeyboardButton(factiv6)
    factiv_btn7 = types.KeyboardButton(otmena(l))

    fact.add(factiv_btn0) 
    fact.add(factiv_btn1,factiv_btn2,factiv_btn3)  
    fact.add(factiv_btn4,factiv_btn5,factiv_btn6)   
    fact.add(factiv_btn7)
    return fact

def crypto(l):
    cact = types.ReplyKeyboardMarkup(True)
    cactiv_btn0 = types.KeyboardButton(cryptocurrency(l))
    cactiv_btn1 = types.KeyboardButton(cactiv1)
    cactiv_btn2 = types.KeyboardButton(cactiv2)
    cactiv_btn3 = types.KeyboardButton(cactiv3)
    cactiv_btn4 = types.KeyboardButton(cactiv4)
    cactiv_btn5 = types.KeyboardButton(cactiv5)
    cactiv_btn6 = types.KeyboardButton(cactiv6)
    cactiv_btn7 = types.KeyboardButton(otmena(l))

    cact.add(cactiv_btn0)
    cact.add(cactiv_btn1,cactiv_btn2,cactiv_btn3)   
    cact.add(cactiv_btn4,cactiv_btn5,cactiv_btn6)   
    cact.add(cactiv_btn7)
    return cact


def akcii(l):
    act = types.ReplyKeyboardMarkup(True)

    activ_btn0 = types.KeyboardButton(companycurrency(l))
    activ_btn1 = types.KeyboardButton(activ1)
    activ_btn2 = types.KeyboardButton(activ2)
    activ_btn3 = types.KeyboardButton(activ3)
    activ_btn4 = types.KeyboardButton(activ4)
    activ_btn5 = types.KeyboardButton(activ5)
    activ_btn6 = types.KeyboardButton(activ6)
    activ_btn7 = types.KeyboardButton(otmena(l))

    act.add(activ_btn0)
    act.add(activ_btn1,activ_btn2,activ_btn3)  
    act.add(activ_btn4,activ_btn5,activ_btn6)  
    act.add(activ_btn7)
    return act





#---------------------------------------------------------------------------

def pravila(l):
    if l == 1:

        prav = "Политика и условия пользования данным ботом.\n\
        1. Перед принятием инвестиционного решения Инвестору необходимо самостоятельно оценить экономические риски и выгоды, налоговые, юридические, бухгалтерские последствия заключения сделки, свою готовность и возможность принять такие риски. Клиент также несет расходы на оплату брокерских и депозитарных услуг\n\
        2. Принимая правила, Вы подтверждаете своё согласие со всеми вышеперечисленными правилами!\n\
        3. Ваш аккаунт может быть заблокирован в подозрении на мошенничество/обман нашей системы! Каждому пользователю необходима верификация для вывода крупной суммы средств.\n\
        4. Мультиаккаунты запрещены!\n\
        5. Скрипты, схемы, тактики использовать запрещено!\n\
        6. Если будут выявлены вышеперечисленные случаи, Ваш аккаунт будет заморожен до выяснения обстоятельств!\n\
        "
    else:
        prav = "Policy and terms of use of this bot.\n\
        1. Before making an investment decision, the Investor must independently assess the economic risks and benefits, tax, legal, accounting consequences of concluding a transaction, his willingness and ability to accept such risks. The client also bears the costs of paying for brokerage and custody services\n\
        2. By accepting the rules, you confirm your agreement with all of the above rules!\n\
        3. Your account may be blocked on suspicion of fraud / deception of our system! Each user needs verification to withdraw a large amount of funds.\n\
        4. Multi-accounts are prohibited!\n\
        5. It is forbidden to use scripts, schemes, tactics!\n\
        6.If the above cases are identified, your account will be frozen until the circumstances are clarified!\n\
        "
    return prav 



workerinfo = f"Статус 1 - всегда проигрыш (обозначение 👎🏻)\n\nСтатус 0 - мамонт будет выигрывать пока у него баланс меньше {maxbalancestatus0},после того как баланс увелечится статус автоматичкесий изменится на 1 - всегда проигрыш\nНа этом статусе ставка на ровно будет проигрыш.(обозначение 👍🏻)\n\nСтатус 2:Любая cтавка будет выигрыш пока у него баланс меньше {maxbalancestatus2},после того как баланс увелечится статус автоматичкесий изменится на 1 - всегда проигрыш (обозначение 🤟🏻)\n\nДефолтом стоит статус - 0\n\n\nВерификация аккаунта мамонта 1 - это аккаунт верифицрован (обозначение ✅), а 2 - это не верифицирован (обозначение ❌), по дефолту стоит 2.\n\n\nЗаморозка акаканта мамонта, 1 это обычное состояние (обозначение ☀️), 2  это заморозка аккаунта (обозначение ⛄️)."

def prinyat(l):
    if l == 1:
        prinyat1 = "Принять правила ✅"
    else:
        prinyat1 = "Accept the rules ✅"

    return prinyat1

def izmenit_cc(l):
    if l == 1:
        izmenit_cc1 = "💳 Изм. карту"
    else:
        izmenit_cc1 = "💳 Change c. card"

    return izmenit_cc1
    
def izmenit_btc(l):
    if l == 1:
        izmenit_btc1 = "💠 Изм. BTC адрес"
    else:
        izmenit_btc1 = "💠 Chg. BTC address"

    return izmenit_btc1

def posmotret_cc(l):
    if l == 1:
        posmotret_cc1 = "👀 Показ. карту"
    else:
        posmotret_cc1 = "👀 See c. card"

    return posmotret_cc1
    
def posmotret_btc(l):
    if l == 1:
        posmotret_btc1 = "👀 Показ. BTC адрес"
    else:
        posmotret_btc1 = "👀 See BTC addr."

    return posmotret_btc1
        
def select_currency(l):
    if l == 1:
        text = 'Выберите валюту'
    else:
        text = 'Select currency'

    return text

def convert(l):
    if l == 1:
        text = '♻️ Конвертация валют'
    else:
        text = '♻️ Currency conversion'
    return text

def start(l):
    if l == 1:
        start1 = "Приветствую!"
    else:
        start1 = "Welcome !"
    return start1   

def start2(l):
    if l == 1:
        start21 = "Приветствую снова!"
    else:
        start21 = "Hello again !"
    return  start21



def chenge_reki_t_b(l):
    if l ==1:
        why_verif1 = "📋 РЕКВИЗИТЫ"
    else:
        why_verif1 = "📋 REQUISITES"

    return why_verif1

def no_verif_reki(l):
    if l ==1:
        why_verif1 = "🔒 Доступ к управлению реквизитами закрыт, пройдите пожалуйста верификацию и вы сможете менять и удалять реквизиты."
    else:
        why_verif1 = "🔒 Access to account management is closed, please go through verification and you will be able to change and delete details."

    return why_verif1

def yes_verif_reki(l):
    if l ==1:
        why_verif1 = "⚙ Управление финансовыми реквизитами"
    else:
        why_verif1 = "⚙ Management of financial details"

    return why_verif1


def why_verif_t_b(l):
    if l ==1:
        why_verif1 = "📛 ВЕРИФИКАЦИЯ"
    else:
        why_verif1 = "📛 VERIFICATION"

    return why_verif1

def go_verif(l):
    if l ==1:
        go_verif1 = "К сожалению, ваш аккаунт не верифцирован, рекомендуем верифицировать аккаунт, вы можете это сделать, нажав на кнопку ниже и написав 'Верификация' в тех.поддержку, спасибо!\n\n1️⃣  Приоритет в очереди к выплате.\n2️⃣  Отсутствие лимитов на вывод средств.\n3️⃣  Возможность хранить средства на балансе бота в криптовалюте.\n4️⃣  Увеличение доверия со стороны администрации, предотвращения блокировки аккаунта.\n"
    else:
        go_verif1 = "Unfortunately, your account has not been verified, we recommend that you verify your account, you can do this by clicking on the button below and writing 'Verification' to technical support, thank you! \n\n1️⃣ Priority in the payout queue. \n2️⃣ Lack of withdrawal limits.\n3️⃣ Ability to store funds on the balance of the bot in cryptocurrency.\n4️⃣ Increase trust on the part of the administration, prevent account blocking.\n"

    return go_verif1

def already_verif(l):
    if l ==1:
        already_verif1 = "Поздравляем , ваш аккаунт верифицирован ✅\n\n✅  Приоритет в очереди к выплате.\n✅  Отсутствие лимитов на вывод средств.\n✅  Возможность хранить средства на балансе бота в криптовалюте.\n✅  Увеличение доверия со стороны администрации, предотвращения блокировки аккаунта.\n"
    else:
        already_verif1 = "Congratulations, your account has been verified ✅\n\n✅ Priority in the queue for payment. \n✅ Absence of limits on withdrawal of funds. \n✅ Ability to store funds on the balance of the bot in cryptocurrency. \n✅ Increase trust from the administration, prevent account blocking. \n"

    return already_verif1
#def cabinet(l,balance,currency,id,randomonline):
   # if l == 1:
    #    cab = f"👨‍💻   Личный кабинет\n\n💵   Баланс: {balance} {currency}\n\n📛   Верификация : ❌\n\n📊   Рейтинг: 🏅\n\n🆔   Ваш ID : {id}\n\n🌐   Сделок онлайн - {randomonline} 💡"
   # else:
    #    cab = f"👨‍💻 Personal account\n\n💵 Balance: {balance} {currency}\nVerification : ❌\nYour ID: {id}\nTransactions online - {randomonline} 🟢"
    #return cab  

def cabinet(l,name,balance,currency,verification,card,id):
    verif_yes="✅"
    verif_no="❌"
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    randomonline = randint(1101,3601)
    if l == 1:
        if verification == 1:
            cab = f"👨‍💻 ВАШ ПРОФИЛЬ {name}\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️\n\n💵 БАЛАНС : <b>{balance}</b> {currency}\n\n📛 ВЕРИФИКАЦИЯ : {verif_yes}\n\n🏦 РЕКВИЗИТЫ : <b>{card[:4]} **** **** {card[-4:]}</b>\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️\n\n🆔 ВАШ ID : {id}\n\n👨‍💻 ОНЛАЙН - {randomonline}\n\n⏰ ВРЕМЯ : {time}\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️"
        else :
            cab = f"👨‍💻 ВАШ ПРОФИЛЬ {name}\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️\n\n💵 БАЛАНС : <b>{balance}</b> {currency}\n\n📛 ВЕРИФИКАЦИЯ : {verif_no}\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️\n\n🆔 ВАШ ID : {id}\n\n👨‍💻 ОНЛАЙН - {randomonline}\n\n⏰ ВРЕМЯ : {time}\n\n▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️▪️◾️▪️◼️"

    else:
        if verification == 1:
            cab = f"👨‍💻 Personal account\n\n💵 Balance: {balance} {currency}\n\n📛 Verification status: {verif_yes}\n\n🆔 Your user ID: {id}\n\nNumber of transactions online - {randomonline}💡\n\n Time\Date : {time}"
        else :
            cab = f"👨‍💻 Personal account\n\n💵 Balance: {balance} {currency}\n\n📛 Verification status: {verif_no}\n\n🆔 Your user ID: {id}\n\nNumber of transactions online - {randomonline} 💡\n\n Time\Date : {time}"

            #cab = f"👨‍💻 Personal account\n\n💵 Balance: {balance} {currency}\n\n📛 Verification status: {verification}\n\n🆔 Your user ID: {id}\n\nNumber of transactions online - {randomonline} 💡"
    return cab


def select(l):
    if l == 1:
        select2 = "Выберите актив."
    else:
        select2 = "Select an asset."
    return  select2 

def qiwiorpromo(l):
    if l == 1:
        qiwiorpromo2 = "Выберите вариант пополнения баланса"
    else:
        qiwiorpromo2 = "Choose a way to top up your balance"
    return qiwiorpromo2

def textlivevp(l):
    if l == 1:
        textotzyv2 = "В данном разделе вы можете подписаться на канал выплат, найти свои выплаты, а так же посмотреть на выплаты других участников."
    else:
        textotzyv2 = "In this section, you can subscribe to the payment channel, find your payments, as well as look at the payments of other participants."
    return   textotzyv2

def textotzyv(l):
    if l == 1:
        textotzyv2 = "Оставить свой отзыв, и прочитать отзывы других пользователей можете тут.\n\nОставьте свой отзыв и получите +5% на следующее пополнение."
    else:
        textotzyv2 = "You can leave your review and read reviews of other users here.\n\nLeave your review and get ( +5% ) on the next replenishment."
    return   textotzyv2

def freezy_t(l):
    if l == 1:
        textozreezy = "🤵 Здравствуйте, к сожалению ваш аккаунт заморожен системой безопасности, вам рекомендуется верицировать аккаунт, для выяснения обстоятельсвт и дальнейших действий, обратитесь в тех. поддержку, спасибо!"
    else:
        textofreezy = "🤵 Hello, unfortunately your account is frozen by the security system, you are advised to verify your account, to find out the circumstances and further actions, contact those. support, thank you!"
    return  textozreezy

def userbtn_frz(l):
    if l == 1:
        userbtn12frz = "🔐 Разморозить аккаунт"
    else:
        userbtn12frz = "🔐 Unfreeze account"
    return  userbtn12frz



def userbtn1(l):
    if l == 1:
        userbtn12 = "⚡️ МОИ АКТИВЫ"
    else:
        userbtn12 = "⚡️ My assets"
    return  userbtn12

def userbtn2(l):
    if l == 1:
        userbtn22 = "💼 ПРОФИЛЬ"
    else:
        userbtn22 = "💼 Account"
    return  userbtn22   

def edit_currency(l):
    if l == 1:
        text = "💱 ВАЛЮТА"
    else:
        text = "💱 CURRENCY"
    return 	text

def edit_language(l):
    if l == 1:
        text = "🌏 ЯЗЫК"
    else:
        text = "🌏 LANGUAGE"
    return  text

def edit_end_language(l):
    if l == 1:
        text = "🌐 Вы изменили язык"
    else:
        text = "🌐 You changed the language"
    return  text

def userbtn3(l):
    if l == 1:
        userbtn32 = "🔺 ПОПОЛНЕНИЕ 🔺"
    else:
        userbtn32 = "🔺 Top up 🔺"
    return  userbtn32       


def userbtn4(l):
    if l == 1:
        userbtn42 = "🔻 ВЫВОД 🔻"
    else:
        userbtn42 = "🔻 Withdraw 🔻"
    return  userbtn42   

def userbtn7(l):
    if l == 1:
        userbtn72 = "📝 ОТЗЫВЫ"
    else:
        userbtn72 = "📝 REVIEW"
    return  userbtn72       


def userbtn8(l):
    if l == 1:
        userbtn82 = "❔ ИНФОРМАЦИЯ"
    else:
        userbtn82 = "❔ INFORMATION"
    return  userbtn82  


def userbtn5(l):
    if l == 1:
        userbtn62 = "👨‍💻 ПОМОЩЬ"
    else:
        userbtn62 = "🛠 Tech Support"
    return  userbtn62
    
def userbtn_tehsup(l):
    if l == 1:
        userbtntehsup = "🛠 Тех Поддержка"
    else:
        userbtntehsup = "🛠 Tech Support"
    return  userbtntehsup

def userbtn6(l):
    if l == 1:
        userbtn52 = "🔴 LIVE ВЫПЛАТЫ"
    else:
        userbtn52 = "🔴 LIVE PAYMENTS"
    return  userbtn52   

 
def otmena(l):
    if l == 1:
        otmena2 = "❌ ОТМЕНА"
    else:
        otmena2 = "❌ CANCEL"
    return  otmena2

def cryptocurrency(l):
    if l == 1:
        cryptocur = "💹 КУРС КРИПТОВАЛЮТЫ ОНЛАЙН"
    else:
        cryptocur = "💹 ONLINE COURSE"
    return  cryptocur

def companycurrency(l):
    if l == 1:
        соmpanycur = "💹 КУРС АКЦИЙ ОНЛАЙН"
    else:
        соmpanycur = "💹 ONLINE COURSE"
    return  соmpanycur

def currencyprice(l):
    if l == 1:
        pricecur = "💹 ЦЕНА ФИАТОВ ОНЛАЙН"
    else:
        pricecur = "💹 ONLINE FIAT COURSE"
    return  pricecur

def verx(l):

    if l == 1:
        verx2 = "📈 ВВЕРХ"
    else:
        verx2 = "📈 TOP"
    return  verx2

def vniz(l):
    if l == 1:
        vniz2 = "📉 ВНИЗ"
    else:
        vniz2 = "📉 DOWN"
    return  vniz2

def rovno(l):
    if l == 1:
        rovno2 = "🔒 НЕ ИЗМЕНИТСЯ"
    else:
        rovno2 = "🔒 WILL NOT CHANGE"
    return  rovno2

def balanceqiwi(l):
    if l == 1:
        balanceqiwi2= "💳 ПОПОЛНИТЬ С КАРТЫ"
    else:
        balanceqiwi2= "💳 TOP UP FROM TO CARD"
    return  balanceqiwi2

def balancebtc(l):
    if l == 1:
        balancebtc2= "💠 ПОПОЛНИТЬ С BTC"
    else:
        balancebtc2= "💠 TOP UP WITH BTC"
    return  balancebtc2

def balanceforma(l):
    if l == 1:
        balanceforma2= "📲 ФОРМА ОПЛАТЫ КАРТОЙ"
    else:
        balanceforma2= "📲 CARD PAYMENT FORM"
    return  balanceforma2

def balancepromo(l):
    if l == 1:
        balancepromo2 = "🧾 ПРОМОКОД"
    else:
        balancepromo2 = "🧾 PROMOCODE"
    return balancepromo2

def neoplatil(l):
    if l == 1:
        neoplatil2 = "⚠️Вы не оплатили⚠️\n\nОплатите заказ после чего нажмите \"Проверить оплату\""
    else:
        neoplatil2 = "⚠️You didn't pay \n\nPay for the order and then click \"Check payment \""

    return  neoplatil2
def oplata(l):

    if l == 1:      
        oplata2 = "ОПЛАТИТЬ"
    else:
        oplata2 = "PAY"
    return oplata2
def proverit(l):
    if l == 1:
        proverit2 = "ПРОВЕРИТЬ"
    else:
        proverit2 = "CHECK"
    return proverit2

def glavnoemenu(l):
    if l == 1:

        glavnoemenu2 = "Главное меню"
    else:
        glavnoemenu2 = "Main menu"

    return glavnoemenu2 
        

def stavkasdelana(l):
    if l == 1:
        stavkasd = "Ставка сделана ✅"
    else:
        stavkasd = "Bet placed ✅"
    return  stavkasd

def idetraschyot(l):
    if l == 1:
        idet = "Идёт рассчёт. . ."
    else:
        idet = "Calculation in progress..."
    return  idet

def podnyalsa(l,p):
    if l == 1:
        pp = f"Курс поднялся 📈 на {p} % "
    else:
        pp = f"The rate has risen 📈 by {p} % "
    return  pp

def upal(l,p):
    if l == 1:
        uu = f"Курс упал 📉 на {p} % "
    else:
        uu = f"The rate fell 📉 by {p} % "
    return  uu

def podnyal(l):
    if l == 1:
        ppp = f"Курс поднялся 📈 на "
    else:
        ppp = f"The rate has risen by "
    return  ppp


def up(l):
    if l == 1:
        uuu = f"Курс упал 📉 на "
    else:
        uuu = f"The rate fell by "
    return uuu

def cenaakcii(l):
    if l == 1:
        cen = "⌛️| Цена акции на данный момент:"
    else:
        cen = "⌛️ | Promotion price:"
    return cen

def cenaakcii2(l):
    if l == 1:
        cen2 = "⏳| Цена акции на данный момент:"
    else:
        cen2 = "⏳ | Promotion price:"
    return cen2 

def neizmenilsa(l):
    if l == 1:
        ne = f"Курс не изменился 🔒"
    else:
        ne = f"Course has not changed 🔒"
    return ne


def verno(l,res,balance):
    if l == 1:
        res = f"🤑 Ваш прогноз оказался верным 👍\n\n{res}\n\nЕсли хотите сыграть еще, введите сумму ставки\nДоступный баланс: {balance}"
    else:
        res = f"🤑 Your prediction turned out to be correct 👍\n\n{res}\n\nIf you want to play again, please enter the bet amount \nAvailable balance: {balance}"
    return res

def neverno(l,res,balance):
    if l == 1:
        res2 = f"😔 Неверный прогноз 👐\n\n{res}\n\nЕсли хотите сыграть еще, введите сумму ставки\nДоступный баланс: {balance}"
    else:
        res2  = f"😔 Wrong prediction 👐\n\n{res}\n\nIf you want to play more, enter your bets\nAvailable balance: {balance}"
    return  res2


def wrongpromo(l):
    if l == 1:
        wp = "❗️ Промокод неправильный или уже использовался"
    else:
        wp = "❗️ The promo code is incorrect or has already been used"
    return  wp


def donepromo(l,summpromo,balance,currency):
    if l == 1:
        dp = f"♻️ Ваш баланс пополнен на {summpromo} {currency}\n\n💰 Баланс {balance}"
    else:
        dp = f"♻️ Your balance has been replenished with {balance} {currency}\n\n💰 Balance {balance}"
    return  dp


    

def vybor(l,akcia,minstavka_rub,minstavka_uah,minstavka_eur,minstavka_byn,minstavka_usd,minstavka_pln,balance,currency):
    if l == 1:

        if currency == 'RUB':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_rub} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo

        elif currency == 'UAH':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_uah} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo

        elif currency == 'EUR':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_eur} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo

        elif currency == 'BYN':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_byn} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo

        elif currency == 'USD':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_usd} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo

        elif currency == 'PLN':

            if akcia == 'BITCOIN':
                oo = f"Битко́йн, или битко́ин, — пиринговая платёжная система, использующая одноимённую единицу для учёта операций. Для обеспечения функционирования и защиты системы используются криптографические методы, но при этом вся информация о транзакциях между адресами системы доступна в открытом виде.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano — блокчейн платформа, которую создали компания Input Output Hong Kong и Чарльз Хоскинсон, бывший соучредитель BitShares, Ethereum и Ethereum Classic. Система ориентирована на запуск смарт-контрактов, децентрализованных приложений, сайдчейнов и многопартийных вычислений.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum — криптовалюта и платформа для создания децентрализованных онлайн-сервисов на базе блокчейна, работающих на базе умных контрактов. Реализована как единая децентрализованная виртуальная машина\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin — криптовалюта, основанная на Litecoin. Названа в честь интернет-мема Doge. Была представлена 8 декабря 2013 года. В отличие от других криптовалют Dogecoin имеет достаточно быстрый период изначального майнинга. На конец 2014 года в обороте находилось 98 млрд DOGE.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin — форк Bitcoin, пиринговая электронная платёжная система, использующая одноимённую криптовалюту. Litecoin является вторым после Namecoin форком Bitcoin и имеет лишь небольшие отличия от него.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin - это криптовалюта с открытым исходным кодом, созданная в начале 2014 года и ориентированная на децентрализацию. Vertcoin использует устойчивый к ASIC механизм Proof-of-Work для выпуска новых монет и стимулирования майнеров к защите сети и проверке транзакций.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon — американская компания, крупнейшая в мире на рынках платформ электронной коммерции и публично-облачных вычислений по выручке и рыночной капитализации. Штаб-квартира — в Сиэтле.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla — американская компания, производитель электромобилей и (через свой филиал SolarCity) решений для хранения электрической энергии\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple — американская корпорация, производитель персональных и планшетных компьютеров, аудиоплееров, смартфонов, программного обеспечения.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. — американская компания по разработке полупроводниковой продукции со штаб-квартирой в Сан-Хосе, Калифорния. На счету компании более 5000 патентов.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"Корпорация Newmont, базирующаяся в Гринвуд-Виллидж, Колорадо, США, является крупнейшей в мире золотодобывающей компанией. Основанная в 1921 году, она владеет золотыми приисками в Неваде, Колорадо, Онтарио, Квебеке, Мексике, Доминиканской Республике, Австралии, Гане, Аргентине, Перу и Суринаме.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. — энергетическая компания из списка Fortune 200 с генерирует около 45 900 мегаватт электроэнергии, имеет выручку более 17 миллиардов долларов за 2017 год. Включает в себя следующие дочерние компании Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners и NextEra Energy Services.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            else:
                oo = f"Фидуциарные, фиатные, символические, бумажные, кредитные, необеспеченные деньги — не обеспеченные золотом и другими драгоценными металлами деньги, номинальная стоимость которых устанавливается и гарантируется государством вне зависимости от стоимости материала, использованного для их изготовления.\n\nВы выбрали {akcia}\nМинимальная сумма инвестиций - {minstavka_pln} {currency}\n\nВаш баланс: {balance} {currency}"
            return  oo
    else :
        if currency == 'RUB':
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            return  oo

        elif currency == 'UAH':
            
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_uah} {currency}\n\nYour balance: {balance} {currency}"
            return  oo

        elif currency == 'EUR':
            
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_eur} {currency}\n\nYour balance: {balance} {currency}"
            return  oo
        elif currency == 'USD':
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_rub} {currency}\n\nYour balance: {balance} {currency}"
            return  oo

        elif currency == 'BYN':
            
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_byn} {currency}\n\nYour balance: {balance} {currency}"
            return  oo

        elif currency == 'PLN':
            
            if akcia == 'BITCOIN':
                oo = f"Bitcoin, is a peer-to-peer payment system that uses the unit of the same name to record transactions. To ensure the functioning and protection of the system, cryptographic methods are used, but at the same time all information about transactions between system addresses is available in clear text.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'CARDANO':
                oo = f"Cardano is a blockchain platform created by Input Output Hong Kong and Charles Hoskinson, the former co-founder of BitShares, Ethereum and Ethereum Classic. The system is focused on launching smart contracts, decentralized applications, sidechains and multiparty computing.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'ETHEREUM':
                oo = f"Ethereum is a cryptocurrency and platform for creating decentralized blockchain-based online services powered by smart contracts. Implemented as a single decentralized virtual machine\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'DOGE':
                oo = f"Dogecoin is a Litecoin based cryptocurrency. Named after the Internet meme Doge. It was introduced on December 8, 2013. Unlike other cryptocurrencies, Dogecoin has a fairly fast initial mining period. At the end of 2014, there were 98 billion DOGE in circulation.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'LITECOIN':
                oo = f"Litecoin is a fork of Bitcoin, a peer-to-peer electronic payment system using the cryptocurrency of the same name. Litecoin is the second Bitcoin fork after Namecoin and has only minor differences from it.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'VERTCOIN':
                oo = f"Vertcoin is an open source cryptocurrency created in early 2014 and focused on decentralization. Vertcoin uses an ASIC-resistant Proof-of-Work mechanism to issue new coins and incentivize miners to secure the network and verify transactions.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'AMAZON':
                oo = f"Amazon is an American company with the largest e-commerce and public cloud computing platform in the world in terms of revenue and market capitalization. The headquarters is in Seattle.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'TESLA':
                oo = f"Tesla is an American company that makes electric vehicles and (through its subsidiary SolarCity) storage solutions for electrical energy.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'APPLE':
                oo = f"Apple is an American corporation that manufactures personal and tablet computers, audio players, smartphones, and software.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'BROADCOM':
                oo = f"Broadcom Inc. Is an American semiconductor development company headquartered in San Jose, California. The company has over 5,000 patents.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEWMONT':
                oo = f"The Newmont Corporation, based in Greenwood Village, Colorado, USA, is the world's largest gold mining company. Founded in 1921, it owns gold mines in Nevada, Colorado, Ontario, Quebec, Mexico, Dominican Republic, Australia, Ghana, Argentina, Peru and Suriname.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'NEXTERA ENERGY':
                oo = f"NextEra Energy, Inc. is a Fortune 200 power company with approximately 45,900 megawatts of electricity generating over $ 17 billion in 2017 revenues. Includes subsidiaries Florida Power & Light, NextEra Energy Resources, NextEra Energy Partners and NextEra Energy Services.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'RUB':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'USD':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'EUR':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'UAH':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            elif akcia == 'KZT':
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            else:
                oo = f"Fiduciary, fiat, symbolic, paper, credit, unsecured money - money not backed by gold and other precious metals, the nominal value of which is set and guaranteed by the state, regardless of the cost of the material used for their manufacture.\n\nYou have chosen {akcia}\nMinimum investment amount - {minstavka_pln} {currency}\n\nYour balance: {balance} {currency}"
            return  oo

def ugaday(l):
    if l ==1:
        ug = f"Вам нужно угадать куда пойдет курс актива через 5 секнуд\n\nЕсли прогноз будет верным ваш выигрыш :\n\nВверх - x2 от ставки\nНе изменится - x100 от ставки\nВниз - x2 от ставки"
    else:
        ug = f"You need to guess where the asset's course will go in 5 seconds\n\nIf the forecast is correct, your winnings will be\nUp - x2 from the bet\nNot change - x100 from the bet\nDown - x2 from the bet"
    return  ug


def printpromo(l):
    if l ==1:
        prp = "Напишите свой промокод"
    else:
        prp = "Write your promo code"
    return  prp

def printsumm(l,minimalka_rub,minimalka_uah,minimalka_eur,minimalka_byn,minimalka_usd,minimalka_pln,currency):

    if l ==1:
        if currency == 'RUB':
            psm = f"💰 Введите сумму пополнения от {minimalka_rub} {currency}:\n\n(например, если вы хотите пополнить баланс на 1000 {currency}, отправьте сюда в чат, желаемую сумму пополнения)"   
        elif currency == 'UAH':
            psm = f"💰 Введите сумму пополнения от {minimalka_uah} {currency}:\n\n(например, если вы хотите пополнить баланс на 500 {currency},  отправьте сюда в чат, желаемую сумму пополнения)"   
        elif currency == 'EUR':
            psm = f"💰 Введите сумму пополнения от {minimalka_eur} {currency}:\n\n(например, если вы хотите пополнить баланс на 100 {currency},  отправьте сюда в чат, желаемую сумму пополнения)"   
        elif currency == 'BYN':
            psm = f"💰 Введите сумму пополнения от {minimalka_byn} {currency}:\n\n(например, если вы хотите пополнить баланс на 100 {currency},  отправьте сюда в чат, желаемую сумму пополнения)"   
        elif currency == 'USD':
            psm = f"💰 Введите сумму пополнения от {minimalka_usd} {currency}:\n\n(например, если вы хотите пополнить баланс на 100 {currency},  отправьте сюда в чат, желаемую сумму пополнения)"   
        else:
            psm = f"💰 Введите сумму пополнения от {minimalka_pln} {currency}:\n\n(например, если вы хотите пополнить баланс на 100 {currency},  отправьте сюда в чат, желаемую сумму пополнения)"     
    else:
        if currency == 'RUB':
            psm = f"💰 Enter the amount of replenishment from {minimalka_rub} {currency}:\n\n(for example, if you want to top up the balance by 1000 {currency}, send the message ‘1000’, without quotes to the chat)"   
        elif currency == 'UAH':
            psm = f"💰 Enter the amount of replenishment from {minimalka_uah} {currency}:\n\n(for example, if you want to top up the balance by 500 {currency}, send the message ‘1000’, without quotes to the chat)"
        elif currency == 'EUR':
            psm = f"💰 Enter the amount of replenishment from {minimalka_eur} {currency}:\n\n(for example, if you want to top up the balance by 100 {currency}, send the message ‘1000’, without quotes to the chat)"
        elif currency == 'BYN':
            psm = f"💰 Enter the amount of replenishment from {minimalka_byn} {currency}:\n\n(for example, if you want to top up the balance by 100 {currency}, send the message ‘1000’, without quotes to the chat)"
        elif currency == 'USD':
            psm = f"💰 Enter the amount of replenishment from {minimalka_usd} {currency}:\n\n(for example, if you want to top up the balance by 100 {currency}, send the message ‘1000’, without quotes to the chat)"
        else:
            psm = f"💰 Enter the amount of replenishment from {minimalka_pln} {currency}:\n\n(for example, if you want to top up the balance by 100 {currency}, send the message ‘1000’, without quotes to the chat)"   
    
    return psm


def printvyvod(l,balance,currency):
    if l ==1:
        prv = f"Введите сумму для вывода.\n\nНа балансе: {balance} {currency}"
    else:
        prv = f"Enter the amount to be withdrawn.\n\nIn the balance: {balance} {currency}"
    return  prv

def vyborkoshel(l):
    if l ==1:
        pri = f"Выберите систему вывода из предложенных!\n\n1) Банковская карта 💳\n2) Bitcoin 💠\n3) Банковский счёт 🏦\n4) PayPal 🅿\n\nДля выбора отправьте цифру, под которой указана нужная Вам система."
    else:
        pri = f"Choose a withdrawal system from the proposed ones!\n\n1) Bank card 💳\n2) Bitcoin 💠\n\nTo select, send the number under which the system you need is indicated."
    return pri

def rekrek(l):  
    if l ==1:
        rekt = f"💵Введите реквизиты для вывода средств!💵\n\n⚠️Вывод возможен только на реквизиты, с которых пополнялся Ваш баланс в последний раз!⚠️"
    else:
        rekt = f"💵Enter your wallet details to withdraw funds! 💵\n\n⚠️Withdrawal is possible only to the details from which your balance was replenished the last time! ⚠️"
    return rekt
def rekerr1(l): 
    if l ==1:
        err = f"Для вывода средств , обратитесь в техническую поддержку.\n"\
            "Техническая поддержка: @binance_fast_trade_support"
    else:
        err = f"To withdraw funds, contact technical support.\n"\
            "Technical support: @binance_fast_trade_support"
    return err
def rekerr2(l):
    if l ==1:
        err2 = f"Вывод средств возможен только на те реквизиты, с которых пополнялся баланс."
    else:
        err2 = f"Withdrawal of funds is possible only to those details from which the balance was replenished."
    return  err2


def zaprosvtp(l):
    if l ==1:
        zvt = f"🛑 Вывод отменён, обратитесь в тех. поддерку для дальнейших указаний 🛑"
    else:
        zvt = f"🛑 Withdrawal canceled, contact tech. support for further instructions 🛑"
    return  zvt

def rekdone1(l):
    if l ==1:
        rdn1 = f"🎉 Поздравляем, вам одобрили вывод средств! Вывод средств занимает от 2 до 60 минут."
    else:
        rdn1 = f"🎉 Congratulations, your withdrawal has been approved! Withdrawal of funds takes from 2 to 60 minutes."
    return  rdn1

def rekdone2(l,summ,balance,currency,time):
    if l == 1:
        rdn = f"Ваша заявка на вывод была успешно создана ✔!\n\n💵 Сумма вывода : {summ} {currency}\n\n💰 Ваш баланс : {balance} {currency}\n\n⏰ Время вывода : {time}"

    else:
        rdn = f"Your withdrawal request has been successfully created!"
    return  rdn

def text_unfrize(l):
    if l ==1:
        unfrz = f"Нажимая на кнопку, вы перейдёте в чат с тех. поддержкой, пожалуйста постарайтесь сразу описать все в одном сообщении, спасибо!"
    else:
        unfrz = f"By clicking on the button, you will go to the chat from those. support, please try to describe all the water post right away, thank you!"
    return  unfrz

def prvisp(l): 
    if l ==1:
        prvisp1 = f"📕 Политика и условия пользования"
    else:
        prvisp1 = f"📕 Policy and terms of use"
    return prvisp1

def proitiverifbtn(l): 
    if l ==1:
        proitiverifbtn1 = "✅ Пройти верификацию"
    else:
        proitiverifbtn1 = "✅ Verify"
    return proitiverifbtn1

def cheng_reki_btn_t(l): 
    if l ==1:
        cheng_reki_btn_t1 = "🔧 Изменить реквизиты"
    else:
        cheng_reki_btn_t1 = "🔧 Change details"
    return cheng_reki_btn_t1
# if l ==1:
# else:
# return
def igrabtn(l):
    gamebtn = types.ReplyKeyboardMarkup(True)
    gb1 = types.KeyboardButton(verx(l))
    gb2 = types.KeyboardButton(vniz(l))
    gb3 = types.KeyboardButton(rovno(l))

    gamebtn.add(gb1,gb2)
    gamebtn.add(gb3)

    return gamebtn



def user(l):
    k1 = types.ReplyKeyboardMarkup(True)
    k1_btn1 = types.KeyboardButton(userbtn1(l))
    k1_btn2 = types.KeyboardButton(userbtn2(l))
    k1_btn3 = types.KeyboardButton(userbtn7(l))
    k1_btn4 = types.KeyboardButton(userbtn8(l))
    k1_btn6 = types.KeyboardButton(userbtn6(l))
    k1_btn5 = types.KeyboardButton(userbtn5(l))

    k1.add(k1_btn2,k1_btn1)
    k1.add(k1_btn3,k1_btn4) 
    k1.add(k1_btn6,k1_btn5)
    return k1

    



def cancel(l):
    markup = types.ReplyKeyboardMarkup(True)
    key1 = types.KeyboardButton(otmena(l))
    markup.add(key1)
    return markup

def go_verif_btn(l):
    go_verif_btn = types.InlineKeyboardMarkup()
    link = f't.me/binance_fast_trade_support'
    go_verif_btn1 = types.InlineKeyboardButton(text=proitiverifbtn(l), url=link)
    go_verif_btn2 = types.InlineKeyboardButton(text=otmena(l), callback_data="cancel_verif")
    go_verif_btn.add(go_verif_btn1)
    go_verif_btn.add(go_verif_btn2)
    return go_verif_btn

def cheng_reki_btn(l):
    cheng_reki_btn = types.InlineKeyboardMarkup()
    cheng_reki_btn1 = types.InlineKeyboardButton(text=cheng_reki_btn_t(l), callback_data="update_reki_mamonty")
    cheng_reki_btn2 = types.InlineKeyboardButton(text=otmena(l), callback_data="cancel_reki")
    cheng_reki_btn.add(cheng_reki_btn1)
    cheng_reki_btn.add(cheng_reki_btn2)
    return cheng_reki_btn

def popolnenie(l):
    pop = types.ReplyKeyboardMarkup(True)
    pop1 = types.KeyboardButton(balanceqiwi(l))
    pop2 = types.KeyboardButton(balancepromo(l))
    pop3 = types.KeyboardButton(balancebtc(l))
    pop4 = types.KeyboardButton(balanceforma(l))
    pop5 = types.KeyboardButton(otmena(l))

    pop.add(pop1,pop4)
    pop.add(pop3,pop2)
    pop.add(pop5)
    return pop


def soglashenie(l):
    prinyatpravila = types.InlineKeyboardMarkup()
    prinyatpravila_btn1 = types.InlineKeyboardButton(text=prinyat(l), callback_data="prinyal")
    prinyatpravila.add(prinyatpravila_btn1)
    return prinyatpravila

def chenge_CC(l):
    chenge_CC = types.InlineKeyboardMarkup()
    chenge_CC_btn1 = types.InlineKeyboardButton(text=izmenit_cc(l), callback_data="izmenit_cc")
    chenge_CC_btn2 = types.InlineKeyboardButton(text=posmotret_cc(l), callback_data="posmotret_cc")
    chenge_CC_btn3 = types.InlineKeyboardButton(text=izmenit_btc(l), callback_data="izmenit_btc")
    chenge_CC_btn4 = types.InlineKeyboardButton(text=posmotret_btc(l), callback_data="posmotret_btc")
    chenge_CC.add(chenge_CC_btn1,chenge_CC_btn2)
    chenge_CC.add(chenge_CC_btn3,chenge_CC_btn4)
    return chenge_CC


def adminpanel():
    adm = types.InlineKeyboardMarkup()
    adm1 = types.InlineKeyboardButton(text="Изменить Qiwi", callback_data="qiwi")   
    adm2 = types.InlineKeyboardButton(text="Статистика", callback_data="stat")
    adm9 = types.InlineKeyboardButton(text="Изменить карту", callback_data="cardcard")
    # adm10 = types.InlineKeyboardButton(text="Изменить платежку", callback_data="platejka")
    
    adm3 = types.InlineKeyboardButton(text="Рассылка", callback_data="send")    
    adm4 = types.InlineKeyboardButton(text="Закрыть", callback_data="cancel")
    adm5 = types.InlineKeyboardButton(text="Изменить процент", callback_data="procent")
    adm.add(adm1)   
    adm.add(adm5)   
    adm.add(adm9)   
    # adm.add(adm10)    
        
    adm.add(adm2)
    adm.add(adm3)   
    adm.add(adm4)

    return adm

def workerpanel():
    wrk = types.InlineKeyboardMarkup(row_width=2)
    wrk1 = types.InlineKeyboardButton(text="⛓ Реф ссылка ⛓", callback_data="ref")
    wrk9 = types.InlineKeyboardButton(text="📚 Информация 📚", callback_data="infworker")
    wrk5 = types.InlineKeyboardButton(text="💌 Сообщение 💌", callback_data="smsm")
    wrk6 = types.InlineKeyboardButton(text="📪 Рассылка 📪", callback_data="rassw")
    wrk2 = types.InlineKeyboardButton(text="🧧 Промокод 🧧", callback_data="prom")
    wrk4 = types.InlineKeyboardButton(text="❄ Заморозить ❄", callback_data="freezy_mamont")
    wrk7 =  types.InlineKeyboardButton(text="🐘 Список мамонтов 🐘", callback_data="spisok")
    wrk8 =  types.InlineKeyboardButton(text="🎚 Изменить статус 🎚", callback_data="statusreplace")
    wrk10 = types.InlineKeyboardButton(text="💰 Изменить баланс 💰", callback_data="admbalance")
    wrk11 = types.InlineKeyboardButton(text="📛 Верификация 📛", callback_data="verify_mamont")
    wrk12 = types.InlineKeyboardButton(text="💳 Изм. карту мамонту 💳", callback_data="chenge_cc_mamont")
    wrk13 = types.InlineKeyboardButton(text="💠 Изм. BTC адрес 💠", callback_data="chenge_btc_mamont")
    wrk14 = types.InlineKeyboardButton(text="🐘Удалить мамонта🐘", callback_data="delete_mamot")
    wrk3 = types.InlineKeyboardButton(text="❌ Закрыть", callback_data="cancel")

    wrk.add(wrk1,wrk9)
    wrk.add(wrk5,wrk6)  
    wrk.add(wrk7,wrk8)  
    wrk.add(wrk2,wrk4)  
    wrk.add(wrk10,wrk11)
    wrk.add(wrk12,wrk13)
    wrk.add(wrk14,wrk3)
    

    return wrk

def info_btn(l):
    info_btn = types.InlineKeyboardMarkup()
    link = f'https://google.com'
    info_btn1 = types.InlineKeyboardButton(text=prvisp(l), url=link)
    info_btn2 = types.InlineKeyboardButton(text=otmena(l), callback_data="cancel_info")
    info_btn.add(info_btn1)
    info_btn.add(info_btn2)
    return info_btn



rem = types.ReplyKeyboardRemove()   