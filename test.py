import requests
import json
import sys
from tokens import *
from boilerpipe.extract import Extractor

if len(sys.argv) == 1 or len(sys.argv) > 2:
  raise ValueError

query = str(sys.argv[1])
payload = {'q': query}
r = requests.get(url, headers=headers, params=payload).json()
for article in r['value']:
  link = article['url']
  break
extractor = Extractor(extractor='ArticleExtractor', url=link)
print extractor.getText()
