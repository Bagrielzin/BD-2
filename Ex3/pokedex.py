from database import Database
from helper.writeAJson import writeAJson

class Pokedex:
    def __init__(self, db: Database):
        self.db = db

    def resetar(self):
        self.db.resetDatabase()
        
    # Fun��o 1 - Pokemons do tipo fogo que n�o evoluem
    def f1(self):
        tipo = ["Fire"]
        pokemons = self.db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$exists": False} })
        writeAJson(pokemons, "Pokemons de fogo que n�o possuem evolu��o")

    # Fun��o 2 - Pokemons com uma chance de spawn menor que 0.05
    def f2(self):
        pokemons = self.db.collection.find({ "spawn_chance": {"$lt": 0.05} })
        writeAJson(pokemons, "Pokemons com uma chance de spawn menor que 0.05")

    # Fun��o 3 - Pokemons do tipo drag�o Drag�o
    def f3(self):
        pokemons = self.db.collection.find({"type": "Dragon"})
        writeAJson(pokemons, "Pokemons do tipo drag�o Drag�o")

    # Fun��o 4 - Pokemons no est�gio final de evolu��o
    def f4(self):
        pokemons = self.db.collection.find({"prev_evolution": {"$size": 2}})
        writeAJson(pokemons, "Pokemons no est�gio final de evolu��o")

    # Fun��o 5 - Pokemons do tipo �gua que possuem tr�s evolu��es
    def f5(self):
        tipo = ["Water"]
        pokemons = self.db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$size": 2} })
        writeAJson(pokemons, "Pokemons do tipo �gua que possuem tr�s evolu��es")