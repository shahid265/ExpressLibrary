import pytest
import pandas as pd
import sys
__package__ = "tests"
sys.path.append("E:\\Assignments\\FTI\\library\\express_visualization_library")
from src.visualizations.scatter_plot import ScatterPlot

# Sample data for the basic tests
data_dict = {
    'X': [1, 2, 3],
    'Y': [10, 11, 12]
}
df = pd.DataFrame(data_dict)

# Sample data for advanced features
data_dict_advanced = {
    'X': [1, 2, 3, 4],
    'Y': [10, 11, 12, 13],
    'HoverText': ['A', 'B', 'C', 'D'],
    'Size': [10, 20, 30, 40]
}
df_advanced = pd.DataFrame(data_dict_advanced)

def test_scatter_plot_initialization():
    chart = ScatterPlot(df, 'X', 'Y')
    assert chart.data.equals(df)
    assert chart.x == 'X'
    assert chart.y == 'Y'

def test_set_labels():
    chart = ScatterPlot(df, 'X', 'Y')
    chart.set_labels('X-Axis', 'Y-Axis')
    assert chart.x_label == 'X-Axis'
    assert chart.y_label == 'Y-Axis'

def test_set_colors():
    chart = ScatterPlot(df, 'X', 'Y')
    chart.set_colors(['red'])
    assert chart.colors == ['red']

def test_set_hover_text():
    chart = ScatterPlot(df_advanced, 'X', 'Y')
    chart.set_hover_text('HoverText')
    assert (chart.hover_text == df_advanced['HoverText']).all()

def test_set_varying_dot_sizes():
    chart = ScatterPlot(df_advanced, 'X', 'Y')
    chart.set_varying_dot_sizes('Size')
    assert (chart.varying_dot_sizes == df_advanced['Size']).all()

