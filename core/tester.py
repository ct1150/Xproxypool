from requests.exceptions import ProxyError

from db.mongo_cli import MongoCli
import requests

def tester(ip,port,httptype='http'):
    proxies = {
        "http": "http://"+str(ip)+":"+str(port),
        "https": "http://"+str(ip)+":"+str(port)
    }
    try:
        res = requests.get(httptype+'://www.baidu.com',proxies=proxies)
        if res.status_code == '200':
            return True
        else: return False
    except ProxyError as e:
        print(e)
        return False


if __name__ == '__main__':
    mongocli = MongoCli()
    for data in mongocli.find().sort('test_time').limit(100):
        print(data)
        if tester(data['ip'],data['port'],httptype=data['httptype']):
            print(data['httptype']+"://"+data['ip']+":"+str(data['port'])+'验证通过')
        else:
            print(data['httptype']+"://"+data['ip']+":"+str(data['port'])+'验证失败')
