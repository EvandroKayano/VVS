from Categoria import Categoria

class Participante():
    def __init__(self, nome: str, idade: int, categoria: Categoria, tempoEstimado: int, assinado: bool):
        self.nome = nome
        self.idade = idade
        self.categoria = categoria
        self.tempoEstimado = tempoEstimado
        self.assinado = assinado

    # def __str__(self):
    #     return f'Nome: {self.nome}, Idade: {self.idade}'