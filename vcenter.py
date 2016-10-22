from client import Request
import config

class VCenter:

    def __init__(self):
        self.username = config.get_username()
        self.password = config.get_password()
        self.ip = config.get_ip()

    def get_vm_list(self, start, end):

        request = Request(self.username, self.password, self.ip)

        start_date = "2016-10-20T13:50:15"
#        start_date = start

        end_date = "2016-10-20T13:50:15"
#        end_date = end

        url = "http://" + self.ip + ":9200/monitor/vcenter/_search"

        body =  {
             "size": 10,
             "query": {
                  "filtered": {
                       "query": {
                           "query_string": {
                           "query": "node_subtype:\"Datacenter\"",
                           "analyze_wildcard": "true"
                           }
                       },
                       "filter": {
                           "bool": {
                               "must": [
                                   {
                                        "range": {
                                            "@timestamp": {
                                                "gte": start_date,
                                                "lte": end_date
                                             }
                                        }
                                   }          
                               ],
                               "must_not": []
                          }
                       }   
                  }
            }
        }
        resp = request.post(url, body)
        return resp
 
    def get_vm_data(self, start_date, end_date):

        return "VM data for vCenter"



def get_plugin():
    return VCenter()

