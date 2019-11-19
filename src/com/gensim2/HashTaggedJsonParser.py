import json

with open('fullFledgedTM.json', encoding="utf-8", errors='ignore') as f:
    events_dict = json.load(f)
listOfEventNames = []
for eachEvent in events_dict['_embedded']['events']:
    eventName = eachEvent['name']
    #print(eventName)
    listOfEventNames.append(eventName)
    
print(listOfEventNames)


with open('fullFledgedTwitter.json', encoding="utf-8", errors='ignore') as f:
    twitter_dict = json.load(f)
listOfTwittNames = []
for eachTwitt in twitter_dict['tweets']:
    twittText = eachTwitt['full_text']
    #print(twittText)
    listOfTwittNames.append(twittText)
    
print(listOfTwittNames)
    