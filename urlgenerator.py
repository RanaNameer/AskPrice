import requests
from bs4 import BeautifulSoup

def userinput(user):
    google_search = requests.get("https://www.google.com/search?q="+user)
    soup = BeautifulSoup(google_search.text, 'html.parser')
    search_results = soup.select('a')
    for link in search_results[14:15]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url1=t[:p]
    for link in search_results[15:16]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url2=t[:p]
    for link in search_results[16:17]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url3=t[:p]
    for link in search_results[17:18]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url4=t[:p]
    for link in search_results[18:19]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url5=t[:p]
    for link in search_results[19:20]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url6=t[:p]
    for link in search_results[21:22]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url7=t[:p]
    for link in search_results[22:23]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url8=t[:p]
    for link in search_results[23:24]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url9=t[:p]
    for link in search_results[24:25]:
        a=link.get('href')
        b=a.lstrip('/url?q=')
        t = b
        p=t.find("&s")
        url10=t[:p]
    

    L = [url1,url2,url3,url4,url5,url6,url7,url8,url9,url10]
    return L
