#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""
import MySQLdb
import sys


if __name__ == "__main__":
    # Check if all required arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
        )

        # Create a cursor object
        cur = db.cursor()

        # Execute SQL query
        cur.execute("SELECT * FROM states ORDER BY id;")

        # Fetch all rows
        rows = cur.fetchall()

        # Print fetched rows
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error [{}]: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

    finally:
        # Close cursor and database connection
        if 'cur' in locals() and cur:
            cur.close()
        if 'db' in locals() and db:
            db.close()
