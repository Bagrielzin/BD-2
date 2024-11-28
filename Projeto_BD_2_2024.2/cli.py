from database import Database
from classes import Habitante, Localizacao
db = Database("bolt://98.80.212.124", "neo4j", "scab-law-push") # esse é o certo

class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            print("*--------------------------------*")
            print("Lotr CLI!")
            print("1 - Criar habitante")
            print("2 - Criar localização")
            print("3 - Criar relação habitante-localização")
            print("4 - Listar habitantes")
            print("5 - Listar localizações")
            print("6 - Exibir habitantes e as cidades pelas quais passaram")
            print("7 - Atualizar habitante")
            print("8 - Atualizar localização")
            print("9 - Deletar habitante")
            print("10 - Deletar localização")
            print("11 - Limpar banco de dados")
            print("12 - Mostrar número total de habitantes")
            print("13 - Mostrar habitante que mais viajou")
            print("14 - Mostrar localização mais visitada")
            print("15 - Sair do programa")
            print("*--------------------------------*")
            command = input("Entre  com um comando: ")
            if command == "15":
                print("Namárië!")
                db.close()
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Comando inválido. Tente novamente.")


class LotrCLI(SimpleCLI):
    def __init__(self, lotr_model):
        super().__init__()
        self.lotr_model = lotr_model
        self.add_command("1", self.create_habitante)
        self.add_command("2", self.create_localizacao)
        self.add_command("3", self.insert_habitante_localizacao)
        self.add_command("4", self.read_habitantes)
        self.add_command("5", self.read_localizacoes)
        self.add_command("6", self.passed_by)
        self.add_command("7", self.update_habitante)
        self.add_command("8", self.update_localizacao)
        self.add_command("9", self.delete_habitante)
        self.add_command("10", self.delete_localizacao)
        self.add_command("11", self.drop_db)
        self.add_command("12", self.amount_habitantes)
        self.add_command("13", self.habitante_has_more_traveled)
        self.add_command("14", self.most_visited_location)

    def create_habitante(self):
        nome = input("Nome: ")
        raca = input("Raça: ")
        idade = int(input("Idade: "))
        altura = float(input("Altura: "))
        habitante = Habitante(nome, raca, idade, altura)
        self.lotr_model.create_habitante(habitante)
        print(f"Habitante '{nome}' criado com sucesso.")

    def create_localizacao(self):
        cidade = input("Cidade: ")
        reino = input("Reino: ")
        num_habitantes = int(input("Número de habitantes: "))
        localizacao = Localizacao(cidade, reino, num_habitantes)
        self.lotr_model.create_localizacao(localizacao)
        print(f"Localização '{cidade}' criada com sucesso.")

    def insert_habitante_localizacao(self):
        nome = input("Nome do habitante: ")
        cidade = input("Cidade: ")
        self.lotr_model.insert_habitante_localizacao(nome, cidade)
        print(f"Relação entre '{nome}' e '{cidade}' criada com sucesso.")

    def read_habitantes(self):
        habitantes = self.lotr_model.read_habitantes()
        if habitantes:
            for habitante in habitantes:
                print(habitante.to_dict())
        else:
            print("Nenhum habitante encontrado.")

    def read_localizacoes(self):
        localizacoes = self.lotr_model.read_localizacoes()
        if localizacoes:
            for localizacao in localizacoes:
                print(localizacao.to_dict())
        else:
            print("Nenhuma localização encontrada.")

    def passed_by(self):
        habitantes = self.lotr_model.read_habitantes()
        if habitantes:
            for habitante in habitantes:
                cidades = self.lotr_model.passed_by(habitante.nome)
                print(f"Habitante: {habitante.nome}")
                if cidades:
                    for cidade in cidades:
                        print(f"  - Cidade: {cidade}")
                else:
                    print("  - Não passou por nenhuma cidade.")
        else:
            print("Nenhum habitante encontrado.")

    def update_habitante(self):
        nome = input("Nome do habitante: ")
        nova_idade = int(input("Nova idade: "))
        self.lotr_model.update_habitante(nome, nova_idade)
        print(f"Habitante '{nome}' atualizado com sucesso.")

    def update_localizacao(self):
        cidade = input("Cidade: ")
        novo_num_habitantes = int(input("Novo número de habitantes: "))
        self.lotr_model.update_localizacao(cidade, novo_num_habitantes)
        print(f"Localização '{cidade}' atualizada com sucesso.")

    def delete_habitante(self):
        nome = input("Nome do habitante a ser deletado: ")
        self.lotr_model.delete_habitante(nome)
        print(f"Habitante '{nome}' deletado com sucesso.")

    def delete_localizacao(self):
        cidade = input("Cidade a ser deletada: ")
        self.lotr_model.delete_localizacao(cidade)
        print(f"Localização '{cidade}' deletada com sucesso.")

    def drop_db(self):
        db.drop_all()
        print("Banco de dados limpo.")

    def amount_habitantes(self):
        total = self.lotr_model.amount_habitantes()
        print(f"Total de habitantes: {total}")

    def habitante_has_more_traveled(self):
        result = self.lotr_model.habitante_has_more_traveled()
        print(f"Habitante que mais viajou: {result['nome']} ({result['total']} localizações)")

    def most_visited_location(self):
        result = self.lotr_model.most_visited_location()
        print(f"Localização mais visitada: {result['cidade']} ({result['total']} visitas)")

    def run(self):
        super().run()
