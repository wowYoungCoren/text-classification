from newSpider import sportSpyider

headers_travel = {
            'Host':'travel.163.com',
            'Referer':'http://travel.163.com/',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie':'WM_NI=BAxJGBQiuOmaCCFCEhp8TIJn5mf%2FpJ3JFyaSUVPkne%2BB4Jt%2BU6WNX%2Fx02BBmnzKcXrAwVKW6Hdy8ibW%2BCO3YXM0fVsF6cwWk99jyLZx3ZR4tG6MRwrOVbebjKM9QHHS3TGQ%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb4cf4094f1bbabc46e969e8eb3c44a879a8e85f774baefaeb3ca7c95eca4b7e22af0fea7c3b92a829fb8abc64a93b7bbb0f06b819d8aa4c864b4e89caac966f7b3aad0f342f1968a9ae459978aa08ced6fe99efcabf72197ea99afdb25bcf0fea3c167aea68584db7a83a99aacd63e8cbcb7d9ec6a95f58db0b2539c930087d57986eaad98d661fbe7a69acf52bced96b3b78085ea83b3f67a8d8aae86e1628993f7b2cb4491ed9ca8d437e2a3; WM_TID=gYtvnSiyH9dEAVFARRZ9hn0bUP5T4kQd; CNZZDATA1271027176=101018060-1552140219-%7C1552140219; CNZZDATA1256734798=463025644-1552140054-%7C1552140054; CNZZDATA1257114097=1371976556-1552141202-%7C1552141202; CNZZDATA1256336326=1388061652-1552144985-%7C1552144985; CNZZDATA5954595=cnzz_eid%3D1433925446-1552142290-null%26ntime%3D1552142290; CNZZDATA5955239=cnzz_eid%3D926408979-1552143439-null%26ntime%3D1552143439; Province=020; City=020; _ntes_nnid=9f2643ca4517413e4754ddebd1eeef32,1552183080987; _ntes_nuid=9f2643ca4517413e4754ddebd1eeef32; vjuids=-70e96c699.169655d779d.0.4789bbb00aa01; vjlast=1552183818.1552183818.30; NNSSPID=0f1c5c30d06b4e19bf90c2d9ef2fb07b; UM_distinctid=16966515001848-0a221e659982d-162a1c0b-1fa400-16966515002a28; __gads=ID=c679bee356214114:T=1552228140:S=ALNI_MZbWpITzIUYjQM5OT5PjSwH78DJOA; __utma=187553192.1619819907.1552230049.1552230049.1552230049.1; __utmc=187553192; __utmz=187553192.1552230049.1.1.utmcsr=travel.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _antanalysis_s_id=1552230049050; s_n_f_l_n3=eb08fdcfb764ec041552233221942; ne_analysis_trace_id=1552275340813; vinfo_n_f_l_n3=eb08fdcfb764ec04.1.7.1552183080180.1552230255571.1552275380700',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept':'*/*',
            
}
baseUrl = 'http://travel.163.com/special/00067VEJ/newsdatas_travel{}.js?callback=data_callback'

travelSpider = sportSpyider(baseUrl,headers_travel,6)
travelSpider.startSpyider('travlenews')