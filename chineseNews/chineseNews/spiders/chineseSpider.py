import scrapy
from scrapy.spiders import Spider
from chineseNews.items import ChinesenewsItem


class chineseSpider(Spider):
    name = 'chineseSpider'
    start_urls = [#'http://www.chinanews.com/society.shtml',
                #'http://www.chinanews.com/mil/news.shtml',
                'http://finance.chinanews.com/it/gd.shtml']

    def parse(self, response):
        # 找到所有连接的入口,一条一条的新闻做解析 //*[@id="news"] //*[@id="news"]/div[2]/div[1]/div[1]/em/a
        for month in range(1, 8):
            for day in range(1, 31):
                if month is 2 and day > 28:
                    continue
                elif month is 7 and day > 6:
                    continue
                else:
                    if day in range(1, 10):
                        url_month = 'http://www.chinanews.com/scroll-news/it/2018/0' + str(month) + '0' + str(
                            day) + '/news.shtml'
                    else:
                        url_month = 'http://www.chinanews.com/scroll-news/it/2018/0' + str(month) + str(
                            day) + '/news.shtml'
                    yield scrapy.Request(url_month, callback=self.parse_month)

    def parse_month(self, response):
        # print(response.body)
        # 到了没一个月的页面下，提取每一天的url
        urls = response.xpath(
            '//div[@id="content_right"]/div[@class="content_list"]/ul/li/div[@class="dd_bt"]/a/@href').extract()
        for url in urls:
            yield scrapy.Request(url, callback=self.parse_news)

    def parse_news(self, response):
        item = ChinesenewsItem()
        item['url'] = response.xpath('//*[@id="newsurl"]/@value').extract()
        item['title'] = response.xpath('//div[@class="con_left"]/div[@id="cont_1_1_2"]/h1/text()').extract()
        item['content'] = '\n'.join(response.xpath('//div[@class="left_zw"]/p/text()').extract())
        item['url'] = item['url'][0].strip().replace('\n', '').replace('\r', '')
        item['title'] = item['title'][0].strip().replace('\n', '').replace('\r', '')
        # if len(item['content']) >= 2:
        #     item['content'] = item['content'][0][0:100] + item['content'][1][0:100]
        # else:
        #     item['content'] = item['content'][0][0:100]
        item['content'] = item['content'][0:100].strip().replace('\n', '').replace('\r', '')


        yield item