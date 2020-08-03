class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    felipe = Pessoa(nome='Felipe')
    mendes = Pessoa(felipe, nome='Mendes')
    print(Pessoa.cumprimentar(mendes))
    print(id(mendes))
    print(mendes.cumprimentar())
    print(mendes.nome)
    mendes.nome = 'Mendes'
    for filho in mendes.filhos:
        print(filho.nome)
