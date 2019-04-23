from services.club_processor import ClubProcessor
from services.toernament_processor import TournamentProcessor
from models.player import Player, Gender
from services.player_processor import PlayerProcessor
from services.firestore import FirestoreService

# import json
# from json_tricks import dumps


clubProcessor = ClubProcessor()
tournamentProcessor = TournamentProcessor()
playerProcessor = PlayerProcessor()
firestoreService = FirestoreService()

tournaments = tournamentProcessor.get_tournaments(2019, 'pbo')

# Exit when no tournaments were found
if len(tournaments) <= 0:
    exit()

# Exit when no clubs were found
clubs = tournamentProcessor.get_clubs(tournaments[0])

if len(clubs) <= 0:
    exit()

clubs[25].players = clubProcessor.get_players(tournaments[0], clubs[25])

# with open('data.json', 'w') as outfile:
#    json.dump(dumps(clubs, primitives=True), outfile)
clubs[25].players[0].player_id = tournamentProcessor.get_user_id(
    clubs[25].players[0])

print(clubs[25].players[0].player_id)

# Process user


# glenn = Player("F5547D29-4A68-4135-8A81-35E381FC4E95",
#                "Glenn, Latomme", Gender.MALE, 50104197)

# playerProcessor.initialize_player_ranking(glenn)
# firestoreService.initialize_info_from_store(glenn)
# firestoreService.update_info_to_store(glenn)
