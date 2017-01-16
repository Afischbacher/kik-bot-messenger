from flask import Flask, request, Response
import os
from kik import KikApi, Configuration
from kik.messages import messages_from_json, TextMessage

app = Flask(__name__)

kik = KikApi("afischbacher95", "2dd4a60c-287b-4b95-8252-fd8dfe577759")
config = kik.get_configuration()

kik.set_configuration(Configuration(webhook='https://kik-bot-messenger.herokuapp.com/incoming'))


@app.route('/incoming', methods=['GET'])
def incoming():
    if not kik.verify_signature(request.headers.get('X-Kik-Signature'), request.get_data()):
        return Response(status=403)

    messages = messages_from_json(request.json['messages'])

    for message in messages:
        if isinstance(message, TextMessage):
            kik.send_messages([
                TextMessage(
                    to=message.from_user,
                    chat_id=message.chat_id,
                    body=message.body
                )
            ])

    return Response(status=200)

@app.route("/", methods=['GET'])
def hello():
    return "Hello World"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
