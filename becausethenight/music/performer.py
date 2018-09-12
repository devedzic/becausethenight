"""Domain classes and functions related to the concept of performer"""


from becausethenight.util import utility

import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band."""

    definition = "An artist in the performing arts. In this project, they perform music."

    def __init__(self, name, is_band=False):
        self.name = name
        self.is_band = is_band

    def __str__(self):
        # return self.name + ', ' + utility.format_performer_type(self.is_band)
        return utility.format_performer_type(self)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.name == other.name) and (self.is_band == other.is_band):
            return True
        else:
            return False

    def py_to_json(self):
        # return self.__dict__
        return json.dumps(self.__dict__)

    @staticmethod
    def json_to_py(json_performer):
        return json.loads(json_performer)


if __name__ == "__main__":

    bruceSpringsteen = Performer('Bruce Springsteen',
                                 is_band=False)
    print(bruceSpringsteen)                                 # test __str__()
    print()

    bruce = Performer('Bruce Springsteen',
                      is_band=False)
    if bruceSpringsteen == bruce:                           # test __eq__()
        print(True)
    else:
        print(False)
    print()

    bruceSpringsteen_json = bruceSpringsteen.py_to_json()   # test JSON serialization/deserialization
    print('bruceSpringsteen.py_to_json():',
          bruceSpringsteen_json)
    bruceSpringsteen_py = \
        Performer.json_to_py(bruceSpringsteen_json)
    print(bruceSpringsteen_py)
    print()



