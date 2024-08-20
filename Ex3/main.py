from database import Database
from helper.writeAJson import writeAJson

db = Database(database="pokedex", collection="pokemons")
# db.resetDatabase()

#Função 1 - Pokemons do tipo fogo que não evoluem
#tipo = ["Fire"]
#pokemons = db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$exists": False} })
#writeAJson(pokemons, "Pokemons de fogo que não possuem evolução") 

#Função 2 - Pokemons com uma chance de spawn menor que 0.05
#pokemons = db.collection.find({ "spawn_chance":{"$lt":0.05}})
#writeAJson(pokemons, "Pokemons com uma chance de spawn menor que 0.05") 

#Função 3 - Pokemons do tipo dragão Dragão
#pokemons = db.collection.find({"type": "Dragon"})
#writeAJson(pokemons, "Pokemons do tipo dragão Dragão")

#Função 4 - Pokemons no estágio final de evolução
#pokemons = db.collection.find({"prev_evolution": {"$size": 2}})
#writeAJson(pokemons, "Pokemons no estágio final de evolução")

#Função 5 - "Pokemons que possuem três evoluções"
#tipo = ["Water"]
#pokemons = db.collection.find({ "type": {"$in": tipo}, "next_evolution": {"$size": 2} })
#writeAJson(pokemons, "Pokemons do tipo água que possuem três evoluções")