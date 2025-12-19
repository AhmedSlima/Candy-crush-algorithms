from collections import deque
from match3game import Match3Game

def bfs_solver(max_depth=10):
    game = Match3Game()
    queue = deque([(game, 0)])
    best_score = game.score
    best_game = game
    nodes = 0

    while queue:
        state, depth = queue.popleft()
        nodes += 1
        if state.score > best_score:
            best_score = state.score
            best_game = state
        if depth < max_depth:
            for succ in state.get_successors():
                queue.append((succ, depth + 1))

    return {
        "Algorithm": "BFS",
        "Final Score": best_game.score,
        "Moves Used": game.max_moves - best_game.moves_left,
        "Nodes Explored": nodes,
        "Reached Goal": best_game.score >= game.target_score
    }

if _name_ == "_main_":
    result = bfs_solver()
    for k, v in result.items():
        print(f"{k:15}: {v}")
        