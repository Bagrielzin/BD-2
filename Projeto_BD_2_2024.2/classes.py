class Habitante:
    def __init__(self,nome,raca,idade,altura):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.altura = altura

    def to_dict(self):
        return{
            "nome": self.nome,
            "raca": self.raca,
            "idade": self.idade,
            "altura": self.altura
    }

class Localizacao:
    def __init__(self,cidade,reino,num_habitantes):
        self.cidade = cidade
        self.reino = reino
        self.num_habitantes = num_habitantes

    def to_dict(self):
        return{
            "cidade": self.cidade,
            "reino": self.reino,
            "num_habitantes": self.num_habitantes 
    }
    
        