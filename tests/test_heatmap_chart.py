import sys
import pytest
import plotly
import numpy as np
import sys
__package__ = "tests"
# sys.path.append('E:\\Assignments\\FTI\\library\\ExpressLibrary')


from src.visualizations.heatmap_chart import HeatmapChart

# Test the constructor and set_color_scheme
def test_constructor_and_set_color_scheme():
    data = np.array([[1, 2], [3, 4]])
    chart = HeatmapChart(data, title="Test", color_scheme="Viridis")
    assert chart.title == "Test"
    assert chart.color_scheme == "Viridis"
    
    chart.set_color_scheme("Plasma")
    assert chart.color_scheme == "Plasma"

# # Test the render function 
# def test_render():
#     data = np.array([[1, 2], [3, 4]])
#     chart = HeatmapChart(data)
#     chart.render()
#     fig_data = chart.fig.to_dict()  # Convert the figure to a dict
    
#     # Asserts on the figure dictionary
#     assert fig_data['data'][0]['type'] == 'heatmap'
#     assert fig_data['layout']['title']['text'] == chart.title


