# -*- coding: utf-8 -*-
from pkg_resources import resource_filename
from typing import Union, Optional

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf


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


def plot_train_test(data, indices, names):
    fig = go.Figure()
    for ts, index, name in zip(data, indices, names):
        scatter = go.Scatter(x=index, y=ts, mode='lines', name=name)
        fig.add_trace(scatter)
    return fig


def plot_acf_pacf(data):
    """
    Plot the ACF and PACF plots side by side. Uses the statsmodels plotting functions.
    """
    fig, axs = plt.subplots(1, 2)
    ax1, ax2 = axs

    plot_acf(data, ax=ax1)
    plot_pacf(data, ax=ax2)


def plot_gp_priors(gp, X, y, nb_samples=10):
    '''
    Plot Gaussian Process Priors
    '''
    gp_prior_samples = gp.sample_y(X=X.reshape(-1, 1), n_samples=nb_samples)

    fig = go.Figure()
    for i in range(nb_samples):
        scatter = go.Scatter(
            x=X,
            y=gp_prior_samples[:,i],
            mode='lines',
            name=f'sample_{i}',
            opacity=.2,
            marker=dict(color='gray'))
        fig.add_trace(scatter)

    # add real data
    scatter = go.Scatter(x=X, y=y, mode='lines', name='original')
    fig.add_trace(scatter)

    # format figure
    title = f'Gaussian Process Priors'
    fig.update_layout(title=title)
    return fig


def plot_gp_ts(
    X_train,
    X_test,
    y_train,
    y_test,
    y_train_pred,
    y_test_pred,
    y_std=None,
    ):
    '''
    '''

    # configure
    blue_marker = dict(color='blue')
    red_marker = dict(color='red')

    # make figure
    fig = go.Figure()

    # add original data
    Xs = np.append(X_train, X_test)
    ys = np.append(y_train, y_test)
    scatter = go.Scatter(x=Xs, y=ys, mode='lines', name='original', marker=blue_marker)
    fig.add_trace(scatter)

    # add prediction
    ypreds = np.append(y_train_pred, y_test_pred)
    scatter = go.Scatter(x=Xs, y=ypreds, mode='lines', name='prediction', marker=red_marker)
    fig.add_trace(scatter)

    # add confidence intervals
    if y_std is None:
        return fig

    # training
    y_upper = ys + 2*y_std
    y_lower = ys - 2*y_std
    scatter = go.Scatter(
            x= np.append(Xs , Xs[::-1]), # x, then x reversed
            y= np.append(y_upper, y_lower[::-1]), # upper, then lower reversed
            fill='toself',
            fillcolor='rgba(0,100,80,0.2)',
            line=dict(color='rgba(255,255,255,0)'),
            hoverinfo="skip",
            showlegend=False
        )
    fig.add_trace(scatter)

    # add vertical line
    l_min, lmax = min(ys), max(ys)
    shapes = [dict(
        type= 'line', y0=l_min, y1=lmax, xref='x', x0=X_test[0], x1=X_test[0])]
    fig.update_layout(shapes=shapes)

    return fig
