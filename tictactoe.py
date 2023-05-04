import os

def clear_console():
    os.system("cls" if os.name == "nt" else "clear")

def print_board(board):
    clear_console()
    print("   |   |   ")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("___|___|___")
    print("   |   |   ")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("   |   |   ")

def check_winner(board):
    # check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] and board[i] != " ":
            return board[i]
    # check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] and board[i] != " ":
            return board[i]
    # check diagonals
    if board[0] == board[4] == board[8] and board[0] != " ":
        return board[0]
    if board[2] == board[4] == board[6] and board[2] != " ":
        return board[2]
    # check for tie
    if " " not in board:
        return "Tie"
    # game is still ongoing
    return None

def get_best_move(board, player):
    """
    Returns the best move for the given player using the minimax algorithm.
    """
    if check_winner(board) is not None:
        # The game is already over
        return None

    if player == "X":
        best_score = float("-inf")
        best_move = None
        for i in range(len(board)):
            if board[i] == " ":
                new_board = board[:i] + "X" + board[i+1:]
                score = minimax(new_board, "O")
                if score > best_score:
                    best_score = score
                    best_move = i
    else:
        best_score = float("inf")
        best_move = None
        for i in range(len(board)):
            if board[i] == " ":
                new_board = board[:i] + "O" + board[i+1:]
                score = minimax(new_board, "X")
                if score < best_score:
                    best_score = score
                    best_move = i

    return best_move

def minimax(board, player):
    """
    Returns the best score for the given player using the minimax algorithm.
    """
    winner = check_winner(board)
    if winner == "X":
        return 1
    elif winner == "O":
        return -1
    elif winner == "Tie":
        return 0

    if player == "X":
        best_score = float("-inf")
        for i in range(len(board)):
            if board[i] == " ":
                new_board = board[:i] + "X" + board[i+1:]
                score = minimax(new_board, "O")
                if score > best_score:
                    best_score = score
    else:
        best_score = float("inf")
        for i in range(len(board)):
            if board[i] == " ":
                new_board = board[:i] + "O" + board[i+1:]
                score = minimax(new_board, "X")
                if score < best_score:
                    best_score = score

    return best_score

def print_game_over(winner):
    if winner == "Tie":
        print("Game over! It's a tie.")
    else:
        print(f"Game over! {winner} wins!")

def get_user_input(board):
    """
    Prompts the user to enter a move and returns the position.
    """
    valid_move = False
    while not valid_move:
        try:
            position = int(input("Enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input. Please enter a number between 1 and 9.")
            elif board[position] != " ":
                print("That position is already taken. Please choose a different one.")
            else:
                valid_move = True
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")
    return position

def play_game():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while check_winner(board) is None and " " in board:
        if current_player == "X":
            position = get_user_input(board)
        else:
            position = get_best_move("".join(board), current_player)
        board[position] = current_player
        print_board(board)
        current_player = players[(players.index(current_player) + 1) % 2]
    print_game_over(check_winner(board))

play_game()