import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功,',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
#该函数如果被调用之后，函数内部的语句不会马上被执行
c = request('www.baidu.com')

#task的使用
loop = asyncio.get_event_loop()
#基于loop创建一个task对象
task = loop.create_task(c)
print(task)

loop.run_until_complete(task)
print(task)
