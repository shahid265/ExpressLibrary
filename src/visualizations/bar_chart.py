from .base_chart import BaseChart
import plotly.graph_objects as go

class BarChart(BaseChart):
    def __init__(self, data, x, y):
        super().__init__(data, x, y)
    

    def set_labels(self, x_label, y_label):
        self.x_label = x_label
        self.y_label = y_label

    def set_colors(self,colors):
        self.colors = colors
    
    def render(self):
        fig = go.Figure(data=[go.Bar(x=self.x, y=self.y)])
        fig.update_xaxes(title_text=self.x_label)
        fig.update_yaxes(title_text=self.y_label)   
        fig.show()