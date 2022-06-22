# This program will help you find the right article based on your needs.

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


#### Start of program UX ####

print("Hello! This program will recommend you with the best articles based on your needs. Let's get started by answering a few questions.")

# First set of questions: About You

isDesignerValue = input("Are you currently working as a product designer? (Y or N) ")
if isDesignerValue == 'Y':
    dict[1]['isDesigner'] += 1
else:
    aspiringDesignerValue = input("Are you interested in becoming a product designer? (Y or N) ")
    if aspiringDesignerValue == 'Y':
        dict[1]['aspiringDesigner'] += 1

# Second set of questions: Your Goals

yourGoalsValue = input("Which of the following are you interested in? A: Improving my skills / learning new skills. B: Finding a new job. C: Breaking into tech. ")
if yourGoalsValue == 'A':
    dict[2]['improvingSkills'] += 1
else:
    if yourGoalsValue == 'B':
        dict[2]['findingNewJob'] += 1
    else:
        dict[2]['breakingIn'] += 1
                
    # Third set of questions: Job Hunting Status

    jobHuntingValue = input("Are you actively applying and/or interviewing? (Y or N) ")
    if jobHuntingValue == 'Y':
        dict[3]['activelyApplying'] += 1
        interviewValue = input("What stage of the process are you in? A: Just applying, I haven't started interviewing. B: Early stage - applying, speaking to recruiters. C: Middle stage - speaking to hiring manager, design exercise. D: Late stage - portfolio presentation, team interviews. ")
        if interviewValue == 'A':
            dict[3]['interviewNoStage'] += 1
        if interviewValue == 'B':
            dict[3]['interviewEarlyStage'] += 1
        if interviewValue == 'C':
            dict[3]['interviewMidStage'] += 1
        if interviewValue == 'D':
            dict[3]['interviewLateStage'] += 1


###  Recommendation Logic ###
            
print("Based on your responses, here are your recommended articles: ")

# Improving Skills

if dict[2]['improvingSkills'] == 1:
    print(
        "Product + Design Resources series \
        What Questions to Ask In Your First 1-1's With Your New Teammates \
        Tips for Remote Offboarding as a Product Designer \
        Crafting Your Elevator Pitch as a Product Designer"
        )
else:

# Job Hunting

    if dict[3]['activelyApplying'] == 0: # For now, this is the same as interviewNoStage
        print( 
            "Organizing Your Product Design Job Hunting Process \
            Crafting Your Elevator Pitch As A Product Designer \
            How to Prepare for Your Product Design Interview Loop \
            Navigating the Design Recruiter Phone Screening \
            How to Evaluate Company Culture for Product Design Roles"
            )

    if dict[3]['interviewNoStage'] == 1:
        print(
            "Organizing Your Product Design Job Hunting Process \
            Crafting Your Elevator Pitch As A Product Designer \
            How to Prepare for Your Product Design Interview Loop \
            Navigating the Design Recruiter Phone Screening \
            How to Evaluate Company Culture for Product Design Roles"
            )

    if dict[3]['interviewEarlyStage'] == 1:
        print(
            "How to Evaluate Company Culture for Product Design Roles \
            Crafting Your Elevator Pitch As A Product Designer \
            Organizing Your Product Design Job Hunting Process \
            Navigating the Hiring Manager Interview \
            Navigating the Design Recruiter Phone Screening \
            How to Prepare for Your Product Design Interview Loop"
            )

    if dict[3]['interviewMidStage'] == 1:
        print(
            "How to Evaluate Company Culture for Product Design Roles \
            Navigating the Hiring Manager Interview \
            Navigating the Portfolio Presentation Part 1 \
            Organizing Your Product Design Job Hunting Process"
            )

    if dict[3]['interviewLateStage'] == 1:
        print(
            "Navigating the Portfolio Presentation \
            How to Prepare for Your Product Design Interview Loop \
            Tips for Remote Offboarding as a Product Designer \
            What Questions to Ask In your first 1-1's With Your New Teammates"
            )







