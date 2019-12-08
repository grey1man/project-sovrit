import requests
import time

#запрос данных о про матчах, аргумент proxy - обязан быть словарем

def load_matches(proxy) :
   return requests.get('https://api.opendota.com/api/proMatches',  proxies = proxy).json()   


#запрос данных о про игроках, аргумент proxy - обязан быть словарем

def load_players(proxy) :
    return requests.get('https://api.opendota.com/api/proPlayers', proxies = proxy).json()   

def load_competitive(proxy) :
    i = 0
    mas = []
    buf = requests.get('https://api.opendota.com/api/proPlayers', proxies = proxy).json()
    print('harvesting data')
    for i in range(len(buf)) :
        print(str(i + 1) + ' of ' + str(len(buf)))
        time.sleep(1)
        mas.append(requests.get('https://api.opendota.com/api/players/' + str(buf[i]['account_id']), proxies = proxy).json())
    return mas
#proxy = None

#print(load_competitive(proxy)[102])
#print(load_competitive(proxy)[102]['solo_competitive_rank'])

