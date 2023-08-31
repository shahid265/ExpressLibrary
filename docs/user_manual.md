Certainly! Here's the user documentation in Markdown format:
# Express Visualization Library: User Documentation

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


## Introduction
The Express Visualization Library allows you to effortlessly create interactive visualizations using the Plotly library. The main goal is to provide a simple interface for creating a variety of charts without much hassle.

## Installation
To install the Express Visualization Library, clone the GitHub repository or download it directly. Once you've downloaded the library, navigate to the root directory and run the setup script.

```bash
python setup.py install
```

## Base Chart
All charts in the library inherit from the BaseChart class. This class provides common functionalities like data loading and axis setting.

## Bar Chart

### Simple Bar Chart
To create a simple bar chart:

```python
from visualizations import BarChart

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
from visualizations import ScatterPlot

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

