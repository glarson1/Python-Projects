import sqlite3

conn = sqlite3.connect(':memory:')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_Roster( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_Name TEXT, \
        col_Species TEXT, \
        col_IQ INT \
        )")
    conn.commit()

    cur.execute("INSERT INTO tbl_Roster(col_Name,col_Species,col_IQ)\
    VALUES('Jean-Baptise Zorg','Human',122),('Korben Dallas','Meat Popsicle',100),('Ak''not','Mangalore',-5)");

    conn.commit()
    
    cur.execute("UPDATE tbl_Roster \
    SET col_Species = 'Human' \
    WHERE col_name = 'Korben Dallas'");

    conn.commit()

    cur.execute("SELECT col_Name, col_IQ FROM tbl_Roster WHERE col_Species = 'Mangalore'");

    result = cur.fetchall()
    print(result)
    
conn.close()

    
