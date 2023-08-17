"""
	right now I just have them in classes without being stored anywhere but the server, so I need to create a db, but other than that I feel good about how this looks
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Employee(db.Model):

	__tablename__ = "employees"

	id = db.Column(db.Integer, primary_key=True, autoincrement = True)
	fname = db.Column(db.String(20), nullable = False)
	lname = db.Column(db.String(20), nullable = False)

	employee_shifts = db.relationship('EmployeeShift', back_populates='employee')
	assignments = db.relationship('Assignment', back_populates='employee')

class EmployeeShift(db.Model):

	__tablename__ = "employee_shifts"

	id = db.Column(db.Integer, primary_key=True, autoincrement = True)
	emp_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
	date = db.Column(db.String(15), nullable = False)
	start_time = db.Column(db.String(15), nullable = False)
	end_time = db.Column(db.String(15), nullable = False)

	employee = db.relationship('Employee', back_populates='employee_shifts')


class SetShift(db.Model):
      
	__tablename__ = "set_shifts"

	id = db.Column(db.Integer, primary_key=True, autoincrement = True)
	start_time = db.Column(db.String(15), nullable = False)
	end_time = db.Column(db.String(15), nullable = False)
	display = db.Column(db.String(15), nullable = False)

class Station(db.Model):

	__tablename__ = "stations"

	id = db.Column(db.Integer, primary_key=True, autoincrement = True)
	station = db.Column(db.String(25), nullable = False)

class Assignment(db.Model):

	__tablename__ = "assignments"
	# __table_args__ = (db.UniqueConstraint("emp_id", "shift_id", "date"),)

	id = db.Column(db.Integer, primary_key=True, autoincrement = True)
	station_id = db.Column(db.Integer, db.ForeignKey("stations.id"), nullable=False)
	emp_id = db.Column(db.Integer, db.ForeignKey("employees.id"), nullable=False)
	shift_id = db.Column(db.Integer, db.ForeignKey("set_shifts.id"), nullable=False)
	date = date = db.Column(db.String(15), nullable = False)

	employee = db.relationship('Employee', back_populates='assignments')


""" 
	Once a database is made:
	(this also might need to take place at lease partially in the ajax page)
	Have a table of "set" shifts.
	If the selected date exists in the "set" shifts, present all those elements on the page
	If not, create a new row with assignments
"""
def connect_to_db(flask_app, db_uri="postgresql:///shift_planner", echo=False):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")
    

if __name__ == "__main__":
    from server import app

    connect_to_db(app)