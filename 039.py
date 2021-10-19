# pip install configparser
from configparser import ConfigParser

config = ConfigParser()

config['DEFAULT'] = {
    'login': 'hello_world',
    'pass': '12345',
    'setting': 'True',
    'setting2': 'None'
}

config['DATABASE'] = {
    'host': 'localhost',
    'user': 'root',
    'pass': '12345',
    'name': 'test_db'
}

config['EMAIL'] = {
    'email': 'test@example.com',
    'pass': '67789'
}

with open('config.ini', 'w') as config_file:
    config.write(config_file)