package bejeweled.util;

public class SpecialGemProcessor {
    public int processSpecialGem(BejeweledBoard board, Gem gem, int x, int y) {
        if (!gem.isSpecial()) {
            return 0;
        }
        
        int score = 0;
        
        switch (gem.getType().getSpecialType()) {
            case FLAME:
                // Destroy gems in a 3x3 area
                score = processFlameGem(board, x, y);
                break;
            case STAR:
                // Destroy all gems of the same color
                score = processStarGem(board, gem.getType());
                break;
            case HYPERCUBE:
                // Destroy all gems of a selected color
                score = processHypercubeGem(board, gem.getType());
                break;
        }
        
        return score;
    }
    
    private int processFlameGem(BejeweledBoard board, int centerX, int centerY) {
        int gemsDestroyed = 0;
        
        // Process 3x3 grid around the flame gem
        for (int x = centerX - 1; x <= centerX + 1; x++) {
            for (int y = centerY - 1; y <= centerY + 1; y++) {
                Gem gem = board.getGemAt(x, y);
                if (gem != null) {
                    gemsDestroyed++;
                    // In a real implementation, you would remove the gem here
                }
            }
        }
        
        return gemsDestroyed * 20; // 20 points per gem destroyed
    }
    
    private int processStarGem(BejeweledBoard board, GemType targetType) {
        // In a real implementation, you would scan the board and destroy all gems of the same color
        // Simplified for this example
        return 500; // Fixed score for star gem activation
    }
    
    private int processHypercubeGem(BejeweledBoard board, GemType targetType) {
        // In a real implementation, you would scan the board and destroy all gems of the selected color
        // Simplified for this example
        return 1000; // Fixed score for hypercube activation
    }
    
    public Gem createSpecialGem(MatchType matchType, GemType baseType) {
        SpecialGemType specialType = null;
        
        // Determine special gem type based on match pattern
        switch (matchType) {
            case FOUR_IN_A_ROW:
                specialType = SpecialGemType.FLAME;
                break;
            case FIVE_IN_A_ROW:
                specialType = SpecialGemType.STAR;
                break;
            case L_SHAPE:
            case T_SHAPE:
            case CROSS:
                specialType = SpecialGemType.HYPERCUBE;
                break;
            default:
                return null; // No special gem for THREE_IN_A_ROW
        }
        
        // Create a new gem type with special properties
        GemType specialGemType = new GemType(
            baseType.getId(),
            baseType.getGemColor(),
            baseType.getSpritePath(),
            true,
            specialType
        );
        
        // Create a special gem at the origin (position will be set later)
        Gem specialGem = new Gem(specialGemType, 0, 0);
        specialGem.setSpecial(true);
        
        return specialGem;
    }
}