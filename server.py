from eve import Eve
import configparser

Config = configparser.ConfigParser()
Config.read("server.ini")

print(Config.get('mongo', 'username'))

app = Eve()
app.run()
