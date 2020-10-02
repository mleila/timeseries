# -*- coding: utf-8 -*-
'''This module provides functions related to Digital Signal Processing and Fourier Analysis.'''
import numpy as np


def make_sinusoidal_signal(
    mean: float=0, 
    amp: float=1.0, 
    freq: int=1, 
    points: int=100,
    noise_mean: float=0.0, 
    noise_var: float=0.1):
    """
    Generate a synthetic signal.

    mean: Signal baseline or average.
    amp: Signal amplitude
    freq: number of times you repeat one cycle
    points: number of points (samples) within each cycle
    noise_mean: mean of the white noise signal
    noise_var: variance of the white noise signal. Note that this impacts your signal/noise ratio
    """
    one_cycle = amp * np.sin(np.linspace(0, 2*np.pi, num=points))
    full_signal = np.tile(one_cycle, freq) + mean
    total_length = points * freq
    noise = np.random.normal(noise_mean, sig_var, size=total_length)
    return full_signal + noise
