'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 - <http://gnu.org/licenses/gpl.txt>'

import datetime
import os

class user():
    'Get the currently logged in user"s OpenStatus name.'
    name = open(os.environ("HOME") + "/.OpenStatus/config.txt", "r").readline(0).strip("name=")
    def current_time():
        return str(datetime.time.hour) + ":" + str(datetime.time.minute) + ":" + str(datetime.time.second)

class timestamper():
    def stamp():
        'Create a timestapmp and return it to the user.'
        return "[" + user.current_time() + "||" + user.name + "] "

class timeline():
    def retrieve():
        'Retrieve the full timeline.'
        return open("/var/OpenStatus/serve/stream.txt", "r").readlines()

    def post(content):
        'Post text specified by "content" to the public timeline.'
        writer = open("/var/OpenStatus/serve/stream.txt", "a").write(timestamper.stamp + content)
        writer.close()

user = user()
timesteamper = timestamper()
timeline = timeline()
