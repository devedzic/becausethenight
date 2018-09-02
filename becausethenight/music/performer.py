"""Domain classes and functions related to the concept of performer"""


from becausethenight.util import utility


class Performer:
    """The class related to the concept of performer.
    It is assumed that a performer is sufficiently described by their
    name and whether it is a solo performer or a band."""

    definition = "An artist in the performing arts. In this project, they perform music."

    def __init__(self, name, band=False):
        self.name = name
        self.band = band

    def __str__(self):
        return str(self.name) + ', ' + utility.format_performer_type(self.band)

    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        if (self.name == other.name) and (self.band == other.band):
            return True
        else:
            return False


if __name__ == "__main__":

    from datetime import date

    bruceSpringsteen = Performer('Bruce Springsteen',
                                 band=False)
    print(bruceSpringsteen)                             # test __str__()
    print()

    bruce = Performer('Bruce Springsteen',
                      band=False)
    if bruceSpringsteen == bruce:                       # test __eq__()
        print(True)
    else:
        print(False)
    print()



