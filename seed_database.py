import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

"""
	I want to pull the data from my json to add it to tables 
"""
os.system('dropdb shift_planner')
os.system('createdb shift_planner')

model.connect_to_db(server.app)
model.db.create_all()

with open('data/employee_shift.json') as f:
    shifts_data = json.loads(f.read())
    
with open('data/employees.json') as e:
    employee_data = json.loads(e.read())

with open('data/shifts.json') as e:
    set_shifts_data = json.loads(e.read())
"""
	Right now I'm just instantiating classes for each of them, but not storing it anywhere in a database, but I'm sure that won't be difficult, this was just the first step in my head
"""
shifts = []
emps = []
for emp in employee_data:
    # emp_id = emp["emp_id"]
    fname = emp["fname"]
    lname = emp["lname"]
    db_emp = crud.create_employee(fname, lname)
    emps.append(db_emp)


model.db.session.add_all(emps)
model.db.session.commit()


for s in shifts_data:
    # shift_id = s['id']
    emp_id = s['emp_id']
    date = s['date']
    start = s['start_time']
    end = s['end_time']
    shift = crud.create_employee_shift(emp_id, date, start, end)
    shifts.append(shift)
    
model.db.session.add_all(shifts)
model.db.session.commit()

set_shifts = []
for shift in set_shifts_data:
    start = shift["start_time"]
    end = shift["end_time"]
    display = shift["display_value"]
    set_shift = crud.create_set_shift(start, end, display)
    set_shifts.append(set_shift)
    
model.db.session.add_all(set_shifts)
model.db.session.commit()
    
# for n in range(5, 24):
    
# 	"""
#     Open
#     8-11
#     11-2
#     2-5
#     5-8
# 	Close
# 	"""