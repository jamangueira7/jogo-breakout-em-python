from objeto import Objeto

class Retangulo(Objeto):
    def __init__(self, largura, altura, cor, pos, vel, tag):
        self.b = largura
        self.h = altura
        super().__init__(cor,pos,vel,tag)

    def desenhar(self, canvas):
        #desenhar a bola
        self.id = canvas.create_rectangle(self.x, self.y, self.x + self.b, self.y + self.h, fill=self.cor)
 
