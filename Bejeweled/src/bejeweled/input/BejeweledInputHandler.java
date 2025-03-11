package bejeweled.input;

import tmge.input.InputHandler;
import javafx.scene.input.MouseEvent;

public class BejeweledInputHandler extends InputHandler {
    private int boardX;
    private int boardY;
    private double tileSize;
    
    public BejeweledInputHandler(int boardX, int boardY, double tileSize) {
        this.boardX = boardX;
        this.boardY = boardY;
        this.tileSize = tileSize;
    }
    
    public SwapGemsCommand handleMouseClick(MouseEvent event) {
        // Calculate grid position from mouse coordinates
        int gridX = (int)((event.getX() - boardX) / tileSize);
        int gridY = (int)((event.getY() - boardY) / tileSize);
        
        // Return a click command with the grid coordinates
        return new ClickGemCommand(gridX, gridY);
    }
    
    public SwapGemsCommand handleDragEnd(MouseEvent startEvent, MouseEvent endEvent) {
        // Calculate starting and ending grid positions
        int startX = (int)((startEvent.getX() - boardX) / tileSize);
        int startY = (int)((startEvent.getY() - boardY) / tileSize);
        int endX = (int)((endEvent.getX() - boardX) / tileSize);
        int endY = (int)((endEvent.getY() - boardY) / tileSize);
        
        // Check if this is a valid swap (adjacent tiles)
        if (isValidSwap(startX, startY, endX, endY)) {
            return new SwapGemsCommand(startX, startY, endX, endY);
        }
        
        return null;
    }
    
    private boolean isValidSwap(int x1, int y1, int x2, int y2) {
        // Check if the two positions are adjacent
        int xDiff = Math.abs(x1 - x2);
        int yDiff = Math.abs(y1 - y2);
        
        return (xDiff == 1 && yDiff == 0) || (xDiff == 0 && yDiff == 1);
    }
}
