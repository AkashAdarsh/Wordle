import sqlite3
from tokenize import maybe

connect = sqlite3.connect('database.db')
cursor = connect.cursor()
gamesPlayed = []
wins = 0
losses = 0

print("Enter the date you want to check ")
mdate = input()

for row in cursor.execute('SELECT * FROM database'):
    if row[1] == mdate:
        gamesPlayed.append(row)
        if row[3] == "Win":
            wins += 1
        else:
            losses += 1
connect.close()

print()
print("On ",mdate)
print()
print("No. of winn are ",wins)
print("No. of lost are ",losses)
print("Win %age ",(wins/1000)*100,"%")
print("Loss %age ",(losses/1000)*100,"%")

