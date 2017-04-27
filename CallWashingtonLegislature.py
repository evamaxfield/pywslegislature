import requests
import xmltodict

def httpGET(arch, service, call, attachments):
    getRequest = arch + service + call + '?'

    index = 0
    for attachment in attachments:
        if index < (len(attachments) - 1):
            getRequest += (attachment + '&')
        else:
            getRequest += attachment

        index += 1

    print('Running ' + call + ' against ' + service)
    print('Full Call:')
    print(getRequest)
    print('----------------------------------------------------------------------------------')
    try:
        read = requests.get(getRequest)
        dictRead = xmltodict.parse(read.content)
    except:
        dictRead = {'ERROR': 'Failed to retrieve data'}

    return dictRead
