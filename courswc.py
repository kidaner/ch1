from decimal import Underflow
from bs4 import BeautifulSoup
import requests

url = "https://lite.cnn.com/en/article/h_ad05d1289475f84d12552414d465ad14"

HEADERS = {'User-Agent': '<Company NAME> <EMAIL ADDRESS>'}
r = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(r.text, features="lxml")

text = soup.get_text()

punctuations = '''!()-[]{};:'"|\,<>./?@#$%^&*_~'''

uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my",
                       "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them",
                       "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being",
                       "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how",
                       "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]


for x in text:
    if x in punctuations:
        text = text.replace(x, "")

text = text.lower().split()


print(uninteresting_words)

# remove stop words
# count frequency
