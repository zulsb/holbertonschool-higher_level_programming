#!/usr/bin/python3
"""
    Script that lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    """Connect to database."""
    conec_db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    """Create cursor to exec queries using SQL
        and join two tables for all info."""
    cursor = conec_db.cursor()
    search = """
    SELECT cities.id, cities.name, states.name
    FROM states
    INNER JOIN cities ON states.id = cities.state_id
    ORDER BY cities.id ASC"""

    cursor.execute(search)

    for row in cursor.fetchall():
        print(row)
    cursor.close()
    conec_db.close()
