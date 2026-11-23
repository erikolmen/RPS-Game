# this is the "web_app/routes/rps_routes.py" file...

import random

from flask import Blueprint, request, render_template, redirect, flash, session

from app.rps import VALID_OPTIONS, determine_winner

rps_routes = Blueprint("rps_routes", __name__)

RESULT_MESSAGES = {
    "user": "You win!",
    "computer": "Computer wins!",
    "tie": "It's a tie!",
}

EMOJIS = {"rock": "✊", "paper": "✋", "scissors": "✌️"}


def get_score():
    # the score is kept in the user's session (a browser cookie signed with the app's SECRET_KEY)
    score = dict(session.get("score") or {"user": 0, "computer": 0, "tie": 0})
    score["played"] = score["user"] + score["computer"] + score["tie"]
    return score


@rps_routes.route("/rps/form")
def rps_form():
    print("RPS FORM...")
    return render_template("rps_form.html", options=VALID_OPTIONS, emojis=EMOJIS, score=get_score())


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
        flash("Invalid choice. Please select rock, paper, or scissors.", "danger")
        return redirect("/rps/form")

    computer_choice = random.choice(VALID_OPTIONS)
    winner = determine_winner(user_choice, computer_choice)

    # update the running score
    score = get_score()
    score[winner] += 1
    session["score"] = {"user": score["user"], "computer": score["computer"], "tie": score["tie"]}
    score["played"] += 1

    return render_template("rps_results.html",
        user_choice=user_choice,
        computer_choice=computer_choice,
        winner=winner,
        message=RESULT_MESSAGES[winner],
        emojis=EMOJIS,
        score=score
    )


@rps_routes.route("/rps/reset", methods=["POST"])
def rps_reset():
    print("RPS RESET...")
    session.pop("score", None)
    flash("Score reset. Good luck!", "success")
    return redirect("/rps/form")
