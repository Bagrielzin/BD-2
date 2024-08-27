from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, db: Database):
        self.db = db

    def resetar(self):
        self.db.resetDatabase()
        
    # Função 1 - Pokemons do tipo fogo que não evoluem
    def f1(self):
        tipo = ["Fire"]
        pokemons = self.db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$exists": False} })
        writeAJson(pokemons, "Pokemons de fogo que não possuem evolução")

    # Função 2 - Pokemons com uma chance de spawn menor que 0.05
    def f2(self):
        pokemons = self.db.collection.find({ "spawn_chance": {"$lt": 0.05} })
        writeAJson(pokemons, "Pokemons com uma chance de spawn menor que 0.05")

    # Função 3 - Pokemons do tipo dragão Dragão
    def f3(self):
        pokemons = self.db.collection.find({"type": "Dragon"})
        writeAJson(pokemons, "Pokemons do tipo dragão Dragão")

    # Função 4 - Pokemons no estágio final de evolução
    def f4(self):
        pokemons = self.db.collection.find({"prev_evolution": {"$size": 2}})
        writeAJson(pokemons, "Pokemons no estágio final de evolução")

    # Função 5 - Pokemons do tipo água que possuem três evoluções
    def f5(self):
        tipo = ["Water"]
        pokemons = self.db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$size": 2} })
        writeAJson(pokemons, "Pokemons do tipo água que possuem três evoluções")