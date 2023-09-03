# README.md for ExpressLibrary

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

`ExpressLibrary` is a Python package designed to streamline the data visualization process in a consultancy environment. This package aims to facilitate the quick transformation of data into insightful visualizations. It is developed on top of standard libraries such as Plotly and Circlify and offers easy integration with Power BI.

## Installation

```bash
pip install ExpressLibrary
```

## Usage

```python
from ExpressLibrary import BarChart

# Load your data (as pandas DataFrame)
data = ...

# Create chart
chart = BarChart(data, 'x_column_name', ['y_column_name'])
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue'])
chart.create_simple_bar()
```

### Available Charts:

- Bar chart with different variations
- Scatter plot with varying dot sizes
- Circle packing chart
- Hierarchical network chart
- Heatmaps

