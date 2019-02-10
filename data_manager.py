# functions for managing files
import common
import csv
import os
import common_data_base
from psycopg2 import sql
import psycopg2.extras as e



@common_data_base.connection_handler
def get_data_list_of_dicts(cursor):
    cursor.execute("""
                    SELECT * FROM storydata
                    ORDER BY id;
                   """)
    rows = cursor.fetchall()
    return rows


def add_data(data):
    connection = common_data_base.open_database()
    cursor = connection.cursor()
    cursor.execute("""
        INSERT INTO storydata 
        (storytitle, acceptancecriteria, businessvalue, estimationtime, status)
        VALUES(%s, %s, %s, %s, %s); """, data)


if __name__ == "__main__":
    pass
