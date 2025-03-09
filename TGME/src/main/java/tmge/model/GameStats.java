package tmge.model;

import java.time.LocalDateTime;

public class GameStats {
    private String playerName;
    private String gameName;
    private int score;
    private LocalDateTime timestamp;
    private int duration;

    public GameStats(String playerName, String gameName) {
        this.playerName = playerName;
        this.gameName = gameName;
        this.score = 0;
        this.timestamp = LocalDateTime.now();
        this.duration = 0;
    }

    public String getPlayerName() {
        return playerName;
    }

    public String getGameName() {
        return gameName;
    }

    public int getScore() {
        return score;
    }

    public LocalDateTime getTimestamp() {
        return timestamp;
    }

    public void updateScore(int result) {
        this.score = result;
        this.timestamp = LocalDateTime.now();
    }

    public void setDuration(int seconds) {
        this.duration = seconds;
    }

    public int getDuration() {
        return duration;
    }

    @Override
    public String toString() {
        return String.format(
                "Game: %s, Player: %s, Score: %d, Played on: %s",
                gameName, playerName, score, timestamp
        );
    }
}
