from tkinter import *
from constantes import *
import random

from retangulo import Retangulo
from bola import Bola

class Jogo(object):

    def __init__(self):
        #criar area principal do jogo
        self.root = Tk()
        self.root.geometry('%ix%i' %(LARGURA, ALTURA))
        self.root.resizable(False, False)
        self.root.title('Primeiro Jogo')

        #frame para conter o canvas
        self.frame = Frame(bg="blue")
        self.frame.pack()

        #codigo de craição do canvas
        self.canvas = Canvas(self.frame, bg="black", width=CANVAS_L, height=CANVAS_A, cursor = 'target')
        foto = PhotoImage(file = "fundo/fundo.gif")
        self.canvas.create_image(CANVAS_L/2, CANVAS_A/2, image=foto)
        self.canvas.pack()

        #criando objetos dentro do canvas
        self.comecar = Button(self.root, text='INICIAR', command=self.comeca)
        self.comecar.focus_force()
        self.comecar.pack()

        #iniciar jogo com enter
        self.comecar.bind('<Return>',self.comeca)
        self.carregaImagens()
        self.novoJogo()
        
        self.root.mainloop()

    def carregaImagens(self):
        
        self.spritesheet = []
        for i in range(1,9):            
            self.spritesheet.append(PhotoImage(file = "fundo/%.2i.gif"%i))
 
        self.number_of_sprite = 0
        self.limite = len(self.spritesheet) - 1
        
    def novoJogo(self):
        #criação dos elementos do jogo
        self.player = Retangulo(largura = 100, altura = 20, cor = 'white', pos =(LARGURA//2 + 360,380), vel = (15,15), tag='player')
        self.player.desenhar(self.canvas)
        #movendo o player com o mouse
        self.canvas.bind('<Motion>', self.move_player)
        
        #criar a bolinha do jogo        
        self.bola = Bola(raio = 30, cor='red', pos = (100, 200), vel=(3,3))
      

        #lista dos retangulos
        self.r = []
        l, c, e = 5, 8, 2 #linhas, colunas e espaçacamentos
        b, h, y0 = 48, 20, 50 #base, altura e posição inicial
        for i in range(l):
            cor = random.choice(['black','orange','white','lightgray','yellow','green','purple'])
            for j in range(c):
                r = Retangulo(b, h, cor, (b*j+(j+1)*e, i*h+(i+1)*e + y0), (0,0), 'rect')
                self.r.append(r)
        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text='Bem Vindos!', fill='white', font='Verdana, 12')

        #mudar o estado para jogando
        self.jogando = True
        
    def comeca(self):
        #iniciar o jogo
        self.jogar()
        
    def jogar(self):
        #vai ser executado enquanto o jogador estiver jogando
        if self.jogando:
            self.update()
            self.desenhar()
            
            if len(self.r) == 0:
                self.jogando = False
                self.msg = "VOCÊ GANHOU!!"
            if self.bola.y > CANVAS_A:
                self.jogando = False
                self.msg = "VOCÊ PERDEU!!"
                
            self.root.after(10, self.jogar)
        else:
            self.acabou(self.msg)
            
    def update(self):
        #movimento da bola
        self.bola.update(self)
        
        self.number_of_sprite += 1
        if self.number_of_sprite > self.limite:
            self.number_of_sprite = 0       
        
    def recomeça(self):
        self.novoJogo()
        self.comecar['text'] = 'INICIAR'
        self.jogar()


    def acabou(self, msg):
        self.canvas.delete(ALL)
        self.canvas.create_text(CANVAS_L/2, CANVAS_A/2, text= msg, fill='white')
        self.comecar['text'] = 'Reiniciar'
        self.comecar['command'] = self.recomeça
        
    def desenhar(self):
        #metodo para redesenhar a tela do jogo
        #primeiro apagamos tudo que ha no canvas
        self.canvas.delete(ALL)

        #inserir imagens no canvas
        self.canvas.create_image((CANVAS_L/2,CANVAS_A/2), image = self.spritesheet[self.number_of_sprite])

        #e o player
        self.player.desenhar(self.canvas)
        
        #e por fim todos os retangulos
        for r in self.r:
            r.desenhar(self.canvas)

        #depois dsenhamos a bola
        self.bola.desenhar(self.canvas)
            
    def verificarColisao(self):
        #criar uma bouding box para a bola
        coord = self.canvas.bbox('bola')

        #pegar informações dos objetos que colidem com a bola
        colisoes = self.canvas.find_overlapping(*coord)
    
        #se o numero de colisoes é diferente de 0
        if len(colisoes) != 0:
            #verificar se o id do objeto colidido é diferente do id do objeto do player
            if colisoes[0] != self.player:
                #vamos colocar para que a colisao ocorre com o objeto mais proximo do topo esquerdo
                m_p = self.canvas.find_closest(coord[0], coord[1])
                #idenfificar com qual retangulo ocorreu a colisao
                for i in self.r:
                    #tendo encontrado um retangulo
                    if i == m_p[0]:
                        self.r.remove(i)#removomento o retangulo do jogo
                        self.canvas.delete(i)
                        #inverter o sentido da valocidade da bola
                        self.b_vy *= -1
                        return
                    
    def move_player(self, event):
        #movimento do meu player - rebatedor
        if event.x > 0 and event.x < CANVAS_L - self.player.b:
            self.player.x = event.x
            
if __name__ == '__main__':
    Jogo()





    
