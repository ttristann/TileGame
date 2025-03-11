package bejeweled.model;

import java.util.List;
import tmge.model.User;

public class BejeweledGame {
    private BejeweledBoard board;
    private User player;
    private int score;
    
    public BejeweledGame(int width, int height, List<GemType> gemTypes, User player) {
        this.board = new BejeweledBoard(width, height, gemTypes);
        this.player = player;
        this.score = 0;
    }
    
    public void initialize() {
        board.generateRandomGrid();
    }
    
    public void selectGem(int x, int y) {
        // Handle gem selection logic
    }
    
    public void swapGems(int x1, int y1, int x2, int y2) {
        if (board.swapGems(board.getGemAt(x1, y1), board.getGemAt(x2, y2))) {
            List<Match> matches = board.checkMatches();
            score += board.removeMatches(matches);
            board.fillEmptySpaces();
        }
    }
    
    public int getScore() {
        return score;
    }
}