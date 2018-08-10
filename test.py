from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
from nltk.stem import WordNetLemmatizer
from dateutil import parser
from datetime import timedelta
dt = parser.parse("2018-03-28T03:17:05")
print(dt)
print(dt - timedelta(hours=20))
print(type(dt))
#lmtzr = WordNetLemmatizer()
#a = lmtzr.lemmatize("here's")
#print(a)
##nltk.download('stopwords')
#sent = "this is a foo bar, heret's? bar black sheep."
#stop = stopwords.words('english') + list(string.punctuation)
#
#print(word_tokenize(sent))
#print([i for i in word_tokenize(sent.lower()) if i not in stop])
#
#print(dt.datetime())

