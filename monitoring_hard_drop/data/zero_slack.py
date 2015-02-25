#!/usr/bin/python

import sys
sys.path.extend(['../..'])
import tsg_plot
import numpy

def geomean(l):
  """
  Return the geometric mean of the passed list.
  """
  prod = 1.0
  n = 0
  for ll in l:
    prod *= ll
    n += 1
  return prod**(1.0/n)


def parse():
  # Parse data
  data = {}
  f = open("zero_slack.csv", 'r')
  for line in f:
    # Skip empty lines and comments
    if not line.strip() or line[0] == '#':
      continue
    ls = line.strip().split(',')
    # Find monitor names
    if len(ls) == 1:
      if ls[0] != '':
        monitor = ls[0]
        data[monitor] = {}
        data[monitor]['categories'] = []
        data[monitor]['data'] = []
    else:
      # Benchmarks
      if ls[0] == '':
        data[monitor]['benchmarks'] = ls[1:] #+ ["geomean"]
      # Data line
      else:
        category = ls[0]
        data[monitor]['categories'].append(category)
        d = [float(x) for x in ls[1:]]
        #d.append(geomean(d))
        data[monitor]['data'].append(d)
  f.close()

  # Transpose data
  for monitor in data.keys():
    data[monitor]['data'] = numpy.array(data[monitor]['data']).transpose()

  return data


def plot(data, filename):
  # Set up plotting options
  opts = tsg_plot.PlotOptions()
  # Benchmarks
  cat = data['benchmarks']
  # Overheads
  subcat = data['categories']
  opts.data = data['data']
  opts.labels = [cat, subcat]

  attribute_dict = \
      {
          'plot_type' : 'stacked_bar',
          'show' : False,
          'file_name' : filename,
          'paper_mode' : True,
          'figsize' : (3.5, 2.0),
          'ylabel' : 'Monitoring Events [%]',
          'legend_ncol' : 6,
          'legend_handlelength' : 1.0,
          'legend_columnspacing' : 0.8,
          'legend_handletextpad' : 0.5,
          'legend_bbox' : [-0.05, 1.05, 1, 0.1],
          'rotate_labels' : True,
          'rotate_labels_angle' : -45,
          'fontsize' : 8,
          'bar_width' : 0.5,
          'yrange' : [0, 100],

          'colors' : ['#deebf7', '#9acae1', '#3182bd'],
          'hatch' : ['']*3 

      }
  for name, value in attribute_dict.iteritems():
    setattr( opts, name, value )

  # Plot
  tsg_plot.add_plot( opts )

if __name__ == "__main__":
  data = parse()
  for mon in data.keys():
    plot(data[mon], "zero_slack_%s.pdf" % (mon))
