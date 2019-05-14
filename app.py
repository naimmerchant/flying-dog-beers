import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart
beers=['Spring', 'Summer', 'Fall', 'Winter']
ibu_values=[20, 30, 15, 8]
abv_values=[10, 15, 7, 2]
color1='red'
color2='blue'

bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name='High Temp',
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name='Low Temp',
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Weather Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Flying Dog Beers'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    ),
    html.A('Code on Github', href='https://github.com/austinlasseter/flying-dog-beers'),
    html.Br(),
    html.A('Data Source', href='https://www.flyingdog.com/beers/'),
    ]
)

if __name__ == '__main__':
    app.run_server()
