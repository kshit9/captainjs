import os


class Config(object):
    DEBUG = False
    DB_NAME = "iky-ai"
    DB_HOST = "mongodb://kshitij:Kshitij.9@ds119070.mlab.com:19070/captainjss"
    DB_USERNAME = "kshitij"
    DB_PASSWORD = "Kshitij.9"
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
    DB_HOST = "mongodb://mongodb:27017/"
    DB_USERNAME = ""
    DB_PASSWORD = ""

    # Web Server details
    WEB_SERVER_PORT = 8001
