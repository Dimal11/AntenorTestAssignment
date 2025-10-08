from mimesis import Person
from mimesis.locales import Locale

class RandomUser:
    person = Person(Locale.RU)
    def __init__(self):
        self.username = RandomUser.person.name()
        self.password = RandomUser.person.password(length=8)