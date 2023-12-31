Certainly! Here's the user documentation in Markdown format:
# ExpressLibrary: User Documentation

## Table of Contents
1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Base Chart](#base-chart)
4. [Bar Chart](#bar-chart)
   - [Simple Bar Chart](#simple-bar-chart)
   - [Stacked Bar Chart](#stacked-bar-chart)
   - [Grouped Bar Chart](#grouped-bar-chart)
5. [Scatter Plot](#scatter-plot)
   - [Basic Scatter Plot](#basic-scatter-plot)
   - [Scatter Plot with Varying Dot Sizes](#scatter-plot-with-varying-dot-sizes)
6. [Circle Packing Charts](#circle-packing-charts)
   - [Simple Circle Packing](#simple-circle-packing)
   - [Hierarchical Circle Packing](#hierarchical-circle-packing)
7. [Hierarchical Network Charts](#hierarchical-network-charts)
7. [Heatmap Chart](#heatmap)


## Introduction
The ExpressLibrary allows you to effortlessly create interactive visualizations using the Plotly library. The main goal is to provide a simple interface for creating a variety of charts without much hassle.

## Installation
To install the ExpressLibrary, clone the GitHub repository or download it directly. Once you've downloaded the library, navigate to the root directory and run the setup script.

```bash
python setup.py install
```

## Base Chart
All charts in the library inherit from the BaseChart class. This class provides common functionalities like data loading and axis setting.

## Bar Chart

### Simple Bar Chart
To create a simple bar chart:

```python
from ExpressLibrary.visualizations.bar_chart import BarChart

# Load your data (as pandas DataFrame)
data = ...

# Create chart
chart = BarChart(data, 'x_column_name', ['y_column_name'])
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue'])
chart.create_simple_bar()
```

### Stacked Bar Chart
To visualize data in a stacked format:

```python
chart = BarChart(data, 'x_column_name', ['y1_column_name', 'y2_column_name'])
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue', 'red'])
chart.create_stacked_bar()
```

### Grouped Bar Chart
To visualize data in a grouped format:

```python
chart = BarChart(data, 'x_column_name', ['y1_column_name', 'y2_column_name'])
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue', 'red'])
chart.create_grouped_bar()
```

## Scatter Plot

### Basic Scatter Plot
To visualize data in a scatter format:

```python
from ExpressLibrary.visualizations.scatter_plot import ScatterPlot

# Load your data
data = ...

# Create scatter plot
chart = ScatterPlot(data, 'x_column_name', 'y_column_name')
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue'])
chart.render()
```

### Scatter Plot with Varying Dot Sizes
To represent another dimension in your data, you can use varying dot sizes:

```python
chart = ScatterPlot(data, 'x_column_name', 'y_column_name')
chart.set_labels('X Label', 'Y Label')
chart.set_colors(['blue'])
chart.set_varying_dot_sizes('size_column_name')
chart.render()
```

## Circle Packing Charts

### Simple Circle Packing

Use `SimpleCirclePackingChart` to visualize non-hierarchical data in a circle packing layout.

Example:

```python
from ExpressLibrary.visualizations.circle_packing_chart import SimpleCirclePackingChart

data = [5, 10, 15]
chart = SimpleCirclePackingChart(data)
chart.render()
```

### Hierarchical Circle Packing

Use `HierarchicalCirclePackingChart` to visualize hierarchical data.

Example:

```python
from ExpressLibrary.visualizations.circle_packing_chart import HierarchicalCirclePackingChart

# data is a nested structure representing the hierarchy
chart = HierarchicalCirclePackingChart(data)
chart.render()
```

## Hierarchical Network Charts

Visualize hierarchical data as a network chart.

Example:

```python
from ExpressLibrary.visualizations.hierarchical_network_chart import HierarchicalNetworkChart

# data should be a DataFrame with ID, Parent, and Name columns
chart = HierarchicalNetworkChart(data)
chart.render()
```
## Heatmap

You can create a heatmap like this:

```python
from ExpressLibrary.visualizations.heatmap_chart import HeatmapChart
import numpy as np

data = np.array([[1, 2], [3, 4]])
chart = HeatmapChart(data, title="Sample Heatmap")
chart.set_color_scheme("Viridis")
chart.render()
```

### Features:

- **Color Scheme**: You can set the color scheme of the heatmap using the `set_color_scheme()` method.
