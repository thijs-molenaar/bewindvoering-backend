import configparser

Config = configparser.ConfigParser()
Config.read("server.ini")

# set dateformat so posting of dates to server is easy
# format example: "1999-12-31"
DATE_FORMAT = "%Y-%m-%d"

# TODO: set up mongo auth
# MongoDB
MONGO_HOST = Config.get('mongo', 'host')
MONGO_PORT = Config.get('mongo', 'port')
#MONGO_USERNAME = Config.get('mongo', 'username')
#MONGO_PASSWORD = Config.get('mongo', 'password')
MONGO_DBNAME = Config.get('mongo', 'dbname')

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
RESOURCE_METHODS = ['GET', 'POST', 'DELETE']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']

schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/pyeve/cerberus) for details.
    'firstname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True
    },
    'lastname': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 100,
        'required': True,
    },
    'dob': {
        'type': 'datetime',
        'required': True,
    },
}

people = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'person',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    #'additional_lookup': {
    #    'url': 'regex("[\w]+")',
    #    'field': 'lastname'
    #},

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],

    'schema': schema
}

# accessible resources of API
DOMAIN = {'people': people}
