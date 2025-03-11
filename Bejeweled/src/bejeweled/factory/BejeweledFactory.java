package bejeweled.factory;

import java.util.ArrayList;
import java.util.List;

import bejeweled.model.BejeweledGame;
import bejeweled.model.GemType;
import javafx.scene.image.Image;
import javafx.scene.paint.Color;
import tmge.core.GameFactory;
import tmge.core.GameInfo;
import tmge.model.User;

public class BejeweledFactory implements GameFactory {
    
    @Override
    public GameInfo getGameInfo() {
        return new GameInfo(
            "Bejeweled",
            "Match three or more gems to score points!",
            1, // Min players
            1, // Max players
            "Match-3"
        );
    }
    
    @Override
    public BejeweledGame createGame(List<User> players) {
        // Set up default board dimensions
        int boardWidth = 8;
        int boardHeight = 8;
        
        // Create game with default settings
        BejeweledGame game = new BejeweledGame(
            boardWidth,
            boardHeight,
            createGemTypes(),
            players.get(0)
        );
        
        // Initialize the game
        game.initialize();
        
        return game;
    }
    
    /**
     * Creates the standard set of gem types used in Bejeweled
     * @return List of gem types
     */
    private List<GemType> createGemTypes() {
        List<GemType> gemTypes = new ArrayList<>();
        
        // Create standard gem types with different colors
        // REPLACE these paths with actual gem images
        gemTypes.add(new GemType(0, Color.RED, "bejeweled/resources/gems/red_gem.png"));
        gemTypes.add(new GemType(1, Color.BLUE, "bejeweled/resources/gems/blue_gem.png"));
        gemTypes.add(new GemType(2, Color.GREEN, "bejeweled/resources/gems/green_gem.png"));
        gemTypes.add(new GemType(3, Color.YELLOW, "bejeweled/resources/gems/yellow_gem.png"));
        gemTypes.add(new GemType(4, Color.PURPLE, "bejeweled/resources/gems/purple_gem.png"));
        gemTypes.add(new GemType(5, Color.ORANGE, "bejeweled/resources/gems/orange_gem.png"));
        gemTypes.add(new GemType(6, Color.CYAN, "bejeweled/resources/gems/cyan_gem.png"));
        
        return gemTypes;
    }
    
    /**
     * Fallback method to create colored rectangles if image resources aren't available
     * This can help during development before you have proper sprites
     * @return List of gem types using simple colors
     */
    private List<GemType> createFallbackGemTypes() {
        List<GemType> gemTypes = new ArrayList<>();
        
        // Create basic colored gem types
        gemTypes.add(new GemType(0, Color.RED, ""));
        gemTypes.add(new GemType(1, Color.BLUE, ""));
        gemTypes.add(new GemType(2, Color.GREEN, ""));
        gemTypes.add(new GemType(3, Color.YELLOW, ""));
        gemTypes.add(new GemType(4, Color.PURPLE, ""));
        gemTypes.add(new GemType(5, Color.ORANGE, ""));
        gemTypes.add(new GemType(6, Color.CYAN, ""));
        
        return gemTypes;
    }
}