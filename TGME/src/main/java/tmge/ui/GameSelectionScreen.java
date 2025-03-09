package tmge.ui;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.ListView;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.stage.Stage;
import tmge.core.GameManager;
import tmge.core.GameRegistry;
import tmge.core.UserManager;
import tmge.model.Player;
import tmge.model.User;

import java.util.ArrayList;
import java.util.List;

public class GameSelectionScreen {
    private UserManager userManager;
    private GameRegistry gameRegistry;
    private GameManager gameManager;

    public GameSelectionScreen(UserManager userManager) {
        this.userManager = userManager;
        this.gameRegistry = new GameRegistry();
        this.gameManager = new GameManager();
    }

    public void show(Stage primaryStage) {
        primaryStage.setTitle("TMGE - Game Selection");

        BorderPane borderPane = new BorderPane();
        borderPane.setPadding(new Insets(20));

        // Header
        Label headerLabel = new Label("Choose a Game");
        headerLabel.setFont(Font.font("Tahoma", FontWeight.BOLD, 20));
        BorderPane.setAlignment(headerLabel, Pos.CENTER);
        borderPane.setTop(headerLabel);

        // Game List
        ListView<String> gameListView = new ListView<>();
        gameRegistry.getAvailableGames().forEach(game ->
                gameListView.getItems().add(game.getGameInfo().getName()));

        // If no games are registered yet, add some placeholders
        if (gameListView.getItems().isEmpty()) {
            gameListView.getItems().addAll("Tetris", "Bejeweled", "Candy Crush");
        }

        VBox centerBox = new VBox(10);
        centerBox.getChildren().addAll(new Label("Available Games:"), gameListView);
        centerBox.setPadding(new Insets(10, 0, 10, 0));
        borderPane.setCenter(centerBox);

        // Buttons
        Button playButton = new Button("Play Game");
        Button logoutButton = new Button("Logout");

        HBox buttonBox = new HBox(10);
        buttonBox.setAlignment(Pos.CENTER);
        buttonBox.getChildren().addAll(playButton, logoutButton);
        borderPane.setBottom(buttonBox);

        // Event handlers
        playButton.setOnAction(e -> {
            String selectedGame = gameListView.getSelectionModel().getSelectedItem();
            if (selectedGame != null) {
                User currentUser = userManager.getCurrentUser();
                if (currentUser != null) {
                    List<User> players = new ArrayList<>();
                    players.add(currentUser);

                    // For demonstration, adding a second player
                    User player2 = userManager.getUser("player2");
                    if (player2 != null) {
                        players.add(player2);
                    }

                    startGame(primaryStage, selectedGame, players);
                }
            }
        });

        logoutButton.setOnAction(e -> {
            userManager.logout();
            showLoginScreen(primaryStage);
        });

        Scene scene = new Scene(borderPane, 500, 400);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void startGame(Stage primaryStage, String gameType, List<User> players) {
        // In a real implementation, this would start the selected game
        // For now, just show a placeholder
        BorderPane gamePane = new BorderPane();
        Label gameLabel = new Label("Playing " + gameType);
        gameLabel.setFont(Font.font("Tahoma", FontWeight.BOLD, 24));
        gamePane.setCenter(gameLabel);

        Button backButton = new Button("Back to Game Selection");
        backButton.setOnAction(e -> show(primaryStage));

        HBox bottomBox = new HBox(10);
        bottomBox.setAlignment(Pos.CENTER);
        bottomBox.getChildren().add(backButton);
        bottomBox.setPadding(new Insets(20));
        gamePane.setBottom(bottomBox);

        Scene gameScene = new Scene(gamePane, 800, 600);
        primaryStage.setScene(gameScene);
    }

    private void showLoginScreen(Stage primaryStage) {
        LoginScreen loginScreen = new LoginScreen(userManager);
        loginScreen.show(primaryStage);
    }

    public void displayGames() {
        // TODO: Display list of available games
    }

    public void selectGame(String game) {
        // TODO: Select a game to play
    }

    public void selectPlayers(List<Player> players) {
        // TODO: Select players for the game
    }
}
