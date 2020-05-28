from myproject import app, db
from flask import Flask, render_template, request, url_for, redirect, flash , abort 
from flask_login import login_user, login_required, logout_user 
from myproject.models import User, Task, Revesion
from myproject.forms import LoginForm, SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['GET','POST'])
def newTask():
    if request.method=="POST":
        name = request.form['name']
        startDay = request.form['day']
        startMonth = request.form['month']
        startYear = request.form['year']
        duration = request.form['duration']
        oneDay = request.form['oneday']
        twoDay = request.form['twoday']
        threeDay = request.form['threeday']
        fiveDay = request.form['fiveday']
        sevenDay = request.form['sevenday']
        tenDay = request.form['tenday']
        fifteenDay = request.form['fifteenday']
        print(name, duration,oneDay,twoDay,threeDay,fiveDay,sevenDay, tenDay,fifteenDay)
    return render_template('newtask.html')

@app.route('/update', methods=['GET','POST'])
def editTask():
    if request.method=="POST":
        name = request.form['name']
        startDay = request.form['day']
        startMonth = request.form['month']
        startYear = request.form['year']
        duration = request.form['duration']
        oneDay = request.form['oneday']
        twoDay = request.form['twoday']
        threeDay = request.form['threeday']
        fiveDay = request.form['fiveday']
        sevenDay = request.form['sevenday']
        tenDay = request.form['tenday']
        fifteenDay = request.form['fifteenday']
        deleteTask = None
        try:
            deleteTask = request.form['delete']
        except:
            deleteTask = None
        print(name, duration,oneDay,twoDay,threeDay,fiveDay,sevenDay, tenDay,fifteenDay)
        print('Will delete the task: ',deleteTask)
    return render_template('edittask.html')


@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        print(f'Email:{email}, Password:{password}')
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        confirmPassword = form.confirmPassword.data
        print(f'Name:{name},Email:{email},Password:{password},Confirm Password:{confirmPassword}')
    return render_template('signup.html', form=form)

if __name__ == "__main__":
    app.run(debug=True)