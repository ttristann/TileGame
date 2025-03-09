package tmge.util;

import javafx.scene.paint.Color;

public class TileType {
    private int id;
    private Color color;
    private String sprite;

    public TileType(int id, Color color, String sprite) {
        this.id = id;
        this.color = color;
        this.sprite = sprite;
    }

    public int getId() {
        return id;
    }

    public Color getColor() {
        return color;
    }

    public String getSprite() {
        return sprite;
    }

    // Factory methods for common tile types
    public static TileType createRedTile() {
        return new TileType(1, Color.RED, "red_tile");
    }

    public static TileType createBlueTile() {
        return new TileType(2, Color.BLUE, "blue_tile");
    }

    public static TileType createGreenTile() {
        return new TileType(3, Color.GREEN, "green_tile");
    }

    public static TileType createYellowTile() {
        return new TileType(4, Color.YELLOW, "yellow_tile");
    }
}
