'''
python
from application import db
db.create_all()
from application import Member
from datetime import date

anthony = Member(username='anthony', password='secret', email='anthony@email.com', join_date=date.today())
db.session.add(anthony)
db.session.commit()

michelle = Member(username='MichelleForever', password='mypassword', email='michelle@email.com', join_date=date.today())
db.session.add(michelle)
db.session.commit()

anthony.password = 'mynewpassword
db.session.commit()

db.session.delete(anthony)
db.session.commit()

anthony = Member(username='Anthony', password='secret', email='anthony@email.com', join_date=date.today())
db.session.add(anthony)
zach = Member(username='Zach1', password='zachisthebest', email='zach@email.com', join_date=date.today())
db.session.add(zach)
db.session.commit()

results = Member.query.all()
ant = Member.query.filter_by(username='Anthony').first()
ant.password = 'mynewpassword'

michelle = Member.query.filter(Member.username == 'MichelleForever').first()
print(michelle.username)

Member.query.first()

q = Member.query
q.filter(Member.username == 'Zach1')
q.first()


q1 = Member.query
q2.filter(Member.username == 'Anthony')
q1.all()
q2.all()
'''