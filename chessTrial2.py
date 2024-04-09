import chess
import chess.svg
from IPython.display import display, HTML, SVG
# Define piece values
piece_values = {
    chess.PAWN: 100,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.ROOK: 500,
    chess.QUEEN: 900,
    chess.KING: 20000
}

# Define piece square tables
pawnEvalWhite = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [50, 50, 50, 50, 50, 50, 50, 50],
    [10, 10, 20, 30, 30, 20, 10, 10],
    [5, 5, 10, 25, 25, 10, 5, 5],
    [0, 0, 0, 20, 20, 0, 0, 0],
    [5, -5, -10, 0, 0, -10, -5, 5],
    [5, 10, 10, -20, -20, 10, 10, 5],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

pawnEvalBlack = list(reversed(pawnEvalWhite))

knightEval = [
    [-50, -40, -30, -30, -30, -30, -40, -50],
    [-40, -20, 0, 0, 0, 0, -20, -40],
    [-30, 0, 10, 15, 15, 10, 0, -30],
    [-30, 5, 15, 20, 20, 15, 5, -30],
    [-30, 0, 15, 20, 20, 15, 0, -30],
    [-30, 5, 10, 15, 15, 10, 5, -30],
    [-40, -20, 0, 5, 5, 0, -20, -40],
    [-50, -40, -30, -30, -30, -30, -40, -50]
]

bishopEvalWhite = [
    [-20, -10, -10, -10, -10, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 10, 10, 5, 0, -10],
    [-10, 5, 5, 10, 10, 5, 5, -10],
    [-10, 0, 10, 10, 10, 10, 0, -10],
    [-10, 10, 10, 10, 10, 10, 10, -10],
    [-10, 5, 0, 0, 0, 0, 5, -10],
    [-20, -10, -10, -10, -10, -10, -10, -20]
]

bishopEvalBlack = list(reversed(bishopEvalWhite))

rookEvalWhite = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [5, 10, 10, 10, 10, 10, 10, 5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [-5, 0, 0, 0, 0, 0, 0, -5],
    [0, 0, 0, 5, 5, 0, 0, 0]
]

rookEvalBlack = list(reversed(rookEvalWhite))

queenEval = [
    [-20, -10, -10, -5, -5, -10, -10, -20],
    [-10, 0, 0, 0, 0, 0, 0, -10],
    [-10, 0, 5, 5, 5, 5, 0, -10],
    [-5, 0, 5, 5, 5, 5, 0, -5],
    [0, 0, 5, 5, 5, 5, 0, -5],
    [-10, 5, 5, 5, 5, 5, 0, -10],
    [-10, 0, 5, 0, 0, 0, 0, -10],
    [-20, -10, -10, -5, -5, -10, -10, -20]
]

kingEvalWhite = [
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-30, -40, -40, -50, -50, -40, -40, -30],
    [-20, -30, -30, -40, -40, -30, -30, -20],
    [-10, -20, -20, -20, -20, -20, -20, -10],
    [20, 20, 0, 0, 0, 0, 20, 20],
    [20, 30, 10, 0, 0, 10, 30, 20]
]

kingEvalBlack = list(reversed(kingEvalWhite))


# Function to evaluate the board
def evaluate(board):
    total_evaluation = 0
    for i in range(8):
        for j in range(8):
            total_evaluation += get_piece_value(board.piece_at(chess.square(i, j)), i, j)
    return total_evaluation

# Function to get the value of a piece
def get_piece_value(piece, x, y):
    if piece is None:
        return 0
    if piece.color == chess.WHITE:
        if piece.piece_type == chess.PAWN:
            return piece_values[chess.PAWN] + pawnEvalWhite[y][x]
        elif piece.piece_type == chess.KNIGHT:
            return piece_values[chess.KNIGHT] + knightEval[y][x]
        elif piece.piece_type == chess.BISHOP:
            return piece_values[chess.BISHOP] + bishopEvalWhite[y][x]
        elif piece.piece_type == chess.ROOK:
            return piece_values[chess.ROOK] + rookEvalWhite[y][x]
        elif piece.piece_type == chess.QUEEN:
            return piece_values[chess.QUEEN] + queenEval[y][x]
        elif piece.piece_type == chess.KING:
            return piece_values[chess.KING] + kingEvalWhite[y][x]
    else:
        if piece.piece_type == chess.PAWN:
            return piece_values[chess.PAWN] + pawnEvalBlack[y][x]
        elif piece.piece_type == chess.KNIGHT:
            return piece_values[chess.KNIGHT] + knightEval[y][x]
        elif piece.piece_type == chess.BISHOP:
            return piece_values[chess.BISHOP] + bishopEvalBlack[y][x]
        elif piece.piece_type == chess.ROOK:
            return piece_values[chess.ROOK] + rookEvalBlack[y][x]
        elif piece.piece_type == chess.QUEEN:
            return piece_values[chess.QUEEN] + queenEval[y][x]
        elif piece.piece_type == chess.KING:
            return piece_values[chess.KING] + kingEvalBlack[y][x]

# Function to generate legal moves
def generate_moves(board):
    return list(board.legal_moves)


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board), 1

    if maximizing_player:
        max_eval = float('-inf')
        nodes_visited = 0
        for move in board.legal_moves:
            board.push(move)
            eval, visited = minimax(board, depth - 1, False)
            nodes_visited += visited
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval, nodes_visited
    else:
        min_eval = float('inf')
        nodes_visited = 0
        for move in board.legal_moves:
            board.push(move)
            eval, visited = minimax(board, depth - 1, True)
            nodes_visited += visited
            board.pop()
            min_eval = min(min_eval, eval)
        return min_eval, nodes_visited

# Modify the main function to take depth from input and print statistics
def main():
    board = chess.Board()
    depth = int(input("Enter the depth for Minimax: "))

    while not board.is_game_over():
        if board.turn == chess.WHITE:
            # Player's turn
            player_move = input("Enter your move (e.g., e2e4): ")
            try:
                board.push_san(player_move)
            except ValueError:
                print("Invalid move. Please try again.")
                continue
        else:
            # AI's turn
            best_move = None
            max_eval = float('-inf')
            nodes_visited = 0
            moves = generate_moves(board)
            for move in moves:
                board.push(move)
                eval, visited = minimax(board, depth - 1, False)
                nodes_visited += visited
                board.pop()
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            board.push(best_move)
            print("\nAI's move:", best_move)
            print("Nodes visited:", nodes_visited)

        print("\n")
        print(board)


# for SVG visulaization


# def main():
#     board = chess.Board()
#     depth = int(input("Enter the depth for Minimax: "))
#     move_counter = 1

#     while not board.is_game_over():
#         if board.turn == chess.WHITE:
#             # Player's turn
#             player_move = input("Enter your move (e.g., e2e4): ")
#             try:
#                 board.push_san(player_move)
#             except ValueError:
#                 print("Invalid move. Please try again.")
#                 continue
#         else:
#             # AI's turn
#             best_move = None
#             max_eval = float('-inf')
#             nodes_visited = 0
#             moves = generate_moves(board)
#             for move in moves:
#                 board.push(move)
#                 eval, visited = minimax(board, depth - 1, False)
#                 nodes_visited += visited
#                 board.pop()
#                 if eval > max_eval:
#                     max_eval = eval
#                     best_move = move
#             board.push(best_move)
#             print("\nAI's move:", best_move)
#             print("Nodes visited:", nodes_visited)

#         # Visualize the board and save it to a file
#         with open(f"board_{move_counter}.svg", "w") as f:
#             f.write(chess.svg.board(board=board))
#         move_counter += 1

if __name__ == "__main__":
    main()
