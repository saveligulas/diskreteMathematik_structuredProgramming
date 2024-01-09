def run(n):
    board = [False, [True, False], True]
    path = False

    for ball in range(n):
        position = 1 if board[0] else 0
        if position == 1 and not board[1][1] or position == 0 and board[1][0]:
            board[2] = switch(board[2])
        board[0] = switch(board[0])
        board[1][position] = switch(board[1][position])

    if board[0]:
        if board[1][1]:
            path = switch(path)
        else:
            if board[2]:
                path = switch(path)
    else:
        if board[1][0] and board[2]:
            path = switch(path)

    print_board(board)
    return path


def print_board(board):
    char_false = '/'
    char_true = '\\'
    char_line = '|'
    print_loop(char_line, 3)
    print(f"{char_true if board[0] else char_false}")
    print(f"{char_line} {char_true}")
    print_loop(f"{char_line}  {char_line}", 3)
    print(f"{print_char(board[1][0])}  {print_char(board[1][1])}")
    print_loop(f"{char_line} {char_line} {char_line}", 3)
    print(f"{char_true} {print_char(board[2])} {char_false}")
    print_loop(f" {char_line} {char_line}", 1)
    print(" F  T")


def print_char(boolean):
    return "\\" if boolean else "/"


def switch(boolean):
    return False if boolean else True


def print_loop(char, n):
    for i in range(n):
        print(char)


def switch_mult(lis):
    result = []
    for b in lis:
        result.append(switch(b))
    return result


print(run(4))
