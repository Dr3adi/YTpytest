from faker import Faker


class PlayesrLocalize:
    def __init__(self, lang):
        self.fake = Faker(lang)
        self.result = {
            'nickname': self.fake.first_name(),
        }

    def build(self):
        return self.result