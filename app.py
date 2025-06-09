from flask import Flask, render_template, request, jsonify
from src.operations.suma import sumar
from src.operations.resta import restar
from src.operations.multiplicacion import multiplicar

app = Flask(__name__)

@app.route("/sumar", methods=["GET"])
def sumar_endpoint():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    resultado = sumar(a, b)
    return jsonify({"mensaje": f"El resultado de {a} + {b} es: {resultado}"})

@app.route("/restar", methods=["GET"])
def restar_endpoint():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    resultado = restar(a, b)
    return jsonify({"mensaje": f"El resultado de {a} - {b} es: {resultado}"})

@app.route("/multiplicar", methods=["GET"])
def multiplicar_endpoint():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    resultado = multiplicar(a, b)
    return jsonify({"mensaje": f"El resultado de {a} * {b} es: {resultado}"})

@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/calcular", methods=["GET"])
def calcular():
    a = float(request.args.get("a", 0))
    b = float(request.args.get("b", 0))
    op = request.args.get("op")

    if op == "sumar":
        resultado = sumar(a, b)
    elif op == "restar":
        resultado = restar(a, b)
    elif op == "multiplicar":
        resultado = multiplicar(a, b)
    else:
        resultado = "Operación inválida"

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

