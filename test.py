

import sqlite3
conn = sqlite3.connect("mydatabase.db")
cursor = conn.cursor()

cursor.execute("""create table matches (match_id number not null, duration number, start_time number, radian_team_id number, radiant_name text,
                              dire_team_id number, dire_name text, leagueid number, league_name text, series_id number, series_type number,
                              radiant_score number, dire_score number, radiant_win bool constrained match_id primary key (match_id)) """)