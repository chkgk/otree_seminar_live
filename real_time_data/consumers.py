from channels import Group
from channels.sessions import channel_session
import random
from .models import Player, Group as OtreeGroup, Constants
import json
import time


def ws_connect(message, group_name):
    Group(group_name).add(message.reply_channel)
    message.reply_channel.send({"accept": True})



# Connected to websocket.receive
def ws_message(message, group_name):
    # decode / de-serialize the message received
    decoded_message = json.loads(message.content['text'])

    # isolate number and player
    number_received = decoded_message['number']
    player = decoded_message['player']

    # prepare a reply
    reply = { 'number': number_received,
              'player': player
    }

    # serialize it for transport
    json_reply = {'text': json.dumps(reply)}

    Group(group_name).send(json_reply)



# Connected to websocket.disconnect
def ws_disconnect(message, group_name):
    Group(group_name).discard(message.reply_channel)