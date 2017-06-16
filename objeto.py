from math import tan

class Objeto(object):
    #objeto geometrico do jogo
    def __init__(self,cor, pos, vel, tag):
        self.cor = cor
        self.x = pos[0]
        self.y = pos[1]
        self.vx = vel[0]
        self.vy = vel[1]
        self.tag = tag
        self.id = -1

    def move(self, canvas):
        #muda a posição do bola
        self.x += self.vx
        self.y += self.vy

    def desenhar(self, canvas):
        #desenhar a bola
        #a ser implementada pela calsse filha
        pass
        
