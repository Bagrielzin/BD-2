'''
Nessa atividade você deve usar seus conhecimentos sobre banco de dados baseados em colunos e chave-valor, mais especificamente sobre Cassandra e Redis para atender os requisitos pedidos.
Todos as questões tem um exemplo de caso de teste (com dados de entrada e saída esperada) para que você valide a sua solução.

Contexto: Imagine que você está desenvolvendo um banco de dados para uma loja online. Essa loja tem um volume muito grande de vendas e por isso foram escolhidos sistemas de gerenciamento de bancos de dados NoSQL. Os principais objetivos do sistema são: 
i) exibir uma lista de produtos mais recomendados para um determinado usuário; 
ii) armazenar temporariamente as informações de produtos no carrinho; e 
iii) registrar as informações de uma venda efetivada.

Para manter as informações das vendas realizadas de forma persistente e distribuída, a tabela de vendas, produtos e usuários foram registrados no Cassandra. 
Apesar de ter um esquema flexível, considere as seguintes informações:
    . Usuário (id: int, estado: text, cidade: text, endereço: text, nome: text, email: text, interesses: list<text>)
    . Produto (id: int, categoria: text, nome: text, custo: int, preco: int, quantidade: int)
    . Venda (id: int, dia: int, mês: int, ano: int, hora: text, valor: int, produtos: list<map<int, int>>, usuario: map<text, text>)
Os dados de usuários devem ser particionados pelo estado e cidade, usando o id para complementar a idenficação.
Produtos devem ser agrupadors por categoria, também usando id para ordenar os produtos em uma mesma partição.
Por fim, os dados das vendas devem ser particionados por dia, mês e ano, usando a hora e o id para complementar a idenficação de uma venda.

A fim de manter consultas rápidas, algumas informações do usuário, suas preferências e seus produtos em carrinho são mantidas no Redis.

---------------------------------------------------------------------------------------------------------------

(20 pontos) Questão 1)
Crie as tabelas e registe as informações dos seguintes usuários e produtos no Cassandra e realize a consutla no Cassandra para apresentar:
a) a quantidade de usuários registrados e 
b) o custo total dos produtos em estoque (obs.: o custo registrado é apenas o custo unitário de cada produto).

    ### Dica: Use valores inteiros ao armazenar os valores monetários no Cassandra (basta multiplicar por 100 na hora de inserir e dividir por 100 quando for apresentar)

(20 pontos) Questão 2)
Carregue do Cassandra as informações de cada um dos usuários do estado de Minas Gerais, incluindo a lista de interesses, registre no Redis e realize a consutla no Redis para apresentar os dados registrados.

(30 pontos) Questão 3) 
Imagine que o usuário 3 acessa o feed dele. Use a lista de interesses desse usuário registrada no Redis para buscar as informações sobre produtos mais interessantes no Cassandra (considere que a lista de interesses contém os nomes das categorias de produtos interessantes).

(10 pontos extras) Questão 4) 
O usuário 3 seleciona alguns produtos para o seu carrinho. Registre essas informações no Redis e realize uma consulta para mostrar os dados cadastrados.

(10 pontos extras) Questão 5)
O usuário 3 efetiva a compra dos produtos em seu carrinho. Realize uma consulta no Redis dos dados do carrinho desse usuário e registre as informações sobre essa venda no Cassandra (considere que a data e a hora vão ser passadas como parâmetro). Por fim recupere e retorne o nome do usuário, a hora e o valor das vendas  realizadas no dia atual registradas no Cassadra.
    ## Dica: Use ALIAS para formatar o retorno. Não esqueça de converter o valor monetário.


'''
import json

from datetime import datetime

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra.query import dict_factory

import redis


# This secure connect bundle is autogenerated when you download your SCB, 
# if yours is different update the file name below
cloud_config= {
  'secure_connect_bundle': 'secure-connect.zip'
}

# This token JSON file is autogenerated when you download your token, 
# if yours is different update the file name below
with open("token.json") as f:
    secrets = json.load(f)

CLIENT_ID = secrets["clientId"]
CLIENT_SECRET = secrets["secret"]

auth_provider = PlainTextAuthProvider(CLIENT_ID, CLIENT_SECRET)
cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
cassandra_session = cluster.connect()
cassandra_session.row_factory = dict_factory # Returning dict from Cassandra
cassandra_session.set_keyspace('ksloja') # Change to your keyspace

redis_conn = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password=1234,
    decode_responses=True
)

# ------------------- !! Attention !! -------------------
redis_conn.flushall() #Clear Redis database 
# -------------------------------------------------------

# Questão 1
def create_tables(self):
    result = CassandraConnector.execute("CREATE TABLE usuarios (id: int, estado: text, cidade: text, endereço: text, nome: text, email: text, interesses: list<text>, primary key((estado,cidade),id))")
    if result is not None:
        print("Sucesso!")

    result = CassandraConnector.execute("CREATE TABLE produtos (id: int, categoria: text, nome: text, custo: int, preco: int, quantidade: int, primary key((categoria),id))")
    if result is not None:
        print("Sucesso!")

    result = CassandraConnector.execute("CREATE TABLE vendas (id: int, dia: int, mês: int, ano: int, hora: text, valor: int, produtos: list<map<int, int>>, usuario: map<text, text>, primary key((dia,mes,ano),hora,id))")
    if result is not None:
        print("Sucesso!")

def questao_1_a(users):
    result = CassandraConnector.execute('BEGIN BATCH '+
        'INSERT INTO usuarios(id,estado,cidade,endereço,nome,email,interesses) VALUES(1,\'Minas Gerais\',\'Santa Rita do Sapucaí\', \'Rua A, 45\', \'Serafim Amarantes\', \'samarantes@g.com\', [\'futebol\', \'pagode\', \'engraçado\', \'cerveja\', \'estética\'])'+
        'INSERT INTO usuarios(id,estado,cidade,endereço,nome,email,interesses) VALUES(2,\'São Paulo\',\'São Bento do Sapucaí\', \'Rua B, 67\', \'Tamara Borges\', \'tam_borges@g.com\', [\'estética\', \'jiujitsu\', \'luta\', \'academia\', \'maquiagem\'])'+
        'INSERT INTO usuarios(id,estado,cidade,endereço,nome,email,interesses) VALUES(3,\'Minas Gerais\',\'Santa Rita do Sapucaí\', \'Rua C, 84\', \'Ubiratã Carvalho\', \'bira@g.com\', [\'tecnologia\', \'hardware\', \'games\', \'culinária\', \'servers\'])'+
        'INSERT INTO usuarios(id,estado,cidade,endereço,nome,email,interesses) VALUES(4,\'Minas Gerais\',\'Pouso Alegre\', \'Rua D, 21\', \'Valéria Damasco\', \'valeria_damasco@g.com\', [\'neurociências\', \'comportamento\', \'skinner\', \'laboratório\', \'pesquisa\'])'+
        'APPLY BATCH;'                            
    )

    result = CassandraConnector.execute("SELECT COUNT (*) FROM usuarios;")
    if result is not None:
        print(result)

def test_questao_1_a():

    users = [
        {"id":1, "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua A, 45", "nome":"Serafim Amarantes", "email":"samarantes@g.com", "interesses": ["futebol", "pagode", "engraçado", "cerveja", "estética"]},
        {"id":2, "estado": "São Paulo", "cidade": "São Bento do Sapucaí", "endereco": "Rua B, 67", "nome":"Tamara Borges", "email":"tam_borges@g.com", "interesses": ["estética", "jiujitsu", "luta", "academia", "maquiagem"]},
        {"id":3, "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua C, 84", "nome":"Ubiratã Carvalho", "email":"bira@g.com", "interesses": ["tecnologia", "hardware", "games", "culinária", "servers"]},
        {"id":4, "estado": "Minas Gerais", "cidade": "Pouso Alegre", "endereco": "Rua D, 21", "nome":"Valéria Damasco", "email":"valeria_damasco@g.com", "interesses": ["neurociências", "comportamento", "skinner", "laboratório", "pesquisa"]}
    ]

    assert len(users) == questao_1_a(users)

def questao_1_b(products):
    result = CassandraConnector.execute("SELECT SUM (preco * quantidade) FROM produtos;")
    if result is not None:
        print(result)

def teste_questao_1_b():
    products = [
        {"id":1, "categoria": "escritório", "nome":"Cadeira HM conforto", "custo": 2000.00, "preco": 3500.00, "quantidade": 120},
        {"id":2, "categoria": "culinária", "nome":"Tábua de corte Hawk", "custo": 360.00, "preco": 559.90, "quantidade": 40},
        {"id":3, "categoria": "tecnologia", "nome":"Notebook X", "custo": 3000.00, "preco": 4160.99, "quantidade": 76},
        {"id":4, "categoria": "games", "nome":"Headset W", "custo": 265.45, "preco": 422.80, "quantidade": 88},
        {"id":5, "categoria": "tecnologia", "nome":"Smartphone X", "custo": 2000.00, "preco": 3500.00, "quantidade": 120},
        {"id":6, "categoria": "games", "nome":"Gamepad Y", "custo": 256.00, "preco": 519.99, "quantidade": 40},
        {"id":7, "categoria": "estética", "nome":"Base Ismusquim", "custo": 50.00, "preco": 120.39, "quantidade": 76},
        {"id":8, "categoria": "cerveja", "nome":"Gutten Bier IPA 600ml", "custo": 65.45, "preco": 122.80, "quantidade": 88}
    ]

    total_cost = 765559.20
    
    assert total_cost == questao_1_b(products)

# Questão 2
def questao_2(state):
    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (1, "escritório", "Cadeira HM conforto", 2000.00, 3500.00, 120))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (2, "culinária", "Tábua de corte Hawk", 360.00, 559.90, 40))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (3, "tecnologia", "Notebook X", 3000.00, 4160.99, 76))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (4, "games", "Headset W", 265.45, 422.80, 88))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (5, "tecnologia", "Smartphone X", 2000.00, 3500.00, 120))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (6, "games", "Gamepad Y", 256.00, 519.99, 40))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (7, "estética", "Base Ismusquim", 50.00, 120.39, 76))

    query = """ INSERT INTO produtos(id, categoria, nome, custo, preco, quantidade) VALUES (%s, %s, %s, %s, %s, %s) """
    cassandra_session.execute(query, (8, "cerveja", "Gutten Bier IPA 600ml", 65.45, 122.80, 88))

    result = CassandraConnector.execute(f"SELECT (*) FROM usuarios WHERE estado = '{state}' ALLOW FILTERING;")
    if result is not None:
        for r in result:
            redis_conn.hset(f"usuario:'{r.id}'", mapping={
                "estado": '{r.estado}',
                "cidade": '{r.cidade}',
                "endereco": '{r.endereco}',
                "nome":'{r.nome}',
                "email": '{r.email}',
                "interesses": '{[r.interesses]}',
            })
    user_keys = redis_conn.keys("usuario:*")
    for u in user_keys:
        redis_conn.hgetall(u)


def test_questao_2():

    state = "Minas Gerais"

    users = [
        {"id":'1', "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua A, 45", "nome":"Serafim Amarantes", "email":"samarantes@g.com", "interesses": ["futebol", "pagode", "engraçado", "cerveja", "estética"]},
        {"id":'3', "estado": "Minas Gerais", "cidade": "Santa Rita do Sapucaí", "endereco": "Rua C, 84", "nome":"Ubiratã Carvalho", "email":"bira@g.com", "interesses": ["tecnologia", "hardware", "games", "culinária", "servers"]},
        {"id":'4', "estado": "Minas Gerais", "cidade": "Pouso Alegre", "endereco": "Rua D, 21", "nome":"Valéria Damasco", "email":"valeria_damasco@g.com", "interesses": ["neurociências", "comportamento", "skinner", "laboratório", "pesquisa"]}
    ]

    assert users == sorted(questao_2(state), key=lambda d: d['id'])


# Questão 3
def questao_3(user_id):
    user = redis_conn.hgetall(f"usuario:'{user_id}'")
    result = CassandraConnector.execute(f"SELECT * FROM produtos WHRE categoria = '{user.interesses}' ALLOW FILTERING;")
    if result is not None:
        for r in result:
            print(r)

def test_questao_3():

    user_id = 3

    products = [
        {"id":2, "nome":"Tábua de corte Hawk", "preco": 559.90},
        {"id":3, "nome":"Notebook X", "preco": 4160.99},
        {"id":4, "nome":"Headset W", "preco": 422.80},
        {"id":5, "nome":"Smartphone X", "preco": 3500.00},
        {"id":6, "nome":"Gamepad Y", "preco": 519.99}
    ]

    assert products == sorted(questao_3(user_id), key=lambda d: d['id'])


# Questão 4
def questao_4(user_id, cart):
    redis_conn.hset(f"usuario:'{user_id}'","interesses",['{cart}'])
    redis_conn.hgetall(f"usuario:'{user_id}'");

def test_questao_4():

    user_id = 3
    
    cart = [
        {"id":'4', "nome":"Headset W", "preco": '422.80', "quantidade": '1'},
        {"id":'6', "categoria": "games", "nome":"Gamepad Y", "preco": '519.99', "quantidade": '2'},
    ]

    assert cart == sorted(questao_4(user_id, cart), key=lambda d: d["id"])

# Questão 5
def questao_5(user_id):
    pass

def test_questao_5():

    user_id = 3
    date_time = datetime.now()

    sales = [{"usuario": 'bira@g.com', 'hora': date_time.strftime("%H:%M"), 'valor': 1462.78}]

    assert sales == questao_5(user_id, date_time)


# cassandra_session.shutdown()
# redis_conn.close()
