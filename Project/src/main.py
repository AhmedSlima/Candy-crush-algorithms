from algorithms import bfs_solver, dfs_solver, hill_climbing_solver, astar_solver, genetic_solver

ALGORITHMS = {
    "BFS": bfs_solver,
    "DFS": dfs_solver,
    "HILLCLIMBING": hill_climbing_solver,
    "A*": astar_solver,
    "GENETIC": genetic_solver
}

def run_algorithm(name):
    algo = ALGORITHMS.get(name.upper())
    if not algo:
        print("❌ Algorithm not supported")
        return
    result = algo()
    print("\n================ RESULT ================\n")
    for k, v in result.items():
        print(f"{k:15}: {v}")
    print("\n=======================================\n")

if __name__ == "__main__":
    print("Available Algorithms:")
    print("BFS | DFS | A* | HillClimbing | Genetic")
    algo = input("\nEnter algorithm name: ")
    run_algorithm(algo)