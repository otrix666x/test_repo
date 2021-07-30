import sqlite3

connect = sqlite3.connect("test.db")
q = connect.cursor()
q.execute("""CREATE TABLE IF NOT EXISTS info(
    id TEXT, name TEXT
)""")

text = input("Введите тект")
arr = text.split(":")
q.execute("INSERT INTO info(id, name) VALUES ('%s', '%s')"%(arr[0], arr[1]))
connect.commit()

text2 = input("Введите действия")
if text2 == "удалить":
    text3 = input("Введите id")
    q.execute(f"DELETE FROM info where id = {text3}")
    connect.commit()