# functions for managing files
import common_data_base
import psycopg2


@common_data_base.connection_handler
def get_data_list_of_dicts(cursor):
    cursor.execute("""
                    SELECT * FROM storydata
                    ORDER BY id;
                   """)
    rows = cursor.fetchall()
    return rows


@common_data_base.connection_handler
def add_data(cursor, data: dict):
    try:
        cursor.execute("""
                INSERT INTO storydata 
                (storytitle, acceptancecriteria, businessvalue, estimationtime, status, story_id)
                VALUES(%(storytitle)s, %(acceptancecriteria)s, %(businessvalue)s,
                        %(estimationtime)s, %(status)s, %(story_id)s); """, data)
    except psycopg2.IntegrityError:
        pass


#### Whats better???
@common_data_base.connection_handler
def set_new_story_id(cursor):
    cursor.execute("""
                    SELECT MAX(story_id) FROM storydata;""")
    counted = cursor.fetchall()
    new_id = counted[0]['max'] + 1
    return new_id
####


@common_data_base.connection_handler
def id_update(cursor):
    data = get_data_list_of_dicts()
    id_index = 0
    for row in data:
        id_index += 1
        row['story_id'] = id_index
        try:
            cursor.execute("""
                        UPDATE storydata
                        SET story_id=%(story_id)s
                        WHERE id=%(id)s; """, row)
        except psycopg2.IntegrityError:
            print('error in id_update')


@common_data_base.connection_handler
def get_data_by_id(cursor, story_id: dict):
    cursor.execute("""
                       SELECT * FROM storydata
                       WHERE story_id=%(story_id)s
                      """, story_id)
    question = cursor.fetchall()
    return question


@common_data_base.connection_handler
def remove_data_by_id(cursor, story_id: dict):
    cursor.execute("""
        DELETE FROM storydata 
        WHERE story_id=%(story_id)s""", story_id)


@common_data_base.connection_handler
def update_story(cursor, story_id: str, updated_data: dict):
    updated_data.update({'story_id': story_id})  # adds actual story id
    cursor.execute("""
        UPDATE storydata 
        SET storytitle=%(storytitle)s, acceptancecriteria=%(acceptancecriteria)s,
        businessvalue=%(businessvalue)s, estimationtime=%(estimationtime)s,
        status=%(status)s
        WHERE story_id=%(story_id)s""", updated_data)


if __name__ == "__main__":
    print(set_new_story_id())
