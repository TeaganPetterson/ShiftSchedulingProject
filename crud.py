from model import db, Employee, EmployeeShift, SetShift, Station, Assignment, connect_to_db
from datetime import datetime, time

def create_employee(fname, lname):
    employee = Employee(fname = fname, 
                        lname = lname)
    return employee

# def create_assignment(emp_id, station_id, shift_id, date):
#     employee = Employee(fname = fname, lname = lname)
#     return employee

def get_all_employees():
    employees = Employee.query.all()
    return employees

def get_unassigned_employees():
    un_emps = Employee.query.filter(station_id = None)
    
# def get_available_employees(shift_id):
#     # get start time and end time from shift_id 
#     # pull employee shifts that start before the end time and end after the start time

def create_employee_shift(emp_id, date, start_time, end_time):
    emp_shift = EmployeeShift(emp_id = emp_id, 
                              date = date, 
                              start_time = start_time, 
                              end_time = end_time)
    return emp_shift

def create_set_shift(start, end, display):
    set_shift = SetShift(start_time = start, 
                         end_time = end, 
                         display = display)
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

def create_assignment(emp_id, station_id, shift_id, date):
    assignment = Assignment(emp_id = emp_id, 
                            station_id = station_id, 
                            shift_id = shift_id, 
                            date = date)
    return assignment


def is_in_time_range(current_time, start_time, end_time):
	return start_time <= current_time <= end_time
	# 	 True
	# else:
	# 	return False

def shifts_in_range(set_shift_id, date):
    all_shifts = EmployeeShift.query.all()
    filtered_shifts = []
    set_shift = SetShift.query.get(set_shift_id)
    start_string = set_shift.start_time
    start_time = datetime.strptime(start_string, "%H:%M:%S")
    end_string = set_shift.end_time
    end_time = datetime.strptime(end_string, "%H:%M:%S")
    for shift in all_shifts:
        shift_date = datetime.strptime(shift.date, "%m-%d-%Y").date()
        emp_start = datetime.strptime(shift.start_time, "%H:%M:%S")
        emp_end = datetime.strptime(shift.end_time, "%H:%M:%S")
        if shift_date == date and (is_in_time_range(emp_start, start_time, end_time) or is_in_time_range(emp_end, start_time, end_time)):
            filtered_shifts.append(shift.id)
    return filtered_shifts

def get_employees_from_shift_ids(shift_ids):
    employees = {}
    for id in shift_ids:
        employee_shift = EmployeeShift.query.get(id)
        full_start = datetime.strptime(employee_shift.start_time, "%H:%M:%S")
        full_end = datetime.strptime(employee_shift.end_time, "%H:%M:%S")
        employees[employee_shift.employee.id] = {
            'first': employee_shift.employee.fname,
            'last': employee_shift.employee.lname,
            'start': full_start.strftime("%I:%M %p"),
            'end': full_end.strftime("%I:%M %p")
        }
    return employees

from sqlalchemy import cast, Date

def get_assignments(date, shift_id):
    selected_assignments = {}
    assignments = Assignment.query.filter(cast(Assignment.date, Date) == date, 
                                          Assignment.shift_id == shift_id).all()
    for assignment in assignments:
        employee = Employee.query.filter(Employee.id == assignment.emp_id).first()
        name = f"{employee.fname} {employee.lname}"
        station = Station.query.filter(Station.id == assignment.station_id).first()
        selected_assignments[station.station] = name
    return selected_assignments
