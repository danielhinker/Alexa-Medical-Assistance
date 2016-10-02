"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""



# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "I am your medical assistant around you" + \
                    "Tell me which patient information you want to pull up by saying, for example, " + \
                    "my patient is Robert Li"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Tell me which patient information you want to pull up by saying, for example, " + \
                    "my patient is Daniel Hinker"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Good luck Doctor! " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


# --------------- Patients --------------- #

def set_patient_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is a " + patient_race + " " + patient_gender + " aged " + patient_age + \
                        ". The patients vitals are within normal range" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_patient_from_session(intent, session):
    session_attributes = True
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        patient_race = "White"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "80mmhg"
        patient_resp = "Steady 15 breaths per minute"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "What do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What's the patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What's the patient's respiratory?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about the patient such as " + \
                        "What are my patient's vitals?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def create_patient_name_attributes(patient_name):
    return {"patientName": patient_name}

# --------------- Basic Info --------------- #

def set_race_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is a " + patient_race + " " + patient_gender + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_race_from_session(intent, session):
    session_attributes = True
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        patient_race = "White"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is " + patient_race + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about the patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



# --------------- Basic Info --------------- #

def set_height_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is " + patient_height + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_height_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient is " + patient_height + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Basic Info --------------- #
def set_weight_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is " + patient_weight + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's BMI?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_weight_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient is 150 pounds" + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Basic Info --------------- #
def set_age_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is " + patient_age  + "years old" + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's temperature?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_age_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient is 20 years old" + \
                        ". You can ask me information about " + patient_name + " by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_bmi_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the bmi of " + patient_name + " is " + patient_bmi  + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's respiratory rate?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_bmi_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient's body mass idex of 19.5" + " What do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_temp_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the temperature of " + patient_name + " is " + patient_temp  + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_temp_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient's temperature is 98.6 degrees" + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_vitals_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = patient_name + " is stable with a resting heart rate of 75 beats per minute and respiratory rate of 15 breathes per minute with a temperature of 98.6 degrees fahrenheit " + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's age?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_vitals_from_session(intent, session):
    session_attributes = true
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient is stable with a resting heart rate of 75 beats per minute and 15 breats per minute" + " What else do you need to know about " + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_resp_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the respiratory rate of " + patient_name + "is" + patient_respiratory + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_resp_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient has is breathing 15 breaths a minute " + " What else do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_os_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the oxygen saturation of " + patient_name + "is" + patient_os + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What are the procedures done on the patient?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_os_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient's oxygen saturation is at 80mmhg " + " What else do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_lab_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the CT Scan of " + patient_name + "is showing subdural hematoma" + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's gender?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_lab_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient had a CT scan showing subdural hematoma" + " What else do you need to know about " + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_note_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the attending nurse noted that, " + patient_name + "was stable" + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def get_notes_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "The attending nurse noted that the patient was stable" + " What do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



# --------------- Basic Info --------------- #
def set_bp_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "the blood pressure of " + patient_name + "is" + patient_bp + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_bp_from_session(intent, session):
    session_attributes = {create_patient_name_attributes(patient_name)}
    reprompt_text = None
    should_end_session = False

    if 'Name' not in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient's blood pressure is 120 over 20" + " What do you need to know about " + \
                        patient_name + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's temperature?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Basic Info --------------- #
def set_procedures_in_session(intent, session):
    """ Sets the color in the session and prepares the speech to reply to the
    user.
    """

    card_title = intent['name']
    session_attributes = True
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = intent['slots']['Name']['value']
        session_attributes = create_patient_name_attributes(patient_name)
        patient_race = "White"
        patient_gender = "Male"
        patient_age = "20"
        patient_bp = "120 over 80"
        patient_temp = "98.6 degrees"
        patient_weight = "150 pounds"
        patient_bmi = "12"
        patient_os = "normal"
        patient_respiratory = "15 breaths per minute"
        patient_height = "5 foot 10"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "patient" + patient_name + "underwent a craniotomy at 7 pm on March 17th" + \
                        "what else do you want to know about your patient" + \
                        ". You can ask me for specific vitals by saying, for example, " + \
                        "What is the patient's Blood pressure?"
        reprompt_text = "You can ask me anything about the patient's specific vitals such as, for example, " + \
                        "What is the patient's Temperature?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's BMI?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_procedure_from_session(intent, session):
    session_attributes = {}
    reprompt_text = None
    should_end_session = False

    if 'Name' in intent['slots']:
        patient_name = "Daniel Hinker"
        # session_attributes = create_patient_name_attributes(patient_name)
        speech_output = "Patient underwent a craniotomy at 7pm on March 17" + " What else do you need to know about " + \
                        ". You can ask me patient information by saying, for example, " + \
                        "What is my patient's bp?"
        reprompt_text = "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    else:
        speech_output = "I'm not sure which patient information that is " + \
                        "Please try again."
        reprompt_text = "I'm not sure which patient information that is " + \
                        "You can ask me anything about a patient such as " + \
                        "What is my patient's name?"
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    # print("on_intent requestId=" + intent_request['requestId'] +
    #       ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "WhatsMyPatientsIntent":
        return get_patient_from_session(intent, session)
    elif intent_name == "MyPatientIsIntent":
        return set_patient_in_session(intent, session)

    elif intent_name == "MyPatientsRaceIntent":
        return set_race_in_session(intent, session)
    elif intent_name == "WhatsMyPatientsRaceIntent":
        return get_race_from_session(intent, session)

    elif intent_name == "WhatsMyPatientsHeightIntent":
        return get_height_from_session(intent, session)
    elif intent_name == "MyPatientsHeightIntent":
        return set_height_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsWeightIntent":
        return get_weight_from_session(intent, session)
    elif intent_name == "MyPatientsWeightIntent":
        return set_weight_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsAgeIntent":
        return get_age_from_session(intent, session)
    elif intent_name == "MyPatientsAgeIntent":
        return set_age_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsBmiIntent":
        return get_bmi_from_session(intent, session)
    elif intent_name == "MyPatientsBmiIntent":
        return set_bmi_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsTempIntent":
        return get_temp_from_session(intent, session)
    elif intent_name == "MyPatientsTempIntent":
        return set_temp_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsOsIntent":
        return get_os_from_session(intent, session)
    elif intent_name == "MyPatientsOsIntent":
        return set_os_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsRespIntent":
        return get_resp_from_session(intent, session)
    elif intent_name == "MyPatientsRespIntent":
        return set_resp_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsVitalsIntent":
        return get_vitals_from_session(intent, session)
    elif intent_name == "MyPatientsVitalsIntent":
        return set_vitals_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsLabIntent":
        return get_lab_from_session(intent, session)
    elif intent_name == "MyPatientsLabIntent":
        return set_lab_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsNotesIntent":
        return get_notes_from_session(intent, session)
    elif intent_name == "MyPatientsNotesIntent":
        return set_notes_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsProceduresIntent":
        return get_procedures_from_session(intent, session)
    elif intent_name == "MyPatientsProceduresIntent":
        return set_procedures_in_session(intent, session)

    elif intent_name == "WhatsMyPatientsBpIntent":
        return get_bp_from_session(intent, session)
    elif intent_name == "MyPatientsBpIntent":
        return set_bp_in_session(intent, session)

    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")
    # if intent_name == "WhatsMyPatientsIntent":
    #     return get_patient_from_session(intent, session)
    # elif intenb_name == "MyPatientIsIntent":
    #     return set_patient_in_session(intent, session)
    #
    # if intent_name == "WhatsMyPatientsIntent":
    #     return get_patient_from_session(intent, session)
    # elif intent_name == "MyPatientIsIntent":
    #     return set_patient_in_session(intent, session)



def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------
def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])



    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
