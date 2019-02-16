# functions for managing files
import common_data_base



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
    cursor.execute("""
        INSERT INTO storydata 
        (storytitle, acceptancecriteria, businessvalue, estimationtime, status)
        VALUES(%(storytitle)s, %(acceptancecriteria)s, %(businessvalue)s, %(estimationtime)s, %(status)s); """,
                   data)


@common_data_base.connection_handler
def get_data_by_id(cursor, story_id: dict):
    cursor.execute("""
                       SELECT * FROM storydata
                       WHERE id=%(storyid)s
                      """, story_id)
    question = cursor.fetchall()
    return question


@common_data_base.connection_handler
def remove_data_by_id(cursor, story_id: dict):
    cursor.execute("""
        DELETE FROM storydata 
        WHERE id=%(story_id)s""", story_id)


@common_data_base.connection_handler
def update_story(cursor, story_id: str, updated_data: dict):
    updated_data.update({'story_id': story_id})  # adds actual story id # HEREQ!!!!!!!
    cursor.execute("""
        UPDATE storydata 
        SET storytitle=%(storytitle)s, acceptancecriteria=%(acceptancecriteria)s,
        businessvalue=%(businessvalue)s, estimationtime=%(estimationtime)s,
        status=%(status)s
        WHERE id=%(story_id)s""", updated_data)


if __name__ == "__main__":
    pass
