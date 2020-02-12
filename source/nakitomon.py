# -*- coding: utf-8 -*-

class Nakitomon:

    @classmethod
    def __init__(cls, strg=0, atk=0, shl=0, agi=0):
        cls.strg = strg
        cls.atk = atk
        cls.shl = shl
        cls.agi = agi

class Game:

    @classmethod
    def __init__(cls):
        cls.cards = []
        cls.scr_dan = 0
        cls.scr_silv = 0
        cls.draw = 0
        cls.stats = ["strg", "atk", "shl", "agi"]

    @classmethod
    def add_card(cls, new: Nakitomon):
        cls.cards.append(new)

    @classmethod
    def all_in(cls, cards_dan, cards_silv):
        for dan, silv in zip(cards_dan, cards_silv):
           cls.one_one(dan, silv) 

    @classmethod
    def one_one(cls, dan, silv):
        for stat in cls.stats:
            if getattr(dan, stat) > getattr(silv, stat):
                cls.scr_dan += 1
                return
            elif getattr(silv, stat) > getattr(dan, stat):
                cls.scr_silv += 1
                return
        cls.draw += 1

    @classmethod
    def show_res(cls):
        print("danette venceu:", cls.scr_dan)
        print("silvio venceu:", cls.scr_silv)
        print("empates:", cls.draw)



            
if __name__ == '__main__':
    print("Ok")
