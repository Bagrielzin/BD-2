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


class BookCLI(SimpleCLI):
    def __init__(self, book_model):
        super().__init__()
        self.book_model = book_model
        self.add_command("create", self.create_book)
        self.add_command("read", self.read_book)
        self.add_command("update", self.update_book)
        self.add_command("delete", self.delete_book)

    def create_book(self):
        titulo = input("Entre com o título: ")
        autor = input("Entre com o nome do autor: ")
        ano = int(input("Entre com o ano: "))
        preco = float(input("Entre com o preco: "))
        self.book_model.create_book(titulo, autor, ano, preco)

    def read_book(self):
        id = input("Enter the id: ")
        book = self.book_model.read_book_by_id(id)
        if book:
            print(f"Titulo: {book['titulo']}")
            print(f"Autor: {book['autor']}")
            print(f"Ano: {book['ano']}")
            print(f"Preco: {book['preco']}")

    def update_book(self):
        id = input("Enter the id: ")
        titulo = input("Entre com novo título: ")
        autor = input("Entre com o novo nome do autor: ")
        ano = int(input("Entre com o novo ano: "))
        preco = float(input("Entre com o novo preco: "))
        self.book_model.update_book(id, titulo, autor, ano, preco)

    def delete_book(self):
        id = input("Enter the id: ")
        self.book_model.delete_book(id)
        
    def run(self):
        print("Welcome to the book CLI!")
        print("Available commands: create, read, update, delete, quit")
        super().run()
        