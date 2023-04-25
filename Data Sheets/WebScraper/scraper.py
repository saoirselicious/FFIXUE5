import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

 
# iterating through the elements of list

startingInt = 0
TotalLinks = 0



Categories = ["name", "level","hp","mp","strength","defense","evade","magic","magic defense","magic evade","attack power","spirit","speed","exp","gil","fire","ice","thunder","water","wind","earth","holy","shadow","healing","petrify","venom","virus","silence","darkness","trouble","zombie","death","confuse","berserk","stop","auto-life","poison","sleep","regen","haste","slow","float","shell","protect","heat","freeze","vanish","doom","mini","reflect","gradual petrify","eat","steal","item dropped","card dropped","abilities","eats","scan", "gravity", "type", "location"]

# initialize dictionary
d = {}
for i in Categories:
    d[i] = []

print(d)

def quickRemoveDup(x):
  return list(dict.fromkeys(x))

def add_values_in_dict(key, value):
    if key in d.keys():
        d[key].extend(value)

    return d

def checkDictionaryIsEqual(idx):
    #print (idx)
    for key in d.keys():
        if idx >= (len(d[key])):
            for i in range(idx-len(d[key])):
                d[key].extend(["MissingEntry"])

def scrapeWikiArticle(url):
    global startingInt
    global TotalLinks

    tempList = []
    
    response = requests.get(
		url=url,
	)
    soup = BeautifulSoup(response.content, 'html.parser')

    data = soup.findAll('div',attrs={'class':'multicolumn'})
    for div in data:
        links = quickRemoveDup(div.findAll('a'))
        #TotalLinks = len(quickRemoveDup(links))
        for a in links:
            tempList.append(a['href'])


    tempList = quickRemoveDup(tempList)
    TotalLinks = len(tempList)
    for val in tempList:
        linkScrape("https://finalfantasy.fandom.com"+val)
    #print(d);
    checkDictionaryIsEqual(startingInt)
    finale(startingInt)

def finale(value):
    print("Finale")
    for key in d.keys():
        print(key)
        print(len(d[key]))
    with open('C:\\Users\\Saoirse\\Documents\\Unreal Projects\\Final_Fantasy_IX\\Data Sheets\\enemies.csv', 'w', encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(Categories)
        for i in range(value):
            print(i)
            arr = []
            for key in d.keys():
                arr.append(d[key][i])
            writer.writerow(arr)

def linkScrape(url):
    global startingInt
    global TotalLinks
    response = requests.get(
		url=url,
	)
    soup = BeautifulSoup(response.content, 'html.parser')

    fullTitle= str(soup.title.string).replace(' | Final Fantasy Wiki | Fandom','')
    headings = soup.findAll('section',attrs={'class':'pi-smart-group-head'})
    texts = soup.findAll('section',attrs={'class':'pi-smart-group-body'})

    datasource= ["level","hp","mp","strength","defense","evade","magic","magic def","magic eva","attack","spirit","speed","exp","gil","fire","ice","thunder","water","wind","earth","holy","shadow","healing","petrify","venom","virus","silence","darkness","trouble","zombie","death","confuse","berserk","stop","auto-​life","poison","sleep","regen","haste","slow","float","shell","protect","heat","freeze","vanish","doom","mini","reflect","gradual petrify","eats","steal","item dropped","card dropped","abilities","eat", "type"]

    #for section in headings:
    #    links = section.findAll('a')
    #    for a in links: 
    #       print(a.getText())

    for i in range(len(soup.findAll('aside',attrs={'class':'portable-infobox pi-background pi-border-color pi-theme-FFIX pi-layout-default type-multi'}))):
        add_values_in_dict("name",[fullTitle])
        startingInt=startingInt+1
        if(i!=0):
            TotalLinks=TotalLinks+1

    print (startingInt,"::StartingInt")
    print (TotalLinks,"::TotalLinks")
    

    if len(soup.findAll('section',attrs={'class':'pi-smart-group-body'}))!= 0:
        for value in texts:
            for data in Categories:
                links = value.findAll("div",attrs={'data-source':data})
                for  div in links:
                    if [div.getText()] != "":
                        add_values_in_dict(data,[str(div.getText())])
        checkDictionaryIsEqual(startingInt)
    else:
        startingInt=startingInt+1
        add_values_in_dict("name",[fullTitle])
        print(fullTitle, "HERE")
        checkDictionaryIsEqual(startingInt)
                
scrapeWikiArticle("https://finalfantasy.fandom.com/wiki/Monster_(Final_Fantasy_IX)")