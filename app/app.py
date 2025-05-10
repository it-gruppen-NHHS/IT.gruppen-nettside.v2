from config import *



@app.route('/', methods=['GET', 'POST'])
def home():
    about = home_about.query.first()  # Hent første rad fra home_about-tabellen
    return flask.render_template('home.html', about = about)

@app.route('/about', methods=['GET', 'POST'])
def about():
    about = home_about.query.first()  # Hent første rad fra home_about-tabellen
    return flask.render_template('about.html', about = about)

@app.route('/faq', methods=['GET', 'POST'])
def faq():
    return flask.render_template('faq.html')

@app.route('/projects', methods=['GET', 'POST'])
def projects():
    return flask.render_template('projects.html')

@app.route('/project_requests', methods=['GET', 'POST'])
def projects_requests():
    return flask.render_template('project_requests.html')

@app.route('/board', methods=['GET', 'POST'])
def board():
    return flask.render_template('board.html')

@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    return flask.render_template('gallery.html')

@app.route('/twoday', methods=['GET', 'POST'])
def twoday():
    return flask.render_template('twoday.html')


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
