import data_manager


FILENAME = 'sample_data/data.csv'


def user_story_counter():
    data_table = data_manager.get_data_from_file(FILENAME)
    return len(data_table) + 1


def prepare_data_for_dictwriter(new_data):
    identity = user_story_counter()
    title = new_data[0]
    criteria = new_data[1]
    value = new_data[2]
    et = new_data[3]
    status = new_data[4]
    dictified_new_data = {'ID': identity, 'Story Title': title, 'Acceptance Criteria': criteria,
                          'Business Value': value, 'Estimation Time': et, 'Status': status}
    return dictified_new_data
