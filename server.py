from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined
from datetime import datetime
from model import db, connect_to_db, Assignment
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def shift_viewer():
    shifts = crud.get_all_set_shifts()
    stations = crud.get_all_stations()
    if 'employees_on_shift' in session:
        emps = session.get('employees_on_shift')
    else:
        emps = crud.get_employees_from_shift_ids([1])
    if 'shift_id' in session:
        shift_id = int(session.get('shift_id'))
    else:
        shift_id = 1
    if 'selected_date' in session:
        selected_date = session.get('selected_date')
    else:
        selected_date = "01-01-2000"
    if crud.get_assignments(selected_date, shift_id):
        assignments = crud.get_assignments(selected_date, shift_id)
        # if assignment[customer experience]
    else:
        assignments = {'Mixing': '', 'Customer Experience': '', 'Dressing': '', 'Ovens': '', 'Prep': ''} 
    print(assignments)
    return render_template("shiftEditor.html", 
                           emps = emps, 
                           shifts = shifts, 
                           stations = stations,
                           assignments = assignments,
                           selected_date = selected_date,
                           selected_shift_id = shift_id)

@app.route('/switchShifts', methods=["POST"])
def switch_shifts():
    selected_date = datetime.strptime(request.form.get("calendar"), '%Y-%m-%d').date()
    shift_id = request.form.get("selectedShift")
    # print(f"shift_id {type(shift_id)}")
    session['shift_id'] = shift_id
    session['selected_date'] = request.form.get("calendar")
    shift_ids = crud.shifts_in_range(shift_id, selected_date)
    session['employees_on_shift'] = crud.get_employees_from_shift_ids(shift_ids)
    session['assignments'] = crud.get_assignments(selected_date, shift_id)
    # print(selected_date)
    # print(session['employees_on_shift'])
    # print(session['assignments'])
    return redirect('/')

"""
take session of employees
get employee by id for each in session
return list of employee objects
"""

@app.route('/makeAssignments', methods=["POST"])
def make_assignments():
    assignment_data = request.form


    selected_shift_id = assignment_data['selectedShift']
    selected_date = assignment_data['calendar']
    print(assignment_data)
    # Iterate through the assignment data and create assignment objects
	# check if an assignment already exists with an emp_id at a shift_id and date
	# use sqlalchemy to check if exists
	# if one employee is already assigned at that station, delete where the og assignments was, and update the desired station with the new emp_id
	# instead of this for loop, I want to use sqlalchemy to update that assignment
    for station_id, employee_id in assignment_data.items():
        if station_id not in ['selectedShift', 'calendar']:
            assignment = Assignment(
                station_id=station_id,
                emp_id=employee_id,
                shift_id=selected_shift_id,
                date=selected_date
            )
            db.session.add(assignment)

    try:
        db.session.commit()
        response = {'success': True, 'message': 'Assignments created successfully.'}
    except Exception as e:
        db.session.rollback()
        response = {'success': False, 'message': 'Error creating assignments.', 'error': str(e)}
    print(response)

    return redirect(request.url)


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)