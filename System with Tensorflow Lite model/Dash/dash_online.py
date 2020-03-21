import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import datetime
from random import randint

X = deque(maxlen=20)
X.append(datetime.datetime.now())
Y = deque(maxlen=20)
Y.append(randint(1,30))


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        html.H1('On-line мониторинг', style={
                                'textAlign': 'center'
                            }),
        dcc.Graph(id='live-graph', animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*5000
        ),
    ]
)

@app.callback(Output('live-graph', 'figure'),
              [Input('graph-update', 'n_intervals')])
def update_graph_scatter(input_data):
    X.append(datetime.datetime.now())
    Y.append(randint(1,30))

    data = plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Scatter',
            mode= 'lines+markers'
            )
    

    return {'data': [data],'layout' : go.Layout(xaxis=dict(range=[min(X),max(X)]),
                                                yaxis=dict(range=[min(Y),max(Y)]),
                                                title={'text': 'Текущая дата 19/03/2020'},
                                                )}


if __name__ == '__main__':
    app.run_server()

