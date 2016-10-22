from configparser import ConfigParser

conf_file = "./plugin.ini"
parser = ConfigParser()
parser.read(conf_file)

def get_plugin_name():
    return parser.get('DEFAULT', 'plugin')

def get_username():
    return parser.get('CREDS', 'username')

def get_password():
    return parser.get('CREDS', 'password')

def get_ip():
    return parser.get('CREDS', 'ip')
