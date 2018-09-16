"""Domain classes and functions related to the concept of performer"""


# from becausethenight.util import utility

import json


class Performer:
    """The class describing the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band."""

    definition = "An artist in performing arts. In this project, they perform music."

    def __init__(self, name, is_band=False):
        self.name = name
        self.is_band = is_band

    def __str__(self):
        # return self.name + ', ' + utility.format_performer_type(self.is_band)
        # return utility.format_performer_type(self)
        return format_performer_type(self)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.name == other.name) and (self.is_band == other.is_band):
            return True
        else:
            return False

    # def py_to_json(self):                                                   # developed just for initial testing
    #     # return self.__dict__
    #     return json.dumps(self.__dict__, indent=4)

    # @staticmethod
    # def json_to_py_dict(json_performer):                                    # developed just for initial testing
    #     return json.loads(json_performer)

    # @staticmethod
    # def json_to_py(json_performer):                                         # developed just for initial testing
    #     if '__Performer__' in json_performer:
    #         # d = Performer.json_to_py_dict(json_performer['__Performer__'])
    #         performer = Performer('')
    #         performer.__dict__.update(json_performer['__Performer__'])
    #         return performer
    #     return json_performer
    #     # elif isinstance(json_performer, dict):
    #     #     d = json_performer
    #     # else:
    #         # d = Performer.json_to_py_dict(json_performer)
    #     # return Performer(d['name'], d['is_band'])


def format_performer(performer):
    """Converts performer object to its name field, for printing purposes."""

    return performer.name if isinstance(performer, Performer) else 'unknown'

    # Alternatively:
    # if isinstance(performer, Performer):
    #     return performer.name
    # else:
    #     return 'unknown'


def format_performer_type(performer):
    """Converts the flag of performer type from boolean to string, if needed."""

    if isinstance(performer, Performer):
        return performer.name + ' (band)' if performer.is_band else performer.name + ' (musician)'
    else:
        return 'unknown if band or musician'

    # Alternatively:
    # if isinstance(performer, Performer):
    #     if performer.is_band:
    #         return performer.name + ' (band)'
    #     else:
    #         return performer.name + ' (musician)'
    # else:
    #     return 'unknown if band or musician'


class PerformerEncoder(json.JSONEncoder):
    """JSON encoder for Performer objects."""

    def default(self, o):
        if isinstance(o, Performer):
            # return {'__Performer__': o.py_to_json()}
            return {'__Performer__': o.__dict__}
        return {'__{}__'.format(o.__class__.__name__): o.__dict__}


def json_to_py(performer_json):
    """JSON decoder for Performer objects (object_hook parameter in json.loads())."""

    if '__Performer__' in performer_json:
        performer = Performer('')
        performer.__dict__.update(performer_json['__Performer__'])
        return performer
    return performer_json


if __name__ == "__main__":

    # bruceSpringsteen = Performer('Bruce Springsteen',
    #                              is_band=False)
    # print(bruceSpringsteen)                                 # test __str__()
    # print()
    #
    # bruce = Performer('Bruce Springsteen',
    #                   is_band=False)
    # if bruceSpringsteen == bruce:                           # test __eq__()
    #     print(True)
    # else:
    #     print(False)
    # print()

    bruceSpringsteen = Performer('Bruce Springsteen',
                                 is_band=False)
    bruceSpringsteen_json = json.dumps(bruceSpringsteen,    # test JSON serialization/deserialization - single object
                                       indent=4,
                                       cls=PerformerEncoder)
    # pe = PerformerEncoder()
    # print(pe.default(bruceSpringsteen))
    # json.dumps(pe.default(bruceSpringsteen), indent=4)
    print(type(bruceSpringsteen_json))
    print(bruceSpringsteen_json)
    print()

    bruce = json.loads(bruceSpringsteen_json,
                       object_hook=json_to_py)
    # bruce = json.loads(bruceSpringsteen_json)
    print(type(bruce))
    print(bruce)
    print()

    list_of_performers_json = \
        json.dumps([bruceSpringsteen,
                   Performer('Patti Smith')],               # test JSON serialization/deserialization - list of objects
                   indent=4,
                   cls=PerformerEncoder)
    performers = json.loads(list_of_performers_json,
                            object_hook=json_to_py)
    print(type(performers))
    print(performers)
    for performer in performers:
        print(performer)
    print()


    # bruceSpringsteen_json = bruceSpringsteen.py_to_json()   # test JSON serialization/deserialization (init. ver.)
    # print('bruceSpringsteen.py_to_json():')
    # print(bruceSpringsteen_json)
    # print()
    # print('bruceSpringsteen.json_to_py_dict():')
    # bruceSpringsteen_py_dict = \
    #     Performer.json_to_py_dict(bruceSpringsteen_json)
    # print(bruceSpringsteen_py_dict)
    # print()
    # print('bruceSpringsteen.json_to_py:')
    # bruceSpringsteen_py = Performer.json_to_py(bruceSpringsteen_json)
    # print(bruceSpringsteen_py)
    # print()


