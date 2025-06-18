import pymysql

connection=pymysql.connect(
    host='localhost',
    user='root',
    password='1234',
    database='test',
    cursorclass=pymysql.cursors.DictCursor
)


try:
    with connection.cursor() as cursor:
        create_query="""

        CREATE TABLE IF NOT EXISTS student(
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            department VARCHAR(100)
        );
        """
        cursor.execute(create_query)

        insert_query ="INSERT INTO student(name,department) VALUES(%s,%s)"
        values=[("Arun","CSE"),("Krish","MECH")]
        cursor.executemany(insert_query,values)
        connection.commit();

        select_query ="SELECT * FROM student"
        cursor.execute(select_query)
        result=cursor.fetchall()

        for row in result:
            print(result)

finally:
    connection.close()










