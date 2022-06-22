from flask import Flask, render_template
## from flask_restful import Api, Resource, reqparse
## from flask_cors import CORS #comment this on deployment
## from api.HelloApiHandler import HelloApiHandler

## from Landing import Landing

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello world from Flask'

@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='welcome to the app recommender')

app.run()


#### Old code ####
## app = Flask(__name__, static_url_path='', static_folder='frontend')
## CORS(app) #comment this on deployment
## api = Api(app)

## @app.route("/", defaults={'path':''})
## def serve(path):
    ## return send_from_directory(app.static_folder, 'index.html')


## api.add_resource(HelloApiHandler, '/flask/hello')


