'OpenStatus - Backend to the OpenStatus decentralized social network.'
'GNU GPL v3.0 '

class timeline():
    def retrieve():
        return open("/var/OpenStatus/serve/stream.txt", "r").readlines()
    
    def post(content):
        writer = open("/var/OpenStatus/serve/stream.txt", "a").write(content)
        writer.close()
    
    def 
