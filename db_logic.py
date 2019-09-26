import sqlite3
import json

def out(request) :
    for i in range(len(request) + 1) :
        request[i] = json.loads(request[i])
        print(type(request))
#def push() :

