from flask import Flask, render_template, request, redirect, url_for
from weather import main as get_weather
from weather import get_lat_lon

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    data = None
    if request.method == "POST":
        city = request.form["cityName"]
        data = get_weather(city)
        lat = get_lat_lon(city)[0]
        lon = get_lat_lon(city)[1]

    return redirect(url_for("city", data=data, lat=lat, lon=lon, city=city))


@app.route("/city")
def city():
    data = request.args.get("data")
    lat = request.args.get("lat")
    lon = request.args.get("lon")
    city = request.args.get("city")

    return render_template("city.html", data=data, lat=lat, lon=lon, city=city)


if __name__ == "__main__":
    app.run(debug=True)
