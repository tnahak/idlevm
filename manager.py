import json
import config

class PluginManager:

    @staticmethod
    def get_plugin_name():
        return config.get_plugin_name()

    @staticmethod
    def load_plugin():
        plugin_name = PluginManager.get_plugin_name()
        return __import__(plugin_name)

class Manager:

    @staticmethod
    def get_vm_data():

        start_date = "2016-10-20T13:50:15"
        end_date = "2016-10-20T13:50:15"
        plugin_handle = PluginManager.load_plugin()

        return plugin_handle.get_plugin().get_vm_list(start_date, end_date)

