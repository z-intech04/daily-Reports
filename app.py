from data_store import save_user_cart, get_user_cart


# app.py
from flask import Flask, render_template, request
from agent import parse_grocery_note
from blinkit_bot import search_blinkit

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    grocery_list = []
    blinkit_results = []

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            ai_output = parse_grocery_note(note)

            # Evaluate AI JSON safely
            try:
                grocery_list = eval(ai_output)
            except:
                grocery_list = []

            # Search on Blinkit for each item
            for item in grocery_list:
                result = search_blinkit(item["item"])
                blinkit_results.append(result)

    return render_template("index.html", grocery_list=grocery_list, blinkit_results=blinkit_results)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request
from blinkit_bot import search_blinkit

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    grocery_list = []
    blinkit_results = []
    username = "default_user"  # Later you can make login logic

    if request.method == "POST":
        note = request.form.get("note")
        if note:
            ai_output = parse_grocery_note(note)

            try:
                grocery_list = eval(ai_output)
            except:
                grocery_list = []

            for item in grocery_list:
                result = search_blinkit(item["item"])
                blinkit_results.append(result)

                total_cost = sum(item["price_numeric"] for item in blinkit_results)

            # Save cart to JSON
            save_user_cart(username, grocery_list, blinkit_results)

    # Show previously saved cart if any
    previous_data = get_user_cart(username)

    return render_template("index.html",
                           grocery_list=grocery_list,
                           blinkit_results=blinkit_results,
                           previous_data=previous_data)


"""Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)"""
