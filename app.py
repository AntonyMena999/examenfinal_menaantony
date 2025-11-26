from flask import Flask, Response, jsonify, request

app = Flask(__name__)


# ------------------------ #
#     CALCULADORA SIMPLE   #
# ------------------------ #
def sumar(a, b):
    return a + b


@app.route("/api/suma", methods=["GET"])
def api_suma():
    """
    Endpoint para sumar dos números: /api/suma?a=5&b=3
    """
    try:
        a = float(request.args.get("a"))
        b = float(request.args.get("b"))
        return jsonify({"resultado": sumar(a, b)})
    except Exception:
        return jsonify({"error": "Parámetros inválidos"}), 400


# ------------------------ #
#       PÁGINA HTML        #
# ------------------------ #
@app.route("/")
def home():
    html = """
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Página Bonita con Flask</title>
        <style>
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #1f1c2c, #928dab);
                color: white;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                height: 100vh;
                text-align: center;
            }
            h1 {
                font-size: 3em;
                margin-bottom: 10px;
                background: -webkit-linear-gradient(#00eaff, #9d00ff);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                animation: glow 3s ease-in-out infinite alternate;
            }
            @keyframes glow {
                from { text-shadow: 0 0 10px #00eaff; }
                to { text-shadow: 0 0 30px #9d00ff; }
            }
            p {
                font-size: 1.2em;
                max-width: 600px;
            }
            button {
                margin-top: 25px;
                background-color: #00eaff;
                border: none;
                color: #111;
                padding: 15px 30px;
                border-radius: 25px;
                font-size: 1em;
                cursor: pointer;
                transition: transform 0.3s, background-color 0.3s;
            }
            button:hover {
                background-color: #9d00ff;
                color: white;
                transform: scale(1.1);
            }
        </style>
    </head>
    <body>
        <h1>✨ EXAMEN MENA ANTONY:) ✨</h1>
        <p>Esta es una página moderna de Exámen y elegante creada completamente dentro de Flask.</p>
        <button onclick="alert('¡Gracias por visitar! 😊')">Haz clic aquí</button>
    </body>
    </html>
    """
    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
