class chatBot:
    def __init__(self, nome, idade): #essa função sempre é rodada ao instanciar uma class
        self.nome = nome #o self basicamente indetifica qual é a instacia criada por exemplo : a.fala substitui -> self.fala
        self.idade = int(idade)

    def fala(self):
        print('O nome do chatBot é {} ' .format(self.nome))
        #a = 'va'
        #return print(a)

nomeDoUsuario = input('Digite seu nome: ')

a = chatBot(nomeDoUsuario, 19) #prenche os paramentros do __init__
a.fala()
print('A idade do chatBot é {}' .format(a.idade))