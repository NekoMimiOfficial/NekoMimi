from pyfiglet import Figlet
import requests
import json
import os

def version():
    return "1.0.5"

def figlet(text, mode="small"):
    f = Figlet(font=mode)
    render = f.renderText(text)
    return render

def urban(query):
    try:
        urban = requests.get(f'https://api.urbandictionary.com/v0/define?term={query}')
        url = json.loads(urban.text)
    except Exception:
        return "Urban API returned invalid data... might be down or your IP is banned."

    if not url:
        return "I think the API broke..."

    if not len(url['list']):
        return "Couldn't find your search in the dictionary..."

    result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]
    return result[0]

def jsonAPI(endpoint):
    url = requests.get(endpoint)
    outputJson = json.loads(url.text)
    return outputJson

def writeToFile(data,file):
    fappen = open(file,"wb")
    fappen.write(data)
    fappen.close()
    return "Done !"

def ReadFromFile(file):
    fappen = open(file,"rb")
    rd = fappen.read()
    fappen.close()
    return rd

def brainshopAi(bid,secret,msg):
    url = f'http://api.brainshop.ai/get?bid={bid}&key={secret}&uid=[42]&msg={msg}'
    response = jsonAPI(url)
    return response['cnt']