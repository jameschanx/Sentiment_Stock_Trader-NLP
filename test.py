from nltk import word_tokenize
from nltk.corpus import stopwords
import nltk
import string
from nltk.stem import WordNetLemmatizer, PorterStemmer
from dateutil import parser
from datetime import timedelta
#dt = parser.parse("2018-03-28T03:17:05")
#print(dt)
#print(dt - timedelta(hours=20))
#print(dt)



lmtzr = WordNetLemmatizer()
stmr = PorterStemmer()
a = lmtzr.lemmatize("here's")
print(a)
#nltk.download('stopwords')
sent = "this is a foo bar, heret's? bar black sheep."
stop = stopwords.words('english')# + list(string.punctuation)


#word = 'Wall Street Journal Tesla Halts Model 3 Production Again Wall Street Journal Tesla Inc. TSLA -3.04% has again halted production of the Model 3 sedan, days after Chief Executive Elon Musk said the auto maker\'s pace of making 2,000 of the sedans a week is susta…'
word = 'Elon Musk was awarded a stock option grant worth up to $2.6 billion if Tesla delivers on its goals.'
print(word)

def news_tokenizer(text):
    text = text.lower() # downcase
    text = text.strip(string.punctuation)
    tokens = nltk.tokenize.word_tokenize(text)
    tokens = [t for t in tokens if len(t) > 3]
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    tokens = [lmtzr.lemmatize(t) for t in tokens]
    tokens = [stmr.stem(t) for t in tokens]
    return tokens

print(news_tokenizer(word))
