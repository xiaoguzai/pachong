import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功,',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
#该函数如果被调用之后，函数内部的语句不会马上被执行
c = request('www.baidu.com')

#future的使用
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
print(task)
#task与future的区别，task基于循环进行回调
#而future并不是基于循环的内容进行回调的
loop.run_until_complete(task)
print(task)
