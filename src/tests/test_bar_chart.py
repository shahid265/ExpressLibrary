import sys
sys.path.append('E:\Assignments\FTI\library\express_visualization_library')

import unittest
from src.visualizations.bar_chart import BarChart

class TestBarChart(unittest.TestCase):
    def test_basic_bar_chart(self):
        data = {'a': 1, 'b': 2, 'c': 3}
        x = list(data.keys())
        y = list(data.values())
        chart = BarChart(data, x, y)
        self.assertEqual(chart.x, x)
        self.assertEqual(chart.y, y)

        
