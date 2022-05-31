import json
from multiprocessing.connection import Connection
import sqlite3
from Question import Question
from datetime import datetime

class Quiz():

    @staticmethod
    def infos():
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            db_conn.row_factory = sqlite3.Row
            cur = db_conn.cursor()

            count_result = cur.execute(
                "SELECT count(*) as nb FROM Questions"
            )
            line = count_result.fetchone()
            nb_quest = line['nb']

            scores_result = cur.execute(
                "SELECT playerName, score, date FROM Scores ORDER BY score DESC"
            )
            scores = scores_result.fetchall()
            scores = list(map(dict, scores))

        except sqlite3.Error:
            db_conn.close()
            return False
            
        db_conn.close()
        return {'size': nb_quest, 'scores': scores}
    
    @staticmethod
    def deleteAllScores():
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            db_conn.row_factory = sqlite3.Row
            cur = db_conn.cursor()
            cur.execute("begin")

            cur.execute(
                "DELETE FROM Scores"
            )

            cur.execute("commit")
        except sqlite3.Error as err:
            cur.execute("rollback")
            db_conn.close()
            return False
            
        db_conn.close()
        return True
    
    @staticmethod
    def submit(playerName, answers):
        questions = Question.allQuestions()
        if not questions:
            return False

        answers_summary = []
        score = 0
        i = 0
        for qst in questions:
            correctAnswer = qst.getCorrectAnswer()
            # Error if question has no correct answer
            if not correctAnswer:
                return False

            wasCorrect = answers[i] == correctAnswer
            if wasCorrect:
                score += 1
            answers_summary.append({'correctAnswerPosition': correctAnswer, 'wasCorrect': wasCorrect })
            i += 1
        
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()
            cur.execute("begin")

            cur.execute(
                "INSERT INTO Scores (playerName, score, date) VALUES (?, ?, ?)",
                (playerName, score, datetime.today().strftime('%d/%m/%Y %H:%M:%S'))
            )

            cur.execute("commit")
        except sqlite3.Error:
            #in case of exception, roolback the transaction
            cur.execute('rollback')
            return False

        return {'answersSummaries': answers_summary, 'playerName': playerName, 'score': score}