# -*- coding: utf-8 -*-


class Megabobagem:

    def __init__(self, txt):
        self.txt = txt
        for x in range(65, 91):
            setattr(self, "{}".format(chr(x)), 0)

    def counter(self):
        for x in range(65, 91):
            occur = self.txt.count("{}".format(chr(x)))
            if occur:
                setattr(self, "{}".format(chr(x)), occur)

    def check_anagram(self) -> bool:
        self.counter()
        count_imp = 0
        for x in range(65, 91):
            if getattr(self, "{}".format(chr(x))) & 1:
                count_imp += 1
        if count_imp > 1:
            print("FALSO")
        else:
            print("VERDADEIRO")


if __name__ == '__main__':
    Megabobagem(input()).check_anagram()
