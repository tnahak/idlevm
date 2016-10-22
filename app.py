# !/usr/bin
import web
import json
from manager import Manager as mgr

urls = (
    '/api', 'ApiManager'
)

class ApiManager:

    def __init__(self):
        pass

    def get_data(self):
        pass

    def create_resource(self):
        pass

    def GET(self):
        data = mgr.get_vm_data()
        return data

    def POST(self):
        pass

    def DELETE(self):
        pass 


if __name__ == "__main__":

    api = web.application(urls, globals())
    api.run()

