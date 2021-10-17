from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") #decorador: definimos una ruta(extiende la funcionalidad)
def welcome():
    return render_template("uno.html")

@app.route("/CV", methods=["POST"]) #decorador: definimos una ruta(extiende la funcionalidad)
def CV():
    name = request.form.get("name")
    return render_template("CV.html",name=name)
