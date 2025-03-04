from src.enums.user_enums import Statuses
from src.generators.player_localize import PlayesrLocalize

class Player:
    def __init__(self):
        self.result = {}
        self.reset()

    def set_status(self, status=Statuses.active.value):
        self.result['account_status'] = status
        return self

    def set_balance(self, balance=0):
        self.result['balance'] = balance
        return self

    def set_avatar(self, avatar='https://www.google.com/'):
        self.result['avatar'] = avatar
        return self

    def reset(self):
        self.set_status()
        self.set_avatar()
        self.set_balance()
        self.result["localize"] = {
            "en": PlayesrLocalize('en_US').build(),
            "ru": PlayesrLocalize('ru_RU').build()
            }
        return self

    def update_inner_value(self, keys, value):
        self.result[keys] = value
        return self

    def build(self):
        return self.result