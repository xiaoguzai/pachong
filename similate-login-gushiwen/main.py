import  requests
from  chaojiying  import  Chaojiying_Client
from  lxml  import  etree
url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'
headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text
tree = etree.HTML(page_text)
data = tree.xpath('//*[@id="imgCode"]/@src')[0]
html_data = 'https://so.gushiwen.cn'+data
img_data = requests.get(url=html_data,headers=headers).content
with  open('./code.jpg','wb')  as  fp:
    fp.write(img_data)
#存储相应的code.jpg图片
chaojiying = Chaojiying_Client('', '', '')	#用户中心>>软件ID 生成一个替换 96001
#这里分别输入用户名，密码，以及从超级鹰当中得到的软件的id
im = open('code.jpg', 'rb').read()
print(chaojiying.PostPic(im, 1902))
