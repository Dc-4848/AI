def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return True
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True
    
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True
    
    return False

def is_draw(board):
    for row in board:
        for cell in row:
            if cell == " ":
                return False
    return True

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    turn = 0
    
    while True:
        print_board(board)
        row = int(input(f"Player {players[turn]}, enter row (0-2): "))
        col = int(input(f"Player {players[turn]}, enter col (0-2): "))
        
        if board[row][col] == " ":
            board[row][col] = players[turn]
            if check_winner(board):
                print_board(board)
                print(f"Player {players[turn]} wins!")
                break
            if is_draw(board):
                print_board(board)
                print("It's a draw!")
                break
            turn = 1 - turn
        else:
            print("Cell already taken! Try again.")

if __name__ == "__main__":
    tic_tac_toe()
