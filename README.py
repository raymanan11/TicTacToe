# TicTacToe
# Tic tac toe!
def print_board(board):
    for r in board:
        for c in r:
            if c == 0:
                print(".", end="")
            elif c == 1:
                print("X", end="")
            else:
                print("O", end="")
        print()

def is_valid(r, c, board):
    if r < 0 or r > 2 or c < 0 or c > 2:
        return False
    elif (r >= 0 and r <=2) and (c >= 0 and c <= 2):
        if board[r][c] == 0:
            return True
        return False

def is_winner(board):
    if board[0][0] == board[0][1] == board[0][2]:
        return True
    return False

def main():
    board = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
    current = 1
    for i in range(9):
        print_board(board)
        if is_winner(board) == True:
            break
        if current == 1:
            print("X's turn: ")
        else:
            print("O's turn: ")
        r = int(input("Give Row!"))
        c = int(input("Give Column!"))
        while not is_valid(r, c, board):
            r = int(input("Give Row!"))
            c = int(input("Give Column!"))

        board[r][c] = current
        if current == 1:
            current = 2
        else:
            current = 1


main()
