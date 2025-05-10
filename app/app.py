from config import *


@app.route('/', methods=['GET', 'POST'])
def home():
    return flask.render_template('home.html')

## User handling
@login_manager.user_loader
def load_user(userid):
    return "User 1"

@app.errorhandler(404)
def not_found(e): 
    return flask.render_template('404.html') 

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


if __name__ == '__main__':
    if (mode == 'production'):
        app.run(port=PRO_PORT, host=PRO_HOST, debug = False)
    if (mode == 'development'):
        app.run(port=DEV_PORT, host=DEV_HOST, debug=True) #change to localhost instead of 0.0.0.0 and port 5000 to run on your computer
