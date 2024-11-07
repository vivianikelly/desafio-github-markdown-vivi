class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def pessoa_formatada():
        return nome, idade 
        
# Entrada do usuário
nome = input()
idade = int(input())

pessoa = Pessoa(nome, idade)
print(f"Nome: {nome}, \tIdade: {idade}")