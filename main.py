from random import choice
from pyautogui import sleep
from innings import Innings
from make_team import cup


while True:
    match_overs = 2
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

    # start first innings
    first_innings = Innings(team_one_obj, team_two_obj,
                            batting_team_obj, bowling_team_obj, match_overs*6)
    # score board shown default
    first_innings.show_score_board()

    # First innings started
    while first_innings.total_overs*6 + first_innings.current_ball < match_overs*6:
        if first_innings.current_ball == 0:
            # selecting bowler by captain/user
            print('Choose Bowler: ')
            for i, player in enumerate(bowling_team_obj.players_list_obj):
                print(f'{i+1}. {player.player_name}')
            bowler_idx = int(input('Select Bowler Serial: '))
            bowler_idx -= 1
            bowler_obj = bowling_team_obj.players_list_obj[bowler_idx]
            first_innings.set_bowler(bowler_obj)

        # no-ball: N4, wide: W2, wicket: W
        status = input('Enter after ball status: ')

        # first_innings update score board
        response = first_innings.bowl(status)

        # handle all-out
        if response == 'end':
            break

        # show updated score board
        first_innings.show_score_board()

    # start Second innings
    batting_team_obj, bowling_team_obj = bowling_team_obj, batting_team_obj
    second_innings = Innings(team_one_obj, team_two_obj,
                             batting_team_obj, bowling_team_obj, match_overs*6)

    second_innings.target = first_innings.total_runs+1

    print(f'\n{batting_team_obj.team_name} Target: {second_innings.target}\n')

    # score board shown default
    second_innings.show_score_board()

    # Second innings started
    while second_innings.total_overs*6 + second_innings.current_ball < 12:
        if second_innings.current_ball == 0:
            # selecting bowler by captain/user
            print('Choose Bowler: ')
            for i, player in enumerate(bowling_team_obj.players_list_obj):
                print(f'{i+1}. {player.player_name}')
            bowler_idx = int(input('Select Bowler Serial: '))
            bowler_idx -= 1
            bowler_obj = bowling_team_obj.players_list_obj[bowler_idx]
            second_innings.set_bowler(bowler_obj)

        # no-ball: N4, wide: W2, wicket: W
        status = input('Enter after ball status: ')

        # second_innings update score board
        response = second_innings.bowl(status)

        # show updated score board
        second_innings.show_score_board()

        # handle win/lose
        if response == 'end':
            print(
                f'\n{bowling_team_obj.team_name} has Won By {second_innings.target-second_innings.total_runs} Runs\n')
            break
        elif response == 'win':
            print(
                f'\n{batting_team_obj.team_name} has Won By {10-second_innings.total_wickets} Wickets\n')
            break

    if second_innings.target > second_innings.total_runs:
        print(f'\n{bowling_team_obj.team_name} has Won By {second_innings.target-second_innings.total_runs} Runs\n')

    break
