from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from jinja2 import StrictUndefined

import model
import seed_database

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined

@app.route('/')
def shift_viewer():
    emps = seed_database.emps
    emp_names = []
    for emp in emps:
        name = f"{emp.fname} {emp.lname}"
        emp_names.append(name)
    return render_template("shiftEditor.html", emp_names = emp_names)

if __name__ == "__main__":
    # connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)