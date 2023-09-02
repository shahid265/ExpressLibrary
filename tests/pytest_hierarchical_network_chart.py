import sys
__package__ = "tests"
sys.path.append('E:\\Assignments\\FTI\\library\\ExpressLibrary')

import pytest
from src.visualizations.hierarchical_network_chart import HierarchicalNetworkChart  
import pandas as pd

@pytest.fixture
def sample_data():
    hierarchy_data = {
        'ID': [1, 2, 3, 4, 5],
        'Parent': ['Root', 1, 1, 2, 2],
        'Name': ['Root', 'Child1', 'Child2', 'Child1.1', 'Child1.2']
    }
    return pd.DataFrame(hierarchy_data)

def test_hierarchical_chart_initialization(sample_data):
    chart = HierarchicalNetworkChart(None)
    assert chart.data is None

def test_set_hierarchy(sample_data):
    chart = HierarchicalNetworkChart(None)
    chart.set_hierarchy(sample_data)
    assert isinstance(chart.hierarchy, pd.DataFrame)
    assert not chart.hierarchy.empty

