
class Innings:
    def __init__(self, team1, team2, bat_team, bowl_team) -> None:
        self.team1_obj = team1
        self.team2_obj = team2
        self.batting_team_obj = bat_team
        self.bowling_team_obj = bowl_team
        self.total_runs = 0
        self.total_wickets = 0
        self.total_overs = 0
        self.current_ball = 0
        self.current_batting_list = [
            bat_team.players_list_obj[0], bat_team.players_list_obj[1]]
        self.striker = bat_team.players_list_obj[0]
        self.current_bowler = None
        self.current_over_status = []
        self.all_over_status = []

    def show_score_board(self):
        print(
            f"{self.batting_team_obj.team_name[:3].upper()}\t{self.total_runs} - {self.total_wickets} \t{self.bowling_team_obj.team_name[:3].upper()} Innings started")
