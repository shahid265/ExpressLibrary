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
from ExpressLibrary import bar_chart

# Create a bar chart
bar_chart(data, x='Name', y='Value')
```

### Available Charts:

- Bar chart with different variations
- Scatter plot with varying dot sizes
- Circle packing chart
- Hierarchical network chart
- Heatmaps

