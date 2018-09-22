# from services.club_processor import ClubProcessor
# from services.toernament_processor import TournamentProcessor
#
# # import json
# # from json_tricks import dumps
#
#
# clubProcessor = ClubProcessor()
# tournamentProcessor = TournamentProcessor()
#
# tournaments = tournamentProcessor.get_tournaments(2018, 'pbo')
#
# # Exit when no tournaments were found
# if len(tournaments) <= 0:
#     exit()
#
# # Exit when no clubs were found
# clubs = tournamentProcessor.get_clubs(tournaments[0].tournament_id)
#
# if len(clubs) <= 0:
#     exit()
#
# clubs[25].players = clubProcessor.get_players(tournaments[0], clubs[25].club_id)
#
# # with open('data.json', 'w') as outfile:
# #    json.dump(dumps(clubs, primitives=True), outfile)
from models.player import Player, Gender
from services.player_processor import PlayerProcessor

playerProcessor = PlayerProcessor()
glenn = Player("F5547D29-4A68-4135-8A81-35E381FC4E95", "Glenn, Latomme", Gender.MALE, 50104197)

playerProcessor.get_player_ranking(glenn)
