                                                                                                                                                                                                                                # import flask dependencies
from flask import Flask, request, make_response, jsonify
from df_response_lib import *
import eliza
import anki_vector


# connect to robot
robot = anki_vector.Robot()
robot.connect()

# initialize the flask app
app = Flask(__name__)


# default route
@app.route('/')
def index():
    return 'Hello World!'


# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)

    print(req)

    # fetch action from json
    action = req.get('queryResult').get('action')

    queryText = req.get('queryResult').get('queryText')

    context = req.get('queryResult').get('outputContexts')[0]['name']

    ff_response = fulfillment_response()

    tl_response = telegram_response()

    res_objects = []

    if "rogerian" in context:

        therapist = eliza.eliza()
        response = therapist.respond(queryText)
        tl_message = tl_response.text_response([response])
        therapy_response = response

        robot.behavior.say_text(therapy_response)

        print(therapy_response)
        res_objects += [tl_message]

    elif 'meditate' in context and action == "meditate":
        title = "Unlike traditional meditation, Yichan would bring to experience in a virtual world. He has the most wisdom in this world, especially in the following areas. What do you wanna ask him?"
        buttons = [
                ['grownups', 'grownups'],
                ['relationship', 'relationship']
        ]
        tl_card = tl_response.card_response(title, buttons)
        tl_img = tl_response.image_response("https://yt3.ggpht.com/a/AGF-l78ar00PZOF6sejESnfkSE988MDPgS78iR0-7Q=s900-c-k-c0xffffffff-no-rj-mo")


        res_objects += [tl_img, tl_card]


        #img = tl_response.image_response("https://thumbs.gfycat.com/CrazyWhiteJoey-small.gif")



    ff_messages = ff_response.fulfillment_messages(res_objects)
    ff_text = ff_response.fulfillment_text([[""]])
    reply = ff_response.main_response(ff_text, ff_messages)

    print(reply)
    # return a fulfillment response
    return make_response(jsonify(reply))


# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    return results()



def read_emotion(string):
    result = service.tone(
        tone_input='%s' % string,
        content_type="text/plain").get_result()
    if not result.get('document_tone').get('tones'):
        emotion = "unexpressed"
    else:
        emotion = result.get('document_tone').get('tones')[0]['tone_name']
    return emotion

# run the app
if __name__ == '__main__':
   app.run()
   robot.disconnect()