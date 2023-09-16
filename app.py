from flask import Flask, render_template, request
from weather import main as get_weather

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = None
    if request.method == "POST":
        city = request.form["cityName"]
        data = get_weather(city)

    return render_template("city.html", data=data, city=city)


if __name__ == "__main__":
    app.run(debug=True)
