import psycopg2
from psycopg2 import sql

connection_string = "postgres://default:GSpToj6IMLZ3@ep-blue-lab-a4kmce5a.us-east-1.aws.neon.tech:5432/verceldb?sslmode=require"


def insert_studytimeline(name,totalcost,d1,d2,duration):
    try:
        # Connect to your postgres DB
        conn = psycopg2.connect(connection_string)
        
        # Create a cursor object
        cursor = conn.cursor()

        # SQL query to insert data into the table
        insert_query = '''
        INSERT INTO studytimeline (projectname, cost, startdate,enddate,duration) VALUES (%s, %s, %s,%s,%s);
        '''

        # Data to be inserted
        record_to_insert = (name,totalcost,d1,d2,duration)

        # Execute the INSERT query
        cursor.execute(insert_query, record_to_insert)

        # Commit the transaction
        conn.commit()

        print("Data inserted successfully.")

    except Exception as error:
        print("Error while inserting data into PostgreSQL", error)

    finally:
        # Close the cursor and connection to the database
        if conn:
            cursor.close()
            conn.close()
            print("PostgreSQL connection is closed.")


def loadData():
    conn = psycopg2.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM studytimeline;")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows