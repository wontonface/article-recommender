from flask import Flask, render_template, request, redirect
from articleRecommender import inputStorage, aboutYou, yourGoals, jobHuntingStatus 
## from flask_restful import Api, Resource, reqparse
## from flask_cors import CORS #comment this on deployment
## from api.HelloApiHandler import HelloApiHandler

## from Landing import Landing

app = Flask(__name__)

dict = {
    1: { # About You
        'isDesigner': 0,
        'aspiringDesigner': 0
        },
    2: { # Your Goals
        'improvingSkills': 0,
        'findingNewJob': 0,
        'breakingIn': 0
        },
    3: { # Job Hunting Status
        'activelyApplying': 0,
        'interviewNoStage': 0,
        'interviewEarlyStage': 0,
        'interviewMidStage': 0,
        'interviewLateStage': 0,
        }
    }

def storeValue(i, key):
    dict[i][key] += 1

## @app.before_request()
## create a function to capture the user's last visited page

@app.route('/')
def entry_page() -> 'html':
    inputStorage()
    return render_template('entry.html', the_title='Welcome to the article recommender')

@app.route('/test')
def hello() -> str:
    return dict

@app.route('/current-designer', methods=['GET', 'POST'])
def currentdesigner_page() -> 'html':
    return render_template('your-role.html')

@app.route('/add', methods=['GET', 'POST'])
def add() -> 'html':
    if request.method == 'POST':
        if request.form.get('currentdesigner') == 'yes':
            storeValue(1, 'isDesigner')
        else:
            storeValue(1, 'aspiringDesigner')
            return redirect('/aspiring-designer')
    return redirect('/your-goals')

@app.route('/aspiring-designer', methods=['GET', 'POST'])
def aspiringdesigner_page() -> 'html':
    return render_template('aspiring-designer.html')

@app.route('/your-goals', methods=['GET', 'POST'])
def yourgoals_page() -> 'html':
    return render_template('your-goals.html')

@app.route('/add2', methods=['GET', 'POST'])
def add2() -> 'html':
    if request.method == 'POST':
        if request.form.get('goal') == 'skills':
            storeValue(1, 'improvingSkills')
        if request.form.get('goal') == 'newjob':
            storeValue(1, 'findingNewJob')
            return redirect('/interview-status')
        if request.form.get('goal') == 'tech':
            storeValue(1, 'breakingIn')
            return redirect('/interview-status')
        else:
            if request.form.get('aspiringdesigner') == 'yes':
                storeValue(1, 'aspiringDesigner')
                return redirect('/your-goals')
    return redirect('/results2')


    if yourGoalsValue == 'A':
        dict[2]['improvingSkills'] += 1
    else:
        if yourGoalsValue == 'B':
            dict[2]['findingNewJob'] += 1
        else:
            dict[2]['breakingIn'] += 1


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

app.run(debug=True)


#### Old code ####
## app = Flask(__name__, static_url_path='', static_folder='frontend')
## CORS(app) #comment this on deployment
## api = Api(app)

## @app.route("/", defaults={'path':''})
## def serve(path):
    ## return send_from_directory(app.static_folder, 'index.html')


## api.add_resource(HelloApiHandler, '/flask/hello')


