import os
import dotenv
import certifi
import motor.motor_asyncio

class Connection:

    def __init__(self):
        dotenv.load_dotenv(dotenv.find_dotenv())
        self.__DB_TYPE = os.getenv('DB_TYPE')
        self.__DB_USER = os.getenv('DB_USER')
        self.__DB_PASSWORD = os.getenv('DB_PASSWORD')
        self.__DB_CLUSTER = os.getenv('DB_CLUSTER')
        self.__DB_NAME = os.getenv('DB_DATABASENAME')

    @property
    def getConnectionString(self):
        __connection_string = "{}://{}:{}@{}/{}?retryWrites=true&w=majority&ssl=true"
        return __connection_string.format(self.__DB_TYPE, 
                                        self.__DB_USER,
                                        self.__DB_PASSWORD,
                                        self.__DB_CLUSTER,
                                        self.__DB_NAME)
                                        
    @property
    def setDatabaseConnection(self):
        __client = motor.motor_asyncio.AsyncIOMotorClient(self.getConnectionString, tlsCAFile=certifi.where())
        __database = __client[self.__DB_NAME]
        return __database

    def setCollectionConnection(self, collection: str):
        __collection = self.setDatabaseConnection[collection]
        return __collection