from random import choice

from pyautogui import sleep
from innings import Innings


class T2Cup:
    all_team = []

    def entry_team(self, team_obj):
        self.all_team.append(team_obj)


class Team(T2Cup):
    def __init__(self, name) -> None:
        self.team_name = name
        self.players_list_obj = []
        super().entry_team(self)

    def entry_player(self, player):  # player is a type of player object
        self.players_list_obj.append(player)

    def __repr__(self) -> str:
        return f'From Team.__repr__:- Team name: {self.team_name}.'


class Player:
    def __init__(self, name, team_obj) -> None:
        self.player_name = name
        self.strike_rate = 0.0
        self.run_added = 0
        self.ball_played = 0
        self.fours = 0
        self.sixes = 0
        self.run_conceded = 0
        self.wicket_taken = 0
        self.ball_bowled = 0
        team_obj.entry_player(self)

    def __repr__(self) -> str:
        return f'From Player.__repr__:- Name: {self.player_name}.'


cup = T2Cup()
bangladesh = Team('Bangladesh')
india = Team('India')
bd_players_list = ['Tamim Iqbal', 'Sakib Al Hasan', 'Mushfiqur Rahim',
                   'Mustafizur Rahman', 'Taskin Ahmed']
for player_name in bd_players_list:
    player = Player(player_name, bangladesh)
# tamim = Player('Tamim Iqbal', bangladesh)
# sakib = Player('Sakib Al Hasan', bangladesh)
kohli = Player('Virat Kohli', india)
rohit = Player('Rohit Sharma', india)
bumra = Player('Jasprit Bumra', india)
# mustafiz = Player('Mustafizur Rahman', bangladesh)

while True:
    print("Select Teams to be played")
    for i, team_obj in enumerate(cup.all_team):
        print(f'{i+1}. {team_obj.team_name}')
    team_one_idx, team_two_idx = map(int, input(
        'Enter options for two teams: ').split(' '))
    team_one_idx -= 1
    team_two_idx -= 1
    team_one_obj = cup.all_team[team_one_idx]
    team_two_obj = cup.all_team[team_two_idx]
    print('Both captains and match officials are heading toward field to TOSS for match')
    sleep(1)
    toss_win = choice([team_one_idx, team_two_idx])
    if toss_win == team_one_idx:
        toss_loose = team_two_idx
    else:
        toss_loose = team_one_idx

    rand = choice(['BAT', 'BOWL'])
    print(
        f'{cup.all_team[toss_win].team_name} won the TOSS and choose to {rand} first')
    if rand == 'BAT':
        # toss winning team opt to bat
        batting_team_obj = cup.all_team[toss_win]
        bowling_team_obj = cup.all_team[toss_loose]
    else:
        # toss winning team opt to bowl
        bowling_team_obj = cup.all_team[toss_win]
        batting_team_obj = cup.all_team[toss_loose]

    first_innings = Innings(team_one_obj, team_two_obj,
                            batting_team_obj, bowling_team_obj)
    first_innings.show_score_board()
    print('Choose Bowler: ')
    for i, player in enumerate(bowling_team_obj.players_list_obj):
        print(f'{i+1}. {player.player_name}')
    bowler_idx = int(input('Select Bowler Serial: '))
    bowler_idx -= 1
    bowler_obj = bowling_team_obj.players_list_obj[bowler_idx]
    first_innings.set_bowler(bowler_obj)

    first_innings.show_score_board()

    break
