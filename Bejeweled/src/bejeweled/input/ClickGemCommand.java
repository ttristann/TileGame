package bejeweled.input;

import tmge.input.Command;
import bejeweled.model.BejeweledGame;

public class ClickGemCommand implements Command {
    private int x;
    private int y;
    
    public ClickGemCommand(int x, int y) {
        this.x = x;
        this.y = y;
    }
    
    @Override
    public void execute(Object game) {
        if (game instanceof BejeweledGame) {
            ((BejeweledGame) game).selectGem(x, y);
        }
    }
}
