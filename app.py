from flask import Flask, render_template
import csv

app = Flask(__name__)


@app.route("/")
def index():
    films = []
    with open("recommendations.csv", newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            films.append(row)
    return render_template("index.html", films=films)


if __name__ == "__main__":
    app.run(debug=True)
