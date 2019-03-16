from newSpider import sportSpyider

headers = {
            'Host':'edu.163.com',
            'Referer':'http://edu.163.com',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
            'Cookie':'Province=020; City=020; _ntes_nnid=9f2643ca4517413e4754ddebd1eeef32,1552183080987; _ntes_nuid=9f2643ca4517413e4754ddebd1eeef32; vjuids=-70e96c699.169655d779d.0.4789bbb00aa01; vjlast=1552183818.1552183818.30; NNSSPID=0f1c5c30d06b4e19bf90c2d9ef2fb07b; UM_distinctid=16966515001848-0a221e659982d-162a1c0b-1fa400-16966515002a28; __gads=ID=c679bee356214114:T=1552228140:S=ALNI_MZbWpITzIUYjQM5OT5PjSwH78DJOA; __utma=187553192.1619819907.1552230049.1552230049.1552230049.1; __utmc=187553192; __utmz=187553192.1552230049.1.1.utmcsr=travel.163.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _antanalysis_s_id=1552230049050; starttime=; nts_mail_user=15018279123@163.com:-1:1; df=mail163_letter; mail_psc_fingerprint=9d6867310e629e2b1764ff0b02eca1e9; mp_MA-9A80-4CC39D40B43D_hubble=%7B%22deviceUdid%22%3A%20%227df1a587-82cf-49b8-8423-1729a4340302%22%2C%22updatedTime%22%3A%201552307215409%2C%22sessionStartTime%22%3A%201552307215399%2C%22sessionReferrer%22%3A%20%22http%3A%2F%2Fjiankang.163.com%2Fspecial%2Fjbbk_h5%2F%22%2C%22sessionUuid%22%3A%20%22333f7afa-097b-4845-a259-e2f1d2c7f1c3%22%2C%22initial_referrer%22%3A%20%22http%3A%2F%2Fjiankang.163.com%2Fspecial%2Fjbbk%2F%22%2C%22initial_referring_domain%22%3A%20%22jiankang.163.com%22%2C%22persistedTime%22%3A%201552307215399%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22%E7%96%BE%E7%97%85%E7%99%BE%E7%A7%91-h5%22%2C%22time%22%3A%201552307215409%7D%7D; NTES_SESS=X3FOPFH7G051qJithBK4hakpdI8IqqIulsP6H2Yj9Tu5wsISwc4gjpjKIaCDYn6sAHWOEKCvh5Q9o0j8rpHsTFukvIhrkuNbuErUUoKYGEB_rdTo6xlN1Mq5KsP5oDBKcWzE5F0Uvo.Y7o1qHZru21cPMeVGxzPzBSRjxLCYLnvX1HDRXvPBhtU8UBPSAqSgaBq6PKuIY7i1_SAqO8q4nRS_3; S_INFO=1552316388|0|3&80##|m15018279123; P_INFO=m15018279123@163.com|1552316388|0|mail163|00&99|gud&1552290682&mail163#gud&440100#10#0#0|150123&1|mail163|15018279123@163.com; usertrack=CrHtflyGd+dmlcRyAwwKAg==; s_n_f_l_n3=eb08fdcfb764ec041552316776573; cm_newmsg=user%3Dm15018279123%40163.com%26new%3D537%26total%3D629; ne_analysis_trace_id=1552316935588; vinfo_n_f_l_n3=eb08fdcfb764ec04.1.10.1552183080180.1552310307133.1552316946512',
            'Connection':'keep-alive',
            'Accept-Encoding':'gzip, deflate',
            'Accept-Language':'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7',
            'Accept':'*/*',
            
}
edu = sportSpyider('http://edu.163.com/special/002987KB/newsdata_edu_hot{}.js?callback=data_callback',headers,7)
edu.startSpyider('edunews')
