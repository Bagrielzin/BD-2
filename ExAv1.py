import threading
import time
import random
from pymongo import MongoClient

connector = MongoClient("mongodb://localhost:27017")
#print(connector)
database = connector['bancoiot']
#print(database)
collection = database.sensores
#print(collection)

# Inicializa os documentos dos sensores no MongoDB
#sensores = [
#    {"nomeSensor": "Sensor 1", "valorSensor": None, "unidade": "°C", "sensorAlarmado": False},
#    {"nomeSensor": "Sensor 2", "valorSensor": None, "unidade": "°C", "sensorAlarmado": False},
#    {"nomeSensor": "Sensor 3", "valorSensor": None, "unidade": "°C", "sensorAlarmado": False},
#]

# Inserindo documentos na coleção
#for sensor in sensores:
#    collection.insert_one(sensor)

# Volta as temperaturas dos sensores para 30 
result = collection.update_many(
    {},  # Filtro vazio: aplica a atualização a todos os documentos
    {
        "$set": {
            "valorSensor": 30,       # Define o valorSensor para 30
            "sensorAlarmado": False  # Define sensorAlarmado para False
        }
    }
)

def monitorar_sensor(sensor_id, intervalo):
    sensor_doc = collection.find_one({"nomeSensor": f"Sensor {sensor_id}"})
    
    while not sensor_doc["sensorAlarmado"]:
        temperatura = round(random.uniform(30, 40),2)
        print(f"Sensor {sensor_id}: {temperatura:.2f}°C")

        # Atualiza o valor do sensor no banco de dados
        collection.update_one(
            {"nomeSensor": f"Sensor {sensor_id}"},
            {"$set": {"valorSensor": temperatura}}
        )

        # Verifica se a temperatura está acima de 38°C
        if temperatura > 38:
            collection.update_one(
                {"nomeSensor": f"Sensor {sensor_id}"},
                {"$set": {"sensorAlarmado": True}}
            )
            print(f"Atenção! Temperatura muito alta! Verificar Sensor {sensor_id}")
            break
        
        time.sleep(intervalo)
        sensor_doc = collection.find_one({"nomeSensor": f"Sensor {sensor_id}"})

# Criação das threads
t1 = threading.Thread(target=monitorar_sensor, args=(1, 5))
t2 = threading.Thread(target=monitorar_sensor, args=(2, 3))
t3 = threading.Thread(target=monitorar_sensor, args=(3, 7))

# Início das threads
t1.start()
t2.start()
t3.start()

# Aguarda que todas as threads terminem
t1.join()
t2.join()
t3.join()

print("Monitoramento de sensores finalizado.")
