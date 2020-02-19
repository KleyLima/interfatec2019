class Bochas:
    """Classe que carrega os atributos necessários para a abstração do jogo de Bochas"""
    
    def __init__(self, balls, turns):
        """Inicia a classe com seus atributos com valor default"""
        self.max_h = 4000
        self.max_l = 25000
        self.bolim = [0, 0]
        self.n_balls = balls
        self.turns = turns
        self.colors = ["wht", "red"]
        self.wht = []
        self.red = []
        
    def turner(self):
    	for _ in range(self.turn):
    		self.inst_ball()
    	self.calc()
     
    def inst_ball(self):
        """Seta o valor das posições das bolas no jogo, tanto o bolim como a dos jogadores"""
        self.bolim = Bochas.spliter()
        for color in self.colors:
            print(color)
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

    def calc(self):
        setattr(self, "na", 123)
        
if __name__ == '__main__':
    bo = Bochas()
    #bo.inst_ball()
   # print(bo.wht, bo.red)
   bo.calc()
   print(bo.na)
