from legislative_api import *
import math
from textblob import TextBlob as tb
import pandas as pd

html_links = pd.DataFrame(columns=['type', 'name', 'link'])

print(GetDocumentClasses()['#text'])

targets = ['Bills', 'Amendments', 'Initiatives']

'''for doc_class in targets:
    class_data = GetAllDocumentsByClass(attachments={'biennium': '2017-18', 'documentClass': doc_class})

    class_links = pd.DataFrame(columns=['type', 'name', 'link'])

    print(class_data['Name'])

    class_list = ([doc_class] * len(class_data))
    class_links['type'] = class_list
    class_links['name'] = class_data['Name']
    class_links['link'] = class_data['HtmUrl']

    html_links = html_links.append(class_links)

html_links.to_csv('all_links.csv', sep=',')'''

all_links = pd.read_csv('all_links.csv')
bill_links = all_links.loc[all_links['type'] == 'Bills']

print(bill_links)
