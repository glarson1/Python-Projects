import sqlite3

conn = sqlite3.connect('prac.db') #this will create a db named prac.db and connect to it

with conn: #while connected do the following 
    cur = conn.cursor() #lets us use the cursor so we can create and edit tables
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_practice( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_txt TEXT \
        )")  #created a table 
    conn.commit() #committing what we created
conn.close() #closes the with

conn = sqlite3.connect('prac.db') #connected to prac.db again

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')#created a list

for x in fileList: #reads through list of file names 
    if x.endswith('.txt'): #determines if file names end in txt
        with conn: #while connnected do the following 
            cur = conn.cursor()#lets us use the cursor so we can create and edit tables
            cur.execute("INSERT INTO tbl_practice (col_txt) VALUES (?)", (x,))#insert the file names that end in .txt in col_txt
            print(x)
conn.close()


