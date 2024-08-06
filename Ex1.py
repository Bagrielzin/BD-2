#classe professor
class Professor:
    #construtor do professor
    def __init__(self, nome):
        self.nome = nome

    #m�todo ministrar aula do professor
    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} est� ministrando uma aula sobre {assunto}')

#classe aluno
class Aluno:
    #construtor do aluno
    def __init__(self, nome):
        self.nome = nome

    #m�todo de presen�a do aluno
    def presenca(self):
        print(f'O aluno {self.nome} est� presente')

#classe aula
class Aula:
    #construtor da aula
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    #m�todo de adicionar aluno
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    #m�todo de listar presen�a
    def listar_presenca(self):
        print(f'Presen�a na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        #varrendo a lista de alunos e mostrando os que est�o presentes
        for aluno in self.alunos:
            aluno.presenca()

#instanciando um professor e 2 alunos
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
alunos = []

#instanciando uma aula ainda sem alunos
aula = Aula(professor, "Programa��o Orientada a Objetos", alunos)

#adicionando alunos na aula
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

#mostrando as informa��es da aula
aula.listar_presenca()
