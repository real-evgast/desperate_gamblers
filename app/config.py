import os
app_dir = os.path.abspath(os.path.dirname(__file__))

class Base_config:
    SECRET_KEY = "hfjksldjryt6783kmdhfdfgvbnfghddjulpfkikotg654132645kjhfdgghjkfdsdfhkgj645489691065df564sdd65f4sd23ds2wqertyuiosdxcvbnmwedrfghjkpl,oikijnyuhtygvrdf"
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:1984@localhost:5432/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopementConfig(Base_config):
    DEBUG = True

class ProductionConfig(Base_config):
    DEBUG = False