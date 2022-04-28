from flask import Flask, render_template
import sqlite3
import folium
from folium.plugins import HeatMap
import statistics as st

app = Flask(__name__)


@app.route("/")
def homePage():
    return render_template("MainPage.html")


@app.route("/airQualityIndex")
def airQualityIndexPage():
    # Establish a connection with the database
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()

    # Query Database
    cursor.execute('''SELECT * from UmbrellaDataTable''')
    data = cursor.fetchall()

    labels = []
    values = []

    # Lists storing values to be used for charts
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


@app.route("/volatileOrganicCompounds")
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
def gasSensorResistancePage():
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
def carbonDioxideEstimatePage():
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


@app.route("/heatMap")
def heatMapPage():
    initialLat = 51.501144
    initialLong = -2.548346
    initialZoomFactor = 10

    heatMap = folium.Map(location=[initialLat, initialLong], zoom_start=initialZoomFactor)

    # Node ID: RSE-L-A5-C
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()

    # Query database for data of a specific sensor node
    cursor.execute('''SELECT temperature from UmbrellaDataTable WHERE hostName = "RSE-L-A-5-C"''')
    nodeData1 = cursor.fetchall()
    conn.commit()
    conn.close()

    node1Values = []

    for row in nodeData1:
        node1Values.append(row[0])

    # Heatmap zone value scaled
    node1Average = st.mean(node1Values) / 10

    # [lat, long, measured value]
    node1 = [51.505145, -2.543547, node1Average],

    # Node ID: RSE-A-8-C
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT temperature from UmbrellaDataTable WHERE hostName = "RSE-A-8-C"''')
    nodeData2 = cursor.fetchall()
    conn.commit()
    conn.close()

    node2Values = []

    for row in nodeData2:
        node2Values.append(row[0])

    node2Average = st.mean(node2Values) / 10
    node2 = [51.503011, -2.544700, node2Average],

    # Node ID: RSS-A-28-C
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT temperature from UmbrellaDataTable WHERE hostName = "RSS-A-28-C"''')
    nodeData3 = cursor.fetchall()
    conn.commit()
    conn.close()

    node3Values = []

    for row in nodeData3:
        node3Values.append(row[0])

    node3Average = st.mean(node3Values) / 10
    node3 = [51.500519, -2.544032, node3Average],

    # Node ID: RSE-16-C
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT temperature from UmbrellaDataTable WHERE hostName = "RSE-16-C"''')
    nodeData4 = cursor.fetchall()
    conn.commit()
    conn.close()

    node4Values = []

    for row in nodeData4:
        node4Values.append(row[0])

    node4Average = st.mean(node4Values) / 10
    node4 = [51.501937, -2.550901, node4Average],

    # Node ID: RSE-12-C
    conn = sqlite3.connect('UmbrellaDataTable.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT temperature from UmbrellaDataTable WHERE hostName = "RSE-12-C"''')
    nodeData5 = cursor.fetchall()
    conn.commit()
    conn.close()

    node5Values = []

    for row in nodeData5:
        node5Values.append(row[0])

    node5Average = st.mean(node5Values) / 10
    node5 = [51.502245, -2.551147, node5Average],

    # Add heatmap zone objects to map
    HeatMap(node1).add_to(heatMap)
    HeatMap(node2).add_to(heatMap)
    HeatMap(node3).add_to(heatMap)
    HeatMap(node4).add_to(heatMap)
    HeatMap(node5).add_to(heatMap)

    # Generate heatmap page
    heatMap.save("templates/HeatMap.html")

    return render_template("HeatMap.html")


if __name__ == "__main__":
    app.run()
