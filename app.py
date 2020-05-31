from myproject import app, db
from flask import Flask, render_template, request, url_for, redirect, flash , abort, session
from flask_login import login_user, login_required, logout_user 
from myproject.models import User, Task, Revesion
from myproject.forms import LoginForm, SignUpForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new', methods=['GET','POST'])
@login_required
def newTask():
    if request.method=="POST":
        name = request.form['name']
        syear,smonth,sday = request.form['sdate'].split('-')
        eyear,emonth,eday = request.form['edate'].split('-')
        regularinterval = request.form['regularinterval']
        everyday = request.form['everyday']
        twoday = request.form['twoday']
        threeday = request.form['threeday']
        fiveday = request.form['fiveday']
        sevenday = request.form['sevenday']
        tenday = request.form['tenday']
        fifteenday = request.form['fifteenday']
        twentyday = request.form['twentyday']
        onemonth = request.form['onemonth']
        fourtyfiveday = request.form['fourtyfiveday']
        twomonth = request.form['twomonth']
        threemonth = request.form['threemonth']
        fourmonth = request.form['fourmonth']
        sixmonth = request.form['sixmonth']
        oneyear = request.form['oneyear']
        userId = session['user_id']
        repList = '{"0":regularinterval, "1": everyday, "2":twoday, "3":threeday, "5":fiveday, "7":sevenday, "10":tenday,"15":fifteenday, "20":twentyday, "30":onemonth, "45":fourtyfiveday, "60":twomonth, "90":threemonth, "120":fourmonth, "180":sixmonth, "360":oneyear}'
        new = Task(name,userId, sday,smonth,syear,repList,eday,emonth,eyear)
        db.session.add(new)
        db.session.commit()
        flash('Task added successfully','success')
        return redirect(url_for('tasklist'))
    return render_template('newtask.html')

@app.route('/update', methods=['GET','POST'])
@login_required
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
        currentUser = User.query.filter_by(email=email).first()
        if  currentUser is not None and currentUser.check_password(password):
            session['user_id'] = currentUser.id
            session['username'] = currentUser.name
            login_user(currentUser)
            return redirect(url_for('index'))
        else:
            flash('Some error occured. Please enter your email and password correctly and try again', 'danger')
            return redirect(url_for('login'))
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
        errorMsg = None
        if not password==confirmPassword:
            errorMsg = 'Password and Confirm Password should match'
        if User.query.filter_by(email=email).first() is not None:
            errorMsg = 'Email already exists.'
        if name=='' or email=='' or password=='':
            errorMsg = 'Name, Email, Password can not be blank'
        if errorMsg is not None:
            flash(errorMsg, 'danger')
            return redirect(url_for('signup'))
        newUser = User(name, email, password)
        db.session.add(newUser)
        db.session.commit()
        print(f'Name:{name},Email:{email},Password:{password},Confirm Password:{confirmPassword}')
        flash('Sign Up seccessfull', 'success`')
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)


@app.route('/tasklist')
def tasklist():
    tasks = Task.query.filter_by(userId = session['user_id'])
    return render_template('taskList.html', tasks=tasks)

@app.route('/logout')
@login_required
def logout():
    session['username'] = None
    session['user_id'] = None
    logout_user()
    return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)