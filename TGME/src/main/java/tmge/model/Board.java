package tmge.model;

import tmge.util.TileType;

public class Board {
    private Tile[][] grid;
    private int width;
    private int height;

    public Board(int width, int height) {
        this.width = width;
        this.height = height;
        this.grid = new Tile[height][width];
        initializeBoard();
    }

    private void initializeBoard() {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                grid[i][j] = null; // Initially empty
            }
        }
    }

    public boolean placeTile(int x, int y, Tile tile) {
        if (x >= 0 && x < width && y >= 0 && y < height && grid[y][x] == null) {
            grid[y][x] = tile;
            return true;
        }
        return false;
    }

    public Tile getTile(int x, int y) {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            return grid[y][x];
        }
        return null;
    }

    public void clearTile(int x, int y) {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            grid[y][x] = null;
        }
    }

    public boolean isPositionValid(int x, int y) {
        return x >= 0 && x < width && y >= 0 && y < height;
    }

    public boolean checkTile(int x, int y, TileType type) {
        Tile tile = getTile(x, y);
        return tile != null && tile.getType() == type;
    }

    public void render() {
        // TODO: Render the board
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public boolean isFull() {
        for (int i = 0; i < height; i++) {
            for (int j = 0; j < width; j++) {
                if (grid[i][j] == null) {
                    return false;
                }
            }
        }
        return true;
    }
}

