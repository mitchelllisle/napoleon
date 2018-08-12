![logo](https://user-images.githubusercontent.com/18128531/38246646-d345c070-3785-11e8-9a92-764d4fd6c369.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)
[![codecov](https://codecov.io/gh/mitchelllisle/napoleon/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/napoleon)

This is a simple Python package designed to make charting with Altair quicker and easier with some sensible defaults.

### Installation
`pip install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Altair](https://altair-viz.github.io/) charting library.

```python
import napoleon as nl
```

Chart Types:
```
nl.lineChart()
nl.barChart()
nl.areaChart()
```

### Examples

```python
from vega_datasets import data

stocks = data.stocks()
amazonStocks = stocks.query("symbol == 'AMZN'")

```
