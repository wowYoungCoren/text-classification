from jinRi import newsSpider

headers ={
        'Host':'www.toutiao.com',
        'Referer':'https://www.toutiao.com/ch/news_fashion/',
        'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
        'Cookie':'tt_webid=6663323848248755725; WEATHER_CITY=%E5%8C%97%E4%BA%AC; UM_distinctid=1693831df34472-0f937e1740d2eb-162a1c0b-1fa400-1693831df35fe9; CNZZDATA1259612802=630908265-1551425067-https%253A%252F%252Fwww.google.com.hk%252F%7C1551425067; __tasessionId=5vwu7psj91551425986390; tt_webid=6663323848248755725; csrftoken=8e3462b8d4014dd38ca1b00b3c81c3da'
    }
params = {
        'category':'news_fashion',
        'utm_source':'toutiao',
        'widen':1,
        'tadrequire':'true',
        'max_behot_time':0,
        'max_behot_time_tmp':0,
        'tadrequire':'true',
        'as':'A115DCC9D321404',
        'cp':'5C938144A0849E1',
        '_signature':'3HYZAAAAgOze2w7GlyMJ3tx2GR'
    }

baseurl = 'https://www.toutiao.com/api/pc/feed/?'

fashionSpider = newsSpider(baseurl,headers,params,11)
fashionSpider.startSpider('fashionnews')