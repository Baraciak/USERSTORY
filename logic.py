import data_manager
import common_data_base

def dictify_list(data: list, dict_keys: tuple):
    dictified_data = {dict_keys[1]: data[0], dict_keys[2]: data[1], dict_keys[3]: data[2],
                      dict_keys[4]: data[3], dict_keys[5]: data[4]}
    print(dictified_data)
    return dictified_data


def dictify_id(story_id):
    dictified_id = {'storyid': story_id}
    return dictified_id


def select_story_by_id(story_id):
    dictified_id = dictify_id(story_id)
    selected_story = data_manager.get_data_by_id(dictified_id)[0]
    return selected_story


def delete_story(story_id: str):
    dictified_id = dictify_id(story_id)
    print(dictified_id)
    data_manager.remove_data_by_id(dictified_id)


if __name__ == "__main__":
    delete_story('1')
