from flask import Flask, render_template
from utils.lol_parser import get_all_perso_from_lol  # Importation depuis utils.lol_parser

app = Flask(__name__)

# Route pour afficher la liste des personnages
@app.route('/')
def index():
    personnages = get_all_perso_from_lol()
    return render_template('index.html', personnages=personnages)

if __name__ == '__main__':
    app.run(debug=True)