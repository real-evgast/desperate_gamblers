import os


app_dir = os.path.abspath(os.path.dirname(__file__))
LOCAL_DATABASE_URL = 'postgresql://postgres:1984@localhost:5432/postgres'
LOCAL_SECRET_KEY = 'dev-only-secret-key-change-in-production'


def normalize_database_url(url):
    if url and url.startswith('postgres://'):
        return url.replace('postgres://', 'postgresql://', 1)
    return url


def get_database_url(default=None):
    return normalize_database_url(
        os.environ.get('DATABASE_URL')
        or os.environ.get('POSTGRES_URL')
        or os.environ.get('POSTGRES_PRISMA_URL')
        or default
    )


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    SECRET_KEY = os.environ.get('SECRET_KEY', LOCAL_SECRET_KEY)
    SQLALCHEMY_DATABASE_URI = get_database_url(LOCAL_DATABASE_URL)


class DevelopementConfig(DevelopmentConfig):
    pass


class ProductionConfig(BaseConfig):
    DEBUG = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_database_url()
