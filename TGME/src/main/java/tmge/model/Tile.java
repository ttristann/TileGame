package tmge.model;

import tmge.util.TileType;

public class Tile {
    private TileType type;
    private int x;
    private int y;

    public Tile(TileType type) {
        this.type = type;
        this.x = 0;
        this.y = 0;
    }

    public Tile(TileType type, int x, int y) {
        this.type = type;
        this.x = x;
        this.y = y;
    }

    public TileType getType() {
        return type;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setPosition(int x, int y) {
        this.x = x;
        this.y = y;
    }

    public void moveUp() {
        y--;
    }

    public void moveDown() {
        y++;
    }

    public void moveLeft() {
        x--;
    }

    public void moveRight() {
        x++;
    }

    public boolean canMoveTo(Board board, int newX, int newY) {
        return board.isPositionValid(newX, newY) && board.getTile(newX, newY) == null;
    }

    public void render() {
        // Render the tile
    }
}
