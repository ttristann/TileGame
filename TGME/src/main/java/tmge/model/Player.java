package tmge.model;

import java.util.ArrayList;
import java.util.List;

public class Player {
    private String username;
    private String password; // may not need this for a simple login process
    private GameStats gameHistory;
    private List<String> gameStats;

    public Player(String username, String password) {
        this.username = username;
        this.password = password;
        this.gameStats = new ArrayList<>();
    }

    public String getUsername() {
        return username;
    }

    public void updateScore(int score) {
        if (gameHistory != null) {
            gameHistory.updateScore(score);
        }
    }

    public void setGameHistory(GameStats history) {
        this.gameHistory = history;
    }

    public GameStats getGameStats() {
        return gameHistory;
    }

    public void addGameStats(String statData) {
        gameStats.add(statData);
    }

    public List<String> getGameHistoryList() {
        return gameStats;
    }
}
