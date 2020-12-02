import configparser
import os

cur_path = os.path.dirname(os.path.realpath(__file__))
config_path = os.path.join(cur_path, "config.ini")

conf = configparser.ConfigParser()
conf.read(config_path)


def get_user_data_dir():
    return conf.get("chrome_options", "user-data-dir")

def get_debugger_address():
    return conf.get("chrome_options", "debuggerAddress")

user_data_dir = conf.get("chrome_options", "user-data-dir")
debugger_address = conf.get("chrome_options", "debuggerAddress")
# print(user_data_dir)