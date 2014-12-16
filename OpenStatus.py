'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 or above - <http://gnu.org/licenses/gpl.txt>'

import datetime

class info():
    'Methods and funtions related to the OpenStatus backend/library itself.'
    def get_version():
        return "1.0.0.0"

class user():
    class name():
        'Methods and funtions related to operating with the OpenStatus user"s username.'

        def change_name(name):
            'Change the username of the OpenStatus user of the system"s currently logged in user.'
            writer = open("~.config/OpenStatus/config.txt", "w").write("name=" + name)
            writer.close()
        def get_name():
            'Get the username of the OpenStatus user of the system"s currently logged in user.'
            return open("~.config/OpenStatus/config.txt", "r").readline(0).strip("name=")
    class mentions():
        def get_count():
            'Get the number of mentions.'
            'Create a counter.'
            mentions_count = 0
            for posts in timeline.retrieve():
                if "@" + user.get_name() in posts:
                    mentions_count = mentions_count + 1
                    return mentions_count
        def get_mentions():
            'Get all the mentions as a list.'
            'Create a counter.'
            mentions_count = 0
            for posts in timeline.retrieve():
                mentions_count = mentions_count + 1
                if "@" + user.get_name() in posts:
                    return posts

    name = name()
    mentions = mentions()

class timestamper():
    'Funtions realted to operating with the timestamping system.'

    def stamp():
        'Create a timestapmp and return it to the user.'
        return "[" + str(datetime.time.hour) + ":" + str(datetime.time.minute) + ":" + str(datetime.time.second) + "||" + user.name.get_name + "] "

class timeline():
    'Methods and functions related to operating with the timeline.'

    def retrieve():
        'Retrieve the full timeline.'
        return open("~.config/OpenStatus/stream/stream.txt", "r").readlines()

    def post(content):
        'Post text specified by "content" to the public timeline.'
        writer = open("~.config/OpenStatus/stream/stream.txt", "a").write(timestamper.stamp + content)
        writer.close()

    class DynamicShift():
        'Put integer here containing the heap size not in dissk size space but in lenghth of cahracters.''
        heap_size = 0
        def check_if_needed():
            if len(open("~.config/OpenStatus/stream/stream.txt", "r").read()) == heap_size or len(open("~.config/OpenStatus/stream/stream.txt", "r").read()) > heap_size:
                'Do archiving here'

    DynamicShift = DynamicShift()

info = info()
user = user()
timesteamper = timestamper()
timeline = timeline()
