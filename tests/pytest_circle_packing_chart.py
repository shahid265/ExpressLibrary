import sys
__package__ = "tests"
sys.path.append("E:\\Assignments\\FTI\\library\\express_visualization_library")
from src.visualizations.circle_packing_chart import SimpleCirclePackingChart, HierarchicalCirclePackingChart
from src.visualizations.base_packing_chart import BasePackingChart
import pytest

simple_data = [
    {'id': 'A', 'datum': 10},
    {'id': 'B', 'datum': 20},
    {'id': 'C', 'datum': 30},
]

hierarchical_data = [
    {'id': 'World', 'datum': 100, 'children': [
        {'id': 'Continent', 'datum': 70, 'children': [
            {'id': 'Country', 'datum': 40},
            {'id': 'Country', 'datum': 30}
        ]},
        {'id': 'Ocean', 'datum': 30}
    ]}
]

def test_base_chart_instantiation():
    chart = BasePackingChart(data=simple_data)
    assert isinstance(chart, BasePackingChart), "BasePackingChart should be instantiated"

def test_simple_chart_instantiation():
    chart = SimpleCirclePackingChart(data=simple_data)
    assert isinstance(chart, SimpleCirclePackingChart), "SimpleCirclePackingChart should be instantiated"

def test_hierarchical_chart_instantiation():
    chart = HierarchicalCirclePackingChart(data=hierarchical_data)
    assert isinstance(chart, HierarchicalCirclePackingChart), "HierarchicalCirclePackingChart should be instantiated"
