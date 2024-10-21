# Import packages
from dash import Dash, html, dash_table, dcc, callback, Output, Input
import pandas as pd
import plotly.express as px

# Incorporate data
df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')

# Initialize the app
app = Dash()

# Get a list of countries for the dropdown
countries = df['country'].unique()

# App layout
app.layout = html.Div([
    html.Div(children='My First App with Data, Graph, and Controls',style={'textAlign':'center'}),
    html.Hr(),
    dcc.Dropdown(options=[{'label': country, 'value': country} for country in countries],
                 value=countries[0], id='country-dropdown'),
    dcc.RadioItems(options=[
        {'label': 'Population', 'value': 'pop'},
        {'label': 'Life Expectancy', 'value': 'lifeExp'},
        {'label': 'GDP per Capita', 'value': 'gdpPercap'}
    ], value='pop', id='controls-and-radio-item'),
    dash_table.DataTable(data=df.to_dict('records'), page_size=6),
    dcc.Graph(figure={}, id='controls-and-graph')
])

# Add controls to build the interaction
@callback(
    Output(component_id='controls-and-graph', component_property='figure'),
    Input(component_id='country-dropdown', component_property='value'),
    Input(component_id='controls-and-radio-item', component_property='value')
)
def update_graph(selected_country, selected_metric):
    filtered_df = df[df['country'] == selected_country]
    fig = px.line(filtered_df, x='year', y=selected_metric, title=f'{selected_metric.capitalize()} over Years for {selected_country}')
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
