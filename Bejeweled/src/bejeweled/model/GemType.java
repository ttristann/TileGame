package bejeweled.model;

import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import tmge.util.TileType;

public class GemType extends TileType {
    private int gemId;
    private Color gemColor;
    private Image gemSprite;
    private boolean special;
    private SpecialGemType specialType;

    public GemType(int gemId, Color gemColor, String spritePath, boolean special, SpecialGemType specialType) {
        super(gemId, spritePath);
        this.gemId = gemId;
        this.gemColor = gemColor;
        this.gemSprite = new Image(spritePath);
        this.special = special;
        this.specialType = specialType;
    }

    public GemType(int gemId, Color gemColor, String spritePath) {
        this(gemId, gemColor, spritePath, false, null);
    }

    public Color getGemColor() {
        return gemColor;
    }

    public Image getGemSprite() {
        return gemSprite;
    }

    public boolean isSpecial() {
        return special;
    }

    public SpecialGemType getSpecialType() {
        return specialType;
    }
}