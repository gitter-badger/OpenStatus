'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 '

class user():
    name_raw = open("homedir/.OpenStatus/config/name", "r")
    name = name_raw.read()
    name_raw.close()
    def current_time():
        return datetime

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
