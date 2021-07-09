from pyfiglet import Figlet
import requests
import json

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