package tmge.model;

import java.util.HashMap;
import java.util.Map;

public class User {
    private String username;
    // private String password;
    private Map<String, GameStats> gameStats;

    public User(String username) {
        this.username = username;
        // this.password = password; -- may not need password since login just has to be simple
        this.gameStats = new HashMap<>();
    }

    public String getUsername() {
        return username;
    }

//    public String getPassword() {
//        return password;
//    }

//    public boolean validatePassword(String password) { // may not need this class
//        return this.password.equals(password);
//    }

    public GameStats getGameStats(String gameType) {
        return gameStats.getOrDefault(gameType, new GameStats(username, gameType));
    }

    public void setGameStats(String gameType, GameStats stats) {
        gameStats.put(gameType, stats);
    }

    public void updateStats(String gameType, int result) {
        GameStats stats = getGameStats(gameType);
        stats.updateScore(result);
        gameStats.put(gameType, stats);
    }
}