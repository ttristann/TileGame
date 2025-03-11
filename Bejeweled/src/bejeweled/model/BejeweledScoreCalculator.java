package bejeweled.model;

import java.util.List;

public class BejeweledScoreCalculator {
    public int calculateScoreForMatch(List<Match> matches) {
        int totalScore = 0;
        
        for (Match match : matches) {
            int baseScore = match.getGems().size() * 10;
            
            // Apply multiplier based on match type
            switch (match.getMatchType()) {
                case THREE_IN_A_ROW:
                    totalScore += baseScore;
                    break;
                case FOUR_IN_A_ROW:
                    totalScore += baseScore * 1.5;
                    break;
                case FIVE_IN_A_ROW:
                    totalScore += baseScore * 2;
                    break;
                case L_SHAPE:
                    totalScore += baseScore * 2.5;
                    break;
                case T_SHAPE:
                    totalScore += baseScore * 3;
                    break;
                case CROSS:
                    totalScore += baseScore * 4;
                    break;
            }
        }
        
        return totalScore;
    }
    
    public int calculateBonusScore(int baseScore, int specialGems, int comboDuration) {
        // Apply bonuses based on special gems and combo duration
        double multiplier = 1.0;
        
        // Special gems bonus
        multiplier += specialGems * 0.5;
        
        // Combo duration bonus (longer combos give better scores)
        if (comboDuration > 1) {
            multiplier += (comboDuration - 1) * 0.2;
        }
        
        return (int)(baseScore * multiplier);
    }
}
