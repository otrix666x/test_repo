from time import sleep
import os

process_name = 'bot.py'

while True:
    try:
        os.system('python3 '+process_name)
    except:
        pass