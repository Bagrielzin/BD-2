from database import Database
from helper.writeAJson import writeAJson
from pokedex import Pokedex

db = Database(database="pokedex", collection="pokemons")
    
pokedex = Pokedex(db)
    
#pokedex.resetar()  
pokedex.f1()       
pokedex.f2()   
pokedex.f3()       
pokedex.f4()      
pokedex.f5()