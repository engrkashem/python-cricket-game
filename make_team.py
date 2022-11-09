from player import Player
from team_tournamets import Tournament, Team

cup = Tournament()
# Team Bangladesh Making
bangladesh = Team('Bangladesh')

bd_players_list = ['Tamim Iqbal', 'Liton Das', 'Sakib Al Hasan', 'Md Ashraful', 'Mushfiqur Rahim',
                   'Mohammadullah', 'Mehedi Meraz', 'Mosaddek Hossain', 'Mashrafee Mortaza', 'Mustafizur Rahman', 'Taskin Ahmed']
for player_name in bd_players_list:
    player = Player(player_name, bangladesh)

# Team India Making
india = Team('India')

ind_players_list = ['Virat Kohli', 'Sachin Tendulkar', 'Sourab Ganguly', 'MS Dhoni', 'Yuvraj Shings',
                    'Mohammad Yousuf', 'Hardik Pandiya', 'Mohammad Irfan', 'Jaspreet Bumrah', 'Bhuvoneshwar Kumar', 'Anil Kumble']
for player_name in ind_players_list:
    player = Player(player_name, india)
