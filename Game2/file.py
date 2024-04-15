from collections import deque

def is_valid_move(board, x, y):
    return 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] != 'O'

def manhattan_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def lower_bound(board, boxes, target_positions):
    """
    Calculates a lower bound on the number of moves needed to solve.
    """
    total_distance = 0
    for box, target in zip(boxes, target_positions):
        min_distance = float('inf')
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_x, new_y = box[0] + dx, box[1] + dy
                if is_valid_move(board, new_x, new_y):
                    min_distance = min(min_distance, manhattan_distance(new_x, new_y, target[0], target[1]))
        total_distance += min_distance
    return len(boxes) + total_distance

def solve_sokoban(board):
    directions = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}
    stack = deque()
    stack.append((0, [], board))
    visited = set()
    best_moves = float('inf')

    while stack:
        moves, path, cur_board = stack.pop()
        robot_pos = None
        boxes = []

        for i in range(len(cur_board)):
            for j in range(len(cur_board[0])):
                if cur_board[i][j] == 'R':
                    robot_pos = (i, j)
                elif cur_board[i][j] == 'B':
                    boxes.append((i, j))

        if not boxes:
            best_moves = min(best_moves, moves)
            if moves == best_moves:
                return path

        if moves >= best_moves:
            continue  # Prune states exceeding the best solution found

        for direction, (dx, dy) in directions.items():
            new_x, new_y = robot_pos[0] + dx, robot_pos[1] + dy
            next_x, next_y = new_x + dx, new_y + dy

            if not is_valid_move(cur_board, new_x, new_y):
                continue

            if (new_x, new_y) in boxes:
                if not is_valid_move(cur_board, next_x, next_y) or (next_x, next_y) in boxes:
                    continue

                new_board = [list(row) for row in cur_board]  # Create a deep copy
                new_board[robot_pos[0]][robot_pos[1]] = ' '
                new_board[new_x][new_y] = 'R'
                new_board[next_x][next_y] = 'B'
                state_hash = tuple(tuple(row) for row in new_board)  # Hash for visited check

                if state_hash not in visited:
                    visited.add(state_hash)
                    lower_bound_value = lower_bound(new_board, boxes, target_positions)
                    if lower_bound_value + moves < best_moves:
                        stack.append((moves + 1, path + [direction], new_board))
                        print("Added:", path + [direction], "Total Moves:", moves + 1)

            else:
                new_board = [list(row) for row in cur_board]  # Create a deep copy
                new_board[robot_pos[0]][robot_pos[1]] = ' '
                new_board[new_x][new_y] = 'R'
                state_hash = tuple(tuple(row) for row in new_board)  # Hash for visited check

                if state_hash not in visited:
                    visited.add(state_hash)
                    stack.append((moves + 1, path + [direction], new_board))
                    print("Added:", path + [direction], "Total Moves:", moves + 1)

    return None

# Define the board configuration
# # Define the board configuration
board = [
    "OOOOOOOO",
    "O  OR O ",
    "O    B O",
    "O   O   ",
    "OOOOOBSO",
    "    O SO",
    "    OOOO"
]

target_positions = [(4, 5), (5, 5)]



result = solve_sokoban(board)

if result:
    print("Solution found:")
    print(result)
else:
    print("No solution found.")
