# Chess Engine with AI Opponent

Welcome to our simple chess engine implementation with an AI opponent!

## Features

- Play chess against a human player.
- Utilizes a basic evaluation function to assess the board position.
- Employs the alpha-beta pruning algorithm to efficiently search for the best move for the AI.

## Code Breakdown

1. **Imports:**
   - `chess`: A Python library for playing chess.

2. **Piece Values:**
   - Defines a dictionary `piece_values` that assigns a static value to each chess piece.

3. **Piece-Square Tables (PSTs):**
   - Defines several two-dimensional arrays (`pawnEvalWhite`, `knightEval`, etc.) representing piece square tables (PSTs) for different piece types and colors. These tables assign a positional bonus or penalty to a piece based on its location on the board.

4. **Evaluation Function (`evaluate`):**
   - Iterates through all squares on the board.
   - For each square with a piece, calls the `get_piece_value` function to retrieve its value based on type, color, and position.
   - Sums the individual piece values to get the total material evaluation of the board. 

5. **Get Piece Value (`get_piece_value`):**
   - Considers the piece type, color, and square coordinates.
   - Uses the corresponding PST and piece value tables to determine the piece's value on the current board.

6. **Generate Legal Moves (`generate_moves`):**
   - A simple function that utilizes the `chess` library to find all legal moves for the current player on the board.

7. **Alpha-Beta Pruning (`alpha_beta`):**
   - A recursive minimax search algorithm enhanced with alpha-beta pruning for efficiency.
   - Takes the chessboard, search depth, alpha, beta values, and a flag indicating the current player (maximizing or minimizing) as input.
   - Base Case: If depth is reached or the game is over, returns the evaluation of the board using the `evaluate` function.
   - Maximizing player:
      - Initializes `max_eval` to negative infinity.
      - Iterates through all legal moves.
        - Makes the move on the board.
        - Recursively calls `alpha_beta` with reduced depth, updated alpha and beta values, and the minimizing player flag.
        - Undoes the move.
        - Updates `max_eval` with the maximum of the current value and the recursive call's result.
        - Updates alpha with the maximum of its current value and `max_eval`.
        - If beta is less than or equal to alpha, prunes further exploration of this branch.
     - Returns `max_eval`.
   - Minimizing player (similar logic but minimizes instead of maximizes).

8. **Main Function (`main`):**
   - Creates a chessboard object.
   - Sets the search depth for the AI.
   - Main game loop that continues until the game is over:
      - If it's white's turn (human player), prompts the user for a move and makes it on the board.
      - If it's black's turn (AI), performs the following steps:
         - Initializes variables to track the best move and the maximum evaluation.
         - Generates all legal moves for the AI.
         - Iterates through each legal move:
            - Makes the move on the board.
            - Calls `alpha_beta` to evaluate the resulting position.
            - Undoes the move.
            - Updates `best_move` and `max_eval` if a better move is found.
         - Makes the best move found on the board and prints it.
      - Prints the current board state.

## Running the Code

1. Save the code as a Python file (e.g., `chess_engine.py`).
2. Open a terminal or command prompt and navigate to the directory containing the file.
3. Run the script using the command: `python chess_engine.py`

This will start a chess game where you can play against the AI. Enter your moves in standard algebraic notation (e.g., `e2e4`).
