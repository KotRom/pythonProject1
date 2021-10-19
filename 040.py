# pip install configparser
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')
print(config['DATABASE']['host'])
print(config['DEFAULT']['login'])
print(list(config['DATABASE']))
print(config['DATABASE']['pass'])
config.add_section('NEW_SECTION')
config.set('NEW_SECTION', 'login', 'PEOPLE')
print(config['NEW_SECTION']['login'])

with open('config.ini', 'w') as config_file:
    config.write(config_file)
