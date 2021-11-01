from flask import Flask, render_template, redirect, request, session, url_for

app = Flask(__name__)
app.secret_key = "abcd1234"
@app.route("/") 
def welcome():
    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        session["user"] = email
        return redirect(url_for("CVS"))
    else:
        return "bad request"

@app.route("/CVS") 
def CVS():
    if "user" in session:
        return render_template("CVS.html")
    else:
        return "No tiene permisos"

@app.route("/ana.conchac") 
def CV():
    return render_template("CV.html")

@app.route("/nicolas.santibañezv") 
def CV1():
    return render_template("CV1.html")

@app.route("/antonio.betancourts") 
def CV2():
    return render_template("CV2.html")

@app.route("/logout") 
def logout():
    session.clear()
    return redirect(url_for("welcome"))

if __name__ == "__main__":
    app.run(debug=True)
