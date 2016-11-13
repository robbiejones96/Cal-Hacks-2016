import matplotlib.pyplot as plt
from matplotlib.dates import date2num, drange
from numpy.random import rand
from textSentiment import generateSentimentData
import sys
from datetime import datetime, timedelta
import sqlite3
import pandas as pd

def plot(keyword, source, count):
  def getDate(dateString):
    if dateString[-2] == '-':
      return int(dateString[-1])
    else:
      return int(dateString[-2:])

  #sentimentData = generateSentimentData(keyword, source, count)

  c = sqlite3.connect('articles.db').cursor()


  list_dates = []
  list_sentiments = []
  # for val_id in sentimentData:
  #   vals = sentimentData[val_id]
  #   list_sentiments.append(float(vals[0]))
  #   date = vals[1].split('-')
  #   print date
  #   date = datetime(int(date[0]), int(date[1]), int(date[2]))
  #   list_dates.append(date)

  table = '_'.join((source.split('.')[0], keyword.lower()))
  sql = 'SELECT * FROM {} ORDER BY dt ASC LIMIT {}'.format(table, count)

  for row in c.execute(sql):
    date = row[0].split('-')
    date = datetime(int(date[0]), int(date[1]), int(date[2]))
    list_dates.append(date)
    list_sentiments.append(row[1])

  date_list = pd.date_range(min(list_dates), periods = len(list_sentiments))

  fig = plt.figure()

  plt.plot_date(list_dates, list_sentiments)

  plt.ylim([-1,1])

  """for color in ['red', 'green', 'blue']:
      n = 750
      x, y = rand(2, n)
      scale = 200.0 * rand(n)
      plt.scatter(x, y, c=color, s=scale, label=color,
                  alpha=0.3, edgecolors='none')
  plt.legend()
  plt.grid(True)"""
  #plt.show()

  return fig
