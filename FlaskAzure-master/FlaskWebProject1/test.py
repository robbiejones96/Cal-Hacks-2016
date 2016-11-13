import requests
import json
import sys
import time
from tokens import *
from boilerpipe.extract import Extractor


def scrapeArticles(topic, newsSource, count):
  #if len(sys.argv) == 1 or len(sys.argv) > 4:
   # raise ValueError

  #query = ' '.join((str(sys.argv[1]), '({0})'.format(str(sys.argv[2]))))
  #count = sys.argv[3]
  query = ' '.join((str(topic), '({0})'.format(str(newsSource))))
  payload = {'q': query, 'count': count, 'category': 'Politics', 'mkt': 'en-US', 'freshness': 'Month'}

  #payload = {'q': query, 'count': count, 'category': 'Politics', 'mkt': 'en-US', 'freshness': 'Month'}

  dictionary = {}

  #while(count > 0):
  r = requests.get(url, headers=headers, params=payload).json()
  print len(r['value'])
  for article in r['value']:
    try:
      link = article['url']
      date = article['datePublished'].split('T')[0]
      text = Extractor(extractor='ArticleExtractor', url=link).getText()
      #text = "testing testing 123" + count
      dictionary[text] = date
      count -= 1
    except:
      pass
  return dictionary
