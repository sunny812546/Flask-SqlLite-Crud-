from app import db, Student


# create_all
ravi = Student("ravi", 20)
yash = Student("yash", 20)

db.session.add_all([ravi, yash])
db.session.commit()
# by filter
puppy_sam = Student.query.filter_by(name='yash').first()  # Returns list
print(puppy_sam)
print('\n')

# upadate
update = Student.query.get(1)
update.name = "sun"
db.session.add(update)
db.session.commit()
# delete
delete = Student.query.get(2)
db.session.delete(delete)
db.session.commit()

# read

# by # ID
id = Student.query.get(1)
print(id)
print('\n')
# all
all = Student.query.all()
print(all)
print('\n')
