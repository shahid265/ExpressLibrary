# README.md for express_visualization_library

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

`express_visualization_library` is a Python package designed to streamline the data visualization process in a consultancy environment. This package aims to facilitate the quick transformation of data into insightful visualizations. It is developed on top of standard libraries such as Plotly and Circlify and offers easy integration with Power BI.

## Installation

```bash
pip install express_visualization_library
```

## Usage

```python
from express_visualization_library import bar_chart

# Create a bar chart
bar_chart(data, x='Name', y='Value')
```

### Available Charts:

- Bar chart with different variations
- Scatter plot with varying dot sizes
- Circle packing chart
- Hierarchical network chart
- Heatmaps

### Power BI Integration

Detailed steps on how to integrate the produced visualizations into Power BI will be updated soon.

## Contributing

For contributing guidelines, please refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for details.
