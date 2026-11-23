# this is the "web_app/routes/stocks_routes.py" file...

from flask import Blueprint, request, render_template, redirect, flash

from app.stocks import fetch_stocks_data, format_usd, get_summary_stats

stocks_routes = Blueprint("stocks_routes", __name__)

POPULAR_SYMBOLS = ["AAPL", "MSFT", "GOOGL", "AMZN", "NFLX", "TSLA"]


@stocks_routes.route("/stocks/form")
def stocks_form():
    print("STOCKS FORM...")
    return render_template("stocks_form.html", popular_symbols=POPULAR_SYMBOLS)


@stocks_routes.route("/stocks/dashboard", methods=["GET", "POST"])
def stocks_dashboard():
    print("STOCKS DASHBOARD...")

    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
        print("FORM DATA:", request_data)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)
        print("URL PARAMS:", request_data)

    symbol = (request_data.get("symbol") or "NFLX").upper().strip()

    try:
        df = fetch_stocks_data(symbol=symbol)
        stats = get_summary_stats(df)
        latest_close_usd = format_usd(stats["latest_close"])
        latest_date = df.iloc[0]["timestamp"]
        data = df.to_dict("records")

        flash("Fetched Real-time Market Data!", "success")
        return render_template("stocks_dashboard.html",
            symbol=symbol,
            latest_close_usd=latest_close_usd,
            latest_date=latest_date,
            stats=stats,
            format_usd=format_usd,
            data=data
        )
    except Exception as err:
        print("OOPS", err)

        flash("Market Data Error. Please check your symbol and try again!", "danger")
        return redirect("/stocks/form")
