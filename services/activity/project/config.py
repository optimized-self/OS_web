class BaseConfig:
    """Base configuration"""
    TESTING = False

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
