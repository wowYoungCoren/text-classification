import requests
import os
import time
from hashlib import md5
from urllib.parse import urlencode
import json
from pyquery import PyQuery as pq
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.wait import WebDriverWait

'''chrome_options=Options()
#设置chrome浏览器无界面模式
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(chrome_options=chrome_options)'''


class newsSpider():
    def __init__(self,baseUrl,headers,params,label):
        
        self.headers = headers
        self.label = label
        self.params = params
        self.baseUrl = baseUrl +urlencode(self.params)
        chrome_options=Options()
        #设置chrome浏览器无界面模式
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.wait = WebDriverWait(self.browser,5)
        
    def getPage(self):
        try:
            response = requests.get(self.baseUrl,headers=self.headers)
            if response.status_code == 200:
                print('get成功')
                #print(response.text)
                return response.json()
            else:
                pass
        except requests.ConnectionError as e:
            print('get失败') 

    def parsePage(self,json):
        if json:
            print('解析页面')
            items = json.get('data')
            for item in items:
                docUrl = item.get('source_url')
                content = self.getDoc('https://www.toutiao.com'+docUrl)
                yield {
                    'content':content,
                    'label':self.label,
                }
        else:
            print('无页面可解析')

    def getDoc(self,docUrl):
        try:
            self.browser.get(docUrl)
            print('爬取文章'+docUrl)
            docText = ""
            title = self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR,'.article-title'))
            )
            #title = self.browser.find_element_by_css_selector('.article-title').text
            docText = title.text
            contents = self.browser.find_elements_by_css_selector(".article-content p")
            for content in contents[1:]:
                docText = docText + content.text
            #time.sleep(1)
            return docText  
        except TimeoutException as e:
            print('爬取文章失败')
            return ""

    def writeItem(self,item,name):
        with open ('datasource/{}.txt'.format(name),'a',encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False)+'\n')

    def startSpider(self,name):
        #result = self.getPage()
        while (True):
            result = self.getPage()
            #print(result)
            try:
                if (result.get('next').get('max_behot_time')):
                    self.parsePage(result)
                    for item in self.parsePage(result):
                        self.writeItem(item,name)
                    print(self.params['max_behot_time'])
                    self.params['max_behot_time'] = result.get('next').get('max_behot_time')
                    self.params['max_behot_time_tmp'] = result.get('next').get('max_behot_time')
                    print(self.params['max_behot_time'])
                else:
                    break
            except AttributeError as e:
                print('结束爬取')
                break
        self.browser.close()
                

                
            


'''def test():
    headers ={
        'Host':'www.toutiao.com',
        'Referer':'https://www.toutiao.com/ch/news_sports/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'tt_webid=6663323848248755725; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1693831df34472-0f937e1740d2eb-162a1c0b-1fa400-1693831df35fe9; CNZZDATA1259612802=630908265-1551425067-https%253A%252F%252Fwww.google.com.hk%252F%7C1551425067; __tasessionId=5vwu7psj91551425986390; tt_webid=6663323848248755725; csrftoken=8e3462b8d4014dd38ca1b00b3c81c3da'
    }
    params = {
        'category':'news_sports',
        'utm_source':'toutiao',
        'widen':1,
        'tadrequire':'true',
        'max_behot_time':1552348684,
        'max_behot_time_tmp':1552348684,
        'as':'A1C5AC28D780B2B',
        'cp':'5C87009BD2BB6E1',
        '_signature':'K9aocwAAd1gpe7-1CuY6mCvWqG'
    }

    baseurl = 'https://www.toutiao.com/api/pc/feed/?'
    url = baseurl + urlencode(params)
    url = 'https://www.toutiao.com/group/6666973298212995588/' 
    browser.get(url)
    doc = pq(browser.page_source)
    #print(browser.page_source)
    title = browser.find_element_by_css_selector('.article-title').text
    print(title)
    text1 = browser.find_elements_by_css_selector(".article-content p")
    for texts in text1[1:]:
        print(texts.text)
    
    print(docTitle)
#test()'''

headers ={
        'Host':'www.toutiao.com',
        'Referer':'https://www.toutiao.com/ch/news_sports/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'tt_webid=6663323848248755725; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1693831df34472-0f937e1740d2eb-162a1c0b-1fa400-1693831df35fe9; CNZZDATA1259612802=630908265-1551425067-https%253A%252F%252Fwww.google.com.hk%252F%7C1551425067; __tasessionId=5vwu7psj91551425986390; tt_webid=6663323848248755725; csrftoken=8e3462b8d4014dd38ca1b00b3c81c3da'
    }
params = {
        'category':'news_sports',
        'utm_source':'toutiao',
        'widen':1,
        'tadrequire':'true',
        'max_behot_time':0,
        'max_behot_time_tmp':0,
        'tadrequire':'true',
        'as':'A1B58C382847BC6',
        'cp':'5C88F74B0C867E1',
        '_signature':'u3OQDQAA6Am53ofLhwcPMrtzkB'
    }

baseurl = 'https://www.toutiao.com/api/pc/feed/?'
sp = newsSpider(baseurl,headers,params,5)
#sp.startSpider('sportnews')