from database import Database
from lotr_crud import LortCrud
from cli import LotrCLI

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://98.80.212.124", "neo4j", "scab-law-push")     # agr vai dog, pode testar

lotr_db = LortCrud(db)
lotr_cli = LotrCLI(lotr_db)
lotr_cli.run()

db.close()