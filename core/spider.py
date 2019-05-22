from pymongo.errors import BulkWriteError

from core.provider import XiciProvider
from db.mongo_cli import MongoCli
from multiprocessing import Process

mongocli = MongoCli()

def spider_xici():
    xicispider = XiciProvider()
    proxylist = xicispider.crawler()
    try:
        a = mongocli.insert_many(proxylist, ordered=False)
        print('入库完成'+str(len(proxylist)))
    except BulkWriteError as e:
        print("数据重复，入库数量"+str(len(proxylist)-len(e.details['writeErrors'])))
    return

if __name__ == '__main__':
    xici_process = Process(target=spider_xici)
    xici_process.start()