import pymysql


connection=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)

try:
    with connection.cursor()as cursor:


        create_event="""
        CREATE TABLE IF NOT EXISTS mydata(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            result VARCHAR(100)
        
        );
        """

        cursor.execute(create_event)

        insert_event="INSERT INTO mydata(name,result)VALUES(%s,%s)"
        values=[("vishnu","PASS"),("Arun","Fail")]
        cursor.executemany(insert_event,values)
        connection.commit()


        select_event="SELECT * FROM mydata "
        cursor.execute(select_event)
        result=cursor.fetchall()

        for row in result:
            print(row)
finally:
    connection.close()