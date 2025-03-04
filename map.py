from pathlib import Path
import json
import plotly.express as px

# Load earthquake data
path = Path('data/readable_data.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Extract earthquake details safely
all_eq_dicts = all_eq_data['features']

mags, lats, lons, eq_titles = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']
    
    # Filter out invalid data
    if mag is not None and mag > 0:  
        mags.append(mag)
        lons.append(lon)
        lats.append(lat)
        eq_titles.append(eq_title)

# Create the scatter map
title = 'This project visualises earthquakes from past 5 years in the Indian Subcontinent Region'
subtitle = 'Tech Stack: Python, Plotly | Data Source: USGS Earthquake Dataset in GeoJSON format'
fig = px.scatter_geo(
    lat=lats,
    lon=lons,
    size=mags,
    color=mags,
    color_continuous_scale='Viridis',
    labels={'color': 'Magnitude'},
    projection='natural earth',
    hover_name=eq_titles
)

# Focus the map on the Indian subcontinent
fig.update_geos(
    scope="asia",  # Restrict to Asia region
    center={"lat": 23.5, "lon": 78.5},  # Center on India
    lataxis={"range": [5, 40]},  # Latitude range (South to North)
    lonaxis={"range": [60, 100]}  # Longitude range (West to East)
)

# Customize title appearance
fig.update_layout(
    title={
        'text': title,
        'font': {
            'size': 30,  # Font size
            'family': 'Arial',  # Font family
            'color': 'black'  # Font color
        },
        'x': 0.5,  # Center align the title
    },
    annotations=[
        {
            'text': subtitle,
            'xref': 'paper', 'yref': 'paper',  # Coordinate system
            # If you use 'paper' for xref and yref,
            # it puts this text anywhere on the paper
            # Example: A subtitle at the bottom of the map.

            # If you use 'x' and 'y',
            # it put this text next to a specific earthquake on the map.
            # Example: Labeling the biggest earthquake by pointing to it.
            
            'x': 0.5, 'y': -0.05,  # Move the subtitle belo chart x centers the text horizontally & y moves data below the char
            'showarrow': False,  # Whether to show an arrow pointing to something
            'font': {
                'size': 16,  # Increase font size slightly
                'family': 'Arial',
                'color': 'gray'
            }
        }
    ]
)

# Show the map
fig.show()
