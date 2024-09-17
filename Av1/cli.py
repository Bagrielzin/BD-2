class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        nome_passageiro = input("Entre com o nome do passageiro: ")
        documento_passageiro = input("Entre com o documento do passageiro: ")
        
        corridas = []
        while True:
            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distância da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = {
                "nota": nota_corrida,
                "distancia": distancia,
                "valor": valor,
                "passageiro": {
                    "nome": nome_passageiro,
                    "documento": documento_passageiro
                }
            }
            corridas.append(corrida)
            mais_corridas = input("Deseja adicionar mais corridas? (s/n): ")
            if mais_corridas.lower() != 's':
                break
        
        nota_motorista = int(input("Entre com a nota do motorista: "))
        
        self.motorista_model.create_motorista(nota_motorista, corridas)
        
    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        if motorista:
            passageiros = {corrida['passageiro']['nome']: corrida['passageiro']['documento'] for corrida in motorista.get('corridas', [])}
            for nome, documento in passageiros.items():
                print(f"Nome do passageiro: {nome}")
                print(f"Documento do passageiro: {documento}")
            
            print("Corridas:")
            for corrida in motorista.get('corridas', []):
                print(f"Nota da corrida: {corrida['nota']}")
                print(f"Distância: {corrida['distancia']}")
                print(f"Valor: {corrida['valor']}")
            
            print(f"Nota do motorista: {motorista.get('nota')}")

    def update_motorista(self):
        id = input("Enter the id: ")
        nota_motorista = int(input("Entre com a nova nota do motorista: "))

        nome_passageiro = input("Entre com o nome do passageiro: ")
        documento_passageiro = input("Entre com o documento do passageiro: ")

        corridas = []
        while True:
            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distância da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = {
                "nota": nota_corrida,
                "distancia": distancia,
                "valor": valor,
                "passageiro": {
                    "nome": nome_passageiro,
                    "documento": documento_passageiro
                }
            }
            corridas.append(corrida)
            mais_corridas = input("Deseja adicionar mais corridas? (s/n): ")
            if mais_corridas.lower() != 's':
                break

        self.motorista_model.update_motorista(id, nota_motorista, corridas)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()