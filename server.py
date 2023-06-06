from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined

import model
import crud

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def shift_viewer():
    all_emps = crud.get_all_employees()
    emps = []
    for emp in all_emps:
        emps.append(emp.id)
    # session['employees'] = emps
    # emps = session['employees']
	# then add the session to the render
    shifts = crud.get_all_set_shifts()
    stations = crud.get_all_stations()
    return render_template("shiftEditor.html", 
                           emps = session['employees'], 
                           shifts = shifts, 
                           stations = stations)

@app.route('/switchShifts', methods=["POST"])
def switch_shifts():
    date = request.form.get("calendar")
    print(date)
    shift_id = request.form.get("selectedShift")
    print(shift_id)
    print(crud.shifts_in_range(shift_id))
    session['employees'] = crud.shifts_in_range(shift_id)
    # change unassigned_emps to the session['employees'] variable
    return redirect('/')

"""
take session of employees
get employee by id for each in session
return list of employee objects
"""

if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    