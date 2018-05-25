import os


class Config(object):
    DEBUG = False
    DB_NAME = "heroku_hxwlp5lv"
    DB_HOST = "mongodb://heroku_hxwlp5lv:heroku_hxwlp5lv@ds135760.mlab.com:35760/heroku_hxwlp5lv"
    DB_USERNAME = ""
    DB_PASSWORD = ""
    # Web Server details
    WEB_SERVER_PORT = 8001

    # Intent Classifier model detials
    MODELS_DIR = "model_files"
    INTENT_MODEL_NAME = "intent.model"
    DEFAULT_FALLBACK_INTENT_NAME = "fallback"
    DEFAULT_WELCOME_INTENT_NAME = "init_conversation"


class Development(Config):
    DEBUG = True


class Production(Config):
    # MongoDB Database Details
    DB_HOST = "mongodb://127.0.0.1:27017/"
    DB_USERNAME = ""
    DB_PASSWORD = ""

    # Web Server details
    WEB_SERVER_PORT = 8001
