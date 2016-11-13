import matplotlib.pyplot as plt
from numpy.random import rand
from textSentiment import generateSentimentData
import sys

def getDate(dateString):
	if dateString[-2] == '-':
		return int(dateString[-1])
	else:
		return int(dateString[-2:])

if (len(sys.argv) != 4):
	raise ValueError

sentimentData = generateSentimentData(sys.argv[1], sys.argv[2], sys.argv[3])

list_dates = []
list_sentiments = []
for val_id in sentimentData:
	vals = sentimentData[val_id]
	list_sentiments.append(float(vals[0]))
	list_dates.append(getDate(vals[1]))

plt.plot(list_dates, list_sentiments, "ro")

"""for color in ['red', 'green', 'blue']:
    n = 750
    x, y = rand(2, n)
    scale = 200.0 * rand(n)
    plt.scatter(x, y, c=color, s=scale, label=color,
                alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)"""

plt.show()

