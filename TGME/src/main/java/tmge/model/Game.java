package tmge.model;
import java.util.List;

public interface Game {
    String getName();
    void initialize();
    void start(List<Player> players);
    void update();
    void render();
    void processInput();
    void end();
}
