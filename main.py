class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = nome
        self.idade = idade
        self.especie = especie
        self.cor = cor
        self.som = som

    def emitir_som(self):
        print(self.som)

    def mudar_cor(self, novacor):
        self.cor = novacor


class Elefante(Animal):
    def __init__(self, nome, idade, especie, cor, som, tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = tamanho

    def trombar(self):
        if self.especie == "Africano":
            if self.idade < 10:
                self.som = "Paaah"
            else:
                self.som = "PAHHHHHH"
        print("Som:", self.som)

    def mudar_tamanho(self, novotamanho):
        if self.especie == "Africano":
            if self.idade < 10:
                self.tamanho = "pequeno"
            else:
                self.tamanho = "grande"
        else:
            self.tamanho = novotamanho
        print("Novo tamanho:", self.tamanho)

elefante = Elefante(input("Digite o nome: "),int(input("Digite a idade: ")),input("Digite a especie: "),input("Digite a cor: "),input("Digite o som: "),input("Digite o tamanho: "))


#elefante.nome = input("Digite o nome: ")
#elefante.idade = input("Digite a idade: ")
#elefante.especie = input("Digite a especie: ")
#elefante.cor = input("Digite a cor: ")
#elefante.som = input("Digite o som: ")
#elefante.tamanho = input("Digite o tamanho: ")

print("Nome:", elefante.nome)
print("Idade:", elefante.idade)
print("Especie:", elefante.especie)
print("Cor:", elefante.cor)
print("Som:", elefante.som)
print("Tamanho:", elefante.tamanho)

elefante.trombar()
elefante.mudar_tamanho(20)

