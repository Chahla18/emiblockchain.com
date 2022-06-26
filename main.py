from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route('/',methods=['POST','GET'])
def index(expediteur=None ,recepteur=None,montant=None):
    if request.method == 'POST':
        expediteur == request.form.get('expediteur')
        recepteur == request.form.get('recepteur')
        montant == request.form.get('montant')
        print(expediteur)
        print(recepteur)
        print(montant)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



