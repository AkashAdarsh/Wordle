import wordle_solver
import db
from datetime import date

today = date.today()

if __name__ == "__main__":

    db.createT()
    db.createT2()

    for i in range(1000):
        print("Game being played is number: ", i + 1)
        todayDate = today.strftime("%m/%d/%y")
        win, guesses, attempts, solution, gid = wordle_solver.playGame()
        solution = "".join(solution)
        for _ in range(6 - attempts):
            guesses.append("NONE")

        db.recordGame(gid, guesses[0], guesses[1], guesses[2], guesses[3], guesses[4], guesses[5], attempts)
        db.gameComplete(gid, todayDate, solution, win)