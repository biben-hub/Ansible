from flask import Flask, request, render_template
from db import *

# db = DatabaseConnection()

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])#renvoie le template de bienvenue
def get_index():
    return render_template("index.html")

# @app.route('/inc')#incrément l'id dans la bdd


# @app.route('/id')#renvoie l'id en cours

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=3000, debug=True)