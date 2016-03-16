#welcome to python!
import requests 

sentence = "Four score and seven years ago, my four fathers"

sentence_no_vowels = ""

for letter in sentence: 
    if letter not in "AEIOUaeiou":
        sentence_no_vowels = sentence_no_vowels + letter

print sentence_no_vowels

r = requests.get('http://wikipedia.org')
print r.status_code 
print unicode(r.content) 