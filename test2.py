from app import db, Tasks, Reps 

tasks = Tasks.query.all()

for t in tasks:
    print(t.name, t.id)