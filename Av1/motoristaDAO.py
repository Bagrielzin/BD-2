from pymongo import MongoClient
from bson.objectid import ObjectId
from classes import Motorista, Corrida, Passageiro

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista: Motorista):
        try:
            corridas_dicts = [{
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            } for corrida in motorista.corridas]

            res = self.db.collection.insert_one({
                "nota": motorista.nota,
                "corridas": corridas_dicts
            })
            print(f"Motorista criado com id: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista_by_id(self, id: str):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res:
                corridas = [Corrida(
                    nota=corrida["nota"],
                    distancia=corrida["distancia"],
                    valor=corrida["valor"],
                    passageiro=Passageiro(
                        nome=corrida["passageiro"]["nome"],
                        documento=corrida["passageiro"]["documento"]
                    )
                ) for corrida in res.get("corridas", [])]
                motorista = Motorista(nota=res.get("nota"), corridas=corridas)
                print(f"Motorista encontrado: {motorista}")
                return motorista
            return None
        except Exception as e:
            print(f"Ocorreu um erro ao procurar o motorista: {e}")
            return None

    def update_motorista(self, id: str, motorista: Motorista):
        try:
            corridas_dicts = [{
                "nota": corrida.nota,
                "distancia": corrida.distancia,
                "valor": corrida.valor,
                "passageiro": {
                    "nome": corrida.passageiro.nome,
                    "documento": corrida.passageiro.documento
                }
            } for corrida in motorista.corridas]

            res = self.db.collection.update_one(
                {"_id": ObjectId(id)},
                {"$set": {
                    "nota": motorista.nota,
                    "corridas": corridas_dicts
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
            print(f"Ocorreu um erro ao procurar o motorista: {e}")
            return None
