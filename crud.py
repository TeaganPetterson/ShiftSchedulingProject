from model import db, Employee, EmployeeShift, SetShift, connect_to_db

def create_employee(fname, lname):
    employee = Employee(fname = fname, lname = lname)
    return employee

def get_all_employees():
    employees = Employee.query.all()
    return employees

def get_unassigned_employees():
    un_emps = Employee.query.filter(station_id = None)
    
# def get_available_employees(shift_id):
#     # get start time and end time from shift_id 
#     # pull employee shifts that start before the end time and end after the start time

def create_employee_shift(emp_id, date, start_time, end_time):
    emp_shift = EmployeeShift(emp_id = emp_id, date = date, start_time = start_time, end_time = end_time)
    return emp_shift

def create_set_shift(start, end, display):
    set_shift = SetShift(start_time = start, end_time = end, display = display)
    return set_shift
