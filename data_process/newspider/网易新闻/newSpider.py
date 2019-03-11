import requests
import json

from pyquery import PyQuery as pq  
from urllib.parse import quote


class newSpider():
    
    def __init__(self):
        self.headers  = {
        
        }
        self.baseUrl=""

    def getPage(self):
        pass
    
    def parsePage(self,page):
        pass 

    def getDoc(self,docUrl):
       pass
    def writeItem(self,item):
        pass 

    def startSpyider(self):
        pass

class sportSpyider(newSpider):
    
    def __init__(self,baseUrl,headers,label):
        ''' self.headers = {
            'Host':'sports.163.com',
            'Referer':'http://sports.163.com/allsports/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie':'Province=020; City=020; _ntes_nnid=9f2643ca4517413e4754ddebd1eeef32,1552183080987; _ntes_nuid=9f2643ca4517413e4754ddebd1eeef32; vjuids=-70e96c699.169655d779d.0.4789bbb00aa01; vjlast=1552183818.1552183818.30; s_n_f_l_n3=eb08fdcfb764ec041552186695900; NNSSPID=0f1c5c30d06b4e19bf90c2d9ef2fb07b; ne_analysis_trace_id=1552186901179; vinfo_n_f_l_n3=eb08fdcfb764ec04.1.1.1552183080180.1552183870713.1552186952226',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept':'*/*',
            
        }'''
        self.headers = headers
        self.label = label
        '''self.proxies = {
            'http':'http://123.163.118.236:9999',
        }'''

        
        #self.baseUrl = 'http://sports.163.com/special/000587PQ/newsdata_allsports_index{}.js?callback=data_callback'
        self.baseUrl = baseUrl
        self.session = requests.Session()
    
    def getPage(self,pageNum):
        print('爬取第'+str(pageNum)+'页面')
        if pageNum == 1:
            baseUrl = self.baseUrl.format("")
        elif pageNum < 10:
            baseUrl = self.baseUrl.format('_0'+str(pageNum))
        else:
            baseUrl = self.baseUrl.format('_'+str(pageNum))

        try:
            response = self.session.get(url=baseUrl,headers=self.headers)
            if response.status_code == 200:
                print('get成功')
                #print(response.text)
                #print (len(response.text))
                text = response.text[14:-1]
                result = json.loads(text)
                return result
            else: 
                print('get 失败')
        except requests.ConnectionError as e:
            print('爬取失败')

    def parsePage(self,json):
        
        if json:
            print('解析页面')
            for item in json:
                docUrl = item.get('docurl')
                content = self.getDoc(docUrl)
                yield {
                    'content':content,
                    'lable': self.label,
                }
        else:
            print('未爬取到页面')
    def getDoc(self,docUrl):
        print('获取文章'+docUrl)
        try:
            response = requests.get(docUrl,headers=self.headers)
            if response.status_code == 200:
                doc = pq(response.text)
                doctext = ''
                dtitle = doc('.post_content_main h1').text()
                doctext = doctext+dtitle
                dcontents = doc('.post_text p').items()
                num = 0
                for dcontent in dcontents:
                    if num == 0:
                        num = 1
                        continue
                    else:
                        doctext = doctext + dcontent.text()
                return doctext 
        except requests.ConnectionError as e:
            print('获取新闻文章失败')

    def writeItem(self,item,name):
        with open ('datasource/{}.txt'.format(name),'a',encoding='utf-8') as f:
            f.write(json.dumps(item, ensure_ascii=False)+'\n')
    
    def startSpyider(self,name):
        for i in range(1,11):
            result = self.getPage(i)
            for item in self.parsePage(result):
                self.writeItem(item,name)
            



'''def test():
    print('开始测试')
    headers = {
        'Host':'sports.163.com',
            'Referer':'http://sports.163.com/allsports/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie':'s_n_f_l_n3=eb08fdcfb764ec041552183080184; Province=020; City=020; _ntes_nnid=9f2643ca4517413e4754ddebd1eeef32,1552183080987; ne_analysis_trace_id=1552183080992; _ntes_nuid=9f2643ca4517413e4754ddebd1eeef32; vinfo_n_f_l_n3=eb08fdcfb764ec04.1.0.1552183080180.0.1552183081714',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept':'*/*'
        }
            
    response = requests.get('http://temp.163.com/special/00804KVA/cm_guonei_02.js')
    if response.status_code == 200:
        print('chenggong')
        print(response.json())'''

