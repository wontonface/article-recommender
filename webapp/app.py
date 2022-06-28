from flask import Flask, render_template
## from flask_restful import Api, Resource, reqparse
## from flask_cors import CORS #comment this on deployment
## from api.HelloApiHandler import HelloApiHandler

## from Landing import Landing

app = Flask(__name__)

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the article recommender')

@app.route('/test')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/current-designer')
def currentdesigner_page() -> 'html':
    return render_template('your-role.html')

## Remove ## when aspiring-designer is ready
## @app.route('/aspiring-designer')
## def aspiringdesigner_page() -> 'html':
##    return render_template('aspiring-designer.html')

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
    return render_template('results2.html')


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


