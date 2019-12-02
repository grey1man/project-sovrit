import requests

#запрос данных о про матчах, аргумент proxy - обязан быть словарем

def load_matches(proxy) :
   return requests.get('https://api.opendota.com/api/proMatches',  proxies = proxy).json()   


#запрос данных о про игроках, аргумент proxy - обязан быть словарем

def load_players(proxy) :
    return requests.get(' https://api.opendota.com/api/proPlayers', proxies = proxy).json()   


proxy = None
print(load_matches(proxy))
print(len(load_matches(proxy)))


