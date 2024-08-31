from database import Database
from helper.writeAJson import writeAJson

class ProductAnalyzer:
    def __init__(self, db: Database):
        self.db = db

    # Funçao 1 - Total de vendas por dia
    def f1(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$data_compra",  # Agrupa por data da compra
                "total_vendas": {"$sum": 1}  # Conta o número de documentos (vendas) por dia
            }},
        ])
        writeAJson(result, "Total de vendas por dia")

    # Funçao 2 - Produto mais vendido em todas as compras
    def f2(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",  # Agrupa por descrição do produto
                "quantidade_vendida": {"$sum": "$produtos.quantidade"}  # Soma as quantidades vendidas de cada produto
            }},
            {"$sort": {"quantidade_vendida": -1}},  # Ordena por quantidade vendida em ordem decrescente
            {"$limit": 1}  # Limita o resultado ao produto mais vendido
        ])
        writeAJson(result, "Produto mais vendido")

    # Funçao 3 - Cliente que mais gastou com 1 compra
    def f3(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$cliente_id",  # Agrupa por cliente
                "total_gasto": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}  # Calcula o total gasto em cada compra
            }},
            {"$sort": {"total_gasto": -1}},  # Ordena por total gasto em ordem decrescente
            {"$limit": 1}  # Limita o resultado ao cliente que mais gastou
        ])
        writeAJson(result, "Cliente que mais gastou em uma única compra")

    # Funçao 4 - Produtos com mais de 1 unidade vendida
    def f4(self):
        result = self.db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {
                "_id": "$produtos.descricao",  # Agrupa por descrição do produto
                "quantidade_vendida": {"$sum": "$produtos.quantidade"}  # Soma as quantidades vendidas
            }},
            {"$match": {"quantidade_vendida": {"$gt": 1}}},  # Filtra para produtos com mais de 1 unidade vendida
            {"$sort": {"quantidade_vendida": -1}}  # Ordena por quantidade vendida em ordem decrescente (opcional)
        ])
        writeAJson(result, "Produtos com mais de 1 unidade vendida")
