def create_board():
    return ["-" for i in range(9)]
def show_board(board):
    print("{} {} {}".format(board[0],board[1],board[2]))
    print("{} {} {}".format(board[3],board[4],board[5]))
    print("{} {} {}".format(board[6],board[7],board[8]))
def win_check(board,player):
    if ((board[0]==player and board[1]==player and board[2]==player)
        or (board[3]==player and board[4]==player and board[5]==player)
        or (board[6]==player and board[7]==player and board[8]==player)
        or (board[0]==player and board[3]==player and board[6]==player)
        or (board[1]==player and board[4]==player and board[7]==player)
        or (board[2]==player and board[5]==player and board[8]==player)
        or (board[0]==player and board[4]==player and board[8]==player)
        or (board[2]==player and board[4]==player and board[7]==player)):
        return True
def draw_check(board):
    for square in board:
        if square != "x" or square != "x":
            return False
    return True

def single_game():
    board = create_board()
    player1 = 'x'
    player2 = 'o'
    show_board(board)
    while True:
        move = int(input("Player " + player1 + " choose a square: "))
        board[move-1] = player1
        show_board(board)
        if win_check(board,player1):
            print("Game over! Player "+ player1+" won!!!")
            break
        if draw_check(board):
            print("Game over! IT'S A DRAAAAAAAAAW")
            break
        move = int(input("Player " + player2 + " choose a square "))
        board[move-1] = player2
        show_board(board)
        if win_check(board,player2):
            print("Game over! Player" + player2 +" won!!!")
            break
        if draw_check(board):
            print("Game over! IT'S A DRAAAAAAAAAW")
            break
if __name__ == "__main__":
    single_game()