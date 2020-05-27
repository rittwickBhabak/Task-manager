from myproject import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    def __init__(self,name,email,password):
        self.name = name
        self.email = email
        self.password_hash = generate_password_hash(password)
    def check_password(self,password):
        return check_password_hash(self.password_hash, password)


class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    taskName = db.Column(db.String)
    userId = db.Column(db.Integer)
    startDay = db.Column(db.Integer)
    startMonth = db.Column(db.Integer)
    startYear = db.Column(db.Integer)
    repetationList = db.Column(db.String)
    duration = db.Column(db.Integer)
    
    def __init__(self,taskName,userId,startDay,startMonth,startYear,repetationList,duration):
        self.taskName = taskName
        self.userId = userId
        self.startDay = startDay
        self.startMonth = startMonth
        self.startYear = startYear
        self.duration = duration
        self.repetationList = repetationList

class Revesion(db.Model):
    __tablename__ = 'revisions'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer)
    taskId = db.Column(db.Integer)
    day = db.Column(db.Integer)
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    
    def __init__(self,taskId,userId,day,month,year):
        self.taskId = taskId
        self.userId = userId
        self.day = day
        self.month = month
        self.year = year

