import pyxel


pyxel.init(160, 120) #tamanho da tela(largura e altura)

def update(): #atualizar o frame 
    pass
       # pyxel.quit() #fecha a apricação


def draw(): #desenhar na tela 
    pyxel.text(10,60, "Olá dilsin.", 8)#imprime texto(x,y,mensagem, cor)
    pyxel.show
    #pyxel.cls(0) #limpa a tela com a cor
    #pyxel.rect(50, 50, 20, 20, 9) #desenha um quadrado(x, y, largura, altura, cor)

pyxel.run(update, draw)