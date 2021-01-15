import asyncio

async def request(url):
    print('正在请求的url是',url)
    print('请求成功,',url)
    return url
#async修饰的函数，调用之后返回的一个协程对象
#该函数如果被调用之后，函数内部的语句不会马上被执行
c = request('www.baidu.com')

#future的使用
#loop = asyncio.get_event_loop()
#task = asyncio.ensure_future(c)
#print(task)
#loop.run_until_complete(task)
#print(task)

def  callback_func(task):
    #result返回的就是任务对象中封装的协程对象对应的函数返回值
    print(task.result())
#回调函数

#绑定回调
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(c)
#现在已经将协程对象注册到对应的任务之中
task.add_done_callback(callback_func)
loop.run_until_complete(task)
#这里的task会先执行async def request函数
#再执行相应的callback_func函数，而callback_func函数
#之中存放的是返回的url的内容，所以callback_func(task)
#中打印的task.result()对应的内容为返回的url的内容
