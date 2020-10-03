# -*- coding: utf-8 -*-
'''This module provides functions related to Digital Signal Processing and Fourier Analysis.'''
import numpy as np
import matplotlib.pyplot as plt


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
    noise = np.random.normal(noise_mean, noise_var, size=total_length)
    return full_signal + noise


def dft_report(signal):
    # compute dft
    fft = np.fft.fft(signal)

    # get real components (index is freq as k/N of 2pi, value is the energy)
    real = np.abs(np.real(fft))

    # keep only the first half
    midpoint = int(signal.size / 2)
    real = real[:midpoint] / signal.size

    top_freq_index = np.argmax(real[1:]) + 1
    top_freq_amp = real[top_freq_index] * 2
    print(f'Average = {real[0]:.2f}', )
    print(f'Index of most prominent freq = {top_freq_index}')
    print(f'Top Freq Amplitude = {top_freq_amp:.4f}')
    print(f'''Period of the most prominent freq = {int(signal.size/top_freq_index)}''')
    plt.stem(2*real[1:]);
