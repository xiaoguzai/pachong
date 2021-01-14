#UA:User-Agent{请求载体的身份标识}
#UA伪装：门户网站的服务器会检测对应请求的载体身份标识
#如果检测到请求的载体身份标识为某一款浏览器，说明该请求是一个正常的请求
#但是如果检测到请求的检测身份标识不是基于某一款浏览器的，则认为是不正常的
#请求(爬虫),则服务器端就很有可能拒绝该次请求

#UA伪装：让爬虫对应的请求载体身份标识伪装成某一款浏览器
import  requests
#第一步：设定url
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'
}
url = 'https://www.sogou.com/web'
#处理url携带的参数：封装到字典中,web后面的？号是否保留都可以
kw = input('enter a word:')
param = {
    'query':kw
}
#只有一组参数的时候作为字典的键值，如果我们有多组
#参数的时候，多组参数都可以作为相应字典的键值
#第二步：发起请求
#对指定的url发起的请求对应的url是携带参数的，
#并且请求过程中处理了参数
response = requests.get(url=url,params=param,headers=headers)
#get(url,params,kwargs)
#在域名后面放入了params，相当于动态拼接出了参数
page_text = response.text
fileName = kw+'.html'
with  open(fileName,'w',encoding='utf-8') as fp:
    fp.write(page_text)
print(fileName,'保存成功!!!')
