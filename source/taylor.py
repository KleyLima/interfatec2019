# -*- coding: utf-8 -*-

class Taylor:

    @classmethod
    def __init__(cls, x):
        cls.x = x

    @classmethod
    def radiano(cls):
        cls.rad = (cls.x * 3.1415) / 180
        return cls.rad

    @classmethod
    def formula_inner(cls, num):
        return (-1)**num * ((cls.r)**2*num)/ # TODO: Implementar fatorial da parte de baixo da função.


if __name__ == '__main__':
    print(Taylor(12).radiano())
