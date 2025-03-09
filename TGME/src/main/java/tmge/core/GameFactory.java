package tmge.core;

import tmge.model.Game;
import tmge.model.GameInfo;

public interface GameFactory {
    Game createGame();
    GameInfo getGameInfo();
}
