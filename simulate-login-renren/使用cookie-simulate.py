import  requests
from  chaojiying  import  Chaojiying_Client
from  lxml  import  etree
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'http://www.renren.com/SysHome.do'
#人人网对应的登录页面的url
session = requests.Session()
page_text = requests.get(url=url,headers=headers).text
with  open('page_text.html','w',encoding='utf-8')  as  file_obj:
    file_obj.write(page_text)
tree = etree.HTML(page_text)
code_img_src = tree.xpath('//*[@id="verifyPic_login"]/@src')[0]
#获取验证码的url
code_img_data = requests.get(url=code_img_src,headers=headers).content
#获取验证码的图片
with  open('./code.jpg','wb')  as  fp:
    fp.write(code_img_data)
#写入相应的文件
#存储相应的code.jpg图片
chaojiying = Chaojiying_Client('xiaoguzai', 'z123456***', '911712')	#用户中心>>软件ID 生成一个替换 96001
im = open('code.jpg', 'rb').read()
code_str = chaojiying.PostPic(im, 1005)
print('code_str = ')
print(code_str)
#想白嫖的可以自己手动输入验证码，设置一个输入框
login_url = 'http://www.renren.com/ajaxLogin/login'
param = {
    '1':'1',
    'uniqueTimestamp':'2021051122961'
}
data = {
    'email': '18833273156',
    'icode': code_str,
    'origURL': 'http://www.renren.com/home',
    'domain': 'renren.com',
    'key_id': '1',
    'captcha_type': 'web_login',
    'password': '454b8682d3b24affd4025fdfbee30269bcd639035c4eee7f7d4a7d940511a3bf',
    'rkey': 'fe41ddb7ec32db83d8bdbcc6945e267a',
    'f': 'http%3A%2F%2Fwww.renren.com%2F975736813'
}
#使用session进行post请求的发送
result_page = session.post(url=login_url,params=param,data=data,headers=headers)
print(result_page.status_code)
result_page = result_page.text
#with  open('result_page.html','w',encoding='utf-8')  as  file_obj:
#    file_obj.write(result_page)
#直接对人人网的相应网页发送请求

#方法1：手动cookie处理，将cookie封装到headers当中，可以成功，但是不建议使用
#主要有的网站的cookie值有动态时长，或者有的网站的cookie值是动态变化的
#headers = {
#    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
#    'Cookie': 'anonymid=kjv16cfs-6kvvnb; depovince=JS; _r01_=1; taihe_bi_sdk_uid=d86c544a8b146827ef9c84244aa24ef4; __utma=151146938.1641095260.1610536758.1610536758.1610536758.1; __utmz=151146938.1610536758.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/; JSESSIONID=abczdp6nq8uk1_N9nTdCx; ick_login=2e7c0ef5-22f2-4b7d-b582-673777dcf0da; taihe_bi_sdk_session=e56eeffa8891688b99aee53fc4c97f8b; first_login_flag=1; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebecookies=76abaa31-97a2-406e-8f9a-acf6e461f3f6|||||; _de=4782F1ECE4130D0502F938525B232DC6; p=fa1224a1afba100c1143f0080a30d6e73; societyguester=14c337019ed8630fb80612d2ec1a89693; id=975736813; ver=7.0; wp_fold=0; t=14c337019ed8630fb80612d2ec1a89693; loginfrom=syshome; ln_uact=user18833273156; xnsid=fb451bfe'
#}
#方法2：自动cookie处理
#cookie值的来源是哪里？模拟登陆post请求后，由服务器端创建
#session会话对象：作用：1.可以进行请求的发送
#2.如果请求过程中产生了cookie，则该cookie会被自动存储/携带在该session对象中

#创建一个session对象：session = requests.Session()
#1.使用session对象进行模拟登陆post请求的发送（cookie就会被存储在session中）
#2.session对象对个人主页对应的get请求进行发送（携带了cookie）

#使用携带cookie的session进行get请求的发送
detail_url = 'http://www.renren.com/975736813/profile'
detail_page_text = session.get(url=detail_url,headers=headers).text
with  open('bobo.html','w',encoding='utf-8')  as  fp:
    fp.write(detail_page_text)

