from db import db
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash
from os import urandom

def login(username, password):
    session["csrf_token"] = os.urandom(16).hex()
    sql = "SELECT password, id FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone() 
    if user == None:
        return False
    else:
        if check_password_hash(user[0],password):
            session["username"] = user[1]
            return True
        else:
             return False

def logout():
    del session["username"]

def register(username,password):
    hash_value = generate_password_hash(password)
    try:
        sql = "INSERT INTO users (username, password) VALUES (:username,:password)"
        db.session.execute(sql, {"username": username,"password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username,password)

def username():
    return session.get("username",0)

def is_admin():
    sql = "SELECT role FROM users WHERE id == user_id"
    result = db.session.execute(sql, {"role":role})
    #if role = 'admin'
    if result.fetchone() != None:
        allow = True
        
def is_user():
    sql = "SELECT role FROM users WHERE id == user_id"
    result = db.session.execute(sql, {"role":role})
    #if role = 'user'
    if result.fetchone() != None:
        allow = True
