#1 - Criando as pessoas que compões a família
#CREATE(:Pessoa:Estudante{name:'Gabriel',idade:22,sexo:'M'}),
#(:Pessoa:Turismologa{name:'Fabiana',idade:43,sexo:'F'}),
#(:Pessoa:Engenheiro{name:'Vinicius',idade:40,sexo:'M'}),
#(:Pessoa:Aposentado{name:'Cesar',idade:73,sexo:'M'}),
#(:Pessoa:DonaDeCasa{name:'Lucia',idade:68,sexo:'F'}), 
#(:Pessoa:Aposentado{name:'Ruben',idade:70,sexo:'M'}), 
#(:Pessoa:DonaDeCasa{name:'Rosangela',idade:66,sexo:'F'}), 
#(:Pessoa:Escrevente{name:'Romero',idade:46,sexo:'M'}),
#(:Pessoa:Gerente{name:'Ana Carolina',idade:43,sexo:'F'}), 
#(:Pessoa:Estudante{name:'Lucas',idade:10,sexo:'M'})

#2 - Criando relacionamentos
#MATCH(g:Pessoa{name:'Gabriel'}),(f:Pessoa{name: 'Fabiana'}) CREATE (f) -[:PAI_MAE_DE]-> (g)
#MATCH(g:Pessoa{name:'Gabriel'}),(v:Pessoa{name: 'Vinicius'}) CREATE (v) -[:PAI_MAE_DE]-> (g)
#MATCH(g:Pessoa{name:'Gabriel'}),(l:Pessoa{name: 'Lucas'}) CREATE (l) <-[:PRIMO_DE]- (g)
#MATCH(g:Pessoa{name:'Gabriel'}),(l:Pessoa{name: 'Lucas'}) CREATE (l) -[:PRIMO_DE]-> (g)
#MATCH(g:Pessoa{name:'Gabriel'})-[pd:PRIMO_DE]->(l:Pessoa{name: 'Lucas'}) SET pd.grau = 1
#MATCH(g:Pessoa{name:'Gabriel'})<-[pd:PRIMO_DE]-(l:Pessoa{name: 'Lucas'}) SET pd.grau = 1
#MATCH(f:Pessoa{name: 'Fabiana'}),(v:Pessoa{name: 'Vinicius'}) CREATE (v) <-[:CASADO_COM]- (f)
#MATCH(f:Pessoa{name: 'Fabiana'}),(v:Pessoa{name: 'Vinicius'}) CREATE (v) -[:CASADO_COM]-> (f)
#MATCH(r:Pessoa{name: 'Ruben'}),(rg:Pessoa{name: 'Rosangela'}) CREATE (r) -[:CASADO_COM]-> (rg)
#MATCH(r:Pessoa{name: 'Ruben'}),(rg:Pessoa{name: 'Rosangela'}) CREATE (r) <-[:CASADO_COM]- (rg)
#MATCH(c:Pessoa{name: 'Cesar'}),(l:Pessoa{name: 'Lucia'}) CREATE (c) -[:CASADO_COM]-> (l)
#MATCH(c:Pessoa{name: 'Cesar'}),(l:Pessoa{name: 'Lucia'}) CREATE (c) <-[:CASADO_COM]- (l)
#MATCH(r:Pessoa{name: 'Romero'}),(c:Pessoa{name: 'Ana Carolina'}) CREATE (c) <-[:CASADO_COM]- (r)
#MATCH(r:Pessoa{name: 'Romero'}),(c:Pessoa{name: 'Ana Carolina'}) CREATE (c) -[:CASADO_COM]-> (r)
#MATCH(g:Pessoa{name:'Gabriel'}),(f:Pessoa{name: 'Fabiana'}) CREATE (f) -[:PAI_MAE_DE]-> (g)
#MATCH(l:Pessoa{name:'Lucia'}),(v:Pessoa{name: 'Vinicius'}) CREATE (l) -[:PAI_MAE_DE]-> (v)
#MATCH(l:Pessoa{name:'Lucia'}),(a:Pessoa{name: 'Ana Carolina'}) CREATE (l) -[:PAI_MAE_DE]-> (a)
#MATCH(c:Pessoa{name:'Cesar'}),(v:Pessoa{name: 'Vinicius'}) CREATE (c) -[:PAI_MAE_DE]-> (v)
#MATCH(c:Pessoa{name:'Cesar'}),(a:Pessoa{name: 'Ana Carolina'}) CREATE (c) -[:PAI_MAE_DE]-> (a)
#MATCH(r:Pessoa{name:'Ruben'}),(f:Pessoa{name: 'Fabiana'}) CREATE (r) -[:PAI_MAE_DE]-> (f)
#MATCH(r:Pessoa{name:'Rosangela'}),(f:Pessoa{name: 'Fabiana'}) CREATE (r) -[:PAI_MAE_DE]-> (f)
#MATCH(r:Pessoa{name:'Romero'}),(l:Pessoa{name: 'Lucas'}) CREATE (r) -[:PAI_MAE_DE]-> (l)
#MATCH(a:Pessoa{name:'Ana Carolina'}),(l:Pessoa{name: 'Lucas'}) CREATE (a) -[:PAI_MAE_DE]-> (l)
#MATCH(a:Pessoa{name:'Ana Carolina'}),(v:Pessoa{name: 'Vinicius'}) CREATE (v) -[:IRMAO_DE]-> (a)
#MATCH(a:Pessoa{name:'Ana Carolina'}),(v:Pessoa{name: 'Vinicius'}) CREATE (v) <-[:IRMAO_DE]- (a)

from neo4j import GraphDatabase
from neo4j.exceptions import ServiceUnavailable

uri = "neo4j+s://aacc6f30.databases.neo4j.io"
user = "neo4j"
password = "OAz9vDafAm2yz9hUQ4lIDT4nrn-an7CKZlVbO7dG6AI"
driver = GraphDatabase.driver(uri, auth=(user, password))

# Função 1: Consulta quem é engenheiro
def consulta_engenheiro(tx):
    query = """
        MATCH(p:Pessoa:Engenheiro) 
        RETURN p.name AS nome, p.idade AS idade, p.sexo AS sexo
    """
    result = tx.run(query)
    for row in result:
        print(f"Nome: {row['nome']}, Idade: {row['idade']}, Sexo: {row['sexo']}")

# Função 2: Consulta quem é o pai de uma pessoa específica
def consulta_pai(tx, nome_filho):
    query = """
        MATCH(p:Pessoa)-[:PAI_MAE_DE]->(filho:Pessoa{name: $nome_filho}) 
        RETURN p.name AS nome, p.sexo AS sexo
    """
    result = tx.run(query, nome_filho=nome_filho)
    for row in result:
        print(f"Pai/Mãe: {row['nome']}, Sexo: {row['sexo']}")

# Função 3: Consulta pessoas com idade maior ou igual a 60 anos
def consulta_idade(tx):
    query = """
        MATCH(p:Pessoa) 
        WHERE p.idade >= 60 
        RETURN p.name AS nome, p.idade AS idade
    """
    result = tx.run(query)
    for row in result:
        print(f"Nome: {row['nome']}, Idade: {row['idade']}")

# Cliente de consulta
def cliente():
    while True:
        print("\n--- Menu ---")
        print("1 - Quem da família é engenheiro")
        print("2 - Quem é o pai de uma pessoa em específico")
        print("3 - Quem tem idade maior ou igual a 60")
        print("4 - Encerrar o código")
        
        opcao = input("Escolha uma opção: ")
        
        with driver.session() as session:
            if opcao == '1':
                session.execute_read(consulta_engenheiro)
            elif opcao == '2':
                nome_filho = input("Digite o nome da pessoa para encontrar o pai/mãe: ")
                session.execute_read(consulta_pai, nome_filho)
            elif opcao == '3':
                session.execute_read(consulta_idade)
            elif opcao == '4':
                print("Encerrando o programa.")
                break
            else:
                print("Opção inválida, tente novamente.")

# Executa o cliente
cliente()

driver.close()
