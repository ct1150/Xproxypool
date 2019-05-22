import pymongo
from setting import *

class MongoCli(object):
    def __init__(self):
        self.client = pymongo.MongoClient(host=MONGO_SERVER,port=MONGO_PORT)
        self.db = self.client[MONGO_DB]
        self.col = self.db[MONGO_COL]
        self.col.ensure_index([('ip',1)],unique=True,name='idx_ip')
    def __getattr__(self,attr):
        return getattr(self.col,attr)

if __name__ == '__main__':
    mongocli = MongoCli()


