# this is the "web_app/routes/rps_routes.py" file...

import random

from flask import Blueprint, request, render_template, redirect

from app.rps import VALID_OPTIONS, determine_winner

rps_routes = Blueprint("rps_routes", __name__)

RESULT_MESSAGES = {
    "user": "You win!",
    "computer": "Computer wins!",
    "tie": "It's a tie!",
}


@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html", options=VALID_OPTIONS)


@rps_routes.route("/rps/results", methods=["GET", "POST"])
def rps_results():
    print("RPS RESULTS...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    user_choice = (request_data.get("user_choice") or "").lower().strip()

    if user_choice not in VALID_OPTIONS:
        return redirect("/rps/form")

    computer_choice = random.choice(VALID_OPTIONS)
    winner = determine_winner(user_choice, computer_choice)

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner,
        message=RESULT_MESSAGES[winner]
    )
