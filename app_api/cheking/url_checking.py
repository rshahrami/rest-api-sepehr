import os

data=open(os.path.join(os.path.dirname(__file__),'url_collection'), 'r')

lines=data.readlines()

def url_pass(header_origin):
    for line in lines:
        line=line.rstrip("\n")
        if header_origin==line:
            return True


