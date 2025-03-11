package bejeweled.input;

import tmge.input.Command;
import bejeweled.model.BejeweledGame;

public class SwapGemsCommand implements Command {
    private int x1;
    private int y1;
    private int x2;
    private int y2;
    
    public SwapGemsCommand(int x1, int y1, int x2, int y2) {
        this.x1 = x1;
        this.y1 = y1;
        this.x2 = x2;
        this.y2 = y2;
    }
    
    @Override
    public void execute(Object game) {
        if (game instanceof BejeweledGame) {
            ((BejeweledGame) game).swapGems(x1, y1, x2, y2);
        }
    }
}
