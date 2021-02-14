from flask import Flask, render_template, request, flash, redirect, url_for, jsonify
from flask_cors import CORS
import logging
from db.db import *
from db.db_functions import *

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = app.config['FLASK_SECRET_KEY']
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + database_file
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)
db.app = app
db.init_app(app)

logging.basicConfig(level=logging.DEBUG)


@app.route('/', methods=["get", "post"])
def index():
    flash("Welcome home !! " , "info")
    return render_template('index.html')


@app.route('/calculate', methods=['post'])
def calculate():
    try:
        # comment just for trying BFG BFG BFG
        # BFG
        app.logger.info('processing request')
        app.logger.info(request)
        app.logger.debug(request.get_json())
        items = request.get_json()
        amount = calculate_amount(items)
        app.logger.debug("amount is " + str(amount))
        app.logger.debug(type(int) is type(amount))
        app.logger.debug(type(amount))
        result = { "url": url_for('statement') + "?amount=" + str(amount)}
        return jsonify(result)
    except Exception as e:
        print(str(e))
        flash("Error occurred: " + str(e), "danger")
        return render_template('errors/404.html'), 400


@app.route('/statement')
def statement():
    flash("Please find your bill ", "info")
    return render_template('statement.html', amount=request.args.get('amount'), currency=app.config['CURRENCY'])


def calculate_amount(items):
    bookTypeInfo = get_book_types_and_charges()
    import json
    app.logger.debug(json.dumps(bookTypeInfo, indent=4))
    amount = 0
    for item in items:
        cost = 0
        originalCharge = bookTypeInfo[item["bookType"]]["charge"]
        minimumCharge = bookTypeInfo[item["bookType"]]["minimumCharge"]
        minimumRetention = bookTypeInfo[item["bookType"]]["minimumRetention"]
        trialCharge = bookTypeInfo[item["bookType"]]["trialCharge"]
        trialPeriod = bookTypeInfo[item["bookType"]]["trialPeriod"]

        quantity = item["bookQuantity"]
        duration = item["dayDuration"]

        if minimumCharge is None and minimumRetention is None:
            if trialPeriod is not None:
                cost = min(trialPeriod, duration) * quantity * trialCharge
                duration = duration - trialPeriod if duration > trialPeriod else 0
            cost += duration * quantity * originalCharge

        elif minimumRetention is None and minimumCharge is not None:
            if trialPeriod is not None:
                cost = min(trialPeriod, duration) * quantity * trialCharge
                duration = duration - trialPeriod if duration > trialPeriod else 0
            cost += duration * quantity * originalCharge
            cost = max(cost, minimumCharge)

        elif minimumCharge is not None and minimumRetention is not None:

            if duration < minimumRetention:
                cost = minimumCharge
            else:
                if trialPeriod is not None:
                    cost = min(trialPeriod, duration) * quantity * trialCharge
                    duration = duration - trialPeriod if duration > trialPeriod else 0
                cost += duration * quantity * originalCharge
        else:
            if trialPeriod is not None:
                cost = min(trialPeriod, duration) * quantity * trialCharge
                duration = duration - trialPeriod if duration > trialPeriod else 0
            cost += duration * quantity * originalCharge

        amount += cost
        app.logger.debug(cost)
    app.logger.debug(amount)
    return amount


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5020, debug=app.debug)