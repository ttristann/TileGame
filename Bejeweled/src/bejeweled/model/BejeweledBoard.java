package bejeweled.model;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import javafx.scene.canvas.GraphicsContext;
import tmge.model.Board;

public class BejeweledBoard extends Board {
    private Gem[][] grid;
    private int width;
    private int height;
    private List<GemType> gemTypes;
    private Random random;

    public BejeweledBoard(int width, int height, List<GemType> gemTypes) {
        super(width, height);
        this.width = width;
        this.height = height;
        this.gemTypes = gemTypes;
        this.grid = new Gem[width][height];
        this.random = new Random();
    }

    public void generateRandomGrid() {
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                GemType randomType = gemTypes.get(random.nextInt(gemTypes.size()));
                grid[x][y] = new Gem(randomType, x, y);
            }
        }
        
        // Make sure we don't start with matches
        while (checkMatches().size() > 0) {
            for (int x = 0; x < width; x++) {
                for (int y = 0; y < height; y++) {
                    if (hasMatchAt(x, y)) {
                        GemType randomType = gemTypes.get(random.nextInt(gemTypes.size()));
                        grid[x][y].setType(randomType);
                    }
                }
            }
        }
    }

    private boolean hasMatchAt(int x, int y) {
        if (x < 2) return false;
        if (y < 2) return false;
        
        Gem current = grid[x][y];
        
        // Check horizontal match
        if (grid[x-1][y].getType().getId() == current.getType().getId() && 
            grid[x-2][y].getType().getId() == current.getType().getId()) {
            return true;
        }
        
        // Check vertical match
        if (grid[x][y-1].getType().getId() == current.getType().getId() && 
            grid[x][y-2].getType().getId() == current.getType().getId()) {
            return true;
        }
        
        return false;
    }

    public boolean swapGems(Gem gem1, Gem gem2) {
        // Check if gems are adjacent
        if (!areGemsAdjacent(gem1, gem2)) {
            return false;
        }

        // Swap positions in grid
        int x1 = gem1.getX();
        int y1 = gem1.getY();
        int x2 = gem2.getX();
        int y2 = gem2.getY();

        grid[x1][y1] = gem2;
        grid[x2][y2] = gem1;

        // Update gem coordinates
        gem1.setX(x2);
        gem1.setY(y2);
        gem2.setX(x1);
        gem2.setY(y1);

        // Check if swap created any matches
        List<Match> matches = checkMatches();
        if (matches.isEmpty()) {
            // If no matches, swap back
            grid[x1][y1] = gem1;
            grid[x2][y2] = gem2;
            gem1.setX(x1);
            gem1.setY(y1);
            gem2.setX(x2);
            gem2.setY(y2);
            return false;
        }

        return true;
    }

    private boolean areGemsAdjacent(Gem gem1, Gem gem2) {
        int xDiff = Math.abs(gem1.getX() - gem2.getX());
        int yDiff = Math.abs(gem1.getY() - gem2.getY());
        
        // Gems are adjacent if they differ by 1 in only one dimension
        return (xDiff == 1 && yDiff == 0) || (xDiff == 0 && yDiff == 1);
    }

    public List<Match> checkMatches() {
        List<Match> matches = new ArrayList<>();
        
        // Check horizontal matches
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width - 2; x++) {
                Match match = checkHorizontalMatch(x, y);
                if (match != null) {
                    matches.add(match);
                    // Skip ahead to avoid duplicate matches
                    x += match.getGems().size() - 1;
                }
            }
        }
        
        // Check vertical matches
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height - 2; y++) {
                Match match = checkVerticalMatch(x, y);
                if (match != null) {
                    matches.add(match);
                    // Skip ahead to avoid duplicate matches
                    y += match.getGems().size() - 1;
                }
            }
        }
        
        // Check for L, T, and cross shapes
        checkComplexMatches(matches);
        
        return matches;
    }

    private Match checkHorizontalMatch(int startX, int y) {
        if (startX >= width - 2) return null;
        
        ArrayList<Gem> matchingGems = new ArrayList<>();
        GemType startType = grid[startX][y].getType();
        
        for (int x = startX; x < width; x++) {
            if (grid[x][y].getType().getId() == startType.getId()) {
                matchingGems.add(grid[x][y]);
            } else {
                break;
            }
        }
        
        if (matchingGems.size() >= 3) {
            MatchType matchType;
            switch (matchingGems.size()) {
                case 3: matchType = MatchType.THREE_IN_A_ROW; break;
                case 4: matchType = MatchType.FOUR_IN_A_ROW; break;
                case 5: matchType = MatchType.FIVE_IN_A_ROW; break;
                default: matchType = MatchType.FIVE_IN_A_ROW; break; // For more than 5
            }
            
            // Basic scoring: 10 points per gem
            int score = matchingGems.size() * 10;
            
            return new Match(matchingGems, matchType, score);
        }
        
        return null;
    }

    private Match checkVerticalMatch(int x, int startY) {
        if (startY >= height - 2) return null;
        
        ArrayList<Gem> matchingGems = new ArrayList<>();
        GemType startType = grid[x][startY].getType();
        
        for (int y = startY; y < height; y++) {
            if (grid[x][y].getType().getId() == startType.getId()) {
                matchingGems.add(grid[x][y]);
            } else {
                break;
            }
        }
        
        if (matchingGems.size() >= 3) {
            MatchType matchType;
            switch (matchingGems.size()) {
                case 3: matchType = MatchType.THREE_IN_A_ROW; break;
                case 4: matchType = MatchType.FOUR_IN_A_ROW; break;
                case 5: matchType = MatchType.FIVE_IN_A_ROW; break;
                default: matchType = MatchType.FIVE_IN_A_ROW; break; // For more than 5
            }
            
            // Basic scoring: 10 points per gem
            int score = matchingGems.size() * 10;
            
            return new Match(matchingGems, matchType, score);
        }
        
        return null;
    }

    private void checkComplexMatches(List<Match> matches) {
        // This is a more complex implementation that would find L, T, and cross shapes
        // Simplified for now
    }

    public int removeMatches(List<Match> matches) {
        int totalScore = 0;
        
        // Mark all matched gems for removal
        for (Match match : matches) {
            for (Gem gem : match.getGems()) {
                grid[gem.getX()][gem.getY()] = null;
            }
            totalScore += match.getScore();
        }
        
        return totalScore;
    }

    public void fillEmptySpaces() {
        // First, move gems down to fill empty spaces
        for (int x = 0; x < width; x++) {
            int emptySpaces = 0;
            
            // Move from bottom to top
            for (int y = height - 1; y >= 0; y--) {
                if (grid[x][y] == null) {
                    emptySpaces++;
                } else if (emptySpaces > 0) {
                    // Move gem down by the number of empty spaces
                    int newY = y + emptySpaces;
                    grid[x][newY] = grid[x][y];
                    grid[x][y] = null;
                    
                    // Update gem's position
                    grid[x][newY].setY(newY);
                }
            }
            
            // Fill the top with new gems
            for (int y = 0; y < emptySpaces; y++) {
                GemType randomType = gemTypes.get(random.nextInt(gemTypes.size()));
                grid[x][y] = new Gem(randomType, x, y);
            }
        }
    }

    public boolean hasValidMoves() {
        // Check for potential matches by trying all possible swaps
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                // Check swap with right neighbor
                if (x < width - 1) {
                    if (wouldCreateMatch(x, y, x + 1, y)) {
                        return true;
                    }
                }
                
                // Check swap with bottom neighbor
                if (y < height - 1) {
                    if (wouldCreateMatch(x, y, x, y + 1)) {
                        return true;
                    }
                }
            }
        }
        
        return false;
    }

    private boolean wouldCreateMatch(int x1, int y1, int x2, int y2) {
        // Temporarily swap and check
        Gem gem1 = grid[x1][y1];
        Gem gem2 = grid[x2][y2];
        
        // Swap positions
        grid[x1][y1] = gem2;
        grid[x2][y2] = gem1;
        
        // Update coordinates
        int tempX = gem1.getX();
        int tempY = gem1.getY();
        gem1.setX(gem2.getX());
        gem1.setY(gem2.getY());
        gem2.setX(tempX);
        gem2.setY(tempY);
        
        // Check for matches
        boolean hasMatch = !checkMatches().isEmpty();
        
        // Swap back
        grid[x1][y1] = gem1;
        grid[x2][y2] = gem2;
        gem1.setX(x1);
        gem1.setY(y1);
        gem2.setX(x2);
        gem2.setY(y2);
        
        return hasMatch;
    }

    public List<Position> getHint() {
        List<Position> hintPositions = new ArrayList<>();
        
        // Check all possible swaps
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                // Check swap with right neighbor
                if (x < width - 1 && wouldCreateMatch(x, y, x + 1, y)) {
                    hintPositions.add(new Position(x, y));
                    hintPositions.add(new Position(x + 1, y));
                    return hintPositions;
                }
                
                // Check swap with bottom neighbor
                if (y < height - 1 && wouldCreateMatch(x, y, x, y + 1)) {
                    hintPositions.add(new Position(x, y));
                    hintPositions.add(new Position(x, y + 1));
                    return hintPositions;
                }
            }
        }
        
        return hintPositions;
    }

    public Gem getGemAt(int x, int y) {
        if (x >= 0 && x < width && y >= 0 && y < height) {
            return grid[x][y];
        }
        return null;
    }

    @Override
    public void render(GraphicsContext gc, double tileSize) {
        // Draw board background
        gc.setFill(javafx.scene.paint.Color.DARKBLUE);
        gc.fillRect(0, 0, width * tileSize, height * tileSize);
        
        // Draw gems
        for (int x = 0; x < width; x++) {
            for (int y = 0; y < height; y++) {
                if (grid[x][y] != null) {
                    grid[x][y].render(gc, tileSize);
                }
            }
        }
    }

    // Helper class for hint positions
    public static class Position {
        private int x;
        private int y;
        
        public Position(int x, int y) {
            this.x = x;
            this.y = y;
        }
        
        public int getX() {
            return x;
        }
        
        public int getY() {
            return y;
        }
    }
}