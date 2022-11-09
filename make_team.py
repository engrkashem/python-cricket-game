from player import Player
from team_tournamets import Tournament, Team

cup = Tournament()
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
