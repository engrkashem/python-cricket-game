from random import choice
from pyautogui import sleep
from innings import Innings
from make_team import cup


while True:
    match_overs = int(input('Enter Total Overs of an Innings: '))
    print("Select Teams to be played (eg. 1 2)")
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
    sleep(2)
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

            # bowler_idx = int(input('Select Bowler Serial: '))
            bowler_idx = choice([10, 11, 9, 5, 8, 7])  # bowlers index
            bowler_idx -= 1
            bowler_obj = bowling_team_obj.players_list_obj[bowler_idx]
            first_innings.set_bowler(bowler_obj)
            print(f'\n New Bowler: {bowler_obj.player_name}\n')
            sleep(1)

        # action after a ball is bowled:  no-ball- N4, wide- W2, wicket- W etc.
        # status = input('Enter after ball status: ')
        status = choice(['6', '4', '3', '2', '1', 'W', 'W1', 'W4', '6', '4', '3', '2', '1', 'N0', 'N1', 'N4',
                        'N6', '6', '4', '3', '2', '1', '1lb', '4lb', '1b', '6', '4', '3', '2', '1'])  # Possible actions

        # first_innings update score board
        response = first_innings.bowl(status)

        # handle all-out
        if response == 'end':
            break

        # show updated score board after every overs
        if (first_innings.total_overs*6 + first_innings.current_ball) % 6 == 0:
            first_innings.show_score_board()

    # start Second innings
    batting_team_obj, bowling_team_obj = bowling_team_obj, batting_team_obj
    second_innings = Innings(team_one_obj, team_two_obj,
                             batting_team_obj, bowling_team_obj, match_overs*6)

    # Set target for second innings
    second_innings.target = first_innings.total_runs+1

    print(f'\n{batting_team_obj.team_name} Match started and Target: {second_innings.target}\n')
    sleep(2)

    # score board shown default
    second_innings.show_score_board()

    # Second innings started
    while second_innings.total_overs*6 + second_innings.current_ball < match_overs*6:
        if second_innings.current_ball == 0:
            # selecting bowler by captain/user
            print('Choose Bowler: ')
            for i, player in enumerate(bowling_team_obj.players_list_obj):
                print(f'{i+1}. {player.player_name}')

            # bowler_idx = int(input('Select Bowler Serial: '))
            bowler_idx = choice([10, 11, 9, 5, 8, 7])  # bowlers index
            bowler_idx -= 1
            bowler_obj = bowling_team_obj.players_list_obj[bowler_idx]
            second_innings.set_bowler(bowler_obj)
            print(f'\n New Bowler: {bowler_obj.player_name}\n')
            sleep(1)

        # action after a ball is bowled:  no-ball- N4, wide- W2, wicket- W etc.
        # status = input('Enter after ball status: ')
        status = choice(['6', '4', '3', '2', '1', 'W', 'W1', 'W4', '6', '4', '3', '2', '1', 'N0', 'N1', 'N4',
                        'N6', '6', '4', '3', '2', '1', '1lb', '4lb', '1b', '6', '4', '3', '2', '1'])  # Possible actions

        # second_innings update score board
        response = second_innings.bowl(status)

        # show updated score board
        if (second_innings.total_overs*6 + second_innings.current_ball) % 6 == 0:
            second_innings.show_score_board()

        # handle win/lose
        if response == 'end':
            second_innings.show_score_board()
            print(
                f'\n{bowling_team_obj.team_name} has Won By {second_innings.target-second_innings.total_runs} Runs\n')
            break
        elif response == 'win':
            second_innings.show_score_board()
            print(
                f'\n{batting_team_obj.team_name} has Won By {10-second_innings.total_wickets} Wickets\n')
            break

    if second_innings.target > second_innings.total_runs:
        second_innings.show_score_board()
        print(f'\n{bowling_team_obj.team_name} has Won By {second_innings.target-second_innings.total_runs} Runs\n')

    break
