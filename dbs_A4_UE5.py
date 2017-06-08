# imports
from bs4 import BeautifulSoup
import requests

#Die Funktion gibt ein Soup Page Objekt zurück
def getPage(url):
    r = requests.get(url)
    data = r.text
    spobj = BeautifulSoup(data, "lxml")
    return spobj

def main():
    # Es werden die Überschriften in 4 URLs gesammelt auf heise.de
    url1 = "https://www.heise.de/thema/https"
    url2 = "https://www.heise.de/thema/https?seite=1"
    url3 = "https://www.heise.de/thema/https?seite=2"
    url4 = "https://www.heise.de/thema/https?seite=3"
    
    split1 = getHeaders(url1)
    split2 = getHeaders(url2)
    split3 = getHeaders(url3)
    split4 = getHeaders(url4)
    
    #Zusammenfügen zu einer großen Überschriftenliste
    
    completesplit = split1 + split2 + split3 + split4
    complete = []
    for i in range(len(completesplit)):
        for j in range(len(completesplit[i])):
            complete.append(completesplit[i][j])
    
    t1 = ""
    t2 = ""
    t3 = ""
    t1c = 0
    t2c = 0
    t3c = 0
    # Zähler für alle Wörter und die top 3 beibehalten
    
    
    for i in range(len(complete)):
        test = complete[i]
        testc = 0
        for j in range(len(complete)):
            if (test == complete[j]):
                testc += 1
        if(testc > t1c):
            t1 = test
            t1c = testc
        if((testc > t2c) & (test != t1)):
            t2 = test
            t2c = testc
        if((testc > t3c) & (test != t1) & (test != t2)):
            t3 = test
            t3c = testc

    print("Top 1:",t1,"mit",t1c,"Vorkommen")
    print("Top 2:",t2,"mit",t2c,"Vorkommen")
    print("Top 3:",t3,"mit",t3c,"Vorkommen")
    
def getHeaders(url):
    data = getPage(url)    
    g_data = data.find_all("div",{"class":"recommendation"}) #Überschriften werden gefunden
    article = []
    for item in g_data:
        article.append(item.header.text) # speicher die Überschriften als String in einer Liste 
    splitarticle = []
    # Umwandeln der wahllos hinzugefügten Strings in Elemente einer Liste von Listen
    while article:
        splitarticle.append((article.pop(0)).split())
    return splitarticle


    
    
    if __name__ == '__main__':
        main()
