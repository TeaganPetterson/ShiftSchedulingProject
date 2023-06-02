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
    emps = crud.get_all_employees()
    shifts = crud.get_all_set_shifts()
    stations = crud.get_all_stations()
    return render_template("shiftEditor.html", 
                           emps = emps, 
                           shifts = shifts, 
                           stations = stations)

@app.route('/switchShifts', methods=["POST"])
def switch_shifts():
    date = request.form.get("calendar")
    print(date)
    shift = request.form.get("selectedShift")
    print(shift)
    return redirect('/')

if __name__ == "__main__":
    model.connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)
    