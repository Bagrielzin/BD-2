class Motorista:

    def __init__(self,nota,corridas =[]):
        self.nota = nota
        self.corridas = corridas

class Corrida:

    def __init__(self,nota,distancia,valor,passageiro):
        self.nota = nota
        self.distancia = distancia
        self.valor = valor
        self.passageiro = passageiro


class Passageiro: 

    def __init__(self,nome,documento):
        self.nome = nome
        self.documento = documento