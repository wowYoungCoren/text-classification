#!/usr/bin/env bash

# scrapy默认为追加形式输出文件
# scrapy crawl chineseSpider -o IT4.json
# 以重写方式输出文件
# 终端不输出抓取过程 --nolog
scrapy crawl chineseSpider -t csv -o - > "IT4.csv"
