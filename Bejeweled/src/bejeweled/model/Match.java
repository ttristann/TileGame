package bejeweled.model;

import java.util.List;

public class Match {
    private List<Gem> gems;
    private MatchType matchType;
    private int score;

    public Match(List<Gem> gems, MatchType matchType, int score) {
        this.gems = gems;
        this.matchType = matchType;
        this.score = score;
    }

    public List<Gem> getGems() {
        return gems;
    }

    public int getScore() {
        return score;
    }

    public MatchType getMatchType() {
        return matchType;
    }

    public Gem createSpecialGem() {
        // Create a special gem based on match type
        if (gems.isEmpty()) {
            return null;
        }

        Gem baseGem = gems.get(0);
        GemType baseType = baseGem.getType();
        
        // Determine special gem type based on match pattern
        SpecialGemType specialType = null;
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
        
        // Create new gem type with special properties
        GemType specialGemType = new GemType(
            baseType.getId(),
            baseType.getGemColor(),
            baseType.getSpritePath(),
            true,
            specialType
        );
        
        // Create the special gem at the first gem's position
        Gem specialGem = new Gem(specialGemType, baseGem.getX(), baseGem.getY());
        specialGem.setSpecial(true);
        
        return specialGem;
    }
}