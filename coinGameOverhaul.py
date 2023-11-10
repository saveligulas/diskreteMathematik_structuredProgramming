def clear_console():
    for i in range(25):
        print()


def input_is_correct(r, a, board):
    if r < 0 or r > 2:
        return False

    if board[r] < a or a < 1:
        return False

    return True


def run():
    QUESTION_ONE = "What row do you want to remove coins from?"
    QUESTION_TWO = "What amount of coins do you want to remove?"
    COIN_CHAR = 'O'
    PLAYER_ONE_STRING = input("Player One's name?")
    PLAYER_TWO_STRING = input("Player Two's name?")

    coin_board = [3, 4, 5]
    is_player_one_turn = True
    row = -1
    amount = 0

    clear_console()
    
    while sum(coin_board) > 0:
        while not input_is_correct(row, amount, coin_board):
            clear_console()
            print(f"{PLAYER_ONE_STRING if is_player_one_turn else PLAYER_TWO_STRING}'s turn:")

            for i in range(len(coin_board)):
                coins = "Row 1:   " if i == 0 else "Row 2:  " if i == 1 else "Row 3: "
                for c in range(coin_board[i]):
                    coins = coins + f"{COIN_CHAR}  "
                print(coins)

            row = int(input(QUESTION_ONE)) - 1
            amount = int(input(QUESTION_TWO))

        coin_board[row] = coin_board[row] - amount
        is_player_one_turn = False if is_player_one_turn else True
        row = -1
        amount = 0
        
    clear_console()

    print(f"{PLAYER_ONE_STRING if not is_player_one_turn else PLAYER_TWO_STRING} has won!")


run()
