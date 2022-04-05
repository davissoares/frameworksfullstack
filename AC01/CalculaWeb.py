from flask import Flask, render_template, request
from Testes import Somar, Subtrair, Multiplicar, Dividir

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/calcular', methods=['POST', 'GET'])
def calcular():
    v1 = request.form['v1']
    v2 = request.form['v2']
    operador = request.form['operador']

    if (operador == "soma"):
        resultado = Somar.calculo(int(v1), int(v2))

    elif (operador == "subtração"):
        resultado = Subtrair.calculo(int(v1), int(v2))

    elif (operador == "multiplicação"):
        resultado = Multiplicar.calculo(int(v1), int(v2))

    elif (operador == "divisão"):
        if (int(v1) == 0):
            return ("Não é possível dividir por 0")
        else:
            resultado = Dividir.calculo(int(v1), int(v2))

    return str(resultado)


if __name__ == "__main__":
    app.run(debug=True)
