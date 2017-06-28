from legislative_api import *
import math
from textblob import TextBlob as tb
import pandas as pd
import requests
from bs4 import BeautifulSoup
import re

def tf(word, blob):
    return float(blob.words.count(word)) / float(len(blob.words))

def n_containing(word, bloblist):
    return sum(1 for blob in bloblist if word in blob)

def idf(word, bloblist):
    return (float(math.log(len(bloblist))) / float((1 + n_containing(word, bloblist))))

def tfidf(word, blob, bloblist):
    return tf(word, blob) * idf(word, bloblist)



html_links = pd.DataFrame(columns=['type', 'name', 'link'])

#targets = ['Bills', 'Amendments', 'Initiatives']

targets = ['Bills']
for doc_class in targets:
    print('starting gadbc')
    class_data = GetAllDocumentsByClass(attachments={'biennium': '2017-18', 'documentClass': doc_class})
    print('ending gadbc')
    class_links = pd.DataFrame(columns=['type', 'name', 'link'])

    class_list = ([doc_class] * len(class_data))
    class_links['type'] = class_list
    class_links['name'] = class_data['Name']
    class_links['link'] = class_data['HtmUrl']

    html_links = html_links.append(class_links)

index = 0

non_valid_words = ['<', '>', 'the', 'of']

print('finished bill collection')

blobs = []

for link in html_links.link:
    r  = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, 'lxml')

    words = (soup.prettify().split())

    actual_words = [ word.lower() for word in words
        if '<' not in word
        and '>' not in word
        and '.' not in word
        and 'cite=' not in word
        and 'the' != word
        and 'of' != word
        and 'for' != word
        and 'a' != word
        and 'or' != word
        and 'and' != word
        and 'to' != word
        and 'in' != word
        and 'by' != word]
    result = ' '.join(actual_words)
    blobs.append(tb(result))

    print('finished index addition', index)

    if index == 20:
        break

    index += 1

large_blob = ''

for i, blob in enumerate(blobs):
    large_blob += str(blob)

    print("Top words in document {}".format(i + 1))
    scores = {word: tfidf(word, blob, blobs) for word in blob.words}
    sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for word, score in sorted_words[:3]:
        print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

large_blob = tb(large_blob)

print("Top words in all:")
print(len(large_blob.words))
scores = {word: tfidf(word, large_blob, blobs) for word in large_blob.words}
print('starting sort')
sorted_words = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print('finishing sort')
for word, score in sorted_words[:20]:
    print("\tWord: {}, TF-IDF: {}".format(word, round(score, 5)))

final_df = pd.DataFrame(sorted_words)
final_df.to_csv('tf-idf-all.csv', sep=',')
