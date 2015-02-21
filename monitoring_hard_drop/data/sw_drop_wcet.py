#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import math
import numpy

# Parse data
f = open("sw_drop_wcet.csv", 'r')
subcat = f.readline().strip().split(',')[1:]
cat = []
data = []
for line in f:
  if not line.strip():
    continue
  ls = line.split(',')
  cat.append(ls[0])
  data.append([float(x) for x in ls[1:]])
f.close()

# Transpose
(cat, subcat) = (subcat, cat)
data = numpy.array(data).transpose()

# Set up plotting options
opts = tsg_plot.PlotOptions()
opts.data = data
opts.labels = [cat, subcat]

attribute_dict = \
    {
        'show' : False,
        'file_name' : 'sw_drop_wcet.pdf',
        'paper_mode' : True,
        'figsize' : (5.8, 2.0),
        'legend_ncol' : 4,
        'legend_handlelength' : 1.0,
        'legend_columnspacing' : 0.8,
        'legend_handletextpad' : 0.5,
        'legend_bbox' : [-0.05, 1.05, 1, 0.1],
        'ylabel' : 'Normalized WCET',
        'rotate_labels' : True,
        'rotate_labels_angle' : -30,
        'fontsize' : 8,

        'colors' : ['#deebf7', '#9ecae1', '#3182bd']
    }
for name, value in attribute_dict.iteritems():
  setattr( opts, name, value )

# Plot
tsg_plot.add_plot( opts )
