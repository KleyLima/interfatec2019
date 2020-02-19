# -*- coding: utf-8 -*-


from math import sqrt


class Bochas:
    """Classe que carrega os atributos necessários para a abstração do jogo de Bochas"""

    def __init__(self, balls, turns):
        """Inicia a classe com seus atributos com valor default"""
        self.max_h = 4000
        self.max_l = 25000
        self.bolim = [0, 0]
        self.n_balls = balls
        self.turns = turns
        self.colors = ["wth", "red"]
        self.wth = []
        self.red = []
        self.wth_points = 0
        self.red_points = 0
        self.dist_wth = []
        self.dist_red = []
        self.draw = False

    def turner(self):
        for _ in range(self.turns):
            self.inst_ball()
            self.calc_dist()

        while self.wth_points == self.red_points:
            self.inst_ball()
            self.calc_dist()
        
        self.printer()

    def inst_ball(self):
        """Seta o valor das posições das bolas no jogo, tanto o bolim como a dos jogadores"""
        self.bolim = Bochas.spliter()
        for color in self.colors:
            self.coord_balls(color=color)

    def coord_balls(self, color):
        """
        Método auxiliar que de fato modifica o valor das posições das bolas no jogo
        param color: Cor da bolinha que esta sendo posicionada, acessando o atributo pertinente
        return: None
        """
        setattr(self, color, [self.spliter() for _ in range(self.n_balls)])

    @staticmethod
    def spliter():
        """Função auxiliar para leitura das entradas, diminuindo repetição de código"""
        return [int(x) for x in input().split()]

    def calc_dist(self):
        for color in self.colors:
            setattr(self, "dist_" + color, [self.pitag(ball) for ball in getattr(self, color)])
            getattr(self, "dist_" + color).sort()
        self.first_closer()

    def pitag(self, coord_ball):
        return int(sqrt((abs(self.bolim[0] - coord_ball[0]) ** 2) + (abs(self.bolim[1] - coord_ball[1]) ** 2)))

    def first_closer(self):  # TODO: Reescrever esse método mais Pythonico
        for ind in range(self.n_balls):
            if self.dist_wth[ind] < self.dist_red[ind]:  # Branco mais perto
                self.calc_points(closer="wth", dist=self.dist_wth[ind])
                break
            elif self.dist_red[ind] < self.dist_wth[ind]:  # Vermelho mais perto
                self.calc_points(closer="red", dist=self.dist_red[ind])
                break
            else:
                self.draw = True

    def calc_points(self, closer, dist):
        if closer == 'wth':
            for dist_ball in self.dist_wth:
                if self.dist_red[0] > dist_ball:
                    self.wth_points += 1

        elif closer == 'red':
            for dist_ball in self.dist_red:
                if self.dist_wth[0] > dist_ball:
                    self.red_points += 1

        self.draw = False

    def printer(self):
        print("PONTOS DAS BOCHAS BRANCAS =", self.wth_points)
        print("PONTOS DAS BOCHAS VERMELHAS =", self.red_points)
        print("VENCEDOR: BOCHAS {}".format("VERMELHAS" if self.red_points > self.wth_points else "BRANCAS"))

if __name__ == '__main__':
    balls, turns = [int(x) for x in input().split()]
    bo = Bochas(balls=balls, turns=turns)
    bo.turner()

