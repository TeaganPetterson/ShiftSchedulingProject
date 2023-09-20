from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined
from datetime import datetime
from model import db, connect_to_db, Assignment, EmployeeShift
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def render_home():
    return render_template('landingPage.html')


@app.route('/homepage')
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
    return redirect('/homepage')

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
    print(f'assignment_data {assignment_data}')

    for station_id, emp_shift_id in assignment_data.items():
        if station_id not in ['selectedShift', 'calendar']:
            employee_shift = EmployeeShift.query.get(emp_shift_id)
            emp_id = employee_shift.emp_id
            assignment = Assignment(
                station_id=station_id,
                emp_id=emp_id,
                shift_id=selected_shift_id,
                emp_shift_id=emp_shift_id,
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

    return redirect('/homepage')

@app.route('/deleteAssignment', methods=["POST"])
def delete_assignment():
    ass_id = request.form.get('ass_id')
    crud.delete_assignment(ass_id)
    return jsonify({'success': True})


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True, port=3000)