from selenium import webdriver
from time import sleep
bro = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')
#加载驱动程序
bro.get('https://www.taobao.com/')

#标签定位到相应的输入框之中
search_input = bro.find_element_by_id('q')
#标签交互，向搜索框之中传递Iphone值
search_input.send_keys('Iphone')

#点击搜索按钮
btn = bro.find_element_by_css_selector('.btn-search')
btn.click()

sleep(5)
bro.quit()
