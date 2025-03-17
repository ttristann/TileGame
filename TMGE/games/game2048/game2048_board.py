import random

SIZE = 4

class Game2048Board:
    def __init__(self):
        """Initialize the game board."""
        self.matrix = [[0] * SIZE for _ in range(SIZE)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()

    def spawn_tile(self):
        """Spawn a new tile (2 or 4) in an empty cell."""
        empty_cells = [(r, c) for r in range(SIZE) for c in range(SIZE) if self.matrix[r][c] == 0]
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.matrix[row][col] = 2 if random.random() < 0.9 else 4

    def move_tiles(self, up=False, left=False):
        """Shift and merge tiles based on the direction (Up, Down, Left, Right)."""
        moved = False

        for i in range(SIZE):
            if left:  # Moving left or right (process rows)
                tiles = self.matrix[i]  # Get the row
            else:  # Moving up or down (process columns)
                tiles = [self.matrix[r][i] for r in range(SIZE)]  # Get the column

            reverse = (not left and not up) or (left and not up)  # Reverse for Right/Down
            if reverse:
                tiles.reverse()

            new_tiles, score_gained = self.merge_tiles(tiles)

            if reverse:
                new_tiles.reverse()  # Reverse back for Right/Down

            if new_tiles != tiles:
                moved = True
                self.score += score_gained

                if left:  # Set row back for Left/Right
                    self.matrix[i] = new_tiles
                else:  # Set column back for Up/Down
                    for r in range(SIZE):
                        self.matrix[r][i] = new_tiles[r]

        return moved



    def merge_tiles(self, row):
        """Merge a row and calculate score."""
        non_empty = [num for num in row if num != 0]
        merged = []
        score_gained = 0
        skip = False

        for i in range(len(non_empty)):
            if skip:
                skip = False
                continue
            if i + 1 < len(non_empty) and non_empty[i] == non_empty[i + 1]:
                merged.append(non_empty[i] * 2)
                score_gained += non_empty[i] * 2
                skip = True
            else:
                merged.append(non_empty[i])

        while len(merged) < SIZE:
            merged.append(0)

        return merged, score_gained

    def is_game_over(self):
        """Check if no more moves are possible."""
        for row in range(SIZE):
            for col in range(SIZE):
                if self.matrix[row][col] == 0:
                    return False
                if col < SIZE - 1 and self.matrix[row][col] == self.matrix[row][col + 1]:
                    return False
                if row < SIZE - 1 and self.matrix[row][col] == self.matrix[row + 1][col]:
                    return False
        return True
