# Online Game Active players


active_players = {"player1", "player2", "player3"}

# New login
active_players.add("player4")

# Duplicate login ignored automatically
active_players.add("player1")

print(active_players)