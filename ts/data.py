# -*- coding: utf-8 -*-
'''This module provides functions to load common time series datastes.'''
from pathlib import Path

import pandas as pd


BASE = Path('../../data/')


# real world datasets
def load_globaltemp(
    frmt: str='pandas',
    mode: str='annual'
    ):
    '''
    Load Global Temperature Dataset from a Github repo.

    Arguments:
    - frmt: returned data structure (pandas or spark dataframes)
    - mode: annual or monthly

    Return:
    - Pandas or Spark dataframe

    Notes:
    Source: https://github.com/datasets/global-temp

    Citations:
    [1] GISTEMP: NASA Goddard Institute for Space Studies (GISS) Surface Temperature Analysis, Global Land-Ocean Temperature Index.
    [2] NOAA National Climatic Data Center (NCDC), global component of Climate at a Glance (GCAG).
    '''
    avail_frmts = ['pandas', 'spark']
    if frmt not in avail_frmts:
        raise NameError(f'{frmt} is not availble, only f{avail_frmts} are allowed')

    url_base = Path('https://raw.githubusercontent.com/datasets/global-temp/master/')
    url = url_base / 'data/annual.csv'
    if mode == 'monthly':
        url = url_base / 'data/monthly.csv'

    if frmt == 'pandas':
        return pd.read_csv(url)


def load_motionsense(
    frmt: str='pandas',
    device: str=None,
    subject: int=None,
    subjects_info: bool=False
    ):
    '''
    Loads subsets of the Motionsense dataset. You can either load the subject information datset, which
    provides metadata about the subjects, or the data for a particular device and subject pair. Here is a
    list of devices:

    - dws_1
    - dws_2
    - dws_11
    - jog_9
    - jog_16
    _ sit_5
    _ sit_13
    - std_6
    - std_14
    - ups_3
    - ups_4
    - ups_12
    _ wlk_7
    - wlk_8
    - wlk_15

    There are 24 subject.

    Arguments:
    - frmt: returned data structure (pandas or spark dataframes)
    - device: device name from the above list
    - subject: subject id (1 to 24)
    - subjects_info: Boolean, if true, it will load subjects metadata and ignore the device and subject arguments

    Return:
    - Path, Pandas dataframe or Spark dataframe
    '''

    if subjects_info:
        path = BASE / Path('Motionsense/data_subjects_info.csv')
        return pd.read_csv(path)
    if device and subject:
        path = BASE / Path(f'Motionsense/{device}/sub_{subject}.csv')

    if frmt == 'pandas':
        return pd.read_csv(path)


def load_trumptweets(frmt: str='pandas'):
    '''
    Load Tweets by Donald Trump from May 2009 to June 2020.

    Arguments:
    - frmt: returned data structure (pandas or spark dataframes)

    Return:
    - Path, Pandas dataframe or Spark dataframe

    Source: Kaggle
    '''
    path = BASE / Path('trumptweets/realdonaldtrump.csv')
    if frmt == 'pandas':
        return pd.read_csv(path)
