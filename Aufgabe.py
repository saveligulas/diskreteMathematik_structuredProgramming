def get_binary_ones_of_number_range(a, b):
    total_ones = 0
    for i in range(a, b + 1):
        division = i
        while division != 0:
            modulo = division % 2
            division = division // 2
            if modulo == 1:
                total_ones += 1
    return total_ones


def one_will_win_run(participants, key):
    players = []
    for i in range(participants):
        players.append(True)
    leng = len(players)

    ind = 0
    key = key - 1
    while sum(players) > 1:
        counter = 0
        player_to_rem = 0
        while counter != key:
            if players[counter % leng]:
                counter += 1
            player_to_rem += 1

        players[player_to_rem] = False

        for i in range(player_to_rem, ind + leng):
            if players[i % leng]:
                ind = i
                break

    for p in range(leng):
        if players[p]:
            return p


print(one_will_win_run(7, 3))