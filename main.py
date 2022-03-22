import dash_bootstrap_components as dbc

from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

from detector import Detector
from translate import Translator
from smrz import summarize

app = Dash(__name__)
server = app.server

# App layout
app.layout = html.Div([
    dcc.Textarea(
        id='input',
        placeholder='Enter your text',
        autoFocus='autoFocus'
    ),
    dcc.Textarea(
        id='output',
        placeholder='Output...',
        readOnly='readOnly'
    ),
    html.Button(
        children='Summarize',
        id='button'
    ),
    html.H5(
        ['Original language: '], id='orig_lang'
    )
], id='main')

@app.callback(
    [Output('output', 'value'), Output('orig_lang', 'children')],
    Input('button', 'n_clicks'),
    State('input', 'value')
)
def func(n_clicks, input_value):
    if n_clicks is None:
        raise PreventUpdate
    elif n_clicks > 0:
        model = Detector()
        trans = Translator()

        lang = model.predict(input_value)
        translation = trans.toeng(input_value, lang)
        summary = summarize(input_value, translation)

        return summary, 'Original Language: %s' % lang
    return ''

if __name__ == '__main__':
    app.run_server(debug=False)