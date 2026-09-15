# Tic Tac Toe game

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("---------")
    print("\n")


def check_winner(board, mark):
    win_states = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [mark, mark, mark] in win_states


def board_full(board):
    return all(cell != " " for row in board for cell in row)


def get_move(player, board):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row and column (1-3 1-3): ").strip().split()
            if len(move) != 2:
                raise ValueError
            row, col = int(move[0]) - 1, int(move[1]) - 1
            if row not in range(3) or col not in range(3):
                raise ValueError
            if board[row][col] != " ":
                print("That cell is already taken. Try again.")
                continue
            return row, col
        except ValueError:
            print("Invalid input. Enter two numbers between 1 and 3 separated by a space.")


def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row, col = get_move(current_player, board)
        board[row][col] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break

        if board_full(board):
            print("It's a draw!")
            break

        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    main()
