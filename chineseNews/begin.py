from scrapy import cmdline
# 原始csv文件
cmdline.execute("scrapy crawl chineseSpider -o IT4.json".split())
