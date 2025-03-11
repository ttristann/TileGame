package bejeweled.model;

import java.util.ArrayList;
import java.util.List;

public class BejeweledMatchProcessor {
    private BejeweledBoard findMatchesBoard;
    
    public BejeweledMatchProcessor() {
        // Default constructor
    }
    
    public List<Match> findMatches(BejeweledBoard board) {
        return board.checkMatches();
    }
    
    public MatchType identifyMatchPattern(Match match) {
        List<Gem> gems = match.getGems();
        
        // Return the existing match type if already identified
        if (match.getMatchType() != null) {
            return match.getMatchType();
        }
        
        // Identify based on number of gems
        if (gems.size() == 3) {
            return MatchType.THREE_IN_A_ROW;
        } else if (gems.size() == 4) {
            return MatchType.FOUR_IN_A_ROW;
        } else if (gems.size() == 5) {
            return MatchType.FIVE_IN_A_ROW;
        } else if (gems.size() > 5) {
            // Complex patterns like L, T or Cross require more analysis
            // This would need to be implemented with specific shape detection
            return MatchType.FIVE_IN_A_ROW; // Default for now
        }
        
        return null;
    }
}