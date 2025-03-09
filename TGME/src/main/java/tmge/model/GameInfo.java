package tmge.model;

import javafx.scene.image.Image;

public class GameInfo {
    private String name;
    private String description;
    private Image thumbnail;

    public GameInfo(String name, String description, String thumbnailPath) {
        this.name = name;
        this.description = description;
        this.thumbnail = new Image(thumbnailPath);
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public Image getThumbnail() {
        return thumbnail;
    }
}
