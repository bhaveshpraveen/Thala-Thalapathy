from channels import Group
import rethinkdb as r
import json


def update(person):
    r.connect("localhost", 28015).repl()

    if 'thalapathy' in person:
        r.table('rating').filter(lambda person: person['name'] == 'thalapathy').update(
            lambda person: {'votes': person['votes'] + 1}).run()
    else:
        r.table('rating').filter(lambda person: person['name'] == 'thala').update(
            lambda person: {'votes': person['votes'] + 1}).run()


def get_value():
    r.connect("localhost", 28015).repl()
    cursor = r.table('rating').run()
    persons = list(cursor)
    return {'text': json.dumps(
        {
            persons[0]['name']: persons[0]['votes'],
            persons[1]['name']: persons[1]['votes']
        }
    )}


def ws_connect(message):
    message.reply_channel.send({"accept": True})
    Group('users').add(message.reply_channel)


def ws_disconnect(message):
    Group('users').discard(message.reply_channel)


def ws_message(message):
    if 'thalapathy' in str(message['text']):
        update('thalapathy')
    else:
        update('thala')

    values = get_value()

    Group("users").send(values)