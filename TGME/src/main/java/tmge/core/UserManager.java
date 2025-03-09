package tmge.core;

import tmge.model.User;

import java.util.HashMap;
import java.util.Map;

// MAY NOT NEED TO ASK FOR PASSWORD SINCE LOGIN JUST NEEDS TO BE SIMPLE
// HAVING PASSWORD WILL JUST ADD MORE UNNECESSARY COMPLEXITIES AND CLUTTER

public class UserManager {
    private Map<String, User> users;
    private User currentUser;

    public UserManager() {
        users = new HashMap<>();
        // Add some demo users for testing
        users.put("player1", new User("player1", "password123"));
        users.put("player2", new User("player2", "password123"));
    }

    public User login(String username, String password) {
        User user = users.get(username);
        if (user != null && user.validatePassword(password)) {
            currentUser = user;
            return user;
        }
        return null;
    }

    public User registerUser(String username, String password) {
        if (users.containsKey(username)) {
            return null; // User already exists
        }

        User newUser = new User(username, password);
        users.put(username, newUser);
        return newUser;
    }

    public User getCurrentUser() {
        return currentUser;
    }

    public User getUser(String username) {
        return users.get(username);
    }

    public void logout() {
        currentUser = null;
    }

    public void loadUserData() {
        // TODO: Load user data from file/database
    }

    public void saveUserData() {
        // TODO: Save user data to file/database
    }
}
