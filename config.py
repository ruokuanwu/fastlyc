class Config(object):
    pass


class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wojiaokuan+25A@localhost/dev'
    JWT_SECRET_KEY = 'fastlyc'


class ProductionConfig(Config):
    ENV = 'production'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:wojiaokuan+25A@localhost/dev'
    JWT_SECRET_KEY = 'fastlyc'


app_config = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}

helper_config = {
    # fastlyc-v1
    "fastlyc_v1_log_file_path": "logs/apiv1.log"
}
