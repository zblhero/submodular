from flask import Flask
from flask import render_template
app = Flask(__name__)

from weibo import Client

APP_KEY = '2975032421'
APP_SECRET = '25e39c3acf0310a2824e94b619773097'
CALLBACK_URL = 'http://apps.weibo.com/submodular'

@app.route('/login')
def login():
    if request.method == 'POST':
        return 'login failed'
    else:
        return 'login first'

@app.route('/')
def index():
    c = Client(APP_KEY, APP_SECRET, CALLBACK_URL)
    c.set_code('3e6c11673cebce92d25b55ce3883553b')
    
    token = c.token
    user = c.get('users/show', uid=2703275934)
    
    return user.location


if __name__ == "__main__":
    app.run(debug = True)
