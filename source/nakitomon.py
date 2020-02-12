# -*- coding: utf-8 -*-


class Nakitomon:

    @classmethod
    def __init__(cls, strg=0, atk=0, shl=0, agi=0):
        cls.strg = strg
        cls.atk = atk
        cls.shl = shl
        cls.agi = agi

    @classmethod
    def __repr__(cls):
        return "strg: {}, atk: {}, shl: {}, agi: {}".format(cls.strg, cls.atk, cls.shl, cls.agi)


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
        """Adiciona uma nova carta ao baralho"""
        print(cls.cards)
        cls.cards.append(new)

    @classmethod
    def all_in(cls, cards_dan, cards_silv):
        """Itera sobre as cartas dos dois jogadores para comparar os atributos e exibe o resultado no fim"""
        print(cards_dan)
        print(cards_silv)
        for dan, silv in zip(cards_dan, cards_silv):
           cls.one_one(dan, silv)
        cls.show_res()

    @classmethod
    def one_one(cls, dan, silv):
        """Compara os atributos pela ordem prioritária para saber quem venceu"""
        for stat in cls.stats:
            print(stat)

            print(getattr(dan, stat)); print(getattr(silv, stat))
            if getattr(dan, stat) > getattr(silv, stat):
                cls.scr_dan += 1
                return
            elif getattr(silv, stat) > getattr(dan, stat):
                cls.scr_silv += 1
                return
        cls.draw += 1

    @classmethod
    def show_res(cls):
        """Exibe os resultados do fim da partida"""
        print("danette venceu:", cls.scr_dan)
        print("silvio venceu:", cls.scr_silv)
        print("empates:", cls.draw)

    @classmethod
    def inst_card(cls):
        strg, atk, shl, agi = [int(x) for x in input().split()]
        cls.add_card(Nakitomon(strg, atk, shl, agi))

            
if __name__ == '__main__':
    dan = Game()
    silv = Game()
    judge = Game()
    num = int(input())
    for x in range(num):
        dan.inst_card()
    for x in range(num):
        silv.inst_card()
    judge.all_in(dan.cards, silv.cards)

