import random

class Ser_Vivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

class Personagem(Ser_Vivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

class Monstro(Ser_Vivo):
    def __init__(self, pontos_vida, pontos_ataque, tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.inteligencia = inteligencia

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, tipo, forca):
        super().__init__(pontos_vida, pontos_ataque, tipo)
        self.forca = forca

goblin1 = Goblin(50, 10, "Goblin", 5)
goblin2 = Goblin(50, 10, "Goblin", 7)
lobo = Lobo(80, 15, "Lobo", 8)
guerreiro = Personagem(100, 20, "Guerreiro")

def batalha(p1, p2):
    print(f"{p1.nome} vs {p2.tipo}")
    print(f"{p1.nome} tem {p1.pontos_vida} pontos de vida e {p1.pontos_ataque} pontos de ataque.")
    print(f"{p2.tipo} tem {p2.pontos_vida} pontos de vida e {p2.pontos_ataque} pontos de ataque.")
    while p1.pontos_vida > 0 and p2.pontos_vida > 0:
        if random.randint(1, 2) == 1:
            p2.pontos_vida -= p1.pontos_ataque
            print(f"{p1.nome} ataca {p2.tipo} causando {p1.pontos_ataque} de dano. {p2.tipo} tem {p2.pontos_vida} pontos de vida restantes.")
        else:
            p1.pontos_vida -= p2.pontos_ataque
            print(f"{p2.tipo} ataca {p1.nome} causando {p2.pontos_ataque} de dano. {p1.nome} tem {p1.pontos_vida} pontos de vida restantes.")
    if p1.pontos_vida <= 0:
        print(f"{p1.nome} morreu.")
    else:
        print(f"{p2.tipo} morreu.")

batalha(guerreiro, goblin1)
batalha(guerreiro, goblin2)
batalha(guerreiro, lobo)
