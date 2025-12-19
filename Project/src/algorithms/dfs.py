import copy
from match3game import Match3Game

def dfs_solver(depth_limit=10):
    game = Match3Game()
    best_game = game
    nodes = 0

    def dfs(state, depth, visited):
        nonlocal best_game, nodes
        nodes += 1
        if state.score > best_game.score:
            best_game = state
        if depth == 0 or state.game_over():
            return
        state_id = tuple(tuple(row) for row in state.board)
        if state_id in visited:
            return
        visited.add(state_id)
        for succ in state.get_successors():
            dfs(succ, depth - 1, visited)

    dfs(game, depth_limit, set())
    return {
        "Algorithm": "DFS",
        "Final Score": best_game.score,
        "Moves Used": game.max_moves - best_game.moves_left,
        "Nodes Explored": nodes,
        "Reached Goal": best_game.score >= game.target_score
    }

if _name_ == "_main_":
    result = dfs_solver()
    for k, v in result.items():
        print(f"{k:15}: {v}") 