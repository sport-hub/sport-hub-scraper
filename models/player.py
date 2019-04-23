from enum import Enum

from models.ranking import PlayerRanking


class Player:
        # Initializer / Instance Attributes

                #  player_id = re.search(
                # r'^(.*[\\\/])(.*)(?=\.jpg)',
                # elements[1].a.img.get('src')).group(1)

    def __init__(self,  name, gender, number, ranking=None,player_id=None, ):
        names = name.split(',')
        self.player_id = player_id
        self.gender = gender
        self.lastName = self.remove_leading_spaces(names[1])
        self.firstName = self.remove_leading_spaces(names[0])
        self.number = number
        self.id = ''
        self.ranking = PlayerRanking()
        self.competitions = []

        if ranking:
            self.ranking = ranking

    # Determine the oldest dog
    def get_full_name(self):
        return "{}, {}".format(self.firstName, self.lastName)

    def to_dict(self):
        return {
            'id': self.id,
            'displayName': self.get_full_name().replace(',', ''),
            'gender': self.gender.value,
            'number': self.number,
            'single': self.ranking.single.totalPoints(),
            'double': self.ranking.double.totalPoints(),
            'mix': self.ranking.mix.totalPoints(),
        }

    def remove_leading_spaces(self, name):
        while (name[0] == " "):
            name = name[1:]

        return name

    def add_competition(self, comp_id, player_id):
        self.competitions.append(PlayerCompetition(comp_id, player_id))


class PlayerCompetition:
    def __init__(self, comp_id, player_id):
        self.player_id = player_id
        self.comp_id = comp_id


class Gender(Enum):
    MALE = 0
    FEMALE = 1
