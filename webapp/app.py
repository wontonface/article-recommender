from flask import Flask, render_template, request, redirect



app = Flask(__name__)

dict = {
    1: { # About You
        'isDesigner': 0,
        'aspiringDesigner': 0,
        'aspiringNonDesigner': 0
        },
    2: { # Your Goals
        'improvingSkills': 0,
        'findingNewJob': 0,
        'breakingIn': 0
        },
    3: { # Job Hunting Status
        'activelyApplying': 0
        },
    4: { # Interview Stage 
        'interviewNoStage': 0,
        'interviewEarlyStage': 0,
        'interviewMidStage': 0,
        'interviewLateStage': 0,
        }
    }

results = {
    'aspiringRole': { # Assumes designer unless otherwise
        'Designer': 'TRUE',
        'nonDesigner': 'FALSE'
    },
    'goals': {
        'improvingSkills': 'TRUE' # Assumes improvingSkills unless otherwise
    },
    'jobHunt': {
        'all': 'FALSE', # Assumes applying and in specific stage
        'noStage': 'TRUE',
        'earlyStage': 'TRUE',
        'midStage': 'TRUE',
        'lateStage': 'TRUE'
        }   
}



mylist = []

def storeValue(i, key):
    dict[i][key] += 1

def aspiringRole_results(): # Check for inverse
    if dict[1]['aspiringNonDesigner'] == 1:
        results['aspiringRole']['nonDesigner'] = 'TRUE'
        return 'nonDesigner'
    else:
        return 'designer'

def improvingSkills_results(): # Check for inverse
    if dict[2]['improvingSkills'] == 0:
        results['goals']['improvingSkills'] = 'FALSE'

def jobHunting_results():
    if dict[3]['activelyApplying'] == 0: # Check for inverse
        results['jobHunt']['all'] = 'TRUE'
    else:
        if sum(dict[4].values()) == 3:
            if dict[4]['interviewNoStage'] == 1:
                if dict[4]['interviewEarlyStage'] == 1:
                    if dict[4]['interviewMidStage'] == 1:
                        results['jobHunt']['lateStage'] = 'FALSE'
                    elif dict[4]['interviewLateStage'] == 1:
                        results['jobHunt']['midStage'] = 'FALSE'
                elif dict[4]['interviewMidStage'] == 1:
                    if dict[4]['interviewLateStage'] == 1:
                        results['jobHunt']['earlyStage'] = 'FALSE'
            elif dict[4]['interviewEarlyStage'] == 1:
                if dict[4]['interviewMidStage'] == 1:
                    results['jobHunt']['noStage'] = 'FALSE' # Early, mid, late
        elif sum(dict[4].values()) == 2:
            if dict[4]['interviewNoStage'] == 1:
                if dict[4]['interviewEarlyStage'] == 1: # None, early
                    results['jobHunt']['midStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                elif dict[4]['interviewMidStage'] == 1: # None, mid
                    results['jobHunt']['earlyStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                else: # None, late
                    results['jobHunt']['earlyStage'] = 'FALSE'
                    results['jobHunt']['midStage'] = 'FALSE'
            elif dict[4]['interviewEarlyStage'] == 1:
                if dict[4]['interviewMidStage'] == 1: # Early, mid
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                else: # Early, late
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['midStage'] = 'FALSE'
            elif dict[4]['interviewMidStage'] == 1:
                if dict[4]['interviewLateStage'] == 1: # Mid, late
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['earlyStage'] = 'FALSE'
        else: # if only one is selected
            if dict[4]['interviewNoStage'] == 1:
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
            elif dict[4]['interviewEarlyStage'] == 1:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
            elif dict[4]['interviewMidStage'] == 1:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
            else:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'



## @app.before_request()
## create a function to capture the user's last visited page

@app.route('/')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to the article recommender')

@app.route('/t')
def hello() -> str:
    return format(dict)

@app.route('/t2')
def answers2() -> str:
    return format(mylist)

@app.route('/current-designer', methods=['GET', 'POST'])
def currentdesigner_page() -> 'html':
    return render_template('your-role.html')

@app.route('/add', methods=['GET', 'POST'])
def add() -> 'html':
    if request.method == 'POST':
        if request.form.get('currentdesigner') == 'yes':
            storeValue(1, 'isDesigner')
        else:
            return redirect('/aspiring-designer')
    return redirect('/your-goals')

@app.route('/aspiring-designer', methods=['GET', 'POST'])
def aspiringdesigner_page() -> 'html':
    return render_template('aspiring-designer.html')

@app.route('/add1', methods=['GET', 'POST'])
def add1() -> 'html':
    if request.method == 'POST':
        if request.form.get('aspiringdesigner') == 'yes':
            storeValue(1, 'aspiringDesigner')
            return redirect('/your-goals')
        else:
            storeValue(1, 'aspiringNonDesigner')
            return redirect('/your-goals')

@app.route('/your-goals', methods=['GET', 'POST'])
def yourgoals_page() -> 'html':
    return render_template('your-goals.html')

@app.route('/add2', methods=['GET', 'POST'])
def add2() -> 'html':
    if request.method == 'POST':
        if 'skills' or 'newjob' or 'tech' in request.form.getlist('goal'):
            goalsResponse = request.form.getlist('goal')
            if len(goalsResponse) == 3:
                storeValue(2, 'improvingSkills')
                storeValue(2, 'findingNewJob')
                storeValue(2, 'breakingIn')
                return redirect('/interview-status')
            elif len(goalsResponse) == 2:
                if 'skills' not in goalsResponse:
                    storeValue(2, 'breakingIn')
                    storeValue(2, 'findingNewJob')
                    return redirect('/interview-status')
                elif 'newjob' not in goalsResponse:
                    storeValue(2, 'improvingSkills')
                    storeValue(2, 'breakingIn')
                    return redirect('/results2')
                else:
                    storeValue(2, 'improvingSkills')
                    storeValue(2, 'findingNewJob')
                    return redirect('/interview-status')
            else:
                if 'skills' not in goalsResponse:
                    if 'newjob' not in goalsResponse:
                        storeValue(2, 'breakingIn')
                        return redirect('/interview-status')
                    elif 'tech' not in goalsResponse:
                        storeValue(2, 'findingNewJob')
                        return redirect('/interview-status')
                else:
                    storeValue(2, 'improvingSkills')
                    return redirect('/results2')
    return redirect('/results2')

@app.route('/interview-status')
def interviewstatus_page() -> 'html':
    return render_template('interview-status.html')

@app.route('/add4', methods=['GET', 'POST'])
def add4() -> 'html':
    if request.method == 'POST':
        if request.form.get('interviewstatus') == 'yes':
            storeValue(3, 'activelyApplying')
            return redirect('/interview-stage')
        else:
            return redirect('/results2')

@app.route('/interview-stage')
def interviewstage_page() -> 'html':
    return render_template('interview-stage.html')

@app.route('/add5', methods=['GET', 'POST'])
def add5() -> 'html':
    if request.method == 'POST':
        jobHuntResponse = request.form.getlist('stage')
        if len(jobHuntResponse) == 4:
            storeValue(4, 'interviewNoStage')
            storeValue(4, 'interviewEarlyStage')
            storeValue(4, 'interviewMidStage')
            storeValue(4, 'interviewLateStage')
            return redirect('/results2')
        elif len(jobHuntResponse) == 3:
            if 'applying' not in jobHuntResponse:
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewMidStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results2')
            elif 'early' not in jobHuntResponse:
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewMidStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results2')
            elif 'mid' not in jobHuntResponse:
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results2')
            else: # if late not in
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewMidStage')
                return redirect('/results2')
        elif len(jobHuntResponse) == 2:
            if 'applying' not in jobHuntResponse:
                if 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewMidStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                elif 'mid' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                else: # if late not in
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results2')
            elif 'early' not in jobHuntResponse:
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewMidStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                elif 'mid' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                else: # if late not in
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results2')
            elif 'mid' not in jobHuntResponse:
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                elif 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results2')
                else: # if late not in
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewEarlyStage')
                    return redirect('/results2')
            else: # if late not in
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results2')
                elif 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results2')
                else: # if mid not in  
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewEarlyStage')
                    return redirect('/results2')
        return redirect('/results2')


@app.route('/add6')
def add6() -> 'html':
    aspiringRole_results()
    improvingSkills_results()
    jobHunting_results()
    

@app.route ('/results2')
def results_page() -> 'html':
    aspiring_role = aspiringRole_results()
    improvingSkills_results()
    jobHunting_results()
    return render_template('results2.html',
                            results_aspiringRole=aspiring_role,)


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


