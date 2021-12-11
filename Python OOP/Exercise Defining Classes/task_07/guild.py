# from task_07.player import Player


class Guild:
    def __init__(self, name):
        self.name = name
        self.players_data = []

    def assign_player(self, player):
        if not player.guild == self.name and not player.guild == "Unaffiliated":
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."

        self.players_data.append(player)
        player.guild = self.name
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        filtered_players = [p for p in self.players_data if p.name == player_name]
        if not filtered_players:
            return f"Player {player_name} is not in the guild."

        player = filtered_players[0]
        self.players_data.remove(player)
        player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players_data:
            result += p.player_info()
        return result



# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())
