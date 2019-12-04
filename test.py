def insert(table_name, table_data, conn) :
    cursor = conn.cursor()
    i = 0
    if table_name == 'matches' :
         for i in range(len(table_data)) :
            cursor.execute("insert into matches values(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (table_data[i]['match_id'], table_data[i]['duration'], table_data[i]['start_time'], table_data[i]['radiant_team_id'], table_data[i]['radiant_name'], 
            table_data[i]['dire_team_id'], table_data[i]['dire_name'], table_data[i]['leagueid'], table_data[i]['league_name'], table_data[i]['series_id'],
            table_data[i]['series_type'], table_data[i]['radiant_score'], table_data[i]['dire_score'], table_data[i]['radiant_win']))