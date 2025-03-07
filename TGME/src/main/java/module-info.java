module org.example.tilegame {
    requires javafx.controls;
    requires javafx.fxml;


    opens org.example.tilegame to javafx.fxml;
    exports org.example.tilegame;
}