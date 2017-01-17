# Kik bot messenger using Python 3, Flask, Gunicorn and Jinja 2
# By: Andre Fischbacher

from flask import Flask, request, Response
import os
from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage

app = Flask(__name__)

kik = KikApi("afischbacher95", "2dd4a60c-287b-4b95-8252-fd8dfe577759")
config = Configuration(webhook='https://kik-bot-messenger.herokuapp.com/incoming')
kik.set_configuration(config)

global kik_chat_id, user

@app.route('/incoming', methods=['POST'])
def incoming():
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:

        kik_chat_id = message.chat_id
        user = message.from_user

        if isinstance(message, TextMessage):
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])


    kik.send_broadcast([
        TextMessage(
            to=user,
            chat_id=kik_chat_id,
            body="Im Andre, Nice to meet you!"
        )
    ])

    return Response(status=200)


@app.route("/", methods=['GET'])
def hello():
    return "<h1> Hello Welcome To My Kik Bot Messenger </h1>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
