import sqlite3
import requests
import re
from bs4 import BeautifulSoup


def getbalance(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select balance from users WHERE id = {msid}")
	balancenow = cur.fetchone()[0]
	con.commit()

	return balancenow
    
def getcurrency(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select currency from users WHERE id = {msid}")
	balancenow = cur.fetchone()[0]
	con.commit()

	return currency

def deleteoplata(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"DELETE FROM oplata WHERE id = {msid}")
	con.commit()

def getstatus(msid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select status from users WHERE id = {msid}")
	statusgame = cur.fetchone()[0]
	con.commit()

	return statusgame



def lang(uid):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute(f"select language from users WHERE id = {uid}")
	lan = cur.fetchone()[0]
	con.commit()

	return lan

def get_user(user_id):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute('SELECT * FROM users WHERE id = ?', (user_id,))
	return cur.fetchone()
    
def get_pay(user_id):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	cur.execute('SELECT * FROM payments WHERE id = ?', (user_id,))
	return cur.fetchone()

def convert_currency(user_id, currency):
	con = sqlite3.connect("data.db")
	cur = con.cursor()
	user = get_user(user_id)
	user_currency = user[8]
	balance = user[4]

	print(balance, user_currency, currency)

	url = f'https://www.xe.com/currencyconverter/convert/?Amount={balance}&From={user_currency}&To={currency}'
	response = requests.get(url)
	soup = BeautifulSoup(response.text, 'lxml')
	result = soup.find_all('p', class_='result__BigRate-sc-1bsijpp-1 iGrAod')[0].text

	rate = re.findall(r'(\S+)', result)[0]
	if ',' in rate:
		rate = rate.replace(',', '')
	amount = (round(float(rate), 2))

	cur.execute('UPDATE users SET balance = ? WHERE id = ?', (amount, user_id))
	cur.execute('UPDATE users SET currency = ? WHERE id = ?', (currency, user_id))
	con.commit()

