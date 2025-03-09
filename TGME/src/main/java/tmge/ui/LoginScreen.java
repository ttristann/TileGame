package tmge.ui;

import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.HBox;
import javafx.scene.text.Font;
import javafx.scene.text.FontWeight;
import javafx.scene.text.Text;
import javafx.stage.Stage;
import tmge.core.UserManager;
import tmge.model.User;

public class LoginScreen {
    private UserManager userManager;

    public LoginScreen(UserManager userManager) {
        this.userManager = userManager;
    }

    public void show(Stage primaryStage) {
        primaryStage.setTitle("TMGE - Login");
        GridPane grid = new GridPane();
        grid.setAlignment(Pos.CENTER);
        grid.setHgap(10);
        grid.setVgap(10);
        grid.setPadding(new Insets(25, 25, 25, 25));

        Text sceneTitle = new Text("Welcome to TMGE");
        sceneTitle.setFont(Font.font("Tahoma", FontWeight.NORMAL, 20));
        grid.add(sceneTitle, 0, 0, 2, 1);

        Label userName = new Label("Username:");
        grid.add(userName, 0, 1);

        TextField userTextField = new TextField();
        grid.add(userTextField, 1, 1);

//        Label pw = new Label("Password:");
//        grid.add(pw, 0, 2);
//
//        PasswordField pwBox = new PasswordField();
//        grid.add(pwBox, 1, 2);

        Button loginBtn = new Button("Sign in");
        HBox hbBtn = new HBox(10);
        hbBtn.setAlignment(Pos.BOTTOM_RIGHT);
        hbBtn.getChildren().add(loginBtn);
        grid.add(hbBtn, 1, 4);

        Button registerBtn = new Button("Register");
        HBox hbRegBtn = new HBox(10);
        hbRegBtn.setAlignment(Pos.BOTTOM_LEFT);
        hbRegBtn.getChildren().add(registerBtn);
        grid.add(hbRegBtn, 0, 4);

        final Text actionTarget = new Text();
        grid.add(actionTarget, 1, 6);

        loginBtn.setOnAction(e -> {
            String username = userTextField.getText();
//            String password = pwBox.getText();

            User user = userManager.login(username);
            if (user != null) {
                actionTarget.setText("Login successful!");
                showGameSelection(primaryStage);
            } else {
                actionTarget.setText("Invalid username or password");
            }
        });

        registerBtn.setOnAction(e -> {
            String username = userTextField.getText();
//            String password = pwBox.getText();

            User user = userManager.registerUser(username);
            if (user != null) {
                actionTarget.setText("Registration successful!");
            } else {
                actionTarget.setText("Username already exists");
            }
        });

        Scene scene = new Scene(grid, 400, 300);
        primaryStage.setScene(scene);
        primaryStage.show();
    }

    private void showGameSelection(Stage primaryStage) {
        GameSelectionScreen selectionScreen = new GameSelectionScreen(userManager);
        selectionScreen.show(primaryStage);
    }
}
