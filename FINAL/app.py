from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route("/") #decorador: definimos una ruta(extiende la funcionalidad)
def welcome():
    return render_template("login.html")

@app.route("/CV") #decorador: definimos una ruta(extiende la funcionalidad)
def CV():
    return render_template("CV.html")

@app.route("/CV1") #decorador: definimos una ruta(extiende la funcionalidad)
def CV1():
    return render_template("CV1.html")

@app.route("/CV2") #decorador: definimos una ruta(extiende la funcionalidad)
def CV2():
    return render_template("CV2.html")