# Earthquake Map of the Indian Subcontinent 🌍

## Overview

This project visualizes earthquakes in the **Indian Subcontinent** over the past five years using **Python**. The data is collected from the [United States Geological Survey (USGS)](https://www.usgs.gov/programs/earthquake-hazards) and displayed using **Plotly Express**.

## Features

✅ Interactive map of earthquakes in the Indian Subcontinent 📍\
✅ Data sourced from USGS in **GeoJSON** format 🌐\
✅ Visual representation of earthquake magnitude using **scatter plots** 🎨\
✅ Focused on the **last five years of earthquake data** 📊

## Tech Stack Used

- **Python** 🐍
- **Plotly Express** for interactive visualization 📈
- **JSON** for data handling 📄
- **GeoJSON** format for spatial data 📌

## Data Source

The earthquake data is fetched from the **USGS Earthquake Hazards Program** using their [GeoJSON data](https://earthquake.usgs.gov/fdsnws/event/1/query.geojson?starttime=2019-01-1%2000:00:00&endtime=2025-03-02%2023:59:59&maxlatitude=36.015&minlatitude=5.596&maxlongitude=95.273&minlongitude=67.676&minmagnitude=1&orderby=time). The dataset includes:

- **Magnitude** of the earthquake
- **Location** (Latitude & Longitude)
- **Date & Time** of occurrence

## Installation & Usage 🚀

### Prerequisites

Make sure you have **Python** installed along with the following libraries:

```bash
pip install plotly
```

### Running the Script

1. Clone this repository:
   ```bash
   git clone https://github.com/pablesaish/Earthquakes-IndianSubcontinent.git
   ```
2. Run the Python script:
   ```bash
   python map.py
   ```
3. The interactive map will be displayed in your web browser!

## Future Enhancements ✨

🔹 Improve UI with custom markers & tooltips\
🔹 Add filtering options based on magnitude & date\
🔹 Integrate real-time earthquake updates

## Contributing 🤝

Feel free to contribute by submitting **issues** or **pull requests**!

Made with ❤️ using Python & Plotly. Happy Coding! 🎯

