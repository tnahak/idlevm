import requests
import json

class Request:

    def __init__(self, username, password, ip):
        self.header = {}
        self.username = username
        self.password = password
        self.ip = ip

    def get(self, url):
        pass

    def post(self, url, request_body):

        print "URL URL URL : " + url
        request_body = json.dumps(request_body)
        header = {'Content-Type': 'application/json'}
        resp = requests.post(url, headers=header, data=request_body)

        return str(resp.text)


        
