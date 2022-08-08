import pyxel

class Quadrado:
    def __init__(self):
        pyxel.init(160, 120)
        self.x = 0 
        pyxel.run(self.update, self.draw)

    def update(self):
        pyxel.cls(14)
        self.x = (self.x + 1) % pyxel.width
        
    def draw(self):
        pyxel.rect(self.x, 50, 10, 10, 5)
        
Quadrado()