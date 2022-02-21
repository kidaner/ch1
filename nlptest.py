import requests
import nltk
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize, word_tokenize

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

wordsFiltered = [word.lower() for word in text if word.isalpha()]
print(wordsFiltered)


stopwords = nltk.corpus.stopwords.words("english")
filtered_words = [
    word for word in wordsFiltered if word not in stopwords]
print(filtered_words)
