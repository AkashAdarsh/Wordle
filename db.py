import sqlite3


def createT():
    con = sqlite3.connect('record.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE record (id integer primary key, first text, second text, third text, fourth text, 
    fifth text, sixth text, attempts real)''')
    con.commit()
    con.close()


def createT2():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur.execute('''CREATE TABLE database (id integer primary key,date text, solution text, win text)''')
    con.commit()
    con.close()


def recordGame(gid, first, second, third, fourth, fifth, sixth, attempts):
    con = sqlite3.connect('record.db')
    cur = con.cursor()
    execute = "INSERT INTO record VALUES  ('" + str(
        gid) + "','" + first + "', '" + second + "', '" + third + "', '" + fourth + "', '" + fifth + "', '" + sixth + "', '" + str(
        attempts) + "')"
    cur.execute(execute)
    con.commit()
    con.close()


def gameComplete(gid, date, solution, win):
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    execute = "INSERT INTO database VALUES  ('" + str(gid) + "', '" + date + "', '" + solution + "', '" + win + "')"
    cur.execute(execute)
    con.commit()
    con.close()


def queryWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("SELECT * FROM wordle")
    for column in c.description:
        print(column[0], end=" ")
    print()
    print(c.fetchall())
    con.close()


def truncateWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DELETE FROM wordle")
    con.commit()
    con.close()


def dropWordle():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DROP TABLE if exists wordle")
    con.commit()
    con.close()


def calcStats():
    con = sqlite3.connect('game.db')

    c = con.cursor()

    c.execute("DROP TABLE if exists WordleStats")

    c.execute(
        '''CREATE TABLE if not exists WordleStats (SuccessfulGames Integer, UnsuccessfulGames Integer, AverageAttemptsToWin Integer)''')

    c.execute("DELETE FROM WordleStats")

    c.execute("SELECT AVG(Attempts) FROM wordle where Attempts != -1")

    avgAttemptsToWin = c.fetchall()[0][0]

    c.execute("SELECT COUNT(*) FROM wordle where Attempts = -1")

    unsuccessful = c.fetchall()[0][0]

    c.execute("SELECT COUNT(*) FROM wordle where Attempts != -1")

    successful = c.fetchall()[0][0]

    c.execute("INSERT INTO WordleStats VALUES (?,?,?)",
              (successful, unsuccessful, avgAttemptsToWin))

    c.execute("SELECT * FROM WordleStats")
    for column in c.description:
        print(column[0], end=" ")
    con.commit()
    print()
    print(c.fetchall()[0])

    con.close()


calcStats()
