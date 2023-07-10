tedad = int(input('Enter tedad:\n'))
sum = {}
for i in range(tedad):
    sum[i] = 0
while True:
    shakhes = str(input('Enter Shakhes:\n'))
    game = {}

    for i in range(tedad):
        game[i] = {}
        game[i]['name'] = str(input(f"player {i} Enter name: "))
        game[i]['city'] = str(input(f"player {i} Enter city: "))
        game[i]['food'] = str(input(f"player {i} Enter food: "))
        game[i]['color'] = str(input(f"player {i} Enter color: "))
    for player in game.keys():
        for field in game[player].keys():
            duplicate = False
            if game[player][field].startswith(shakhes):
                for item in range(tedad):
                    if player == item:
                        pass
                    else:
                        if game[player][field] == game[item][field]:
                            sum[player] += 5
                            duplicate = True
                if not duplicate:
                    sum[player] += 10
    print(sum)
    max_grade = 0
    winner = None
    for key, value in sum.items():
        if value > max_grade:
            max_grade = value
            winner = [key]
        elif value==max_grade:
            winner.append(key)
    print(f"winner is {winner}.")
