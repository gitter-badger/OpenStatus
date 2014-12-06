'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 or above - <http://gnu.org/licenses/gpl.txt>'

import datetime
import os

class user()
    class name():
        'Methods and funtions related to operating with the OpenStatus user"s username.'

        def change_name(name):
            'Change the username of the OpenStatus user of the system"s currently logged in user.'
            writer = open(os.environ("HOME") + "/.OpenStatus/config.txt", "w").write("name=" + name)
            writer.close()
        def get_name():
            'Get the username of the OpenStatus user of the system"s currently logged in user.'
            return name = open(os.environ("HOME") + "/.OpenStatus/config.txt", "r").readline(0).strip("name=")
    
    def get_mentions():
        'Create a counter.'
        mentions_count = 0
        for posts in timeline.retrieve():
            if "@" + user.get_name() in posts:
                mentions_count = mentions_count + 1
        return mentions_count

    name = name()

class timestamper():
    'Funtions realted to operating with the timestamping system.'
    
    def stamp():
        'Create a timestapmp and return it to the user.'
        return "[" + str(datetime.time.hour) + ":" + str(datetime.time.minute) + ":" + str(datetime.time.second) + "||" + user.name.get_name + "] "

class timeline():
    'Methods and functions related to operating with the timeline.'

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
