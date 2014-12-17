'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 or above - <http://gnu.org/licenses/gpl.txt>'

import datetime
import os

class info():
    'Methods and funtions related to the OpenStatus backend/library itself.'
    def get_version():
        return "1.0.0.0"

class user():
    'Classes to do with the user.'

    class name():
        'Methods and funtions related to operating with the OpenStatus user"s username.'

        def change_name(name):
            'Change the username of the OpenStatus user of the system"s currently logged in user.'
            writer = open("~.config/OpenStatus/config/config.txt", "w").write("name=" + name)
            writer.close()

        def get_name():
            'Get the username of the OpenStatus user of the system"s currently logged in user.'
            return open("~.config/OpenStatus/config/config.txt", "r").readline(0).strip("name=")

    class mentions():
        'Funtions related to operating with the mentions system.'

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

    class hashtags():
        'Funtions related to operating with the hashtagging system.'

        def get_count(hashtag):
            'Get the number of posts where the hashtag was used.'
            'Create a counter.'
            hashtags_count = 0
            for posts in timeline.retrieve():
                if hashtag in posts:
                    hashtags_count = hashtags_count + 1
                    return hashtags_count

        def get_hashtags(hashtag):
            'Get all the mentions as a list.'
            'Create a counter.'
            hashtags_count = 0
            for posts in timeline.retrieve():
                hashtags_count = hashtags_count + 1
                if hashtag in posts:
                    return posts

    hashtags = hashtags()
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
        return open("~.config/OpenStatus/network/timeline/default", "r").readlines()

    def post(content):
        'Post text specified by "content" to the public timeline.'
        writer = open("~.config/OpenStatus/network/timeline/default", "a").write(timestamper.stamp + content)
        writer.close()

    class DynamicShift():
        'Methods related to operating with the Dynamic-Shift system.'

        'Put integer here containing the heap size not in disk size space but in lenghth of cahracters.'
        heap_size = 0
        def shift_needed():
            if len(open("~.config/OpenStatus/network/timeline/default.txt", "r").read()) == heap_size or len(open("~.config/OpenStatus/stream/stream.txt", "r").read()) > heap_size:
                return True
            else:
                return False

        def shift():
            'Do archiving here'
            'Always do in a try statement, as the task could of been completed already by someone else.'
            try:
                os.move("~.config/OpenStatus/network/default.txt", "~.config/openStatus/network/archive/" + datetime.time.hour + "-" + datetime.time.minute + "-" + datetime.time.second + "-" + datetime.date.day + "-" + datetime.date.month + "-" + datetime.date.year)
                'Just in-case, create a new timeline.'
                writer = open("~.config/OpenStatus/network/default.txt", "w").write("")
                writer.close()
                'If the DynamicShift succeeds, return the error code "0".'
                return 0
            except:
                'If the DynamicShift fails for some reason, return the error code "1".'
                return 1

    class motd():
        def get_motd():
            return open("~.config/OpenStatus/network/.config/motd/motd.txt", "r").readlines()

    motd = motd()
    DynamicShift = DynamicShift()

info = info()
user = user()
timesteamper = timestamper()
timeline = timeline()
