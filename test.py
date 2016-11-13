import requests
import json
import sys
import time
from tokens import *
from boilerpipe.extract import Extractor

if len(sys.argv) == 1 or len(sys.argv) > 4:
  raise ValueError

query = ' '.join((str(sys.argv[1]), '({0})'.format(str(sys.argv[2]))))
count = sys.argv[3]
payload = {'q': query, 'count': count, 'category': 'Politics', 'mkt': 'en-US', 'freshness': 'Month'}

dictionary = {}

while(count > 0):
  r = requests.get(url, headers=headers, params=payload).json()
  for article in r['value']:
    try:
      link = article['url']
      date = article['datePublished'].split('T')[0]
      text = Extractor(extractor='ArticleExtractor', url=link).getText()
      dictionary[date] = text
      count -= 1
    except:
      pass
