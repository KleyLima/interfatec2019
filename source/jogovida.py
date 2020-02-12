# -*- coding: utf-8 -*-

class JogoVida:

    def __init__(self, lin, col):
        self.lin = lin
        self.col = col
        self.mat = [[0] * col for x in range(lin)]
        self.new_mat = [[0] * col for x in range(lin)]

    def fill_mat(self):
        for x in range(self.lin):
            linha = input()
            for y in range(self.col):
                self.mat[x][y] = int(linha[y])
        print(self.mat)

    def stage(self):
        for x in range(self.lin):
            for y in range(self.col):
                self.check_neigh(x, y)


    def check_neigh(self, x,y):
    # TODO: Cuidar do new_mat zerando a cada iteração, apenas integrar ele no fim do fluxo, ou printar ele como resposta
        if self.mat[x][y] == 0:
            if self.check_alive(x, y) == 3:
                self.new_mat[x][y] = 1
        else:
            if self.check_alive(x, y) < 2 or self.check_alive(x, y) > 3:
                self.new_mat[x][y] = 0
            elif self.check_alive(x, y) in [2,3]:
                self.new_mat[x][y] = 0


    def check_alive(self, x, y):
        count_alive = 0
        coord = (x, y)
        poss = [(1, 1), (1, 0), (1, -1), (0, -1), (0, 1), (-1, -1), (-1, 0), (-1, 1)]
        for tup in poss:
            new_coord = tuple(map(sum, zip(coord, tup)))
            try:
                if self.mat[new_coord[0]][new_coord[1]]:
                    count_alive += 1
            except:
                pass
        return count_alive

    def cycle(self, reps):
        for x in range(reps):
            self.stage()
        print(self.mat)


if __name__ == '__main__':
    jogo = JogoVida(*[int(x) for x in input().split()])
    jogo.fill_mat()
    jogo.cycle(int(input()))
