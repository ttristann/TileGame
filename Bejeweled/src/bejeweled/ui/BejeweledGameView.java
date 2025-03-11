package bejeweled.ui;

import bejeweled.model.BejeweledGame;
import bejeweled.model.Gem;
import javafx.scene.canvas.Canvas;
import javafx.scene.canvas.GraphicsContext;

public class BejeweledGameView {
    private BejeweledGame game;
    private Canvas canvas;
    private double tileSize;
    
    public BejeweledGameView(BejeweledGame game, int width, int height, double tileSize) {
        this.game = game;
        this.canvas = new Canvas(width * tileSize, height * tileSize);
        this.tileSize = tileSize;
    }
    
    public void render() {
        GraphicsContext gc = canvas.getGraphicsContext2D();
        game.getBoard().render(gc, tileSize);
    }
    
    public Canvas getCanvas() {
        return canvas;
    }
}