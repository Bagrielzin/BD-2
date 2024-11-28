from classes import Habitante, Localizacao

class LortCrud():
    def __init__(self, database):
        self.db = database

    def create_habitante(self, habitante):  # Aceita um objeto Habitante
        query = "CREATE (:Habitante {nome: $nome, raca: $raca, idade: $idade, altura: $altura})"
        parameters = habitante.to_dict()
        self.db.execute_query(query, parameters)

    def create_localizacao(self, localizacao):  # Aceita um objeto Localizacao
        query = "CREATE (:Localizacao {cidade: $cidade, reino: $reino, num_habitantes: $num_habitantes})"
        parameters = localizacao.to_dict()
        self.db.execute_query(query, parameters)

    def insert_habitante_localizacao(self, nome, cidade):  # cria relação entre habitante e local
        query = "MATCH (h:Habitante {nome: $nome}) MATCH (l:Localizacao {cidade: $cidade}) CREATE (h)-[:PASSOU_POR]->(l)"
        parameters = {"nome": nome, "cidade": cidade}
        self.db.execute_query(query, parameters)

    def read_habitantes(self):  # lê todos os habitantes e retorna objetos Habitante
        query = "MATCH (h:Habitante) RETURN h.nome AS nome, h.raca AS raca, h.idade AS idade, h.altura AS altura ORDER BY nome ASC"
        results = self.db.execute_query(query)
        return [Habitante(**record) for record in results]

    def read_localizacoes(self):  # lê todas as localizações e retorna objetos Localizacao
        query = "MATCH (l:Localizacao) RETURN l.cidade AS cidade, l.reino AS reino, l.num_habitantes AS num_habitantes ORDER BY cidade ASC"
        results = self.db.execute_query(query)
        return [Localizacao(**record) for record in results]
    
    def passed_by(self, nome_habitante): # mostra os habitantes e as cidades pelas quais eles passaram
        query = """
        MATCH (h:Habitante {nome: $nome_habitante})-[:PASSOU_POR]->(c:Localizacao)
        RETURN c.cidade AS cidade ORDER BY cidade ASC
        """
        results = self.db.execute_query(query, {"nome_habitante": nome_habitante})
        return [record["cidade"] for record in results]

    def update_habitante(self, nome, nova_idade):  # atualiza idade com base no nome
        query = "MATCH (h:Habitante {nome: $nome}) SET h.idade = $nova_idade"
        parameters = {"nome": nome, "nova_idade": nova_idade}
        self.db.execute_query(query, parameters)

    def update_localizacao(self, cidade, novo_num_habitantes):  # atualiza num_habitantes com base na cidade
        query = "MATCH (l:Localizacao {cidade: $cidade}) SET l.num_habitantes = $novo_num_habitantes"
        parameters = {"cidade": cidade, "novo_num_habitantes": novo_num_habitantes}
        self.db.execute_query(query, parameters)

    def delete_habitante(self, nome):  # deleta um habitante com base no nome
        query = "MATCH (h:Habitante {nome: $nome}) DETACH DELETE h"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def delete_localizacao(self, cidade):  # deleta uma localizacao com base na cidade
        query = "MATCH (l:Localizacao {cidade: $cidade}) DETACH DELETE l"
        parameters = {"cidade": cidade}
        self.db.execute_query(query, parameters)

    def amount_habitantes(self):    # Função para mostrar o número de habitantes
        query = "MATCH (h:Habitante) RETURN count(h) AS total"
        result = self.db.execute_query(query)
        return result[0]["total"]
    
    def habitante_has_more_traveled(self):  # Função para mostrar o habitante que mais viajou
        query = """
        MATCH (h:Habitante)-[:PASSOU_POR]->(:Localizacao)
        RETURN h.nome AS nome, COUNT(*) AS total
        ORDER BY total DESC
        LIMIT 1
        """
        result = self.db.execute_query(query)
        return result[0]
    
    def most_visited_location(self):    # Função que retorna a localização mais visitada
        query = """
        MATCH (:Habitante)-[:PASSOU_POR]->(l:Localizacao)
        RETURN l.cidade AS cidade, COUNT(*) AS total
        ORDER BY total DESC
        LIMIT 1
        """
        result = self.db.execute_query(query)
        return result[0]