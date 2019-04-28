from app import db, Student

db.create_all()

sunny = Student("Sunny", 20)

db.session.add(sunny)

db.session.commit()
print(sunny.id)
