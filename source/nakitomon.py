# -*- coding: utf-8 -*-


class Nakitomon:

    def __init__(self, strg=0, atk=0, shl=0, agi=0):
        self.strg = strg
        self.atk = atk
        self.shl = shl
        self.agi = agi

    def __repr__(self):
        return "strg: {}, atk: {}, shl: {}, agi: {}".format(self.strg, self.atk, self.shl, self.agi)


class Game:

    def __init__(self):
        self.cards = []
        self.scr_dan = 0
        self.scr_silv = 0
        self.draw = 0
        self.stats = ["strg", "atk", "shl", "agi"]


    def add_card(self, new: Nakitomon):
        """Adiciona uma nova carta ao baralho"""
        print(self.cards)
        self.cards.append(new)

    def all_in(self, cards_dan, cards_silv):
        """Itera sobre as cartas dos dois jogadores para comparar os atributos e exibe o resultado no fim"""
        print(cards_dan)
        print(cards_silv)
        for dan, silv in zip(cards_dan, cards_silv):
           self.one_one(dan, silv)
        self.show_res()

    def one_one(self, dan, silv):
        """Compara os atributos pela ordem prioritária para saber quem venceu"""
        for stat in self.stats:
            print(stat)

            print(getattr(dan, stat)); print(getattr(silv, stat))
            if getattr(dan, stat) > getattr(silv, stat):
                self.scr_dan += 1
                return
            elif getattr(silv, stat) > getattr(dan, stat):
                self.scr_silv += 1
                return
        self.draw += 1

    def show_res(self):
        """Exibe os resultados do fim da partida"""
        print("danette venceu:", self.scr_dan)
        print("silvio venceu:", self.scr_silv)
        print("empates:", self.draw)

    def inst_card(self):
        strg, atk, shl, agi = [int(x) for x in input().split()]
        self.add_card(Nakitomon(strg, atk, shl, agi))

            
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

