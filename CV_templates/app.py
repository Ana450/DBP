from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/") #decorador: definimos una ruta(extiende la funcionalidad)
def welcome():
    return render_template("vista.html")

@app.route("/CV") #decorador: definimos una ruta(extiende la funcionalidad)
def CV():
    return render_template("CV.html")
