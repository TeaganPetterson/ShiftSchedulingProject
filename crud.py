from model import db, Employee, EmployeeShift, SetShift, Station, connect_to_db
from datetime import datetime, time

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

def get_all_set_shifts():
    all_shifts = SetShift.query.all()
    return all_shifts

def create_station(st):
    station = Station(station = st)
    return station

def get_all_stations():
    all_stations = Station.query.all()
    return all_stations

def is_in_time_range(current_time, start_time, end_time):
	if start_time <= current_time <= end_time:
		return True
	else:
		return False

def shifts_in_range(set_shift_id):
    all_shifts = EmployeeShift.query.all()
    filtered_shifts = []
    set_shift = SetShift.query.get(set_shift_id)
    start_string = set_shift.start_time
    start_time = datetime.strptime(start_string, "%H-%M-%S")
    end_string = set_shift.end_time
    end_time = datetime.strptime(end_string, "%H-%M-%S")
    for shift in all_shifts:
        emp_start = shift.start_time
        emp_end = shift.end_time
        if is_in_time_range(emp_start, start_time, end_time) or is_in_time_range(emp_start, start_time, end_time):
            filtered_shifts.append(shift)
    return filtered_shifts
