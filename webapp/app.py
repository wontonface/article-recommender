from flask import Flask, flash, render_template, request, redirect



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

def minusValue(i, key):
    dict[i][key] -= 1

def clearValue(i, key):
    dict[i][key] = 0

def aspiringRole_results(): # Check for inverse
    if dict[1]['aspiringNonDesigner'] == 1:
        results['aspiringRole']['nonDesigner'] = 'TRUE'
        return 'nonDesigner'
    else:
        return 'designer'

def improvingSkills_results(): # Check for inverse
    if dict[2]['improvingSkills'] == 0:
        results['goals']['improvingSkills'] = 'FALSE'
        return 'nonImprovingSkills'

def jobHunting_results():
    if dict[3]['activelyApplying'] == 0: # Check for inverse (not in specific stage)
        results['jobHunt']['all'] = 'TRUE'
        return 'allJobHunting'
    else:
        if sum(dict[4].values()) == 3:
            if dict[4]['interviewNoStage'] == 1:
                if dict[4]['interviewEarlyStage'] == 1:
                    if dict[4]['interviewMidStage'] == 1:
                        results['jobHunt']['lateStage'] = 'FALSE' # None, early, Mid
                        return 'earlyMidJobHunting'
                    elif dict[4]['interviewLateStage'] == 1:
                        results['jobHunt']['midStage'] = 'FALSE' # None, early, Late
                        return 'allJobHunting'
                elif dict[4]['interviewMidStage'] == 1:
                    if dict[4]['interviewLateStage'] == 1:
                        results['jobHunt']['earlyStage'] = 'FALSE' # No, mid, Late
                        return 'midLateJobHunting'
            elif dict[4]['interviewEarlyStage'] == 1:
                if dict[4]['interviewMidStage'] == 1:
                    results['jobHunt']['noStage'] = 'FALSE' # Early, mid, late
                    return 'allJobHunting'
        elif sum(dict[4].values()) == 2:
            if dict[4]['interviewNoStage'] == 1:
                if dict[4]['interviewEarlyStage'] == 1: # None, early
                    results['jobHunt']['midStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                    return 'earlyJobHunting'
                elif dict[4]['interviewMidStage'] == 1: # None, mid
                    results['jobHunt']['earlyStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                    return 'earlyMidJobHunting'
                else: # None, late
                    results['jobHunt']['earlyStage'] = 'FALSE'
                    results['jobHunt']['midStage'] = 'FALSE'
                    return 'lateJobHunting'
            elif dict[4]['interviewEarlyStage'] == 1:
                if dict[4]['interviewMidStage'] == 1: # Early, mid
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['lateStage'] = 'FALSE'
                    return 'earlyMidJobHunting'
                else: # Early, late
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['midStage'] = 'FALSE'
                    return 'lateJobHunting'
            elif dict[4]['interviewMidStage'] == 1:
                if dict[4]['interviewLateStage'] == 1: # Mid, late
                    results['jobHunt']['noStage'] = 'FALSE'
                    results['jobHunt']['earlyStage'] = 'FALSE'
                    return 'midLateJobHunting'
        else: # if only one is selected
            if dict[4]['interviewNoStage'] == 1:
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
                return 'allJobHunting'
            elif dict[4]['interviewEarlyStage'] == 1:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
                return 'earlyJobHunting'
            elif dict[4]['interviewMidStage'] == 1:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['lateStage'] = 'FALSE'
                return 'midJobHunting'
            else:
                results['jobHunt']['noStage'] = 'FALSE'
                results['jobHunt']['earlyStage'] = 'FALSE'
                results['jobHunt']['midStage'] = 'FALSE'
                return 'lateJobHunting'

        
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
    error = None
    if request.method == 'POST':
        clearValue(1, 'isDesigner')
        if request.form.get('currentdesigner') == 'yes':
            storeValue(1, 'isDesigner')
        elif request.form.get('currentdesigner') == 'no':
            return redirect('/aspiring-designer')
        else:
            error = 'Invalid input'
            return render_template('your-role.html', error=error)
    return redirect('/your-goals')

    

@app.route('/aspiring-designer', methods=['GET', 'POST'])
def aspiringdesigner_page() -> 'html':
    return render_template('aspiring-designer.html')

@app.route('/add1', methods=['GET', 'POST'])
def add1() -> 'html':
    error = None
    if request.method == 'POST':
        if request.form.get('aspiringdesigner') == 'yes':
            if dict[1]['aspiringNonDesigner'] == 1: # Check if user changed answer
                minusValue(1, 'aspiringNonDesigner')
                storeValue(1, 'aspiringDesigner')
            elif dict[1]['aspiringDesigner'] == 0: # Check that it doesn't already exist. Otherwise skip
                storeValue(1, 'aspiringDesigner')
        elif request.form.get('aspiringdesigner') == 'no':
            if dict[1]['aspiringDesigner'] == 1: # Check if user changed answer
                minusValue(1, 'aspiringDesigner')
                storeValue(1, 'aspiringNonDesigner')
            elif dict[1]['aspiringNonDesigner'] == 0:
                storeValue(1, 'aspiringNonDesigner')
        else:
            error = 'Invalid input'
            return render_template('aspiring-designer.html', error=error)
    return redirect('/your-goals')

@app.route('/your-goals', methods=['GET', 'POST'])
def yourgoals_page() -> 'html':
    return render_template('your-goals.html')

@app.route('/add2', methods=['GET', 'POST'])
def add2() -> 'html':
    error = None
    if request.method == 'POST':
        if 'skills' or 'newjob' or 'tech' in request.form.getlist('goal'):
            clearValue(2, 'improvingSkills')
            clearValue(2, 'findingNewJob')
            clearValue(2, 'breakingIn')  
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
                    return redirect('/results')
                else:
                    storeValue(2, 'improvingSkills')
                    storeValue(2, 'findingNewJob')
                    return redirect('/interview-status')
            elif len(goalsResponse) == 1:
                if 'skills' not in goalsResponse:
                    if 'newjob' not in goalsResponse:
                        storeValue(2, 'breakingIn')
                        return redirect('/interview-status')
                    elif 'tech' not in goalsResponse:
                        storeValue(2, 'findingNewJob')
                        return redirect('/interview-status')
                else:
                    storeValue(2, 'improvingSkills')
                    return redirect('/results')
            else:
                error = 'Invalid input'
                return render_template('your-goals.html', error=error)
    return redirect('/results')

@app.route('/interview-status')
def interviewstatus_page() -> 'html':
    return render_template('interview-status.html')

@app.route('/add4', methods=['GET', 'POST'])
def add4() -> 'html':
    error = None
    if request.method == 'POST':
        if request.form.get('interviewstatus') == 'yes':
            storeValue(3, 'activelyApplying')
            return redirect('/interview-stage')
        elif request.form.get('interviewstatus') == 'no':
            return redirect('/results')
        else:
            error = 'Invalid input'
            return render_template('interview-status.html', error=error)

@app.route('/interview-stage')
def interviewstage_page() -> 'html':
    return render_template('interview-stage.html')

@app.route('/add5', methods=['GET', 'POST'])
def add5() -> 'html':
    error = None
    if request.method == 'POST':
        clearValue(4, 'interviewNoStage')
        clearValue(4, 'interviewEarlyStage')
        clearValue(4, 'interviewMidStage')
        clearValue(4, 'interviewLateStage')  
        jobHuntResponse = request.form.getlist('stage')
        if len(jobHuntResponse) == 4:
            storeValue(4, 'interviewNoStage')
            storeValue(4, 'interviewEarlyStage')
            storeValue(4, 'interviewMidStage')
            storeValue(4, 'interviewLateStage')
            return redirect('/results')
        elif len(jobHuntResponse) == 3:
            if 'applying' not in jobHuntResponse:
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewMidStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results')
            elif 'early' not in jobHuntResponse:
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewMidStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results')
            elif 'mid' not in jobHuntResponse:
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewLateStage')
                return redirect('/results')
            else: # if late not in
                storeValue(4, 'interviewNoStage')
                storeValue(4, 'interviewEarlyStage')
                storeValue(4, 'interviewMidStage')
                return redirect('/results')
        elif len(jobHuntResponse) == 2:
            if 'applying' not in jobHuntResponse:
                if 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewMidStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                elif 'mid' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                else: # if late not in
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results')
            elif 'early' not in jobHuntResponse:
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewMidStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                elif 'mid' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                else: # if late not in
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results')
            elif 'mid' not in jobHuntResponse:
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                elif 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewLateStage')
                    return redirect('/results')
                else: # if late not in
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewEarlyStage')
                    return redirect('/results')
            else: # if late not in
                if 'applying' not in jobHuntResponse:
                    storeValue(4, 'interviewEarlyStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results')
                elif 'early' not in jobHuntResponse:
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewMidStage')
                    return redirect('/results')
                else: # if mid not in  
                    storeValue(4, 'interviewNoStage')
                    storeValue(4, 'interviewEarlyStage')
                    return redirect('/results')
        elif len(jobHuntResponse) == 1:
            if 'applying' in jobHuntResponse:
                storeValue(4, 'interviewNoStage')
            elif 'early' in jobHuntResponse:
                storeValue(4, 'interviewEarlyStage')
            elif 'mid' in jobHuntResponse:
                storeValue(4, 'interviewMidStage')
            else:
                storeValue(4, 'interviewLateStage')
        else:
            error = 'Invalid input'
            return render_template('interview-stage.html', error=error)
        return redirect('/results')


@app.route('/add6')
def add6() -> 'html':
    aspiringRole_results()
    improvingSkills_results()
    jobHunting_results()
    

@app.route ('/results')
def results_page() -> 'html':
    aspiring_role = aspiringRole_results()
    improving_skills = improvingSkills_results()
    job_hunting = jobHunting_results()
    return render_template('results2.html',
                            results_aspiringRole=aspiring_role,
                            results_improvingSkills=improving_skills,
                            results_jobHunting=job_hunting,)




app.run(debug=True)

