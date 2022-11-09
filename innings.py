from decimal import Decimal, getcontext
import math
getcontext().prec = 1


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
        self.extra_run = 0
        self.current_batting_list = [
            bat_team.players_list_obj[0], bat_team.players_list_obj[1]]
        self.striker = bat_team.players_list_obj[0]
        self.current_bowler = None
        self.current_over_status = []
        self.all_over_status = []

    def show_score_board(self):
        print('\n********************************************************')
        print('\t\tSCORE BOARD')
        print(
            f'* {self.current_batting_list[0].player_name} - {self.current_batting_list[0].run_added} ({self.current_batting_list[0].ball_played})', end='\t')
        print(
            f'{self.current_batting_list[1].player_name} - {self.current_batting_list[1].run_added} ({self.current_batting_list[1].ball_played})')
        print(
            f"{self.batting_team_obj.team_name[:3].upper()}\t{self.total_runs} - {self.total_wickets} \t{self.bowling_team_obj.team_name[:3].upper()} Innings started")
        print(f'Overs: {self.total_overs}.{self.current_ball}')

        if self.current_bowler is not None:
            overs = math.floor(self.current_bowler.ball_bowled/6)
            balls = self.current_bowler.ball_bowled % 6
            # print(overs, balls)
            print(
                f'{self.current_bowler.player_name} - {self.current_bowler.run_conceded}/{self.current_bowler.wicket_taken}\t {overs}.{balls}')

        print('********************************************************\n')

    def set_bowler(self, bowler_obj):
        self.current_bowler = bowler_obj

    def bowl(self, status):
        run = 0
        bat_run = 0
        bowl_run = 0
        ext_run = 0
        is_ball_valid = True
        if status.isnumeric():
            bat_run = bowl_run = run = int(status)

        else:
            if status[0].upper() == 'W' and len(status) == 1:
                pass
            elif status[0].upper() == 'N':
                # if ball is NO Ball
                is_ball_valid = False
                ext_run = bowl_run = run = 1+int(status[1:])
                bat_run = int(status[1:])

            elif status[0].upper() == 'W':
                # if ball is WIDE Ball
                is_ball_valid = False
                ext_run = bowl_run = run = 1+int(status[1:])

            elif status[1:].upper() == 'LB':
                # if ball is Valid and run is leg by
                bat_run = bowl_run = run = int(status[0])

            elif status[1:].upper() == 'B':
                # if ball is Valid and run is BY
                ext_run = run = int(status[0])

        # Score board updating
        self.total_runs += run
        self.current_bowler.run_conceded += bowl_run
        self.striker.run_added += bat_run

        # if ball is No/Wide
        if is_ball_valid:
            self.current_ball += 1
            self.striker.ball_played += 1
            self.current_bowler.ball_bowled += 1

        # for extra run
        self.extra_run = ext_run

        # ball converted to overs and ball
        if self.current_ball == 6:
            self.current_ball = 0
            self.total_overs += 1
