from app import app
from flask import render_template, request, redirect
import users, forms
import re

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
            return render_template("error.html",error="Wrong username or password. Please try again.")

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/register", methods=["GET","POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        repassword = request.form["repassword"]

        if repassword != password:
            return render_template("register.html",error="Entered passwords do not match. Please try again.") 
        elif len(password) < 8: 
            return render_template("register.html",error="Entered password is too short. Please try again.")  
        elif not re.search("[a-z]", password): 
            return render_template("register.html",error="Entered password does not include small letters. Please try again.")  
        elif not re.search("[A-Z]", password): 
            return render_template("register.html",error="Entered password does not include capital letters. Please try again.")  
        elif not re.search("[0-9]", password): 
            return render_template("register.html",error="Entered password does not include numbers. Please try again.")  
        elif not re.search("[\s]", password): 
            return render_template("register.html",error="Entered password includes spaces. Please try again.")  
        else:
            if users.register(username,password):
                return redirect("/main")
            else:
                return render_template("error.html",error="Registration was unsuccessful. Please try again.")

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/profile/<int:id>")
def profile(id):
    allow = False
    if is_admin():
        allow = True
    elif is_user() and user_id() == id:
        allow = True
    if not allow:
        return render_template("error.html",error="You do not have the access to this page. Try logging in.")
        
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
