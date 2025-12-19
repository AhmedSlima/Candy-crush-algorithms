import copy
from board import BOARD_SIZE, CANDIES, TARGET_SCORE, MAX_MOVES, generate_board

class Match3Game:
    def _init_(self, board=None):
        self.size = BOARD_SIZE
        self.max_moves = MAX_MOVES
        self.target_score = TARGET_SCORE
        self.board = board if board else generate_board()
        self.score = 0
        self.moves_left = self.max_moves

    def in_bounds(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size

    def is_goal(self):
        return self.score >= self.target_score

    def game_over(self):
        return self.is_goal() or self.moves_left <= 0

    def swap(self, x1, y1, x2, y2):
        if not self.in_bounds(x1, y1) or not self.in_bounds(x2, y2):
            return None

        new_game = copy.deepcopy(self)
        new_game.board[x1][y1], new_game.board[x2][y2] = new_game.board[x2][y2], new_game.board[x1][y1]

        matches = new_game.find_matches()
        if not matches:
            return None

        new_game.apply_matches(matches)
        new_game.moves_left -= 1
        return new_game

    def find_matches(self):
        matches = []

        # Horizontal matches
        for i in range(self.size):
            count = 1
            for j in range(1, self.size):
                if self.board[i][j] == self.board[i][j - 1]:
                    count += 1
                else:
                    if count >= 3:
                        matches.append((i, j - 1, count, 'H'))
                    count = 1
            if count >= 3:
                matches.append((i, self.size - 1, count, 'H'))

        # Vertical matches
        for j in range(self.size):
            count = 1
            for i in range(1, self.size):
                if self.board[i][j] == self.board[i - 1][j]:
                    count += 1
                else:
                    if count >= 3:
                        matches.append((i - 1, j, count, 'V'))
                    count = 1
            if count >= 3:
                matches.append((self.size - 1, j, count, 'V'))

        return matches

    def apply_matches(self, matches):
        SCORE_TABLE = {3: 30, 4: 50, 5: 80}
        for x, y, length, direction in matches:
            self.score += SCORE_TABLE.get(min(length, 5), 0)
            for k in range(length):
                if direction == 'H':
                    self.board[x][y - k] = random.choice(CANDIES)
                else:
                    self.board[x - k][y] = random.choice(CANDIES)

    def get_successors(self):
        successors = []
        if self.game_over():
            return successors

        directions = [(0, 1), (1, 0)]
        for x in range(self.size):
            for y in range(self.size):
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if self.in_bounds(nx, ny):
                        new_state = self.swap(x, y, nx, ny)
                        if new_state:
                            successors.append(new_state)
        return successors