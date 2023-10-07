# config.py

import pyodbc

class Config:
    SECRET_KEY = 'clave_secreta_para_proteger_sesiones'
    DEBUG = True

    # Configuración de la base de datos MS Access
    DATABASE_CONNECTION_STRING = r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Desktop\BP II\Examen II\EXAMEN-ii\TaskDB.accdb;'

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}
