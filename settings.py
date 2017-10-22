import configparser

Config = configparser.ConfigParser()
Config.read("server.ini")

DOMAIN = {'people': {}}

# MongoDB
MONGO_HOST = Config.get('mongo', 'host')
MONGO_PORT = Config.get('mongo', 'port')
MONGO_USERNAME = Config.get('mongo', 'username')
MONGO_PASSWORD = Config.get('mongo', 'password')
MONGO_DBNAME = Config.get('mongo', 'dbname')
