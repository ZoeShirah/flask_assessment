from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension


app = Flask(__name__)


# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


@app.route("/")
def home():
    """displays the home page"""

    return render_template("index.html")


@app.route("/application-form")
def application():
    """displays application form with drop-down of available positions"""

    available_jobs = ["QA Engineer", "Software Engineer", "Product Manager"]
    return render_template("application-form.html",
                           available=available_jobs)


@app.route("/application-success", methods=["POST"])
def app_submitted():
    """Takes info from application form and sends it to a response"""

    applicant_firstname = request.form.get("first")
    applicant_lastname = request.form.get("last")
    applicant = str(applicant_firstname) + " " + str(applicant_lastname)
    salary = str(request.form.get("salary",))
    if salary == '':
        salary = '0.0'
    job = request.form.get("jobtitle")

    return render_template("/application-response.html",
                           applicant=applicant,
                           salary=float(salary),
                           job=job)

# YOUR ROUTES GO HERE


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = True

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
