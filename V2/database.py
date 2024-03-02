import mysql.connector
import datetime
import os
from dotenv import load_dotenv




def conectToDB(reset=False):
    print('connecting to db')
    load_dotenv()
    print(os.environ['PASSWORD_FRAN'])
    timeout = 10
    conn = mysql.connector.connect(
        connect_timeout=timeout,
        database="konstanty",
        host=os.environ['HOST_FRAN'],
        password=os.environ['PASSWORD_FRAN'],
        port=22681,
        user="avnadmin",
    )



    MeinCursor = conn.cursor()

    if reset:
        MeinCursor.execute("DROP DATABASE IF EXISTS konstanty;")
        conn.commit()
    

    MeinCursor.execute("CREATE DATABASE IF NOT EXISTS konstanty;")
    MeinCursor.execute(
        """
        CREATE TABLE IF NOT EXISTS konstanty.konstantyTable (
            id INT AUTO_INCREMENT PRIMARY KEY, 
            cas VARCHAR(19), 
            jmeno VARCHAR(255), 
            znalost_PI INT, 
            znalost_E INT, 
            znalost_FI INT, 
            IP VARCHAR(255)
            );
            """)

    conn.commit()
    return conn, MeinCursor




def addRow(MeinCursor, conn, name, znalost_PI, znalost_E, znalost_FI, IP):

    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    MeinCursor.execute("""
        INSERT INTO konstantyTable (cas, jmeno, znalost_PI, znalost_E, znalost_FI, IP)
        VALUES
            (%s, %s, %s, %s, %s, %s);
        
    """, (now, name, znalost_PI, znalost_E, znalost_FI, IP))
    conn.commit()

def getRows(MeinCursor):
    MeinCursor.execute("SELECT * FROM konstantyTable;")
    allData = MeinCursor.fetchall()
    print(allData)
    return allData

if __name__ == "__main__":
    conn, MeinCursor = conectToDB()
    
    #addRow(MeinCursor, conn, 'jmeno', 1, 2, 3, 'IP')
    getRows(MeinCursor)
