from flask import Flask, render_template, request, redirect, url_for
from articleRecommender import inputStorage, aboutYou, yourGoals, jobHuntingStatus 
## from flask_restful import Api, Resource, reqparse
## from flask_cors import CORS #comment this on deployment
## from api.HelloApiHandler import HelloApiHandler

## from Landing import Landing

app = Flask(__name__)

## @app.before_request()
## create a function to capture the user's last visited page

@app.route('/')
def entry_page() -> 'html':
    inputStorage()
    return render_template('entry.html', the_title='Welcome to the article recommender')

@app.route('/test')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/current-designer', methods=['GET', 'POST'])
def currentdesigner_page() -> 'html':
    return render_template('your-role.html')
    if request.method == 'POST':
        isDesignerInput = request.form.get['currentdesigner']
        if isDesignerInput == 'yes':
            return redirect('/your-goals')
        else:
            return redirect('/aspiring-designer')


@app.route('/aspiring-designer')
def aspiringdesigner_page() -> 'html':
    return render_template('aspiring-designer.html')

@app.route('/your-goals')
def yourgoals_page() -> 'html':
    return render_template('your-goals.html')


@app.route('/interview-status')
def interviewstatus_page() -> 'html':
    return render_template('interview-status.html')


@app.route('/interview-stage')
def interviewstage_page() -> 'html':
    return render_template('interview-stage.html')

@app.route ('/results2')
def results_page() -> 'html':
    aboutYou(isDesignerInput)

    return render_template('results2.html')


## @app.errorhandler(404)
## def not_found():
##  return make_response(render_template("404.html"), 404)

# @app.route('/entry')
# def entry_page() -> 'html':
  #  return render_template('entry.html', the_title='welcome to the app recommender')

app.run()


#### Old code ####
## app = Flask(__name__, static_url_path='', static_folder='frontend')
## CORS(app) #comment this on deployment
## api = Api(app)

## @app.route("/", defaults={'path':''})
## def serve(path):
    ## return send_from_directory(app.static_folder, 'index.html')


## api.add_resource(HelloApiHandler, '/flask/hello')


