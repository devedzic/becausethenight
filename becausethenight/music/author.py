"""Domain classes and functions related to the concept of author"""


class Author:
    """The class related to the concept of author.
    It is assumed that an author is sufficiently described by his/her
    name, age, birth date, birth place, nationality, and whether he/she is still living or is deceased."""

    definition = "The creator or originator of an artwork."

    def __init__(self, name, age=0, birth_date=None, birth_place='unknown', nationality='unknown', living=True):
        self.name = name
        self.age = age
        self.birth_date = birth_date
        self.birth_place = birth_place
        self.nationality = nationality
        self.living = living

    def __str__(self):
        return (str(self.name) + '\n' +
                '\t' + 'age: ' + str(self.age) +
                '\t' + 'born: ' + str(self.birth_date))

if __name__ == "__main__":

    pass


