from flask import Flask, flash, redirect, render_template, \
     request, url_for

import data_manager
import logic

LABELS = ('ID', 'Story Title', 'Acceptance Criteria', 'Business Value', 'Estimation Time', 'Status')
DICT_KEYS = ('id', 'storytitle', 'acceptancecriteria', 'businessvalue', 'estimationtime', 'status')
FILENAME = 'sample_data/data.csv'


app = Flask(__name__)
app.static_folder = 'static'


@app.route('/', methods=['GET'])
def index():
    data_dict = data_manager.get_data_list_of_dicts()
    return render_template('main-page.html', data=data_dict, labels=LABELS, keys=DICT_KEYS)


@app.route('/story', methods=['GET'])
def add_new_story():
    return render_template('story.html')


@app.route('/story', methods=['POST'])
def save_story():
    new_data = request.form.getlist('user_story_info')
    dicitified_new_data = logic.dictify_list(new_data, DICT_KEYS)
    data_manager.add_data(dicitified_new_data)
    return redirect(url_for('index'))


@app.route('/story/<story_id>', methods=['GET'])
def update_story(story_id: str):
    selected_story = logic.select_story_by_id(story_id)
    return render_template('update_story.html', selected_story=selected_story, story_id=story_id)


@app.route('/story/<story_id>', methods=['POST'])
def save_updated_story(story_id):
    updated_data = request.form.getlist('user_story_info')
    dicitified_updated_data = logic.dictify_list(updated_data, DICT_KEYS)
    data_manager.update_story(story_id, dicitified_updated_data)
    return redirect(url_for('index'))


@app.route('/delete/<story_id>', methods=['POST'])
def remove_story(story_id):
    #logic.delete_story(story_id)
    data_manager.remove_data_by_id(story_id)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True,
            port=5000)
