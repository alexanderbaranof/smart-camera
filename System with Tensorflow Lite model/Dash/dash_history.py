import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime

app = dash.Dash()

df = pd.read_csv('result.csv')

app.layout = html.Div([
    html.H1('Просмотр исторических данных', style={
                                'textAlign': 'center'
                            }),
   dcc.DatePickerSingle(
        id='pick-date',
        date = datetime.now(),
        style={'margin': '0 auto'})
    , 
   dcc.Graph(
      id='life-exp-vs-gdp',
      figure={
         'data': [
            go.Scatter(
               x=df['date-time'].astype(str).tolist(),
               y=df['count'].tolist(),
            )
         ]
         
      }
   )
], style= dict(justifyContent='center'))



if __name__ == '__main__':
    app.run_server()