from app import appl
from flask import request
from app.user import User
from app import db
from app.facades import Str, Vect
import logging
logging.basicConfig(level=logging.DEBUG)

@appl.post("/register")
def register():
    data:dict = request.json
    user = User()
    user.password = Str.hash(data['password'])
    user.petname = Str.hash(data['petname'])
    signature = Str.fromList(data['signature'])
    user.signature = Str.encrypt(signature)
    user.username = data['username']
    db.session.add(user)
    db.session.commit()
    return "Successful"


@appl.post("/login")
def login():
    data:dict = request.json
    user:User = User.query.filter_by(username=data['username']).first()
    if not user:
        return "Invalid Credentials",401
    
    if user.password != Str.hash(data['password']):
        return "Invalid Credentials",401
    
    if 'petname' in data:
        if user.petname!=Str.hash(data['petname']):
            return 'Invalid Answer',431
        else:
            return user.username
    
    signature = Str.decrypt(user.signature)
    distance = Vect.euclead_dist(data['signature'],Str.toList(signature)) 

    if distance> 100:
        return 'Please confirm identity with secret qn',433
    
    return user.username
    
        
    



if __name__=='__main__':
    appl.run(host='localhost',port=5500,debug=True)
    
        