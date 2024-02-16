import random

def print_board(board):
    """
    Function to print the tic-tac-toe board.
    """
    print("-------------")
    print("| " + board[0] + " | " + board[1] + " | " + board[2] + " |")
    print("-------------")
    print("| " + board[3] + " | " + board[4] + " | " + board[5] + " |")
    print("-------------")
    print("| " + board[6] + " | " + board[7] + " | " + board[8] + " |")
    print("-------------")

def check_winner(board, player):
    """
    Function to check if a player has won the game.
    """
    if (
        (board[0] == player and board[1] == player and board[2] == player) or
        (board[3] == player and board[4] == player and board[5] == player) or
        (board[6] == player and board[7] == player and board[8] == player) or
        (board[0] == player and board[3] == player and board[6] == player) or
        (board[1] == player and board[4] == player and board[7] == player) or
        (board[2] == player and board[5] == player and board[8] == player) or
        (board[0] == player and board[4] == player and board[8] == player) or
        (board[2] == player and board[4] == player and board[6] == player)
    ):
        return True
    else:
        return False

def make_move(board, position, player):
    """
    Function to make a move on the board.
    """
    board[position] = player

def get_available_moves(board):
    """
    Function to get the available moves on the board.
    """
    available_moves = []
    for i in range(len(board)):
        if board[i] == " ":
            available_moves.append(i)
    return available_moves

def ai_move(board, player):
    """
    Function for the AI to make a move.
    """
    available_moves = get_available_moves(board)
    move = random.choice(available_moves)
    make_move(board, move, player)

def play_game():
    """
    Function to play the tic-tac-toe game.
    """
    board = [" " for _ in range(9)]
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Player's move
        player_move = int(input("Enter your move (0-8): "))
        make_move(board, player_move, "X")
        print_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if len(get_available_moves(board)) == 0:
            print("It's a tie!")
            break
        # AI's move
        ai_move(board, "O")
        print_board(board)
        if check_winner(board, "O"):
            print("Sorry, you lose!")
            break

play_game()
