from client import Request
import config

class VCenter:

    def __init__(self):
        self.username = config.get_username()
        self.password = config.get_password()
        self.ip = config.get_ip()

    def parse_vm_list(self, raw_vm_list):
        vm_list = []
        hits = raw_vm_list['hits']['hits']
        for hit in hits:
            clusters = hit['_source']['node_data']['Datacenter_Clusters']
            for cluster in clusters:
                hosts = cluster['Datacenter_Hosts']
                for host in hosts:
                    vms = host['Datacenter_VMs']
                    for vm in vms:
                        vm = vm['Datacenter_VM_Name']
                        vm_list.append(str(vm))
        vm_list = list(set(vm_list))
        return vm_list

    def get_vm_list(self, start, end):
        request = Request(self.username, self.password, self.ip)
        start_date = start
        end_date = end
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
        return self.parse_vm_list(resp) 
 
    def get_vm_data(self, start_date, end_date):
        return "VM data for vCenter"

def get_plugin():
    return VCenter()


