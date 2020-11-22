from app import app
from flask import render_template, request, redirect
import users, forms

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html") 

@app.route("/information")
def information():
    count = forms.numberofforms()
    linelisting = forms.linelisting()
    return render_template("information.html", count=count, linelisting=linelisting)

@app.route("/login", methods=["get","post"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username,password):
            return redirect("/main")
        else:
            return render_template("error.html",error="Wrong username or password")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["get","post"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username,password):
            return redirect("/")
        else:
            return render_template("error.html",error="Registration was unsuccessful")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/send", methods=["POST"])
def send():
        aedescription = request.form["aedescription"]
        reporter = request.form["reporter"]
        product = request.form["product"]
        patient = request.form["patient"]
        if forms.send(aedescription, reporter, product, patient):
            return render_template("result.html")
        else:
            return render_template("error.html",message="The submission of the form was unsuccessful.")
