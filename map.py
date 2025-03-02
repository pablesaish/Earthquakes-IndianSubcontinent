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
title = 'Earthquakes in the Indian Subcontinent'
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
            'size': 35,  # Font size
            'family': 'Arial',  # Font family
            'color': 'black'  # Font color
        },
        'x': 0.5,  # Center align the title
    }
)

# Show the map
fig.show()
