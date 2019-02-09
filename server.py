from flask import Flask, flash, redirect, render_template, \
     request, url_for

import data_manager

LABELS = ['ID', 'Story Title', 'Acceptance Criteria', 'Business Value', 'Estimation Time', 'Status']
FILENAME = 'sample_data/data.csv'


app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    data_manager.check_labels_in_csv(FILENAME, LABELS)
    data_dict = data_manager.get_data_from_file(FILENAME)
    return render_template('main-page.html', data=data_dict, labels=LABELS)


@app.route('/story', methods=['GET'])
def add_new_story():
    return render_template('story.html')


@app.route('/story', methods=['POST'])
def save_story():
    new_data = request.form.getlist('user_story_info')
    data_manager.add_data_to_file(FILENAME, new_data, LABELS)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(debug=True,
            port=5000)
