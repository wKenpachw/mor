import flask 
import pandas as pd
import os.path

app = flask.Flask(__name__)


@app.route('/')
def index():
    #with open(os.path.dirname(__file__)+'/data.txt', 'r', encoding='utf-8') as f:
        #dataframe = pd.read_csv(f, sep='\t', names=['name', 'version', 'size', 'date'], parse_dates=[3])
    exls = pd.read_excel(os.path.dirname(__file__)+'/data.xlsx', sheet_name='Лист1', names=['name', 'KD', 'HP', 'speed'])
    return flask.render_template('index.html', data=exls.iterrows())


@app.route('/char')
def char(name=None):
    return flask.render_template('char.html')

@app.route('/char/<char_name>')
def char_name(char_name):
    return flask.render_template('char.html', char_name = char_name)

@app.route('/chars/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

if __name__ == '__main__':
    app.debug = True
    app.run(debug = True, host='0.0.0.0')



