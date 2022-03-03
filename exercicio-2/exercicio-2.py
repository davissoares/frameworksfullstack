import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False


#Criar Conexão com Banco MySQL
conexao = mysql.connector.connect(database='db_usuario', user='root', password='dsoares04')
criar_tabela_sql = """CREATE TABLE IF NOT EXISTS tb_usuarios(
                        id int(11) NOT NULL AUTO_INCREMENT,
                        nome VARCHAR(255) NOT NULL,
                        email VARCHAR(200) NOT NULL,
                        senha VARCHAR(255) NOT NULL,
                        PRIMARY KEY (id))"""


cursor = conexao.cursor()
cursor.execute(criar_tabela_sql)
print("Tabela criada com sucesso!")


@app.route('/')
def main():
    return render_template('login.html')


@app.route('/usuarios.html')
def lista():
    return render_template('usuarios.html')


@app.route("/adicionar_usuario", methods=['POST', 'GET'])
def incluir_usuario():
    cursor = conexao.cursor()
    nome = request.form['nome']
    email = request.form['email']
    senha = request.form['senha']
    cursor.execute("""INSERT INTO tb_usuarios(nome, email, senha) VALUES(%s, %s, %s)""", (nome, email, senha))
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('login.html')


@app.route("/listar_usuario", methods=['POST', 'GET'])
def listar_usuario():
    consulta_bd = "select * from tb_usuarios"
    cursor = conexao.cursor()
    cursor.execute(consulta_bd)
    details = cursor.fetchall()
    print("Quantidade de registros: ", cursor.rowcount)

    for x in range(len(details)):
        print(details[x])
    conexao.commit()
    cursor.close()
    conexao.close()
    return render_template('usuarios.html')


if __name__ == '__main__':
    app.run(host='localhost', port=5003, debug=True)
