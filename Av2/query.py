from database import Database

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://3.94.88.86", "neo4j", "crack-september-accruement")
#db.drop_all()

#Função auxiliar para mostrar os resultados
def result(query_function):
    # Executa a função de consulta e obtém os dados
    data = query_function()
    if data:
        for record in data:
            print(record)
    else:
        print("No results found.")

#Questão 1

# a.
def q1A():
    query = "MATCH (t:Teacher {name: $name}) RETURN t.ano_nasc, t.cpf"
    parameters = {"name": "Renzo"}
    return db.execute_query(query, parameters)

#Mostrando os dados
result(q1A)


# b.
def q1B():
    query = """
        MATCH (t:Teacher) 
        WHERE t.name STARTS WITH 'M' 
        RETURN t.name, t.cpf
    """
    return db.execute_query(query)

#Mostrando os dados
result(q1B)


# c.
def q1C():
    query = """
        MATCH (c:City)  
        RETURN c.name
    """
    return db.execute_query(query)

#Mostrando os dados
result(q1C)


# d.
def q1D():
    query = """
        MATCH (s:School)
        WHERE s.number >= 150 AND s.number <= 550  
        RETURN s.name, s.address, s.number
    """
    return db.execute_query(query)

#Mostrando os dados
result(q1D)

# Questão 2

# a.
def q2A():
    query = """
        MATCH (t:Teacher) 
        RETURN MIN(t.ano_nasc), MAX(t.ano_nasc)
    """
    return db.execute_query(query)

#Mostrando os dados
result(q2A)


# b.
def q2B():
    query = """
        MATCH (c:City) 
        RETURN AVG(c.population)
    """
    return db.execute_query(query)

#Mostrando os dados
result(q2B)


# c.
def q2C():
    query = """
        MATCH (c:City) 
        WHERE c.cep = "37540-000"
        RETURN REPLACE(c.name,"a","A")
    """
    return db.execute_query(query)

#Mostrando os dados
result(q2C)


# d.
def q2D():
    query = """
        MATCH (t:Teacher) 
        RETURN substring(t.name,2,1)
    """
    return db.execute_query(query)

#Mostrando os dados
result(q2D)


db.close()