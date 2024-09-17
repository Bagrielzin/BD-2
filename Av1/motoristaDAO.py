from pymongo import MongoClient
from bson.objectid import ObjectId

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, nota_motorista: int, corridas: list):
        try:
            res = self.db.collection.insert_one({
                "nota": nota_motorista,
                "corridas": corridas
            })
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None


    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            print(f"Motorista encontrado: {res}")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o morista: {e}")
            return None

    def update_motorista(self, id: str, nota_motorista: int, corridas):
        try:
            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "nota": nota_motorista,
                    "corridas": corridas
                }}
            )
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificados")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id: str):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletados")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o morista: {e}")
            return None