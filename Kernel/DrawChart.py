import plotly.graph_objects as go  # 画柱状图的库
import plotly_express as px  # 画散点图的库


# 用于绘制图像的类
class DrawChart:

    # 绘制散点图
    @staticmethod
    def drawScatter(x_coordinate, y_coordinate, id, data=None):
        line = px.scatter(x=x_coordinate, y=y_coordinate, labels={'x': 'ord', 'y': 'PR'}, text=data)
        fig = go.Figure(line)
        fig.update_traces(textposition='top center', textfont_size=1)
        fig.write_html(f"./temp/plotly_scatter{id}.html")

    # 绘制柱状图
    @staticmethod
    def drawBar(x_coordinate, y_coordinate, id):
        line = go.Bar(x=x_coordinate, y=y_coordinate)
        fig = go.Figure(line)
        fig.write_html(f"./temp/plotly_bar{id}.html")
