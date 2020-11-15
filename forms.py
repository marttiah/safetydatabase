from db import db
import users

def form(aedescription, reporter, product, patient):
    username = users.username()
    if username == 0:
        return False
    sql =  "INSERT INTO adrs (aedescription, reporter, product, patient) VALUES (:aedescription, :reporter, :product, :patient)"
    db.session.execute(sql, {"aedescription":aedescription, "reporter":reporter, "product":product, "patient":patient})
    db.session.commit()
    return True

def numberofforms():
    result = db.session.execute("SELECT COUNT (*) FROM adrs")
    count = result.fetchone()[0]

def linelisting():
    result = db.session.execute("SELECT aedescription, reporter, product, patient FROM adrs")
    adrs = result.fetchall()
    
