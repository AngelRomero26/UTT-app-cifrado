from flask import Flask, jsonify, request, render_template
from crypto import cifrar_aes, cifrar_rsa, hash_sha256

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/procesar", methods=["POST"])
def procesar():
    data = request.json
    texto = data.get("texto")
    modo = data.get("modo")

    if not texto:
        return jsonify({"error": "No se envió texto."})

    if modo == "aes":
        resultado = cifrar_aes(texto)
    elif modo == "rsa":
        resultado = cifrar_rsa(texto)
    elif modo == "sha256":
        resultado = hash_sha256(texto)
    else:
        return jsonify({"error": "Modo no válido"}), 400

    return jsonify({
        "texto_original": texto,
        "modo": modo,
        "resultado": resultado
    })

if __name__ == "__main__":
    app.run(debug=True)

