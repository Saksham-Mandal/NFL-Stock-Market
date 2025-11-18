package backend;

public class Player {
    private String name;
    private String team;
    private String pos;

    public String getPlayerName(Player player) {
        return player.name;
    }

    public String getPlayerTeam(Player player) {
        return player.team;
    }

    public String getPlayerPos(Player player) {
        return player.pos;
    }
}