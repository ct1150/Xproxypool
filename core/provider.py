from requests_html import HTMLSession
import datetime

class BaseProvider(object):
    def __init__(self,headers=None):
        self.proxylist = []
        self.session = HTMLSession()
        self.headers = headers or {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
    def crawler(self):
        pass

class XiciProvider(BaseProvider):
    def crawler(self):
        html = self.session.get('https://www.xicidaili.com/nn/',headers=self.headers).html
        iplist = [ip.text for ip in html.find('tr td:nth-child(2)')]
        portlist = [port.text for port in html.find('tr td:nth-child(3)')]
        addresslist = [address.text for address in html.find('tr td:nth-child(4)')]
        proxytypelist = [proxytype.text for proxytype in html.find('tr td:nth-child(5)')]
        httptypelist = [httptype.text for httptype in html.find('tr td:nth-child(6)')]
        for ip,port,address,proxytype,httptype in zip(iplist,portlist,addresslist,proxytypelist,httptypelist):
            proxydict = {
                "ip":ip,
                "port":port,
                "address":address,
                "proxytype":proxytype,
                "httptype":httptype,
                "rate":5,
                "create_time":datetime.datetime.now(),
                "test_time":datetime.datetime.strptime('2000','%Y')
            }
            self.proxylist.append(proxydict)
        return self.proxylist

if __name__ == '__main__':
    crawler = XiciProvider()
    print(crawler.crawler())

