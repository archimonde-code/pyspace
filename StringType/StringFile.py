import requests
from lxml import etree
from fake_useragent import UserAgent


class GetBook(object):
    def __init__(self):
        self.url = 'https://book.qidian.com/info/1020580616#Catalog'
        ua = UserAgent(verify_ssl=False)
        for i in range(1, 100):
            self.headers = {
                'User-Agent': ua.random
            }

    def get_html(self, url):
        response = requests.get(url, headers=self.headers)
        html = response.content.decode('utf-8')
        return html

    def parse_html(self, html):
        target = etree.HTML(html)
        links = target.xpath('//ul[@class="cf"]/li/a/@href')
        for link in links:
            host = 'https:'+link
            # 解析链接地址
            res = requests.get(host, headers=self.headers)
            c = res.content.decode('utf-8')
            target = etree.HTML(c)
            names = target.xpath('//span[@class="content-wrap"]/text()')
            results = target.xpath('//div[@class="read-content j_readContent"]/p/text()')
            for name in names:
                print(name)
                with open('H:/Pycharm/' + name + '.txt', 'a') as f:
                    for result in results:
                        f.write(result+'\n')

    def main(self):
        url = self.url
        html = self.get_html(url)
        self.parse_html(html)


if __name__ == '__main__':

    spider = GetBook()
    spider.main()
