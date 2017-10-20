import ConfigParser, os
import yaml

configuration = ConfigParser.ConfigParser()
if os.path.isfile('settings.local.yaml'):
    configuration = yaml.load(file("settings.local.yaml"))
elif os.path.isfile('settings.yaml'):
    configuration = yaml.load(file("settings.yaml"))
else:
    configuration.read('settings.cfg')


def get(*args, **kwargs):
    try:
        if type(configuration) is dict:
            return configuration[args[0]][args[1]]
        return configuration.get(*args, **kwargs)
    except KeyError:
        return ''


def items(*args, **kwargs):
    if type(configuration) is dict:
        return configuration[args[0]]
    return configuration.items(*args, **kwargs)


def get_database_uri():
    schema = get('database', 'schema')
    username = get('database', 'username')
    password = get('database', 'password')
    host = get('database', 'host')
    port = get('database', 'port')
    database = get('database', 'name')
    return "{}://{}:{}@{}:{}/{}".format(schema, username, password, host, port, database)
