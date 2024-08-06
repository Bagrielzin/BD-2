#classe professor
class Professor:
    #construtor do professor
    def __init__(self, nome):
        self.nome = nome

    #método ministrar aula do professor
    def ministrar_aula(self, assunto):
        print(f'O professor {self.nome} está ministrando uma aula sobre {assunto}')

#classe aluno
class Aluno:
    #construtor do aluno
    def __init__(self, nome):
        self.nome = nome

    #método de presença do aluno
    def presenca(self):
        print(f'O aluno {self.nome} está presente')

#classe aula
class Aula:
    #construtor da aula
    def __init__(self, professor, assunto, alunos):
        self.professor = professor
        self.assunto = assunto
        self.alunos = alunos

    #método de adicionar aluno
    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    #método de listar presença
    def listar_presenca(self):
        print(f'Presença na aula sobre {self.assunto}, ministrada pelo professor {self.professor.nome}:')
        #varrendo a lista de alunos e mostrando os que estão presentes
        for aluno in self.alunos:
            aluno.presenca()

#instanciando um professor e 2 alunos
professor = Professor("Lucas")
aluno1 = Aluno("Maria")
aluno2 = Aluno("Pedro")
alunos = []

#instanciando uma aula ainda sem alunos
aula = Aula(professor, "Programação Orientada a Objetos", alunos)

#adicionando alunos na aula
aula.adicionar_aluno(aluno1)
aula.adicionar_aluno(aluno2)

#mostrando as informações da aula
aula.listar_presenca()
