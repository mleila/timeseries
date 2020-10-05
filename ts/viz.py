# -*- coding: utf-8 -*-
from pkg_resources import resource_filename
from typing import Union, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go


MPL_STYLE = 'https://gist.githubusercontent.com/mleila/2030f50322fc87764693c8e3501d5348/raw/ce54a5035178d9f2b65524a29c7b90b930d209a0/mleila.mplstyle'

def set_mpl_style():
    """
    Sets Matplotlib style.
    """
    plt.style.use(MPL_STYLE)


def plot_basic_timeseries(
    timeseries: Union[list, np.array],
    name: str=None,
    names: list=[],
    index: Union[pd.Series, list]=None
    )-> go.Figure:

    fig = go.Figure()
    if type(timeseries) == list:
        title = f'Timeseries Data'
        names = names if names else [f'ts{i}' for i in range(len(timeseries))]
        for ts, name in zip(timeseries, names):
            scatter = go.Scatter(x=index, y=ts, mode='lines', name=name)
            fig.add_trace(scatter)
        fig.update_layout(title=title)
        return fig

    title = f'{name}' if name else ''
    scatter = go.Scatter(x=index, y=timeseries, mode='lines')
    fig.add_trace(scatter)
    fig.update_layout(title=title)
    return fig
