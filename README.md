![logo](https://user-images.githubusercontent.com/18128531/38246646-d345c070-3785-11e8-9a92-764d4fd6c369.png)

[![CircleCI](https://circleci.com/gh/mitchelllisle/napoleon.svg?style=svg)](https://circleci.com/gh/mitchelllisle/napoleon)
[![codecov](https://codecov.io/gh/mitchelllisle/napoleon/branch/master/graph/badge.svg)](https://codecov.io/gh/mitchelllisle/napoleon)

This is a simple Python package designed to make charting with Altair quicker and easier with some sensible defaults.

### Installation
`pip3 install git+https://github.com/mitchelllisle/napoleon`

#### Upgrade
`pip3 install --upgrade git+https://github.com/mitchelllisle/napoleon`

### Getting Started
The whole idea of Napoleon was to make it much quicker to go from data to chart using the [Altair](https://altair-viz.github.io/) charting library.

```python
import napoleon as nl
```

Chart Types:
```python
nl.line()
nl.bar()
nl.area()
nl.scatter()

# Coming soon
nl.hist()
nl.heatmap()
nl.boxPlot()
nl.candleStick()
nl.streamGraph()
nl.scatterHist()
```

### Examples

```python
from vega_datasets import data

stocks = data.stocks()

nl.line(data = stocks, x = "date:T", y = "price:Q", color = "symbol")
```
![visualization](https://user-images.githubusercontent.com/18128531/44091662-8af9df28-a011-11e8-8bb5-1b8a9db357a1.png)


```python
from vega_datasets import data

stocks = data.stocks()

scatterData = stocks.groupby("symbol").agg({"price" : ["mean", "max"]}).reset_index()
scatterData.columns = ['symbol', 'mean', 'max']

scatter(data = scatterData, x = "symbol", y = 'mean', color = "symbol", size = "max")
```
![visualization](https://user-images.githubusercontent.com/18128531/44295509-a4c31f80-a2ed-11e8-8db1-b256e45f2499.png)


```python
import numpy as np
import pandas as pd
import napoleon as nl

df = pd.DataFrame({'Trial A': np.random.normal(0, 0.8, 1000),
                   'Trial B': np.random.normal(-2, 1, 1000),
                   'Trial C': np.random.normal(3, 2, 1000)})

df = pd.melt(df, id_vars=df.index.name,
             value_vars=df.columns,
             var_name='Experiment',
             value_name='Measurement')

nl.hist(df, 'Measurement', color = 'Experiment', bins = 100)
```
![visualization](https://user-images.githubusercontent.com/18128531/44845601-515bb480-ac91-11e8-93cb-f0aa7bd93822.png)
