class Tournament:
    all_team = []

    def entry_team(self, team_obj):
        self.all_team.append(team_obj)


class Team(Tournament):
    def __init__(self, name) -> None:
        self.team_name = name
        self.players_list_obj = []
        super().entry_team(self)

    def entry_player(self, player):  # player is a type of player object
        self.players_list_obj.append(player)

    def __repr__(self) -> str:
        return f'From Team.__repr__:- Team name: {self.team_name}.'
