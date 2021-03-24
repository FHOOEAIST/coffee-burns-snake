import io
from base64 import b64encode

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas
import plotly.graph_objects as go

buffer = io.StringIO()

df = pandas.read_csv("Runtime.csv", delimiter=";")

fig = go.Figure()
for column in df.columns:
    fig.add_trace(go.Box(y=df[column], name=column))

fig.update_layout(
    template="plotly_dark",
    title="Runtime Comparison",
    xaxis_title="Execution Name",
    yaxis_title="Runtime [ms]",
)

# fig = px.box(df, color=df.columns)
fig.write_html(buffer)

html_bytes = buffer.getvalue().encode()
encoded = b64encode(html_bytes).decode()

app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(id="graph", figure=fig),
    html.A(
        html.Button("Download HTML"),
        id="download",
        href="data:text/html;base64," + encoded,
        download="plotly_graph.html"
    )
])

app.run_server(debug=True, use_reloader=False)
