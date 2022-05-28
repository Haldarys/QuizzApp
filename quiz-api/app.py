from flask import Flask, request
from lib import *
from Question import Question
import jwt_utils
import sqlite3

app = Flask(__name__)

def authent():
    jwt = request.headers.get('Authorization')
    if(jwt):
        jwt = jwt.split(' ')[1]
    
    try:
        jwt_utils.decode_token(jwt)
    except jwt_utils.JwtError:
        return False
    return True

@app.route('/')
def hello_world():
	x = 'world'
	return f"Hello, {x}"

@app.route('/login', methods=['POST'])
def PostLogin():
    payload = request.get_json()
    if(payload['password'] == 'mdp'):
        return {"token": jwt_utils.build_token()}, 200
    return '', 401

@app.route('/quiz-info', methods=['GET'])
def GetQuizInfo():
	return {"size": 0, "scores": []}, 200

@app.route('/questions', methods=['POST'])
def PostQuestion():
    if(not authent()):
        return '', 401

    payload = request.get_json()
    qst = Question.fromDict(payload)
    if not Question.saveToDb(qst):
        return '', 500

    return '', 200

@app.route('/questions/<position>', methods=['GET'])
def GetQuestion(position):
    qst = Question.fromPosition(position)
    if(not qst):
        return '', 404

    return qst.toJson(), 200

@app.route('/questions/<position>', methods=['DELETE'])
def DeleteQuestion(position):
    if(not authent()):
        return '', 401
    
    qst = Question.fromPosition(position)
    if(not qst):
        return '', 404

    if not Question.deleteQuestion(qst):
        return '', 500
    return '', 204

@app.route('/questions/<position>', methods=['PUT'])
def UpdateQuestion(position):
    if(not authent()):
        return '', 401
    
    payload = request.get_json()
    qst_new = Question.fromDict(payload)
    qst_old = Question.fromPosition(position)
    
    if(not qst_old):
        return '', 404
    qst_new.index = qst_old.index

    if not Question.saveToDb(qst_new):
        return '', 500
    return '', 200
	

if __name__ == "__main__":
    app.run(ssl_context='adhoc')