import plotly.graph_objects as go
import plotly_express as px


class DrawChart:
    def drawScatter(self, x_coordinate, y_coordinate, id):
        line = px.scatter(x=x_coordinate, y=y_coordinate, labels={'x': 'ord', 'y': 'PR'})
        fig = go.Figure(line)
        fig.write_html(f"./temp/plotly_scatter{id}.html")

    def drawBar(self, x_coordinate, y_coordinate, id):
        line = go.Bar(x=x_coordinate, y=y_coordinate)
        fig = go.Figure(line)
        fig.write_html(f"./temp/plotly_bar{id}.html")
