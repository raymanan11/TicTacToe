# TicTacToe

def print_board(board):
    
    for r in board:
        for c in r:
            if c == 0:
                print(".", ' ', "|", ' ', end="")
            elif c == 1:
                print("X", ' ', "|", ' ', end="")
            else:
                print("O", ' ', "|", ' ', end="")
        
            
        print()
    
        '''print(board[0][0], "|", board[0][1], "|", board[0][2])
        print("---------")
        print(board[1][0], "|", board[1][1], "|", board[1][2])
        print("---------")
        print(board[2][0], "|", board[2][1], "|", board[2][2])'''

        '''print(board[r][c], "|", board[r][c], "|", board[r][c])
        print("---------")
        print(board[r][c], "|", board[r][1], "|", board[r][c])
        print("---------")
        print(board[r][c], "|", board[r][c], "|", board[r][c])'''

    '''print('.', "|", '.', "|", '.')
    print("---------")
    print('.', "|", '.', "|", '.')
    print("---------")
    print('.', "|", '.', "|", '.')'''


def is_valid(r, c, board):
    if r < 0 or r > 2 or c < 0 or c > 2:
        return False
    elif (r >= 0 and r <=2) and (c >= 0 and c <= 2):
        if board[r][c] == 0:
            return True
        return False
    

def is_winner(board):
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != 0:
            return True
    # this 1st for loop looks for horizontal cases
    # it will check the first value in the row of either 1 and 2 (not 0) and count how many times it is in the row. If that value equals the length of the row that means three in a row, horizontally

    for col in range(len(board)):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            return True
    # 2nd for loop checks for vertical cases of 3 in a row
    # created a list called check so that it will append the same index in each row giving us a potential vertical 3 in a row.
    # it will then check the first value in the list check and count how many times that value is in the list. If that value equals the length of the list check, then it means three in a row vertically
        
    diag = []   
    for i in range(len(board)):
        diag.append(board[i][i])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        return True
    # 3rd for loop is for cases of diagonal from top left to bottom right
    # again I made a list called diag and I saw a pattern that the diagonal places are board[i][i] so I made a for loop to iterate numbers from the length of the board and then appended those values to the list diag
    # then it checks the first value of diag (only 1 and 2 not 0) and counts how many times it is in the list. If that value equals length of the list diag then it means three in a row diagonally from top left to bottom right
    
    diag = []
    rows = reversed(range(len(board)))
    cols = range(len(board))
    for row, col, in zip(rows, cols):
            diag.append(board[row][col])
    if diag.count(diag[0]) == len(diag) and diag[0] != 0:
        return True
    # 4th for loop is for cases of diagonal three in a row from bottom left to top right
    # I saw that the indexes for diagonal bottom left to top right were from board[2][0] to board[1][1] to board[0][2]. So the first index referred to the row and second index referred to the column
    # So I made a variable called rows which is based off of the range of the length of the board but because the pattern showed the rows went from 2 to 0, then I used a built in python function called
    # reversed in order to go from 2, then 1, to 0
    # the rows went from 0 to 1 so that was just range of the length of board
    # I used another python functin called zip to combine rows and colums to get the indexes and append all those values to a list called diag in what is a potential diagonal three in a row
    # then it checks the first value of diag (only 1 and 2 not 0) and counts how many times it is in the list. If that value equals length of the list diag then it means three in a row diagonally from bottom left to top right
    
def main():
    board = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    current = 1
    for i in range(9):
        print_board(board)
        if is_winner(board) == True:
            print("Yay! You won!")
            break
        if current == 1:
            print("X's turn: ")
        else:
            print("O's turn: ")
        r = int(input("Give Row! "))
        c = int(input("Give Column! "))
        while not is_valid(r, c, board):
            r = int(input("Give Row! "))
            c = int(input("Give Column! "))

        board[r][c] = current
        if current == 1:
            current = 2
        else:
            current = 1


main()

