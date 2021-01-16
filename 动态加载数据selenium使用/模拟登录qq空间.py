from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(executable_path=r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver')

driver.get('https://qzone.qq.com/')
driver.switch_to.frame('login_frame')
#!!!特别注意这里有个iframe属性，需要先切换到iframe之中进行操作!!!
a = driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
#.click()
print('a = ')
print(a)
sleep(2)
#点击下方的账号密码输入按钮

driver.find_elements_by_xpath('//*[@id="u"]')[0].send_keys('')#在send_keys之中输入用户名
a1 = driver.find_element_by_xpath('//*[@id="u"]')
sleep(2)

driver.find_element_by_xpath('//*[@id="p"]').send_keys('')#在send_keys之中输入密码
a2 = driver.find_element_by_xpath('//*[@id="p"]')
sleep(2)

driver.find_element_by_xpath('//*[@id="login_button"]').click()
sleep(2)
#输入用户名，密码之后点击登录按钮进行登录

page_text = driver.page_source
#获取浏览器当前页面的数据
with  open('page_text.html','w',encoding='utf-8')  as  file_obj:
    file_obj.write(page_text)

driver.quit()
