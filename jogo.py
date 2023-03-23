class ser_vivo:
    def __init__(self, pontos_vida, pontos_ataque ):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def atacar(self, dano_causado, alvo):
        self.pontos_vida -= dano_causado
        self.alvo = alvo
    
    def status(self):
        print(self.pontos_vida)

class personagem(ser_vivo):
    def __init__(self, nome):
        super().__init__(pontos_vida=150, pontos_ataque=20)
        self.nome = nome
    
class monstro(ser_vivo):
    def __init__(self, tipo):
        super().__init__(pontos_vida= 150, pontos_ataque=20)
        self.tipo = tipo

class lobo(monstro):
    def __init__(self, forca):
        super().__init__(pontos_vida = 100, pontos_ataque = 10)
        self.forca = forca

class goblin(monstro):
    def __init__(self, inteligencia):
        super().__init__(pontos_vida = 50, pontos_ataque = 5)
        self.iteligencia = inteligencia
        
personagem = personagem(nome="Ferreiro")

personagem.atacar(20, '')
personagem.status()
