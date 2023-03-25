Nessa nova versão, foi adicionado um loop de rodadas na batalha.
A cada rodada, é sorteado se o guerreiro irá esquivar ou não do ataque do monstro. Se ele não esquivar, 
o guerreiro ataca o monstro e o monstro ataca o guerreiro. Se a vida de algum dos personagens chegar a 0, a batalha acaba.

import random

class SerVivo:
    def __init__(self, pontos_vida, pontos_ataque):
        self.pontos_vida = pontos_vida
        self.pontos_ataque = pontos_ataque

    def atacar(self, alvo):
        alvo.perder_vida(self.pontos_ataque)

    def perder_vida(self, pontos):
        self.pontos_vida -= pontos
        if self.pontos_vida <= 0:
            print(f"{self.nome} morreu.")

class Personagem(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, nome):
        super().__init__(pontos_vida, pontos_ataque)
        self.nome = nome

class Monstro(SerVivo):
    def __init__(self, pontos_vida, pontos_ataque, tipo):
        super().__init__(pontos_vida, pontos_ataque)
        self.tipo = tipo

class Goblin(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, inteligencia):
        super().__init__(pontos_vida, pontos_ataque, "Goblin")
        self.inteligencia = inteligencia

class Lobo(Monstro):
    def __init__(self, pontos_vida, pontos_ataque, forca):
        super().__init__(pontos_vida, pontos_ataque, "Lobo")
        self.forca = forca

def batalha(pers, mons):
    print(f"{pers.nome} encontrou um {mons.tipo} selvagem!")
    print(f"{pers.nome} - Vida: {pers.pontos_vida}, Ataque: {pers.pontos_ataque}")
    print(f"{mons.tipo} - Vida: {mons.pontos_vida}, Ataque: {mons.pontos_ataque}\n")

    rodada = 1
    while pers.pontos_vida > 0 and mons.pontos_vida > 0:
        print(f"--- Rodada {rodada} ---")
        if random.choice([True, False]):
            print(f"{pers.nome} esquivou do ataque do {mons.tipo}!")
        else:
            pers.atacar(mons)
            print(f"{pers.nome} atacou o {mons.tipo}!")

        if mons.pontos_vida <= 0:
            break

        mons.atacar(pers)
        print(f"{mons.tipo} atacou {pers.nome}!\n")

        if pers.pontos_vida <= 0:
            break

        rodada += 1

# Criação dos personagens
guerreiro = Personagem(20, 5, "Guerreiro")
goblin = Goblin(10, 3, 1)
lobo = Lobo(15, 4, 3)

# Batalha
batalha(guerreiro, goblin)
print("------------------")
batalha(guerreiro, lobo)
