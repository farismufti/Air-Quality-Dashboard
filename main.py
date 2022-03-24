from flask import Flask, render_template
import random

app = Flask(__name__)


@app.route("/homePage")
def home():
    return render_template("MainPage.html")


@app.route("/airQualityIndex")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("AirQualityIndex.html", labels=labels, values=values)


@app.route("/humidityLevel")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("HumidityLevel.html", labels=labels, values=values)


@app.route("/temperature")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("Temperature.html", labels=labels, values=values)


@app.route("/airPressure")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("AirPressure.html", labels=labels, values=values)


@app.route("/volatileOrganicComounds")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("VolatileOrganicCompounds.html", labels=labels, values=values)


@app.route("/carbonDioxideEstimate")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("CarbonDioxideEstimate.html", labels=labels, values=values)


@app.route("/gasSensorResistance")
def airQualityIndexPage():
    data = [
        ("01-01-2022", random.randrange(1, 70)),
        ("02-01-2022", random.randrange(1, 70)),
        ("03-01-2022", random.randrange(1, 70)),
        ("04-01-2022", random.randrange(1, 70)),
        ("05-01-2022", random.randrange(1, 70)),
        ("06-01-2022", random.randrange(1, 70)),
        ("07-01-2022", random.randrange(1, 70)),
    ]

    labels = [row[0] for row in data]
    values = [row[1] for row in data]

    return render_template("GasSensorResistance.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run()
