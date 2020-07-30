class Card:
    def __init__(self, suit,value):
        self.suit=suit
        self.value=value


    def __repr__(self):
        if self.value==11:
            self.value='J'
        if self.value==12:
            self.value='Q'
        if self.value==13:
            self.value='K'
        if self.value==14:
            self.value='ACE'

        return f'{self.suit} {self.value}'

