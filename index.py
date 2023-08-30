from flask import Flask, render_template, request, redirect, url_for, flash, session
from Utils.tree import tree
from Utils.rw_data import get_data


app = Flask(__name__)

# Se agrega la carpeta estatica
app._static_folder = 'static'

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        try:
            tolerancia = float(request.form['tolerancia'])
            if 0 <= tolerancia <= 1:
                resultado_tree = tree(tolerancia)
                return render_template('index.html', tree_result = resultado_tree)
            else:
                error = "El valor de tolerancia debe estar entre 0 y 1"
                return render_template('index.html', error = error)
        except:
            error = "El valor de tolerancia debe ser un numero"
            return render_template('index.html', error = error)
    else:
        
        return render_template('index.html')

@app.route('/alumnos_primero')

def alumnos_primero():
    return render_template('alum_p.html', data = get_data("Resource\data.xlsx")[0].values.tolist())

@app.route('/hello')

def hello():
    return 'Hello world'


if __name__ == '__main__':
    app.run(port=8000)

