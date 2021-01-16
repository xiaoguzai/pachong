from selenium import webdriver
from time import sleep
#先在淘宝的搜索框输入Iphone，然后向下滚动一屏的距离，之后再点击搜索按钮
#然后进入www.baidu.com的界面，最后再返回到淘宝对应的界面，再前进到百度对应的界面，最后退出所有的界面
bro = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#加载驱动程序
bro.get('https://www.taobao.com/')

#标签定位到相应的输入框之中
search_input = bro.find_element_by_id('q')
#标签交互，向搜索框之中传递Iphone值
search_input.send_keys('Iphone')


#执行一组js程序
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#让滚轮实现向下滚动一屏的高度
sleep(2)

#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
#class="btn-search"，这里根据class的属性值进行相应的选择
btn.click()

bro.get('https://www.baidu.com')
sleep(2)
#回退
bro.back()
sleep(2)
#前进
bro.forward()

sleep(5)

bro.quit()
