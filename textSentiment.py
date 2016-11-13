########### Python 2.7 #############
import httplib, urllib, base64

headers = {
    # Request headers
    'Content-Type': 'application/json',
    'Ocp-Apim-Subscription-Key': '95531d3b1a924a03b4e52eca1708d506',
}

params = urllib.urlencode({
})

try:
    body = str({"documents": [
        {
            "language": "en",
            "id":  "1",
            "text": "this is some text to analyze the sentiment of"
        }
    ]})
    conn = httplib.HTTPSConnection('westus.api.cognitive.microsoft.com')
    conn.request("POST", "/text/analytics/v2.0/sentiment?%s" % params, body, headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
