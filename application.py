from flask import Flask, redirect, render_template, request, url_for
import os
import sys
import helpers
from analyzer import Analyzer

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # validate screen_name
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    analyzer = Analyzer(positives, negatives)

    # get screen_name's tweets
    tweets = helpers.get_user_timeline(screen_name, 100)
    positiveVal, negativeVal, neutralVal = 0.0, 0.0, 0.0

    for lines in tweets:
        score = analyzer.analyze(lines)
        if score > 0.0:
            positiveVal = positiveVal + 1
        elif score < 0.0:
            negativeVal = negativeVal + 1
        else:
            neutralVal = neutralVal + 1

    total = positiveVal + negativeVal + neutralVal



    # TODO
    positive, negative, neutral = positiveVal/total, negativeVal/total, neutralVal/total

    # generate chart
    chart = helpers.chart(positive, negative, neutral)

    # render results
    return render_template("search.html", chart=chart, screen_name=screen_name)
