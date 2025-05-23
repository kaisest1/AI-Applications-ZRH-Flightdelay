# AI-Applications-ZRH-Flightdelay
Project 1 for w.3KIA  

## Project Description
ZRH Flight Delay Prediction is a End-to-End Machine Learning application that estimates flight delays at Zurich Airport (ZRH) based on weather forecasts and flight informations.

## Results

### Name & URL
| Name          | URL |
|--------------|----|
| Huggingface  | [Huggingface Space](https://huggingface.co/spaces/kaisest1/ZRH-Flight-Delay) |
| Code         | [GitHub Repository](https://github.com/kaisest1/AI-Applications-ZRH-Flightdelay) |

## Data Sources and Features Used Per Source
Obtaining flight data from Zurich Airport proved to be very difficult. A large, publicly accessible dataset was not available. As a workaround, I used web scraping on Flightradar to retrieve flight data from the previous day. This approach allowed me to collect flight data for Zurich Airport covering the period from April 28, 2025, to May 18, 2025. Weather data, on the other hand, was easily accessible via MeteoStat for the weather station located in Zurich-Kloten.
| Data Source | Features |
|-------------|----------|
| [Flightradar24](https://www.flightradar24.com) | Time, Flight, Destination, Airline, Aircraft, Status |
| [Meteostat](https://meteostat.net/de/station/06670) | time, temp (Air Temperature), dwpt (Dew Point), rhum (Relative Humidity), prcp (Total Precipitation), snow (Snow Depth), wdir (Wind Direction), wspd (Average Wind Speed), wpgt (Wind Peak Gust), pres (Sea-Level Air Pressure), tsun (Total Sunshine Duration), coco (Weather Condition Code) |

### Weather Condition Codes
Source: [Meteostat Developers](https://dev.meteostat.net/formats.html#time-format)
| Code | Weather Condition         |
|------|---------------------------|
| 1    | Clear                    |
| 2    | Fair                     |
| 3    | Cloudy                   |
| 4    | Overcast                 |
| 5    | Fog                      |
| 6    | Freezing Fog             |
| 7    | Light Rain               |
| 8    | Rain                     |
| 9    | Heavy Rain               |
| 10   | Freezing Rain            |
| 11   | Heavy Freezing Rain      |
| 12   | Sleet                    |
| 13   | Heavy Sleet              |
| 14   | Light Snowfall           |
| 15   | Snowfall                 |
| 16   | Heavy Snowfall           |
| 17   | Rain Shower              |
| 18   | Heavy Rain Shower        |
| 19   | Sleet Shower             |
| 20   | Heavy Sleet Shower       |
| 21   | Snow Shower              |
| 22   | Heavy Snow Shower        |
| 23   | Lightning                |
| 24   | Hail                     |
| 25   | Thunderstorm             |
| 26   | Heavy Thunderstorm       |
| 27   | Storm                    |


## Features Created
| Feature | Description |
|---------|-------------|
| room_per_m2 | Room / area |
| price_per_m2 | Price / area (not used!) |
| Luxurious, temporary, furnished | Extracted binary feature from description_raw if luxurious, temporary, furnished |
| area_cat, area_cat_encoded | Encoded area into three groups:<br>0: 0 – 49 m²<br>1: 50 – 99 m²<br>2: 100 – 500 m² |
| (LOFT), (POOL), (ATTIKA), (EXKLUSIV), (SEESICHT), (LUXURIÖS) | One hot encoding of feature Luxurious depending on type of luxurious |
| Kreis 1-12 | One hot encoding of apartments in the city Zurich |
| zurich_city | Binary feature if apartment is in the city Zurich |

## Model Training

### Amount of Data
- Total of 7'487 flight records collected for Zurich Airport (ZRH).

### Data Splitting Method (Train/Validation/Test)

### Performance


## References


