#!/usr/bin/python3
"""
    Script that takes in the name of a state
    as an argument and lists all cities of that state,
    using the database hbtn_0e_4_usa.
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
    SELECT cities.name
    FROM states
    INNER JOIN cities ON states.id = cities.state_id
    WHERE states.name LIKE %s
    ORDER BY cities.id ASC"""

    cursor.execute(search, (argv[4], ))

    """Format to print the cities with same state separated by commas."""
    coma = ""
    for row in cursor.fetchall():
        print("{:s}{:s}".format(coma, row[0]), end="")
        coma = ", "
    print()
    cursor.close()
    conec_db.close()
