"""
	right now I just have them in classes without being stored anywhere but the server, so I need to create a db, but other than that I feel good about how this looks
"""

class Employee:
	def __init__(self, id, fname, lname):
		self.id = id
		self.fname = fname
		self.lname = lname

class EmployeeShifts:
	def __init__(self, id, emp_id, date, start_time, end_time):
		self.id = id
		self.emp_id = emp_id
		self.date = date
		self.start_time = start_time
		self.end_time = end_time

""" 
	Once a database is made:
	(this also might need to take place at lease partially in the ajax page)
	Have a table of "set" shifts.
	If the selected date exists in the "set" shifts, present all those elements on the page
	If not, create a new row with assignments
"""