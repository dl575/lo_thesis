#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math

# Parse data
f = open("filter_mon.csv", 'r')
subcat = f.readline().strip().split(',')[1:]
cat = []
data = []
for line in f:
  if line.strip():
    ls = line.strip().split(',')
    cat.append(ls[0])
    data.append([float(x) for x in ls[1:]])
f.close()

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data
opts.labels = [cat, subcat]

attribute_dict = \
    {
        'show' : False,
        'file_name' : 'filter_mon.pdf',
        'paper_mode' : True,
        'figsize' : (5.8, 1.5),
        'ylabel' : 'Normalized Execution Time',
        'legend_ncol' : 5,
        'legend_handlelength' : 1.0,
        'legend_columnspacing' : 0.8,
        'legend_handletextpad' : 0.5,
        'legend_bbox' : [-0.05, 1.05, 1, 0.1],
        'rotate_labels' : False,
        'rotate_labels_angle' : -30,
        'fontsize' : 8,

        'colors' : ['#eff3ff', '#bdd7e7', '#6baed6', '#3182bd', '#08519c', '#eff3ff', '#bdd7e7', '#6baed6', '#3182bd', '#08519c'],
        'hatch' : ['']*5 + ['//']*5

    }
for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )