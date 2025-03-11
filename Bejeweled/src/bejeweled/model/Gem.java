package bejeweled.model;

import javafx.scene.canvas.GraphicsContext;
import tmge.model.Tile;

public class Gem extends Tile {
    private GemType type;
    private int x;
    private int y;
    private boolean isSelected;
    private boolean isSpecial;

    public Gem(GemType type, int x, int y) {
        super(x, y, type);
        this.type = type;
        this.x = x;
        this.y = y;
        this.isSelected = false;
        this.isSpecial = type.isSpecial();
    }

    public GemType getType() {
        return type;
    }

    public void setType(GemType type) {
        super.setType(type);
        this.type = type;
        this.isSpecial = type.isSpecial();
    }

    public boolean isSelected() {
        return isSelected;
    }

    public void setSelected(boolean selected) {
        isSelected = selected;
    }

    public boolean isSpecial() {
        return isSpecial;
    }

    public void setSpecial(boolean special) {
        isSpecial = special;
    }

    public int activateSpecial() {
        // Returns score from activating the special gem
        if (!isSpecial) {
            return 0;
        }

        // Score depends on special type
        switch (type.getSpecialType()) {
            case FLAME:
                return 200;
            case STAR:
                return 500;
            case HYPERCUBE:
                return 1000;
            default:
                return 0;
        }
    }

    public boolean isMovable() {
        // Check if this gem can be moved (some special gems might be immovable)
        return true;
    }

    @Override
    public void render(GraphicsContext gc, double tileSize) {
        // Draw gem background
        gc.setFill(type.getGemColor());
        
        // Apply visual effect if selected
        if (isSelected) {
            gc.setStroke(javafx.scene.paint.Color.YELLOW);
            gc.setLineWidth(3);
            gc.strokeRect(x * tileSize, y * tileSize, tileSize, tileSize);
        }
        
        // Draw gem sprite
        gc.drawImage(type.getGemSprite(), x * tileSize, y * tileSize, tileSize, tileSize);
        
        // Draw special indicator if needed
        if (isSpecial) {
            gc.setStroke(javafx.scene.paint.Color.WHITE);
            gc.setLineWidth(2);
            
            switch (type.getSpecialType()) {
                case FLAME:
                    // Draw flame symbol
                    gc.strokeOval(x * tileSize + tileSize / 4, y * tileSize + tileSize / 4, tileSize / 2, tileSize / 2);
                    break;
                case STAR:
                    // Draw star symbol
                    gc.strokeText("★", x * tileSize + tileSize / 3, y * tileSize + 2 * tileSize / 3);
                    break;
                case HYPERCUBE:
                    // Draw hypercube symbol
                    gc.strokeRect(x * tileSize + tileSize / 4, y * tileSize + tileSize / 4, tileSize / 2, tileSize / 2);
                    break;
            }
        }
    }
}