import sqlite3
import json

row = 0
conn = sqlite3.connect("mydatabase.db") # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()
#Создание таблицы
def insert(row_table) :
    global conn
    global cursor
    try :
        cursor.execute("""insert into matches values ('avs' ,'123', '123123', '333', 'ddd', '1', '2', '3', '4', '10', '11', '12', '13')""")
    except sqlite3.OperationalError :
        cursor.execute("""create table matches (match_id text, duration text, start_time text, radian_team_id text, radiant_name text
                          dire_team_id text, dire_name text, leagueid text, league_name text, series_id text, series_type text,
                          radiant_score text, dire_score text, radiant_win text )""")
        insert(row_table)

   

insert(1) 


conn.commit()

 
with conn:    
    cur = conn.cursor()    
    cur.execute("SELECT * FROM matches")
    rows = cur.fetchall()
 
    for row in rows:
        print(row)
