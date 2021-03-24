#!/usr/bin/env python3
from flask import Flask
from flask_ask import Ask, request, session, question, statement
import requests
import ast
import datetime

URL = 'http://localhost:3002/api/v1/todo/'
app = Flask(__name__)
ask = Ask(app, '/')


@ask.launch
def launch_request_handler():
    speech_text = "シナリオ2の検証を開始します。明日、外出してみませんか？"
    return question(speech_text).reprompt(speech_text).simple_card("", speech_text)


@ask.intent('AMAZON.YesIntent')
def yes_intent_handler():
    tomorrow_str = str(datetime.date.today() + datetime.timedelta(days=1))

    todo = {
                'uid': 1000,
                'date': tommorrow_str
                'content': 'going_out',
                'done': 'false'
            }

    res = requests.post(URL, todo)
    speech_text = "明日の行動予定に外出を追加しました。"
    return statement(speech_text).simple_card("", speech_text)


@ask.intent('AMAZON.NoIntent')
def no_intent_handler():
    speech_text = "そうですか、残念です。外出は健康に良いですよ。"
    return statement(speech_text).simple_card("", speech_text)


@ask.session_ended
def session_ended():
    return "{}", 200


@app.route("/healthz", methods=['GET'])
def healthz():
    return "ok"


if __name__ == '__main__':
    app.run(host='localhost', port=8080)
