# Geogrphical-Plotting
plotly graphs based on World Energy Consumption using pandas
# World Energy Consumption Data Analysis

This repository contains data analysis and visualizations of world energy consumption. It utilizes the Plotly library in Python to create interactive choropleth, bar, and line plots based on the provided dataset.

## Dataset

The dataset used in this project is called "World Energy Consumption.csv" and contains information on various energy-related metrics for different countries. The columns in the dataset include:

- iso_code
- country
- year
- coal_prod_change_pct
- coal_prod_change_twh
- gas_prod_change_pct
- gas_prod_change_twh
- oil_prod_change_pct
- oil_prod_change_twh
- energy_cons_change_pct
...
- solar_elec_per_capita
- solar_energy_per_capita
- gdp
- wind_share_elec
- wind_cons_change_pct
- wind_share_energy
- wind_cons_change_twh
- wind_consumption
- wind_elec_per_capita
- wind_energy_per_capita

## Plots

The following plots are generated from the dataset:

1. Choropleth Plot: Visualizes the GDP (Gross Domestic Product) of countries using a color-coded map.

2. Bar Plot: Displays the coal production change percentage by country.

3. Line Plot: Shows the oil production change percentage by country.

## Usage

To use this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/world-energy-consumption.git`

2. Install the necessary dependencies: `pip install -r requirements.txt`

3. Run the Python script to generate the plots: `python geo_plot.py`

4. Open the generated HTML files in your web browser to view the plots.

Feel free to customize and modify the code to suit your needs or use it as a reference for your own data analysis projects.

## Dependencies

This project relies on the following dependencies:

- Plotly: A Python graphing library for interactive visualizations.

- pandas: A powerful data manipulation library for data analysis.

Make sure to install these dependencies before running the code.
