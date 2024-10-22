from database import Database
from teacher_crud import TeacherCrud

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.94.88.86", "neo4j", "crack-september-accruement")
#db.drop_all()

teacher_db = TeacherCrud(db)

#Questão 3

# b.
teacher_db.create('Chris Lima',1956,'189.052.396-66')

# c.
print(teacher_db.read("Chris Lima"))

# d.
teacher_db.update("Chris Lima","162.052.777-77")