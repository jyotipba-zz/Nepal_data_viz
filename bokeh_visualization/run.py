#!/usr/bin/env python
# coding: utf-8

# load libraries
import pandas as pd

# Bokeh basics 
from bokeh.io import curdoc,output_file, show
from bokeh.models.widgets import Tabs,Select
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource, Panel
from bokeh.transform import dodge
from bokeh.layouts import column, row, WidgetBox

# import different ploting function as module

from province import province_plot
from summary import show_summary_stat 

# Read data 
data = pd.read_csv('../data_analysis/main_data.csv')

data.isnull().sum()

data = data.dropna(axis=0,how='any' )

 
data = data.replace(regex=r',', value='')
col_to_change = ['Total number of active male accounts','Total number of active female accounts','Total population',
              'Percentage of active male accounts','Percentage of active female accounts','Female with Cooperative Access'
              ,'Male with Cooperative access', 'Total population', 'Total Male', 'Total Female']
for col in col_to_change:
    data[col] = pd.to_numeric(data[col])


tabs_province = province_plot(data)
tabs_summary = show_summary_stat(data)
tabs = Tabs(tabs=[ tabs_province,tabs_summary])
# Put the tabs in the current document for display
curdoc().add_root(tabs)







