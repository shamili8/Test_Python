import json
import psycopg2

conn = psycopg2.connect(database="python", user="postgres", password="9618", host="127.0.0.1", port="5432")
print("Opened database successfully")
cur = conn.cursor()
cur.execute("CREATE TABLE DEPT(DEPTID int,FIRSTNAME varchar(255),LASTNAME varchar(255),GENDER varchar(255),CITY varchar(255)");
print("Table created successfully")

with open("department.json") as file:
    data = json.load(file)
    print(data)
    for dict in data:
        cur.execute("INSERT INTO DEPT (DEPTID ,FIRSTNAME,LASTNAME,ADDRESS ,CITY) VALUES('%d','%s','%s','%s','%s')" %(dict['DEPTID'],dict['FIRSTNAME'],dict['LASTTNAME'],dict['ADDRESS'],dict['CITY']));
        conn.commit()
    print("Records created successfully")
conn.close()