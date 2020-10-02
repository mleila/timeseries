# -*- coding: utf-8 -*-
from typing import Union, Optional

import numpy as np
import plotly.graph_objects as go


def plot_basic_timeseries(
    timeseries: Union[list, np.array],
    name: str=None,
    names: list=[],
    )-> go.Figure:

    fig = go.Figure()
    if type(timeseries) == list:
        title = f'Timeseries Data'
        names = names if names else [f'ts{i}' for i in range(len(timeseries))]
        for ts, name in zip(timeseries, names):
            scatter = go.Scatter(y=ts, mode='lines', name=name)
            fig.add_trace(scatter)
        fig.update_layout(title=title)
        return fig

    title = f'{name}' if name else ''
    scatter = go.Scatter(y=timeseries, mode='lines')
    fig.add_trace(scatter)
    fig.update_layout(title=title)
    return fig
