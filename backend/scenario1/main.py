#!/usr/bin/env python3
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import requests
import ast

URL = 'http://localhost:3001/api/v1/activities/'
app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def launch_request_handler():
    speech_text = "実験を開始します。実験番号を指定して下さい。"
    return question(speech_text).reprompt(speech_text).simple_card("", speech_text)


@ask.intent('ExperimentNumberIntent', convert={'number': int})
def number_intent_handler(number):
    if number == 1:
        res = requests.get(URL + 'going_out/date/2018-12-02')
    elif number == 2:
        res = requests.get(URL + 'going_out/date/2018-12-03')
    
    data = ast.literal_eval(res.text)[0]
    print(data)

    if data['count']:
        speech_text = "今日は外で何をしてたの？"
    else:
        speech_text = "今日はお家で何をしてたの？"

    return question(speech_text).reprompt(speech_text).simple_card("", speech_text)


@ask.intent('WordIntent', convert={'word': str})
def word_intent_handler(word):
    print(word)
    speech_text = word + "をしていたのですね"
    return statement(speech_text).simple_card("", speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


@app.route("/healthz", methods=['GET'])
def healthz():
    return "ok"


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
