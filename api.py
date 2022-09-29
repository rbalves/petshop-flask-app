from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

@app.route("/animais")
def hello_world():
    animais = []
    with open('animais.csv', newline='') as ficheiro:
        for row in csv.reader(ficheiro):
            animais.append({"nome": row[0], "peso": row[1], "idade": row[2]})
    return render_template('animais.html', animais=animais)

@app.route("/animais/novo")
def formulario():
    return render_template('cadastro.html')

@app.route("/cadastro")
def cadastro():
    with open('animais.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow([request.args.get('nome'), request.args.get('peso'), request.args.get('idade')])
    return redirect('animais')