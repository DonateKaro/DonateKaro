class Config:
    TESTING = False
    DATABASE_URL = "postgres://ecsugvbutyrcno:4bd33495ccccaed20a615cdcdc3a2b3c621ddaf4aa93bec51ade97cf41aa9d18@ec2-34-227-120-79.compute-1.amazonaws.com:5432/dafr5uav2id13j"


class ProductionConfig(Config):
    DEBUG = False
    ENV = 'production'
    SESSION_COOKIE_SECURE = True



class DevelopmentConfig(Config):
    ENV = 'development'
    DEBUG = True
    SESSION_COOKIE_SECURE = False
