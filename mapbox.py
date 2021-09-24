import os

import pandas as pd

from mapboxgl.utils import create_color_stops, df_to_geojson
from mapboxgl.viz import CircleViz
TOKEN='pk.eyJ1IjoiMzA1NzU4MDI2OCIsImEiOiJjazgyaWM4ZmkxMW5kM2ZvcTY4dGR4amtjIn0.TJrXjIIqVSpQOHM6MS_g6g'

# Load data from sample csv
data_url = 'https://raw.githubusercontent.com/mapbox/mapboxgl-jupyter/master/examples/data/points.csv'
df = pd.read_csv(data_url)

# Must be a public token, starting with `pk`
token = os.getenv(TOKEN)

# Create a geojson file export from a Pandas dataframe
df_to_geojson(df, filename='points.geojson',
              properties=['Avg Medicare Payments', 'Avg Covered Charges', 'date'],
              lat='lat', lon='lon', precision=3)

# Generate data breaks and color stops from colorBrewer
color_breaks = [0,10,100,1000,10000]
color_stops = create_color_stops(color_breaks, colors='YlGnBu')

# Create the viz from the dataframe
viz = CircleViz('points.geojson',
                access_token=token,
                height='400px',
                color_property = "Avg Medicare Payments",
                color_stops = color_stops,
                center = (-95, 40),
                zoom = 3,
                below_layer = 'waterway-label'
              )
viz.show()