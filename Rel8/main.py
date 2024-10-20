from database import Database
from central_database import CentrallDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.86.219.225:7687", "neo4j", "deals-thoughts-hatch")
db.drop_all()

central_db = CentrallDatabase(db)

central_db.create_player("Pelé")
central_db.create_player("Maradona")
central_db.create_player("Junim")
central_db.create_player("Zezin")

central_db.create_match(1,"Pelé")
central_db.create_match(2,"Maradona")
central_db.create_match(3,"Pelé")
central_db.create_match(4,"Junim")

central_db.insert_player_match("Pelé",1)
central_db.insert_player_match("Maradona",2)
central_db.insert_player_match("Maradona",3)
central_db.insert_player_match("Pelé",3)
central_db.insert_player_match("Junim",4)
central_db.insert_player_match("Junim",2)
central_db.insert_player_match("Pelé",4)

central_db.get_match_by_id(3)
central_db.get_player_history("Pelé")

print("Jogadores: ")
print(central_db.get_players())
print("Partidas: ")
print(central_db.get_matches())

central_db.delete_player("Zezin")
central_db.delete_match(4)

# Fechando a conexão com o banco de dados
db.close()