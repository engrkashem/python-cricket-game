from player import Player
from team_tournamets import Tournament, Team
# 10 11 9 5 7
cup = Tournament()
# Team Bangladesh Making
bangladesh = Team('Bangladesh')

bd_players_list = ['Tamim Iqbal', 'Liton Das', 'Md Ashraful', 'Mushfiqur Rahim', 'Sakib Al Hasan',
                   'Mohammadullah', 'Akram Khan', 'Mehedi Meraz', 'Mashrafee Mortaza', 'Mustafizur Rahman', 'Taskin Ahmed']
for player_name in bd_players_list:
    player = Player(player_name, bangladesh)

# Team India Making
india = Team('India')

ind_players_list = ['Virat Kohli', 'Sachin Tendulkar', 'Sourab Ganguly', 'MS Dhoni', 'Yuvraj Shings',
                    'Mohammad Yousuf', 'Hardik Pandiya', 'Mohammad Irfan', 'Jaspreet Bumrah', 'Bhuvoneshwar Kumar', 'Anil Kumble']
for player_name in ind_players_list:
    player = Player(player_name, india)


# Team South Africa Making
sa = Team('South Africa')

sa_players_list = ['Hashim Amla', 'F du Plessis', 'AB de Villiers', 'HH Gibbs', 'JH Kallis',
                   'MV Boucher', 'GA Faulkner', 'Keshav Maharaj', 'Imran Tahir', 'Shaun Pollock', 'Dayl Stayn']
for player_name in sa_players_list:
    player = Player(player_name, sa)


# Team South Africa Making
aus = Team('Australia')

aus_players_list = ['AC Gilchrist', 'ML Hayden', 'RT Ponting', 'A Symonds', 'GJ Maxwell',
                    'SPD Smith', 'Steve Waugh', 'SR Watson', 'Shane Warne', 'Glenn McGrath', 'B Lee']
for player_name in aus_players_list:
    player = Player(player_name, aus)
