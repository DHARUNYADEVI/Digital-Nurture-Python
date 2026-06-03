import configparser
class Config:
    pass
class DatabaseConfig(Config):
    def load(self):
        config = configparser.ConfigParser()
        config.read("db.ini")
        print("Host:", config["DATABASE"]["host"])
        print("User:", config["DATABASE"]["user"])
db = DatabaseConfig()
db.load()