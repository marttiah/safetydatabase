from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login",methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    sql = "SELECT password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone() 
    if user == None:
        return render_template("error.html",error="Invalid username")
    else:
        hash_value = user[0]
    if check_password_hash(hash_value,password):
        session["username"] = username
        return redirect("/main")
    else:
        return render_template("error.html", error="Invalid password")

@app.route("/logout")
def logout():
    del session["username"]
    return redirect("/")

@app.route("/main")
def main():
    return render_template("main.html") 

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/result", methods=["POST"])
def result():
#    name = request.form["name"]
 #   email = request.form["email"]
  #  phone = request.form["phone"]
   # seriousness = request.form["seriousness"]
    #seriousnesslevel = request.form["seriousnesslevel"] 
    ###name, email, phone, seriousness, seriousnesslevel,
    ###:name, :email, :phone, :seriousness, :seriousnesslevel, 
    ###"name":name, "email":email, "phone":phone, "seriousness":seriousness, "seriousnesslevel":seriousnesslevel, 
    aedescription = request.form["aedescription"]
    reporter = request.form["reporter"]
    product = request.form["product"]
    patient =request.form["patient"]
    sql =  "INSERT INTO adrs (aedescription, reporter, product, patient) VALUES (:aedescription, :reporter, :product, :patient)"
    db.session.execute(sql, {"aedescription":aedescription, "reporter":reporter, "product":product, "patient":patient})
    db.session.commit()
    return render_template("result.html")

@app.route("/information")
def information():
    result = db.session.execute("SELECT COUNT(*) FROM adrs")
    count = result.fetchone()[0]
    result = db.session.execute("SELECT aedescription, reporter, product, patient FROM adrs")
    adrs = result.fetchall()
    return render_template("information.html", count=count, adrs=adrs) 