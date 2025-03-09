module tgme {
    requires javafx.controls;
    requires javafx.fxml;


    opens tgme to javafx.fxml;
    exports tgme;
}