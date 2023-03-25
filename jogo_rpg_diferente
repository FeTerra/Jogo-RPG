# Uma  breve história para vocês!
print("Era uma vez um grande guerreiro chamado Kratos, que se deparou com um lobo feroz e um goblin astuto.\n")

print("Kratos sacou sua espada e se preparou para a batalha...\n")

print("O lobo avançou primeiro com toda a sua força, mas Kratos, com seus reflexos rápidos, conseguiu desviar do ataque e contra-atacar com um golpe certeiro.\n")

print("O goblin, vendo o companheiro em apuros, usou sua inteligência para criar uma distração e atacar por trás. Kratos, porém, já estava preparado e conseguiu bloquear o ataque com seu escudo.\n")

# Criando a classe SerVivo
class SerVivo:
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        self.pontos_de_vida = pontos_de_vida
        self.pontos_de_ataque = pontos_de_ataque

    def atacar(self, alvo):
        alvo.pontos_de_vida -= self.pontos_de_ataque

    def verificar_vida(self):
        if self.pontos_de_vida <= 0:
            if isinstance(self, Personagem):
                print("O personagem morreu.")
            elif isinstance(self, monstro1):
                print("O Lobo morreu.")
            elif isinstance(self, monstro2):
                print("O Goblin morreu.")

# Criando um novo objeto da classe SerVivo
ser_vivo1 = SerVivo(100, 20)

# Acessando os atributos do objeto criado
print("Pontos de vida:", ser_vivo1.pontos_de_vida)
print("Pontos de ataque:", ser_vivo1.pontos_de_ataque)

class Personagem(SerVivo):
    def __init__(self, nome, pontos_de_vida, pontos_de_ataque):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.nome = nome

# Criando um novo objeto da classe Personagem
personagem1 = Personagem("Guerreiro", 100, 20)

# Acessando os atributos do objeto criado
print("Nome:", personagem1.nome)
print("Pontos de vida:", personagem1.pontos_de_vida)
print("Pontos de ataque:", personagem1.pontos_de_ataque)

class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo, inteligencia=10, forca=10):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo
        self.inteligencia = inteligencia
        self.forca = forca

# Criando um novo objeto da classe Monstro
monstro1 = Monstro(150, 30, "Lobo", 0, 12)
monstro2 = Monstro(80, 15, "Goblin", 8, 0)

# Acessando os atributos do objeto criado
print("Pontos de vida:", monstro1.pontos_de_vida)
print("Pontos de ataque:", monstro1.pontos_de_ataque)
print("Tipo:", monstro1.tipo)
print("Monstro 2 - Pontos de vida:", monstro2.pontos_de_vida)
print("Monstro 2 - Pontos de ataque:", monstro2.pontos_de_ataque)
print("Monstro 2 - Tipo:", monstro2.tipo)

# Personagem ataca o monstro
personagem1.atacar(monstro1)
print("O Guerreiro atacou o lobo! Pontos de vida do lobo:", monstro1.pontos_de_vida)

personagem1.atacar(monstro2)
print("O Guerreiro atacou o goblin! Pontos de vida do goblin:", monstro2.pontos_de_vida)


# Monstro ataca o personagem
monstro1.atacar(personagem1)
print("O monstro atacou o Guerreiro! Pontos de vida do Guerreiro:", personagem1.pontos_de_vida)

monstro2.atacar(personagem1)
print("O monstro atacou o Guerreiro! Pontos de vida do Guerreiro:", personagem1.pontos_de_vida)
