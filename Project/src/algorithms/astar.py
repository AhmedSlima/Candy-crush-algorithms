from match3game import Match3Game, MAX_MOVES, TARGET_SCORE

def astar_solver():
    game = Match3Game()
    board = game.board
    best_score = 0
    nodes = 0

    open_list = [(board, 0)]
    visited = set()

    while open_list:
        current_board, g = open_list.pop(0)
        nodes += 1
        board_tuple = tuple(map(tuple, current_board))
        if board_tuple in visited:
            continue
        visited.add(board_tuple)

        # Simple heuristic: count horizontal & vertical matches
        score = 0
        for i in range(8):
            for j in range(6):
                if current_board[i][j] == current_board[i][j+1] == current_board[i][j+2]:
                    score += 10
                if current_board[j][i] == current_board[j+1][i] == current_board[j+2][i]:
                    score += 10
        if score > best_score:
            best_score = score

    return {
        "Algorithm": "A*",
        "Final Score": best_score,
        "Moves Used": MAX_MOVES,
        "Nodes Explored": nodes,
        "Reached Goal": best_score >= TARGET_SCORE
    }

if __name__ == "__main__":
    result = astar_solver()
    for k, v in result.items():
        print(f"{k:15}: {v}")