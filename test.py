from app import db, Reps, Tasks 
import datetime

# # db.create_all()

# task1 = Tasks('Task1', 'asldkfjasf')
# task2 = Tasks('Task2', 'asdklfjasdf')
# task3 = Tasks('Task3', '8usdafjffasfjd')
# db.session.add_all([task1, task2, task3])
# db.session.commit()

# for i in range(1, 4):
#     rep1 = Reps(datetime.date(2020,10, 25), i, 0)
#     rep2 = Reps(datetime.date(2020,10, 25), i, 0)
#     db.session.add_all([rep1, rep2])
#     db.session.commit()

# rep = Reps(datetime.date(2020,10, 26), 1, 0)
# db.session.add(rep)
# db.session.commit()

# rep1 = Reps(datetime.date(2020, 12, 10), 1, 0)
# rep2 = Reps(datetime.date(2020, 12, 1), 1, 0)

# db.session.add(rep1)
# db.session.commit()

# db.session.add(rep2)
# db.session.commit()

# a = None 
# b = None 
reps = Reps.query.all()
for rep in reps:
    print(rep.date)
    print(type(rep.date))
    # if a is None:
    #     a = rep.date.date()
    #     b = rep.date.date()
    # else:
    #     b = rep.date.date()

# print(a<b)


# import datetime 
# s = '2020-02-2'
# print(date)