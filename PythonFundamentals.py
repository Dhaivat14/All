def board_setup():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    return board

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def board_full(board):
    for row in board:
        for cell in row:
            if cell == ' ':
                return False
    return True

def valid_input(value):
    return value in ['0', '1', '2']

def player_moves(board, player):
    valid_move = False
    while not valid_move:
        move = input(f"Player {player}, Enter row and column: ")
        split_move = move.split()
        if len(split_move) != 2:
            print("Invalid input. Enter row and column:")
            continue
        row, col = split_move
        if not valid_input(row) or not valid_input(col):
            print("Invalid input. Enter numbers between 0 and 2.")
            continue
        row, col = int(row), int(col)
        if board[row][col] != ' ':
            print("Invalid move(occupied cell)")
            continue
        board[row][col] = player
        valid_move = True

def switch_player(player):
    return 'O' if player == 'X' else 'X'

def tic_tac_toe():
    board = board_setup()
    current_player = 'X'

    while True:
        print_board(board)
        player_moves(board, current_player)
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        if board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = switch_player(current_player)

# Start the game
tic_tac_toe()