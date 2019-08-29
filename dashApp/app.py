import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

app = dash.Dash(
          __name__,
          external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])
server = app.server

app.css.append_css({"external_url":
                        "https://codepen.io/chriddyp/pen/bWLwgP.css"})

app.layout = html.Div([
    html.H4('Testing app'),
    dcc.Dropdown(
        id='dropdown',
        options=[{'label': 'option 1', 'value': 'A'},
                 {'label': 'option 2', 'value': 'B'}],
        value='A'),
    html.P(id='texts', children='initial value')
])

@app.callback(
    Output('texts', 'children'),
    [Input('dropdown', 'value')]
)
def callbackFunc(ivalue):
    if ivalue == 'A':
        ftext = 'initial value'
    elif ivalue == 'B':
        ftext = 'second option'
    else:
        ftext = 'something wrong'
    return ftext

if __name__ == '__main__':
    app.run_server(debug=True)