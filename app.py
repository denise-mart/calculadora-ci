from flask import Flask, request, jsonify
from src.operations.suma import sumar

app = Flask(__name__)

@app.route("/sumar", methods=["GET"])
def sumar_endpoint():
    try:
        a = float(request.args.get("a", 0))
        b = float(request.args.get("b", 0))
        resultado = sumar(a, b)
        mensaje = f"El resultado de {a} + {b} es: {resultado}"
        return jsonify({"mensaje": mensaje})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
