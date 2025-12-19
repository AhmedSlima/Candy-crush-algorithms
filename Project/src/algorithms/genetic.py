import copy
import random
from match3game import Match3Game, MAX_MOVES, TARGET_SCORE

def genetic_solver(pop_size=10, generations=5, mutation_rate=0.1):
    game = Match3Game()
    best_score = 0
    nodes = 0

    def create_random_chromosome():
        return [(random.randint(0,7), random.randint(0,7), random.choice([(0,1),(1,0)])) for _ in range(MAX_MOVES)]

    def evaluate(chrom):
        nonlocal nodes
        nodes +=1
        test_game = copy.deepcopy(game)
        for x, y, (dx, dy) in chrom:
            if test_game.game_over():
                break
            nx, ny = x + dx, y + dy
            if test_game.in_bounds(nx, ny):
                result = test_game.swap(x, y, nx, ny)
                if result:
                    test_game = result
        return test_game.score

    population = [create_random_chromosome() for _ in range(pop_size)]
    for _ in range(generations):
        scores = [evaluate(ind) for ind in population]
        best_score = max(best_score, max(scores))
        sorted_pop = [x for _, x in sorted(zip(scores, population), key=lambda pair: pair[0], reverse=True)]
        new_pop = sorted_pop[:max(1,int(0.2*pop_size))]
        while len(new_pop) < pop_size:
            parent1, parent2 = random.sample(sorted_pop[:pop_size//2], 2)
            point = random.randint(1, MAX_MOVES-1)
            c1 = parent1[:point] + parent2[point:]
            c2 = parent2[:point] + parent1[point:]
            if random.random() < mutation_rate: 
                c1[random.randint(0,MAX_MOVES-1)] = (random.randint(0,7), random.randint(0,7), random.choice([(0,1),(1,0)]))
            if random.random() < mutation_rate: 
                c2[random.randint(0,MAX_MOVES-1)] = (random.randint(0,7), random.randint(0,7), random.choice([(0,1),(1,0)]))
            new_pop.extend([c1,c2])
        population = new_pop[:pop_size]

    return {
        "Algorithm": "Genetic",
        "Final Score": best_score,
        "Moves Used": MAX_MOVES,
        "Nodes Explored": nodes,
        "Reached Goal": best_score >= TARGET_SCORE
    }

if __name__ == "__main__":
    result = genetic_solver()
    for k, v in result.items():
        print(f"{k:15}: {v}")