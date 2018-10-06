from enum import Enum

from models.ranking import PlayerRanking


class Player:
        # Initializer / Instance Attributes

    def __init__(self, player_id, name, gender, number):
        names = name.split(',')
        self.player_id = player_id
        self.gender = gender
        self.lastName = names[1]
        self.firstName = names[0]
        self.number = number
        self.ranking = PlayerRanking()

    # Determine the oldest dog
    def get_full_name(self):
        return "{}, {}".format(self.firstName, self.lastName)

    def to_dict(self):
        return {
            'name': self.get_full_name(),
            'gender': self.gender,
            'number': self.number,
            'single': self.ranking.single,
            'double': self.ranking.double,
            'mix': self.ranking.mix,
        }


class Gender(Enum):
    MALE = 0
    FEMALE = 1
