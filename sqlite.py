# Bancos de dados SQLITE
import sqlite3
import pandas as pd

con = sqlite3.connect("teste.db")
cur = con.cursor()

# Apaga a tabela antiga (se existir)
cur.execute("DROP TABLE IF EXISTS pessoas")
            
# Cria a tebela
def create_table():
    cur.execute(
        """CREATE TABLE IF NOT EXISTS pessoas (
        id INTEGER,
        Nome TEXT,
        Idade INTEGER,
        Cidade TEXT,
        Numero INTEGER,
        Rua TEXT
        )
    """)

create_table()

# Ensere dados
def inserirdados():
    cur.execute("INSERT INTO pessoas (Nome, Idade, Cidade, Rua, Numero) VALUES (?, ?, ?, ?, ?)", ("Marcos", 30, "Aveiro", "Avenida Guilheme correia", 15))
    cur.execute("INSERT INTO pessoas (Nome, Idade, Cidade, Rua, Numero) VALUES (?, ?, ?, ?, ?)", ("Ana", 25, "Santarém", "Abrel frazão", 56))
    con.commit()
inserirdados()
            
#consulta
cur.execute("SELECT * FROM pessoas")
dados = cur.fetchall()
df = pd.DataFrame(dados, columns=["id", "Nome", "Idade", "Cidade", "Rua", "Numero"])
print(df)


# Consultando Nome e o Cidade
sql = 'SELECT * FROM pessoas WHERE nome = ?'

def ler_dados(vlrbusca):
    for row in cur.execute(sql, (vlrbusca,)):
        print(row)
ler_dados('Marcos')
              
# Fecha a conexão
con.close()

