'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 '

import datetime
import os

class user():
    name_raw = open(os.environ("HOME") + "/.OpenStatus/config.txt", "r")
    name = name_raw.readline(1).strip("name=")
    name_raw.close()
    def current_time():
        return str(datetime.time.hour) + ":" + str(datetime.time.minute) + ":" + str(datetime.time.second)

class generator():
    def generate_post(content):
        return "[" + user.current_time() + "||" + user.name + "] " + content

class timeline():
    def retrieve():
        return open("/var/OpenStatus/serve/stream.txt", "r").readlines()
    
    def post(content):
        writer = open("/var/OpenStatus/serve/stream.txt", "a").write(generator.generate_post(content))
        writer.close()
    
    def 
