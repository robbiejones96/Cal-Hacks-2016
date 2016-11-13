########### Python 2.7 #############
import httplib, urllib, base64, sys, json
from test import scrapeArticles

if (len(sys.argv) != 4):
    raise ValueError

articleDictionary = scrapeArticles(sys.argv[1], sys.argv[2], sys.argv[3])

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '95531d3b1a924a03b4e52eca1708d506',
}

params = urllib.urlencode({
})

idCount = 1

#try:
body_list = []
dateIdDict = {}
"""body = str({"documents": [
    {
        "language": "en",
        "id":  "1",
        "text": "this is some text to analyze the sentiment of"
    }
]})"""
for text, date in articleDictionary.iteritems():
    encoded = text.encode('ascii', 'ignore')
    if len(encoded) < 5120:
        temp = {}
        temp["language"] = "en"
        temp["id"] = str(idCount)
        encoded = text.encode('ascii', 'ignore')
        temp["text"] = encoded
        dateIdDict[idCount] = date
        idCount+=1
        body_list.append(temp)

    

body = {}
body["documents"] = body_list
body = str(body)

conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
response = conn.getresponse()
data = response.read()
print(data)
data = json.loads(data)
conn.close()
results_list = data["documents"]
finalDict = {}
for result in results_list:
    new_list = []
    new_list.append(str(result["score"]))
    new_list.append(dateIdDict[int(result["id"])])
    finalDict[result["id"]] = new_list
print finalDict
#return finalDict

#except Exception as e:
 #   print("[Errno {0}] {1}".format(e.errno, e.strerror))
