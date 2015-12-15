import os
import platform
import yaml

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

with open(os.path.join(__location__, 'settings.yaml')) as yaml_settings:
    settings = yaml.load(yaml_settings)


class Config(object):
    DEBUG = False
    TESTING = False
    BOT_DEBUG = False
    BOT_TOKEN = settings['bot_token']


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    BOT_DEBUG = 'Win' in platform.system()
