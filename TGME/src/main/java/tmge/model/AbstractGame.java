package tmge.model;

import java.util.List;

public abstract class AbstractGame implements Game {
    protected String name;
    protected List<Player> players;
    protected Board board;
    protected GameState state;

    public AbstractGame(String name) {
        this.name = name;
        this.state = GameState.INITIALIZING;
    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public void initialize() {
        // Create game board
        createBoard();
        state = GameState.INITIALIZED;
    }

    @Override
    public void start(List<Player> players) {
        this.players = players;
        state = GameState.RUNNING;
    }

    @Override
    public void update() {
        // TODO: Game loop logic
    }

    @Override
    public void render() {
        // TODO: Render game
    }

    @Override
    public void end() {
        state = GameState.ENDED;

        // Update player stats
        for (Player player : players) {
            player.updateScore(calculateScore());
        }
    }

    protected abstract void createBoard();
    protected abstract int calculateScore();
}
