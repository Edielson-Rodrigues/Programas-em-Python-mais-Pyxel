import pyxel

class Teste: 
    def __init__(self):
        pyxel.init(150, 100, title='Movimento barras', fps=60)
        self.altura = 10
        self.posicaoP1 = 0
        self.velocidade = 1
        self.tamanho = pyxel.height
        self.condicao = True
        pyxel.run(self.update, self.draw)

    def update(self):
        #alterando movimento, direcionando para baixo(o eixo y cresce de cima para baixo)
        if self.condicao:
            self.posicaoP1 += self.velocidade
            if self.posicaoP1 + self.altura == pyxel.height:
                self.condicao = False
                #vereficando e aumentando a velocidade
                if self.velocidade <= 2.5:
                    self.velocidade += 0.5
                
        #alterando movimento, direcionando para cima(o eixo y diminui de baixo para cima)
        else: 
            self.posicaoP1 -= self.velocidade
            if self.posicaoP1 == 0:
                self.condicao = True
                #vereficando e aumentando a velocidade
                if self.velocidade <= 2.5:
                    self.velocidade += 0.5
        
        #obs: o eixo x, cresce da esquerda para direita e diminui da direita para esquerda
    def draw(self):
        pyxel.cls(1)
        pyxel.rect(2, self.posicaoP1, 3, self.altura, 3)

Teste()