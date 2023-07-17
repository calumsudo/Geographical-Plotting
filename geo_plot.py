import plotly.graph_objs as go
import pandas as pd
from plotly.offline import init_notebook_mode, iplot, plot

df = pd.read_csv('World Energy Consumption.csv')

data = dict(
    type='choropleth',
    colorscale='Viridis',
    reversescale=True,
    locations=df['country'],
    locationmode='country names',
    z=df['gdp'],
    text=df['country'],
    colorbar={'title': 'GDP'},
)

layout = dict(
    title='GDP',
    geo=dict(showframe=False, projection={'type': 'natural earth'})
)

choromap = go.Figure(data=[data], layout=layout)

# Save the plot as an HTML file
plot(choromap, filename='choropleth.html', auto_open=True)



# Bar plot: Coal Production Change Percentage
bar_data = go.Bar(
    x=df['country'],
    y=df['coal_prod_change_pct'],
    name='Coal Production Change Percentage'
)
bar_layout = go.Layout(
    title='Coal Production Change Percentage by Country',
    xaxis={'title': 'Country'},
    yaxis={'title': 'Coal Production Change Percentage'}
)
bar_figure = go.Figure(data=[bar_data], layout=bar_layout)

# Line plot: Oil Production Change Percentage
line_data = go.Scatter(
    x=df['country'],
    y=df['oil_prod_change_pct'],
    mode='lines',
    name='Oil Production Change Percentage'
)
line_layout = go.Layout(
    title='Oil Production Change Percentage by Country',
    xaxis={'title': 'Country'},
    yaxis={'title': 'Oil Production Change Percentage'}
)
line_figure = go.Figure(data=[line_data], layout=line_layout)

# Save the plots as HTML files
plot(bar_figure, filename='coal_prod_change.html', auto_open=True)
plot(line_figure, filename='oil_prod_change.html', auto_open=True)