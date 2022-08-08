import pyxel

class Teste: 
    def __init__(self):
        pyxel.init(150, 100)
        self.altura = 14
        self.posicaoP1 = 0
        self.aceleracao = 1
        self.tamanho = pyxel.height
        self.condicao = True
        pyxel.run(self.update, self.draw)

    def update(self):
        #alterando movimento, direcionando para baixo(o eixo y cresce de cima para baixo)
            if self.condicao:
                self.posicaoP1 += self.aceleracao 
                if self.posicaoP1 + self.altura == pyxel.height:
                    self.condicao = False

        #alterando movimento, direcionando para cima(o eixo y diminui de baixo para cima)
            else: 
                self.posicaoP1 -= self.aceleracao
                if self.posicaoP1 == 0:
                    self.condicao = True
        #obs: o eixo x, cresce da esquerda para direita e diminui da direita para esquerda
    def draw(self):
        pyxel.cls(1)
        pyxel.rect(2, self.posicaoP1, 3, self.altura, 3)

Teste()