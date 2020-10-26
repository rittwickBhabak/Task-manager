from flask import Flask, url_for, redirect, request, render_template, flash, current_app
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import time
import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'super secret key'

db = SQLAlchemy(app)
Migrate(app, db)

class Tasks(db.Model):

    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String)
    name = db.Column(db.String, unique=True)

    reps = db.relationship('Reps', cascade="all,delete", backref='tasks', lazy='dynamic')
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc


class Reps(db.Model):

    __tablename__ = 'reps'
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime)
    status = db.Column(db.Integer)
    task = db.Column(db.Integer, db.ForeignKey('tasks.id'))

    def __init__(self, date, task, status):
        self.task = task
        self.date = date
        self.status = status


@app.route('/')
def index():

    today = datetime.datetime.now().date()
    # today = datetime.date(2020,10,29)
    # today is in the form yyyy-mm-dd

    reps = Reps.query.all()
    list_of_reps = []
    for r in reps:
        print(r.date)
        y, m, d = str(r.date).split()[0].split('-')
        y = int(y)
        m = int(m)
        d = int(d)
        date = datetime.date(y,m,d)
        if date==today:
            task = Tasks.query.get(r.task)
            rep = { 'name': task.name, 'id': r.id, 'status': r.status, 'task': task.id }
            list_of_reps.append(rep)
        
    params = { 
        'reps': list_of_reps,
        'today': today.strftime('%d, %b %Y')
    }
    return render_template('index.html', params=params)

@app.route('/new', methods=['GET', 'POST'])
def newtask():
    if request.method=='POST':
        name = request.form['name']
        desc = request.form['desc']
        dates = request.form['dates'].split(',')
        print(name, desc, dates)
        # flash('success', 'success')
        # return redirect(url_for('newtask'))
        task = Tasks(name, desc)
        try: 
            db.session.add(task)
            db.session.commit()
            task = Tasks.query.filter_by(name=name)[0]
            id = task.id 
            for date in dates:
                date = datetime.date(*list(map(lambda x: int(x), date.split('-'))))
                rep = Reps(date, id, 0)
                db.session.add(rep)
                db.session.commit()
            flash('Task added successful.', 'success')
            return redirect(url_for('task', id=id))
        except Exception as e:
            msg = "Either the task name already exists or some internal error occoured."
            # msg = str(e)
            flash(msg, 'danger')
            params = {
                'task': task,
                'desc': desc,
                'dates': ','.join(dates)
            }
            return render_template('newtask.html', params=None)
    else:
        return render_template('newtask.html', params=None)

@app.route('/task/<int:id>')
def task(id):
    task = Tasks.query.get(id)
    reps = Reps.query.filter_by(task=task.id).order_by(Reps.date)
    params = {
        'task': task,
        'reps': reps
    }
    return render_template('task.html', params=params)

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Tasks.query.get(id)
    reps = Reps.query.filter_by(task=task.id)
    dates = []
    for r in reps:
        dates.append(str(r.date).split()[0])
        
    dates = ','.join(dates)
    if request.method == 'GET':
        params = {
            'task': task,
            'reps': reps,
            'dates': dates
        }
        return render_template('newtask.html', params=params)
    else:
        new_name = request.form['name']
        new_desc = request.form['desc']
        new_dates = request.form['dates'].split(',')
        task.name = new_name
        task.desc = new_desc
        db.session.add(task)
        db.session.commit()
        reps = Reps.query.filter_by(task=id)
        for rep in reps:
            db.session.delete(rep)
            db.session.commit()

        for date in list(set(new_dates)):
            date = datetime.date(*list(map(lambda x: int(x), date.split('-'))))
            rep = Reps(date, id, 0)
            db.session.add(rep)
            db.session.commit()

        flash('Task updated successful', 'success')
        return redirect(url_for('task', id=id))
    
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    task = Tasks.query.get(id)
    if request.method == 'POST':
        db.session.delete(task)
        db.session.commit()
        flash('Task successfully deleted', 'success')
    return redirect(url_for('index'))   
    
@app.route('/alltask')
def alltask():
    tasks = Tasks.query.all()
    params = {
        'tasks': tasks
    }
    return render_template('tasklist.html', params=params)

@app.route('/finishrep/<int:id>', methods=['GET', 'POST'])
def finishrep(id):
    rep = Reps.query.get(id)
    task = Tasks.query.get(rep.task)
    if request.method == 'POST':
        rep.status = 1
        db.session.add(rep)
        db.session.commit()
        flash('1 Task completed', 'success')
    return redirect(url_for('index'))


@app.route('/undonerep/<int:id>', methods=['GET', 'POST'])
def undonerep(id):
    rep = Reps.query.get(id)
    task = Tasks.query.get(rep.task)
    if request.method == 'POST':
        rep.status = 0
        db.session.add(rep)
        db.session.commit()
        flash('1 task undone', 'success')
    return redirect(url_for('index'))

@app.route('/privious-undone-tasks')
def undonePrev():
    
    today = datetime.datetime.now().date()
    # today = datetime.date(2020,10,29)
    # today is in the form yyyy-mm-dd

    reps = Reps.query.all()
    list_of_reps = []
    for r in reps:
        print(r.date)
        y, m, d = str(r.date).split()[0].split('-')
        y = int(y)
        m = int(m)
        d = int(d)
        date = datetime.date(y,m,d)
        if date<=today and r.status==0:
            task = Tasks.query.get(r.task)
            rep = { 'name': task.name, 'id': r.id, 'status': r.status, 'task': task.id, 'date': r.date }
            list_of_reps.append(rep)
        
    params = { 
        'reps': list_of_reps,
        'header': 'Previous Undone Tasks'
    }
    return render_template('otherdaytasks.html', params=params)


@app.route('/tomorrow')
def tomorrowTasks():
    
    today = datetime.datetime.now().date()
    # today = datetime.date(2020,10,29)
    # today is in the form yyyy-mm-dd
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    print(tomorrow)

    reps = Reps.query.all()
    list_of_reps = []
    for r in reps:
        # print(r.date)
        y, m, d = str(r.date).split()[0].split('-')
        y = int(y)
        m = int(m)
        d = int(d)
        date = datetime.date(y,m,d)
        if date==tomorrow:
            task = Tasks.query.get(r.task)
            rep = { 'name': task.name, 'id': r.id, 'status': r.status, 'task': task.id, 'date': r.date }
            list_of_reps.append(rep)
        
    params = { 
        'reps': list_of_reps,
        'header': 'Tomorrow\'s Tasks',
        'date': tomorrow 
    }
    return render_template('otherdaytasks.html', params=params)

@app.route('/goto')
def goto():
    y, m, d = request.args.get('date').split('-')
    
    gotoDate = datetime.date(int(y),int(m),int(d))

    reps = Reps.query.all()
    list_of_reps = []
    for r in reps:
        # print(r.date)
        y, m, d = str(r.date).split()[0].split('-')
        y = int(y)
        m = int(m)
        d = int(d)
        date = datetime.date(y,m,d)
        if date==gotoDate:
            task = Tasks.query.get(r.task)
            rep = { 'name': task.name, 'id': r.id, 'status': r.status, 'task': task.id, 'date': r.date }
            list_of_reps.append(rep)
        
    params = { 
        'reps': list_of_reps,
        'header': 'Tasks',
        'date': gotoDate
    }
    return render_template('otherdaytasks.html', params=params)

if __name__ == "__main__":
    app.run(debug=True)