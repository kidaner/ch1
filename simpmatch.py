from pickle import NONE
import re

result = re.search(r"aza", "plaza")

bazaar = re.search(r"aza", "bazaar")

print(re.search(r"^x", "xenon"))
print(re.search(r"p.ng", "clapping"))
print(re.search(r"p.ng", "sponge"))


def check_aei(text):
    result = re.search(r"a.a", text)
    return result != None


print(check_aei("academia"))
print(check_aei("aerial"))
print(check_aei("paramedic"))

print(re.search(r"[Pp]ython", "Python"))

print(re.search(r"[a-z]way", "highway"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces."))
print(re.search(r"[^a-zA-Z ]", "This is a sentence with spaces."))
print(re.search(r"cats|dogs", "I like dogs and cats"))
print(re.findall(r"cats|dogs", "I like cats and dogs"))
print(re.search(r"P.*n", "Python Programming"))
