import pyxel

class teste:
    def __init__(self):
        pyxel.init(100, 100)
        self.x = 50
        self.y = 50
        self.largura = 20
        self.altura = 10
        self.colisao = False
        pyxel.run(self.update, self.draw)

    def update(self):
        self.colisao = self.detectarColisao(self.x, self.y, self.largura, self.largura, pyxel.mouse_x, pyxel.mouse_y, self.largura/2, self.altura)
        
        self.cor = 7

        if self.colisao:
            self.cor = 2

    def draw(self):
        pyxel.cls(0)
        pyxel.rect(self.x, self.y, self.largura, self.largura, 5)
        pyxel.rect(pyxel.mouse_x, pyxel.mouse_y, self.largura/2, self.altura, self.cor)

    def detectarColisao(self, x1, y1, l1, a1, x2, y2, l2, a2):
        if  x1 < x2 + l2 and x1 + l1 > x2 and y1 < y2 + a2 and y1 + a1 > y2:
            return True

        else:
            return False
teste()