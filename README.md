# Introduction
This repository provides a high-level overview of modern techniques for time series analysis and Forecasting. Jupyter Notebooks will be used to explain concepts and show code and visualizations. I also developed an accompanying core library `ts` to provide useful functionality in a modular and systematic way to all notebooks.

# Installation
You can install the core library by cloning this repository and then following these steps
```bash
git clone https://github.com/mleila/timeseries
cd timeseries
pip install -r requirements.txt
```
This will install the core library in your virtualenv and you'll be able to run the notebooks. Make sure you are using `Python 3` (preferably 3.7).

# Guide
The notebooks are divided into the following three categories

## Time Series Concepts
These notebooks provide a high-level overview of some of the useful ideas for time series analysis and forecasting.

- [Digital Signal Processing and Fourier Analysis](https://github.com/mleila/timeseries/blob/master/notebooks/01_Concepts/01_Digital%20Signal%20Processing.ipynb)
- [Classic Time Series Models](https://github.com/mleila/timeseries/blob/master/notebooks/01_Concepts/02_Classic%20Time%20Series%20Models.ipynb)
- Machine Learning for Time Series Analysis and Forecasting
- Deep Learning for Time Series Analysis and Forecasting

## Time Series Data Processing and Visualization

- [Interesting Time Series Datasets](https://github.com/mleila/timeseries/blob/master/notebooks/02_Processing/01_Interesting%20Time%20Series%20Datasets.ipynb)
- [Visualizing Time Series Data with Matplotlib and Plotly](https://github.com/mleila/timeseries/blob/master/notebooks/02_Processing/02_Visualizing%20Time%20Series%20Data%20with%20Matplotlib%20and%20Plotly.ipynb)
- [Spark and Pandas Time Series Pipelines](https://github.com/mleila/timeseries/blob/master/notebooks/02_Processing/03_Spark%20and%20Pandas%20Time%20Series%20Pipelines.ipynb)
- Dealing with Missing Data

## Popular Time Series Python Libraries

- Facebook's Prophet
- [Statsmodels](https://github.com/mleila/timeseries/blob/master/notebooks/03_Libraries/01_statsmodels.ipynb)
