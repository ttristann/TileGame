package tmge.core;

import tmge.model.Game;
import tmge.model.Player;
import tmge.model.User;

import java.util.ArrayList;
import java.util.List;

public class GameManager {
    private List<Player> players;
    private Game currentGame;

    public GameManager() {
        players = new ArrayList<>();
    }

    public void startGame(String gameType, List<User> users) {
        GameRegistry registry = new GameRegistry();
        currentGame = registry.createGame(gameType);

        // Convert Users to Players
        players.clear();
        for (User user : users) {
            Player player = new Player(user.getUsername()); // may not need password
            player.setGameHistory(user.getGameStats(gameType));
            players.add(player);
        }

        if (currentGame != null) {
            currentGame.initialize();
            currentGame.start(players);
        }
    }

    public Game getCurrentGame() {
        return currentGame;
    }

    public List<Player> getPlayers() {
        return players;
    }

    public void endGame() {
        if (currentGame != null) {
            currentGame.end();
            currentGame = null;
        }
    }
}
