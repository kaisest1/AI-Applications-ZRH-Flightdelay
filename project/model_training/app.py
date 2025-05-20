# app.py
import gradio as gr
import pandas as pd
import pickle

# Mapping-Daten laden (z. B. Ziel, Airline, Aircraft-Codes)
df = pd.read_csv("zrh_flightdelay.csv")

# Wettervorhersage laden
forecast = pd.read_csv("forecast.csv")
forecast["time"] = pd.to_datetime(forecast["time"])

# Modell laden (local pickle file – du kannst den Pfad ggf. anpassen)
model_filename = "zrh-flight-delay.pkl"
with open(model_filename, "rb") as f:
    model = pickle.load(f)

# Mappings vorbereiten
destinations = sorted(df['DESTINATION'].unique().tolist())
airlines = sorted(df['AIRLINE'].unique().tolist())
aircrafts = sorted(df['AIRCRAFT'].unique().tolist())

city_to_code = dict(zip(df['DESTINATION'], df['DEST_CODE']))
airline_to_code = dict(zip(df['AIRLINE'], df['AIRLINE_CODE']))
aircraft_to_code = dict(zip(df['AIRCRAFT'], df['AIRCRAFT_CODE']))

# Verfügbare Datums- und Uhrzeitoptionen aus der Wettervorhersage
available_dates = sorted(forecast["time"].dt.strftime("%d.%m.%Y").unique().tolist())
available_hours = [f"{hour:02d}:00" for hour in range(5, 24)]

# Vorhersagefunktion
def predict(destination, airline, aircraft, datum, uhrzeit):
    try:
        datetime_input = pd.to_datetime(f"{datum} {uhrzeit}", format="%d.%m.%Y %H:%M")
    except:
        return "Invalid date or time format."

    row = forecast[forecast["time"] == datetime_input]
    if row.empty:
        return "No weather data available for the selected combination."

    # Wetterwerte aus forecast.csv lesen
    sea_level_pressure = row["pres"].values[0]
    wind_direction = row["wdir"].values[0]
    wind_peak_gust = row["wpgt"].values[0]
    temperature = row["temp"].values[0]

    # Mappings abrufen
    DEST_CODE = city_to_code.get(destination)
    AIRLINE_CODE = airline_to_code.get(airline)
    AIRCRAFT_CODE = aircraft_to_code.get(aircraft)

    if None in [DEST_CODE, AIRLINE_CODE, AIRCRAFT_CODE]:
        return "Invalid input for destination, airline, or aircraft."

    # Input für das Modell vorbereiten
    input_data = [[DEST_CODE, wind_peak_gust, AIRLINE_CODE, AIRCRAFT_CODE, wind_direction, sea_level_pressure, temperature]]
    prediction = model.predict(input_data)[0]

    return f"We estimate a {round(prediction)} minute delay for your {airline} flight to {destination}."

# Gradio-Interface
demo = gr.Interface(
    fn=predict,
    inputs=[
        gr.Dropdown(choices=destinations, label="Destination", value=None),
        gr.Dropdown(choices=airlines, label="Airline", value=None),
        gr.Dropdown(choices=aircrafts, label="Aircraft", value=None),
        gr.Dropdown(choices=available_dates, label="Date", value=None),
        gr.Dropdown(choices=available_hours, label="Time", value=None),
    ],
    outputs="text",
    title="ZRH Flight Delay Prediction",
    description="Select destination, airline, aircraft, as well as date and time (based on available forecast weather data) to predict the delay.",
    examples=[
        ["London", "Swiss", "A21N", "23.05.2025", "07:00"],
        ["Lisbon", "TAP Air Portugal", "A320", "24.05.2025", "12:00"],
        ["Abu Dhabi", "Etihad Airways", "B789", "25.05.2025", "11:00"],
        ["Paris", "Air France", "BCS3", "26.05.2025", "14:00"],
        ["Cape Town", "Edelweiss Air", "A343", "27.05.2025", "22:00"],
    ]
)


demo.launch()
