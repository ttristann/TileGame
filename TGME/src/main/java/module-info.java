module tmge {
    requires javafx.controls;
    requires javafx.fxml;


    opens tmge to javafx.fxml;
    exports tmge;
}