import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '387216340:AAFZMz_-Ve4VeEuLSAMf3er0VyYpw03Fx44'
WEBHOOK_URL = 'https://deda5724.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'findid',
        'findcourse',
        'start',
        'change',
        'leave'
    ],
    transitions=[
        {
            'trigger' : 'advance',
            'source': 'user',
            'dest': 'start',
            'conditions': 'start'
        },
        {
            'trigger' : 'go_back',
            'source': 'start',
            'dest': 'user'
        },
        {
            'trigger' : 'advance',
            'source': 'user',
            'dest': 'findid',
            'conditions': 'findid'
        },
        {
            'trigger' : 'advance',
            'source': 'user',
            'dest': 'change',
            'conditions': 'change'
        },
        {
            'trigger' : 'advance',
            'source': 'change',
            'dest': 'user',
            'conditions': 'bear'
        },
        {
            'trigger' : 'advance',
            'source': 'change',
            'dest': 'user',
            'conditions': 'doge'
        },
        {
            'trigger' : 'advance',
            'source': 'change',
            'dest': 'user',
            'conditions': 'cat'
        },
        {
            'trigger' : 'advance',
            'source': 'change',
            'dest': 'change',
            'conditions': 'alwaysleave'
        },
        {
            'trigger': 'advance',
            'source': 'findid',
            'dest': 'user',
            'conditions': 'leave'
        },
        {
            'trigger' : 'advance',
            'source': 'user',
            'dest': 'user',
            'conditions': 'notfindid'
        },
        {
            'trigger' : 'advance',
            'source': 'findid',
            'dest': 'findcourse',
            'conditions': 'findcourse'
        },
        {
            'trigger' : 'advance',
            'source': 'findid',
            'dest': 'findid',
            'conditions': 'notfindcourse'
        },
        {
            'trigger': 'advance',
            'source': 'findcourse',
            'dest': 'leave',
            'conditions': 'alwaysleave'
        },
        {
            'trigger': 'advance',
            'source': 'leave',
            'dest': 'user',
            'conditions': 'yes'
        },
        {
            'trigger': 'advance',
            'source': 'leave',
            'dest': 'findcourse',
            'conditions': 'no'
        },
        {
            'trigger': 'advance',
            'source': 'leave',
            'dest': 'leave',
            'conditions': 'alwaysleave'
        },
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.from_user.last_name+update.message.from_user.first_name+" : "+update.message.text)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    print("show_fsm\n")
    byte_io = BytesIO()
    machine.get_graph().draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='img/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
