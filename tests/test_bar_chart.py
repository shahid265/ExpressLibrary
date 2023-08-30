# # import unittest
# # import os
# # from src.visualizations.bar_chart import BarChart




import pytest
import pandas as pd
import sys
__package__ = "tests"
sys.path.append("E:\\Assignments\\FTI\\library\\express_visualization_library")
from src.visualizations.bar_chart import BarChart

# Sample data for the tests
data_dict = {
    'Category': ['A', 'B', 'C'],
    'Value1': [1, 2, 3],
    'Value2': [4, 5, 6]
}
df = pd.DataFrame(data_dict)
# x = 'Category'
# y = ['Value1', 'Value2']
# chart = BarChart(df, x, y)

# chart.create_stacked_bar()
# chart.create_grouped_bar()

def test_bar_chart_initialization():
    chart = BarChart(df, 'Category', ['Value1', 'Value2'])
    assert chart.data.equals(df)
    assert chart.x == 'Category'
    assert chart.y == ['Value1', 'Value2']

def test_set_labels():
    chart = BarChart(df, 'Category', ['Value1', 'Value2'])
    chart.set_labels('X-Axis', 'Y-Axis')
    assert chart.x_label == 'X-Axis'
    assert chart.y_label == 'Y-Axis'

def test_set_colors():
    chart = BarChart(df, 'Category', ['Value1', 'Value2'])
    chart.set_colors(['red', 'blue'])
    assert chart.colors == ['red', 'blue']

def test_validate_data():
    chart = BarChart(df, 'Category', ['Value1', 'Value2'])
    assert chart.validate_data() is None

def test_validate_data_invalid_column():
    with pytest.raises(ValueError):
        chart = BarChart(df, 'InvalidCategory', ['Value1', 'Value2'])
        chart.validate_data()

def test_validate_data_insufficient_colors():
    with pytest.raises(ValueError):
        chart = BarChart(df, 'Category', ['Value1', 'Value2'])
        chart.set_colors(['red'])
        chart.validate_data()
