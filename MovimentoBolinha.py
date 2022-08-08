import pyxel

class Bolinha:
    def __init__(self):
        pyxel.init(150, 100, title='Bolinha Movimento')
        self.condicaoX = True
        self.condicaoY = True
        self.posicao = [0, 0]
        self.velocidade = 1
        self.raio = 2
        pyxel.run(self.update, self.draw)

    def update(self):
        #aplicando movimento na horizontal (no eixo X)
        if self.condicaoX:
            self.posicao[0] += self.velocidade
            if self.posicao[0] + (self.raio * 2) + 2 == pyxel.width:
                self.condicaoX = False
        else:
            self.posicao[0] -= self.velocidade
            if self.posicao[0] + 1 == 0:
                self.condicaoX = True

        #aplicando movimento na vertical (eixo Y)
        if self.condicaoY:
            self.posicao[1] += self.velocidade
            if self.posicao[1] + (self.raio * 2) + 2 == pyxel.height:
                self.condicaoY = False
        else:
            self.posicao[1] -= self.velocidade
            if self.posicao[1] + 1 == 0:
                self.condicaoY = True
            

    def draw(self):
        pyxel.cls(2)
        pyxel.circ(self.posicao[0] + self.raio+1, self.posicao[1] + self.raio+1, self.raio, 1)


Bolinha()
