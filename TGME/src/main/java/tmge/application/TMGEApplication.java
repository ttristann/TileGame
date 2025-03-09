package tmge.application;

import javafx.application.Application;
import javafx.stage.Stage;
import tmge.core.GameManager;
import tmge.core.GameRegistry;
import tmge.core.UserManager;
import tmge.model.User;
import tmge.ui.LoginScreen;

import java.util.List;

public class TMGEApplication extends Application {
    private UserManager userManager;
    private GameManager gameManager;
    private GameRegistry gameRegistry;

    @Override
    public void start(Stage primaryStage) {
        // Initialize core components
        initializeComponents();

        // Show login screen
        LoginScreen loginScreen = new LoginScreen(userManager);
        loginScreen.show(primaryStage);
    }

    private void initializeComponents() {
        userManager = new UserManager();
        gameRegistry = new GameRegistry();
        gameManager = new GameManager();
    }

    public void initialize() {
        // TODO: Initialize application components
    }

    public void startGame(String gameType, List<User> players) {
        gameManager.startGame(gameType, players);
    }

    public void showGameSelection() {
        // TODO: Show game selection screen
    }

    public void login(String username) {
        userManager.login(username); // may not need password
    }

    public void registerUser(String username) {
        userManager.registerUser(username);
    }

    public static void main(String[] args) {
        launch(args);
    }
}