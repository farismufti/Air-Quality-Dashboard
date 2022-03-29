from flask import Flask, render_template
import random
import sqlite3
import time
import parser

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("MainPage.html")


@app.route("/airQualityIndex")
def airQualityIndexPage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[2])

    conn.commit()
    conn.close()

    return render_template("AirQualityIndex.html", labels=labels, values=values)


@app.route("/humidityLevel")
def humidityLevelPage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[3])

    conn.commit()
    conn.close()

    return render_template("HumidityLevel.html", labels=labels, values=values)


@app.route("/airTemperature")
def airTemperaturePage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[4])

    conn.commit()
    conn.close()

    return render_template("AirTemperature.html", labels=labels, values=values)


@app.route("/airPressure")
def airPressurePage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[5])

    conn.commit()
    conn.close()

    return render_template("AirPressure.html", labels=labels, values=values)


@app.route("/volatileOrganicComounds")
def volatileOrganicCompoundsPage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[6])

    conn.commit()
    conn.close()

    return render_template("VolatileOrganicCompounds.html", labels=labels, values=values)


@app.route("/gasSensorResistance")
def carbonDioxideEstimatePage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[7])

    conn.commit()
    conn.close()

    return render_template("GasSensorResistance.html", labels=labels, values=values)


@app.route("/carbonDioxideEstimate")
def gasSensorResistancePage():
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    for row in data:
        labels.append(row[0])
        values.append(row[8])

    conn.commit()
    conn.close()

    return render_template("CarbonDioxideEstimate.html", labels=labels, values=values)


if __name__ == "__main__":
    app.run()
