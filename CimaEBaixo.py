import pyxel

class Quadrado:

    def __init__(self):   
        pyxel.init(160, 120)
        self.y = 55
        pyxel.run(self.update, self.draw)
        
    def update(self):
        pyxel.cls(14)
        self.y = ((self.y + 1)) % pyxel.height
        self.seno = pyxel.sin(self.y)
        self.y = ((self.y + 1) - self.seno) % pyxel.height

    def draw(self):
        pyxel.rect(75, self.y, 10, 10, 10)

Quadrado()
