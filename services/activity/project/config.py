import os
from urllib import parse

class BaseConfig:
    """Base configuration"""
    TESTING = False

    user    = parse.quote_plus(os.environ['DB_USER'])
    host    = parse.quote_plus(os.environ['DB_HOST'])
    port    = parse.quote_plus(os.environ['DB_PORT'])
    db_name = os.environ['DB_NAME']

    # extract the db password from the secret file
    with open(os.environ['DB_PASSWORD_FILE']) as f:
        password = parse.quote_plus(f.readline().rstrip('\n'))

    # build the db connection string and store it in MONGODB_HOST
    MONGODB_HOST = f"mongodb://{user}:{password}@{host}:{port}/{db_name}?authSource=admin"

class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    pass

class TestingConfi(BaseConfig):
    """Testing configuration"""
    TESTING = True
    pass

class ProductionConfig(BaseConfig):
    """Production configuration"""
    pass
