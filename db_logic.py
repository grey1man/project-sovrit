import sqlite3
import json

#conn = sqlite3.connect("mydatabase.db")
#cursor = conn.cursor()
#Создание таблицы
def insert(table_name, table_data, conn) :
    cursor = conn.cursor()
    #global conn
    #global cursor
    i = 0
    try :
        if table_name == 'matches' :
            for i in range(len(table_data)) :
                cursor.execute("insert into matches values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (table_data[i]['match_id'], table_data[i]['duration'], table_data[i]['start_time'], table_data[i]['radiant_team_id'], table_data[i]['radiant_name'], 
                table_data[i]['dire_team_id'], table_data[i]['dire_name'], table_data[i]['leagueid'], table_data[i]['league_name'], table_data[i]['series_id'],
                table_data[i]['series_type'], table_data[i]['radiant_score'], table_data[i]['dire_score'], table_data[i]['radiant_win']))
                conn.commit()
        if table_name == 'players' :
            for i in range(len(table_data)) :
                cursor.execute("insert into " + table_name + " values ( " + table_data[i]['account_id'] + " , " + table_data[i]['steamid'] + " , " + table_data[i]['avatar'] +
                            " , " + table_data[i]['awatarmedium'] + " , " + table_data[i]['awatarfull'] + " , " + table_data[i]['profileurl'] + " , " +
                            table_data[i]['personaname'] + " , " + table_data[i]['last_login'] + " , " + table_data[i]['full_history_time'] + " , " + table_data[i]['cheese'] + " , " +
                            table_data[i]['fh_unavaible'] + " , " + table_data[i]['loccountrycode'] + " , " + table_data[i]['name'] + " , " + table_data[i]['country_code'] + " , " +
                            table_data[i]['fantasy_role'] + " , " + table_data[i]['team_id'] + " , " + table_data[i]['team_name'] + " , " + table_data[i]['team_tag']
                             + " , " + table_data[i]['is_locked'] + " , " + table_data[i]['is_pro'] + " , " + table_data[i]['locked_until'])

    except sqlite3.OperationalError :
        if table_name == 'matches' :
            cursor.execute("""create table matches (match_id number not null primary key, duration number, start_time number, radian_team_id number, radiant_name text,
                              dire_team_id number, dire_name text, leagueid number, league_name text, series_id number, series_type number,
                              radiant_score number, dire_score number, radiant_win bool) """)
        if table_name == 'players' :
            cursor.execute("""create table players (account_id number not null, steamid number, avatar text, awatarmedium text, avatarfull text,
                              profileurl text, personaname text, last_login number, full_history_time text, cheese number, fh_unavaible bool,
                             loccountrycode text, name text, country_code text, fantasy_role number, team_id number
                             team_name text, team_tag text, is_locked bool, is_pro bool, locked_until number constrained match_id primary key (match_id))""")
    




