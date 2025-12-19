from match3game import Match3Game

def hill_climbing_solver():
    game = Match3Game()
    current = game
    nodes = 0

    while not current.game_over():
        nodes += 1
        neighbors = current.get_successors()
        if not neighbors:
            break
        best_neighbor = max(neighbors, key=lambda s: s.score)
        if best_neighbor.score <= current.score:
            break
        current = best_neighbor

    return {
        "Algorithm": "HillClimbing",
        "Final Score": current.score,
        "Moves Used": game.max_moves - current.moves_left,
        "Nodes Explored": nodes,
        "Reached Goal": current.score >= game.target_score
    }

if __name__ == "__main__":
    result = hill_climbing_solver()
    for k, v in result.items():
        print(f"{k:15}: {v}")