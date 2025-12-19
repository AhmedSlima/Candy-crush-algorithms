import random

BOARD_SIZE = 8
CANDIES = ['R', 'G', 'B', 'Y', 'P']
TARGET_SCORE = 600
MAX_MOVES = 15

def generate_board():
    return [[random.choice(CANDIES) for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)]