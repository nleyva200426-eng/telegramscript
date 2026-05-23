import threading
from perfil1 import start
from flask import Flask, render_template_string

app = Flask(__name__)

def funcion_background():
    pass

HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MANCOS DE DOTA 2</title>

    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: Arial, sans-serif;
        }

        body {
            background: linear-gradient(135deg, #0f0f0f, #1d1d1d);
            color: white;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 40px;
            border-radius: 20px;
            background: rgba(255,255,255,0.05);
            backdrop-filter: blur(10px);
            box-shadow: 0 0 30px rgba(255,0,0,0.3);
            width: 90%;
            max-width: 900px;
        }

        h1 {
            font-size: 4rem;
            color: #ff3b3b;
            margin-bottom: 20px;
            text-shadow: 0 0 15px rgba(255,0,0,0.7);
        }

        p {
            font-size: 1.3rem;
            margin-bottom: 20px;
            color: #d6d6d6;
        }

        .cards {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }

        .card {
            background: rgba(255,255,255,0.08);
            border-radius: 15px;
            padding: 20px;
            transition: 0.3s;
            border: 1px solid rgba(255,255,255,0.1);
        }

        .card:hover {
            transform: translateY(-5px) scale(1.03);
            box-shadow: 0 0 20px rgba(255,0,0,0.5);
        }

        .rank {
            font-size: 2rem;
            margin-bottom: 10px;
        }

        .btn {
            margin-top: 30px;
            display: inline-block;
            padding: 15px 30px;
            border-radius: 12px;
            background: #ff3b3b;
            color: white;
            text-decoration: none;
            font-weight: bold;
            transition: 0.3s;
        }

        .btn:hover {
            background: #ff0000;
            transform: scale(1.05);
        }

        footer {
            margin-top: 35px;
            opacity: 0.6;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>MANCOS DE DOTA 2</h1>

    <p>
        Bienvenido al salón oficial de los supports que no compran wards,
        los carries 0/15 y los mid que pierden contra Techies.
    </p>

    <div class="cards">
        <div class="card">
            <div class="rank">🤡</div>
            <h2>Herald Supremo</h2>
            <p>Farmear 40 minutos para perder igual.</p>
        </div>

        <div class="card">
            <div class="rank">💀</div>
            <h2>Feeder Profesional</h2>
            <p>Muere antes de poner un solo stun.</p>
        </div>

        <div class="card">
            <div class="rank">🔥</div>
            <h2>Tóxico Legendario</h2>
            <p>"GG END MID" minuto 3.</p>
        </div>
    </div>

    <a class="btn" href="#">
        REPORTAR MANCOS
    </a>

    <footer>
        Powered by Tilt + Café + Ranked Perdidas
    </footer>
</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":

    thread = threading.Thread(target=start, daemon=True)
    thread.start()

    print("SCRIPT ACTIVADO")

    app.run(host="0.0.0.0", port=5000, debug=False)
    print("Server on http://0.0.0.0:5000")

# def per2 ():
# 	os.system("python perfil2.py")
#
# def per3 ():
# 	os.system("python perfil3.py")
#
# def per4 ():
# 	os.system("python perfil4.py")
#
# def per5 ():
# 	os.system("python perfil5.py")
#
# def per6 ():
# 	os.system("python perfil6.py")
#
# def per7 ():
# 	os.system("python perfil7.py")
#
# def per8 ():
# 	os.system("python perfil8.py")
#
# def per9 ():
# 	os.system("python perfil9.py")
#
# def per10 ():
# 	os.system("python perfil10.py")
