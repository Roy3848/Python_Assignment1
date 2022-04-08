# Football points


def football_points(win, draw, loss):
    win = win * 3
    loss = loss * 0
    draw = draw * 1
    return win+loss+draw


team1 = football_points(int(input("How many wins: ")), int(input("How many draws: ")), int(input("How many losses: ")))
team2 = football_points(int(input("How many wins: ")), int(input("How many draws: ")), int(input("How many losses: ")))
team3 = football_points(int(input("How many wins: ")), int(input("How many draws: ")), int(input("How many losses: ")))


print("Total points scored by team1 is ", team1)
print("Total points scored by team2 is ", team2)
print("Total points scored by team3 is ", team3)
