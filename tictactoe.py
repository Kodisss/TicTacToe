def print_board(board):
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

def play_game():
    board = [" "] * 9
    current_player = "X"
    winner = None

    while not winner:
        print_board(board)
        print(f"It's {current_player}'s turn.")
        move = int(input("Enter a position (1-9): ")) - 1
        if board[move] == " ":
            board[move] = current_player
            current_player = "O" if current_player == "X" else "X"
        else:
            print("That position is already taken. Please try again.")
        winner = check_winner(board)

    print_board(board)
    if winner == "Tie":
        print("It's a tie!")
    else:
        print(f"{winner} wins!")

play_game()