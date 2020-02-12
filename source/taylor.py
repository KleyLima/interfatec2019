# -*- coding: utf-8 -*-

class Taylor:

    @classmethod
    def __init__(cls, x=0):
        cls.x = x
        cls.rad = (cls.x * 3.1415) / 180

    @classmethod
    def formula_inner(cls, num):
        print("num=", num)
        mid = ((-1)**num) * ((cls.rad**(2*num))/Taylor().fatorial(num=2*num))
        print(mid)
        return mid

    @classmethod
    def fatorial(cls, num, acc=1):
        if num > 1:
            return  Taylor().fatorial(num=num-1, acc=acc*num)
        else:
            print("acc=", acc)
            return acc

    @classmethod
    def formula_apply(cls):
        return sum([Taylor(x=cls.x).formula_inner(num=x) for x in range(0, 6)])


if __name__ == '__main__':
    print(Taylor(int(input())).formula_apply())
