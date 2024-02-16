class Config(object):
    TESTING = False
    ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
    UPLOAD_FOLDER = './uploads'
    OUTPUT_FOLDER = './output'

class ProductionConfig(Config):
    def __init__(self):
        super().__init__()
        self.DATABASE_URI = 'mysql://user@localhost/foo'

class DevelopmentConfig(Config):
    def __init__(self):
        super().__init__()
        self.DATABASE_URI = "sqlite:////tmp/foo.db"

class TestingConfig(Config):
     def __init__(self):
        super().__init__()
        self.DATABASE_URI = 'sqlite:///:memory:'
        self.TESTING = True    