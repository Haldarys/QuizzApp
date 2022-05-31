import json
from multiprocessing.connection import Connection
import sqlite3

class Question():

    def __init__(self, title: str, text: str, image: str, position: int, possibleAnswers: list, index: int = -1):
        self.title = title
        self.text = text
        self.image = image
        self.position = position
        self.index = index
        # possibleAnswer : [ {}, {}, ... ]
        # keys : { id, question_id, text, isCorrect }
        # values : { int, int, str, bool }
        for answer in possibleAnswers:
            answer['isCorrect'] = True if answer['isCorrect'] == 1 else False
            
        self.possibleAnswers = possibleAnswers

    def __str__(self):
        return self.toJson()

    
    def toJson(self):
        return json.dumps(
            {
                "title": self.title,
                "text": self.text,
                "image": self.image,
                "position": self.position,
                "possibleAnswers": self.possibleAnswers
            }
        )
    
    def getCorrectAnswer(self):
        i = 1
        for answer in self.possibleAnswers:
            if answer['isCorrect']:
                return i
            i += 1
        return False
    
    @staticmethod
    def fromJson(jsonInput: str):
        input = json.loads(jsonInput)
        return Question(input["title"], input["text"], input["image"], input["position"], input["possibleAnswers"])
    
    @staticmethod
    def fromDict(dictInput: dict):
        return Question(dictInput["title"], dictInput["text"], dictInput["image"], dictInput["position"], dictInput["possibleAnswers"])
    
    @staticmethod
    def fromPosition(position: int):
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            db_conn.row_factory = sqlite3.Row
            cur = db_conn.cursor()
            cur.execute("begin")

            # get question from db
            select_result = cur.execute(
                "SELECT id, text, title, image, position FROM Questions WHERE position = ?",
                (position,)
            )
            res_question = select_result.fetchone()
            if(res_question is None):
                return False
            id = res_question['id']

            # get question answers from db
            select_result = cur.execute(
                "SELECT id, question_id, text, isCorrect FROM Answers WHERE question_id = ?",
                (id,)
            )
            res_answer = select_result.fetchall()
            possibleAnswers = []
            for answer in res_answer:
                answer_dict = dict(answer)
                possibleAnswers.append(answer_dict)


            cur.execute("commit")
        except sqlite3.Error:
            #in case of exception, roolback the transaction
            cur.execute('rollback')
            return False
        
        return Question(res_question["title"], res_question["text"], res_question["image"], res_question["position"], possibleAnswers, id)
    
    @staticmethod
    def allQuestions():
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            db_conn.row_factory = sqlite3.Row
            cur = db_conn.cursor()

            # get question from db
            select_result = cur.execute(
                "SELECT id, text, title, image, position FROM Questions"
            )
            res_question = select_result.fetchall()
            if(res_question is None):
                return False
            
            questions = []
            for qst in res_question:
                questions.append(Question(qst["title"], qst["text"], qst["image"], qst["position"], [], qst["id"]))

            # get question answers from db
            select_result = cur.execute(
                "SELECT id, question_id, text, isCorrect FROM Answers"
            )
            res_answer = select_result.fetchall()
            for qst in questions:
                for answer in res_answer:
                    if answer['question_id'] == qst.index:
                        qst.possibleAnswers.append(dict(answer))

        except sqlite3.Error as err:
            return False
        
        return questions
    
    @staticmethod
    def saveToDb(qst):
        # Peut ajouter vérif si aucune réponse n'est valide
        if qst.index >= 1:
            return Question.updateIntoDb(qst)
        else:
            return Question.insertIntoDb(qst)

    @staticmethod
    def insertIntoDb(qst):
        if not Question.incrementQuestionsOnInsert(qst):
            return False
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()
            cur.execute("begin")

            # save the question to db
            insertion_result = cur.execute(
                "insert into Questions (title, text, image, position) values (?, ?, ?, ?)",
                (qst.title, qst.text, qst.image, qst.position)
            )
            id = insertion_result.lastrowid

            for answer in qst.possibleAnswers:
                cur.execute(
                    "insert into Answers (question_id, text, isCorrect) values (?, ?, ?)",
                    (id, answer['text'],  1 if answer['isCorrect'] == True else 0)
                )

            cur.execute("commit")
        except sqlite3.Error as err:
            #in case of exception, rollback the transaction
            print(err)
            cur.execute('rollback')
            db_conn.close()
            return False
        db_conn.close()
        return True
    
    @staticmethod
    def incrementQuestionsOnInsert(qst):
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()

            cur.execute(
                "UPDATE Questions SET position = position + 1 WHERE position >= ?",
                (qst.position,)
            )

        except sqlite3.Error:
            db_conn.close()
            return False
            
        db_conn.close()
        return True

    @staticmethod
    def decrementQuestionsOnDelete(qst):
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()

            cur.execute(
                "UPDATE Questions SET position = position - 1 WHERE position >= ?",
                (qst.position,)
            )

        except sqlite3.Error:
            db_conn.close()
            return False
            
        db_conn.close()
        return True

    
    @staticmethod
    def updateIntoDb(qst):
        if not Question.repositionQuestionsOnUpdate(qst):
            return False
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()
            cur.execute("begin")

            # update the question
            cur.execute(
                "UPDATE Questions SET title = ?, text = ?, image = ?, position = ? WHERE id = ?",
                (qst.title, qst.text, qst.image, qst.position, qst.index)
            )

            # delete old answers
            cur.execute(
                "DELETE FROM Answers WHERE question_id = ?",
                (qst.index,)
            )

            for answer in qst.possibleAnswers:
                cur.execute(
                    "insert into Answers (question_id, text, isCorrect) values (?, ?, ?)",
                    (qst.index, answer['text'],  1 if answer['isCorrect'] == True else 0)
                )

            cur.execute("commit")
        except sqlite3.Error as err:
            #in case of exception, rollback the transaction
            print(err)
            cur.execute('rollback')
            db_conn.close()
            return False
        db_conn.close()
        return True
    
    @staticmethod
    def repositionQuestionsOnUpdate(qst):
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            db_conn.row_factory = sqlite3.Row
            cur = db_conn.cursor()
            cur.execute('begin')

            position_result = cur.execute(
                "SELECT position FROM Questions WHERE id = ?",
                (qst.index,)
            )
            line = position_result.fetchone()
            if(line is not None):
                oldpos = line['position']
            else:
                return False

            if oldpos > qst.position:
                cur.execute(
                    "UPDATE Questions SET position = position + 1 WHERE position <= ? AND position >= ? AND id <> ?",
                    (oldpos, qst.position, qst.index)
                )
            else:
                cur.execute(
                    "UPDATE Questions SET position = position - 1 WHERE position >= ? AND position <= ? AND id <> ?",
                    (oldpos, qst.position, qst.index)
                )

            cur.execute('commit')

        except sqlite3.Error as err:
            print(err)
            cur.execute('rollback')
            db_conn.close()
            return False
        
        db_conn.close()
        return True
    
    @staticmethod
    def deleteQuestion(qst):
        if qst.index <= 0:
            return False
        
        if not Question.decrementQuestionsOnDelete(qst):
            return False
        
        try:
            db_conn = sqlite3.connect("./quiz.db")
            db_conn.isolation_level = None
            cur = db_conn.cursor()
            cur.execute('begin')

            cur.execute(
                "DELETE FROM Questions WHERE id = ?",
                (qst.index,)
            )

            cur.execute(
                "DELETE FROM Answers WHERE question_id = ?",
                (qst.index,)
            )

            cur.execute('commit')

        except sqlite3.Error as err:
            print(err)
            cur.execute('rollback')
            db_conn.close()
            return False
        
        db_conn.close()
        return True
