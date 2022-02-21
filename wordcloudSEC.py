# https://blog.toadworld.com/2018/05/21/creating-a-word-cloud-using-python

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import nltk
import requests
from bs4 import BeautifulSoup
from wordcloud import WordCloud
import matplotlib.pyplot as plt

url = 'https://www.sec.gov/Archives/edgar/data/1679788/000162828021006850/coinbaseglobalinc424b.htm'
HEADERS = {'User-Agent': '<Company NAME> <EMAIL ADDRESS>'}
r = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(r.text, features="lxml")

for script in soup(["script", "style"]):
    script.extract()

text = soup.get_text()
lines = (line.strip() for line in text.splitlines())
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
text = 'n'.join(chunk for chunk in chunks if chunk)
stop_words = set(stopwords.words('english'))

nltk.download('punkt')
words = word_tokenize(text)

wordsFiltered = [word.lower() for word in words if word.isalpha()]

filtered_words = [
    word for word in wordsFiltered if word not in stopwords.words('english')]

wc = WordCloud(max_words=1000, margin=10, background_color='white',
               scale=3, relative_scaling=0.5, width=500, height=400,
               random_state=1).generate(' '.join(filtered_words))
plt.figure(figsize=(20, 10))
plt.imshow(wc)
plt.axis("off")
plt.show()
