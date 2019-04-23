class Club:
    def __init__(self, name, number, club_id=None):
        self.name = name
        self.number = number
        self.club_id = club_id
        self.players = []
        self.competitions = []

    def add_competition(self, comp_id, club_id):
        self.competitions.append(ClubCompetition(comp_id, club_id))


class ClubCompetition:
    def __init__(self, comp_id, club_id):
        self.club_id = club_id
        self.comp_id = comp_id
