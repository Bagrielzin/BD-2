from classes import Motorista, Corrida, Passageiro

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
        corridas = []
        while True:
            nome_passageiro = input("Entre com o nome do passageiro: ")
            documento_passageiro = input("Entre com o documento do passageiro: ")
            passageiro = Passageiro(nome_passageiro, documento_passageiro)

            nota_corrida = int(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distância da corrida: "))
            valor = float(input("Entre com o valor da corrida: "))

            corrida = Corrida(nota_corrida, distancia, valor, passageiro)
            corridas.append(corrida)

            mais_corridas = input("Deseja adicionar mais corridas? (s/n): ")
            if mais_corridas.lower() != 's':
                break
        
        nota_motorista = int(input("Entre com a nota do motorista: "))
        motorista = Motorista(nota_motorista, corridas)

        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Enter the id: ")
        motorista = self.motorista_model.read_motorista_by_id(id)
        
        if motorista:
            print(f"Nota do motorista: {motorista.nota}\n")
            for corrida in motorista.corridas:
                print(f"  Nota da corrida: {corrida.nota}")
                print(f"  Distância: {corrida.distancia}")
                print(f"  Valor: {corrida.valor}")
                print(f"  Nome do passageiro: {corrida.passageiro.nome}")
                print(f"  Documento do passageiro: {corrida.passageiro.documento}\n")

    def update_motorista(self):
        id = input("Enter the id: ")
        motorista_atual = self.motorista_model.read_motorista_by_id(id)

        if not motorista_atual:
            print("Motorista não encontrado.")
            return

        nota_motorista = int(input("Entre com a nova nota do motorista: "))

        corridas = []
        for corrida in motorista_atual.corridas:
            print(f"\nAtualizando informações da corrida:")
            nota_corrida = int(input(f"Nota da corrida ({corrida.nota}): "))
            distancia = float(input(f"Distância ({corrida.distancia}): "))
            valor = float(input(f"Valor ({corrida.valor}): "))
            
            nome_passageiro = input(f"Nome do passageiro ({corrida.passageiro.nome}): ")
            documento_passageiro = input(f"Documento do passageiro ({corrida.passageiro.documento}): ")

            passageiro_atualizado = Passageiro(nome_passageiro, documento_passageiro)
            corrida_atualizada = Corrida(nota_corrida, distancia, valor, passageiro_atualizado)
            corridas.append(corrida_atualizada)

        motorista_atualizado = Motorista(nota_motorista, corridas)
        self.motorista_model.update_motorista(id, motorista_atualizado)

    def delete_motorista(self):
        id = input("Enter the id: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Welcome to the motorista CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
