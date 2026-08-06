# CRIANDO UMA AGENDA
import sqlite3, time
conectar = sqlite3.connect('agenda.db')
c = conectar.cursor()

# Criando o banco de dados
def criar_db():
    c.execute("""CREATE TABLE IF NOT EXISTS cadastro (
              nome TEXT,
              telefone VARCHAR(20),
              email TEXT,
              data TEXT
              )
        """)

try:
    criar_db()
except:
    print('Erro ao criar o banco de dados')
else:
    print('Banco de dados criado com sucesso')

def inserir(n, t, e):
    d = time.strftime('%d/%m/%y')
    c.execute("INSERT INTO cadastro(nome, telefone, email, data) VALUES(?, ?, ?, ?)", (n, t, e, d))
    conectar.commit()


# Solicitando o casdastro ou pesquisa
def pesquisar(p):
    sql = 'SELECT * FROM cadastro WHERE nome = ?'
    for row in c.execute(sql, (p,)):
        print(row)

fc = int(input(' == O que deseja fazer? == \n1 - Cadastrar  2 - Pesquesar?\n'))
if fc == 1:
    try:
        print('Cadastro da Agenda')
        time.sleep(2)
        n = str(input('Digite seu nome: '))
        t = int(input('Digite seu número: '))
        e = str(input('Digite um email: '))
        inserir(n, t, e)

    except:
        print('ERRO ao cadastra!')
    else:
        print('Cadastrado com sucesso')

elif fc == 2:
    print('Buscando!!')
    time.sleep(1)
    p = str(input("Digite seu nome a ser buscado: "))
    pesquisar(p)
else:
    print('...')
        
    
