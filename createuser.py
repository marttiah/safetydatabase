from flask import Flask
from flask import redirect, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from os import getenv
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
app.secret_key = getenv("SECRET_KEY")
db = SQLAlchemy(app)


username = input("Username: ")
password = input("Password: ")

hash_value = generate_password_hash(password)
sql = "INSERT INTO users (username,password) VALUES (:username,:password)"
db.session.execute(sql, {"username":username,"password":hash_value})
db.session.commit()