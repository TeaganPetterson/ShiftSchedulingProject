import os
import json
from random import choice, randint
from datetime import datetime

# import crud
import model
import server

"""
	I want to pull the data from my json to add it to tables 
"""

with open('data/employee_shift.json') as f:
    shifts_data = json.loads(f.read())
    
with open('data/employees.json') as e:
    employee_data = json.loads(e.read())

"""
	Right now I'm just instantiating classes for each of them, but not storing it anywhere in a database, but I'm sure that won't be difficult, this was just the first step in my head
"""
emps = []
shifts = []
for emp in employee_data:
    model.Employee(emp.id, emp.fname, emp.lname)
    emps.append(emp)

for shift in shifts_data:
    model.EmployeeShifts(shift.id, shift.emp_id, shift.date, shift.start_time, shift.end_time)
    shift.append(shift)