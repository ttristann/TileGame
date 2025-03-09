package tmge.core;

import tmge.model.Game;
import tmge.model.GameInfo;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class GameRegistry {
    private Map<String, GameFactory> availableGames;

    public GameRegistry() {
        availableGames = new HashMap<>();
        // Register default games
        // This would be where you register your specific game implementations
    }

    public List<GameFactory> getAvailableGames() {
        return new ArrayList<>(availableGames.values());
    }

    public void registerGame(GameFactory factory) {
        GameInfo info = factory.getGameInfo();
        availableGames.put(info.getName(), factory);
    }

    public Game createGame(String gameType) {
        GameFactory factory = availableGames.get(gameType);
        if (factory != null) {
            return factory.createGame();
        }
        return null;
    }
}
