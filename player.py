
class Player:
    def __init__(self, name, team_obj) -> None:
        self.player_name = name
        # batsman info
        self.strike_rate = 0
        self.run_added = 0
        self.ball_played = 0
        self.fours = 0
        self.sixes = 0
        # bowler info
        self.run_conceded = 0
        self.wicket_taken = 0
        self.ball_bowled = 0
        team_obj.entry_player(self)

    def __repr__(self) -> str:
        return f'From Player.__repr__:- Name: {self.player_name}.'
