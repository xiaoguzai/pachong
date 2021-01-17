#12306具体查看了相应网页的内容，发现使用post无法直接得到对应的数据包
#同时登录页面的时候有一个向右滑动的操作，综上所述决定使用selenium对
#12306进行模拟登录

#使用selenium打开登录页面
#对当前selenium打开的这张页面进行截图
#对当前图片局部区域(验证码图片)进行裁剪
    #好处：将验证码和模拟图片进行一一对应
#使用超级鹰识别验证码图片(坐标)
from  selenium  import  webdriver
import  time
from  PIL  import  Image
from  chaojiying  import  Chaojiying_Client
from  selenium.webdriver  import  ActionChains
from  selenium.webdriver.common.keys  import  Keys
option = webdriver.ChromeOptions()
option.add_argument('disable-infobars')
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver',chrome_options=option)
#使用上面三行调用的方法的时候，浏览器不会弹出'Chrome正在受到自动软件的控制'

driver.get('https://kyfw.12306.cn/otn/resources/login.html')
#driver.maximize_window()
time.sleep(1)
script = 'Object.defineProperty(navigator,"webdriver",{get:()=>undefined,});'
driver.execute_script(script)
#!!!!!!必须加上这一部分的内容，不然登录成功之后浏览器会识别出滑块是selenium操作的


driver.find_element_by_xpath('/html/body/div[2]/div[2]/ul/li[2]/a').click()
time.sleep(1)
#注意这里一定要先转到对应的账号密码登录的界面，再去截图，否则找不到对应的xpath
#的相应的内容
#driver.maximize_window()

#driver.save_screenshot('12306.png')
#screentshot将整个界面完全地截图下来

code_img_element = driver.find_element_by_xpath('//*[@id="J-loginImg"]')
print('code_img_element = ')
print(code_img_element)
location = code_img_element.location   #验证码图片左上角的坐标x，y
print('location = ')
print(location)
size = code_img_element.size    #验证码标签对应的长和宽
#rangle对应左上角和右下角的坐标
print('size = ')
print(size)
rangle = (
    int(location['x']),int(location['y']),int(location['x']+size['width']),int(location['y']+size['height'])
)
#想要截取局部的内容需要获得局部的坐标
#确定验证码图片对应的左上角和右下角的坐标
#range之中的location['x'],location['y']为左上角的坐标
#location['x']+size['width'],location['y']+size['height']拿到的是右下角的坐标
#至此验证码图片就确定下来了
print('rangle = ')
print(rangle)

#出现tile cannot extend outside image的时候，需要注意这里是图像裁剪的时候发生了
#越界的情况
driver.save_screenshot('12306.png')
i = Image.open('./12306.png')
code_img_name = 'code.png'
#crop根据指定区域进行图片裁剪
frame = i.crop(rangle)
#对验证码图片进行裁剪
frame.save(code_img_name)
#裁剪下来的验证码图片保存到本地
#!!!截图歪的原因是因为电脑比例被调整过，不是100%!!!

r"""#chaojiying = Chaojiying_Client('xiaoguzai','z123456***','911712')
#im = open('code.png','rb').read()
#result = chaojiying.PostPic(im,9104)
#print('result type = ')
#print(type(result))
#print('result = ')
#print(result)
#finalresult = result['pic_str']
#这里返回的53,156|247,73|39,150是在这个图片上对应的坐标的内容
#而不是在整个区域之中对应的图片内容

#print('finalresult = ')
#print(finalresult)
#finalresult = '59,86|56,143|261,72|268,137'
data = Image.open('./code.png')
print(data.size)
width = data.size[0]
height = data.size[1]
strlist = finalresult.split('|')
posdata = []
print('locationx = ')
print(location['x'])
print('locationy = ')
print(location['y'])
for  i  in  range(len(strlist)):
    currents = strlist[i].split(',')
    currents[0] = int(currents[0])
    currents[1] = int(currents[1])
    posdata.append(currents)
print('posdata = ')
print(posdata)
#从字符串中切分出来相应的坐标数值
#posdata = list(set(posdata))
"""
currentpath = driver.find_elements_by_xpath('//*[@id="nc_1__scale_text"]/span')
driver.find_element_by_xpath('//*[@id="J-userName"]').send_keys('##############################################################')#输入对应的用户名
driver.find_element_by_xpath('//*[@id="J-password"]').send_keys('##############################################################')#输入对应的密码
#先输入相应的用户名和密码，否则在循环之中不断地输入用户名和密码会出现迭加输入的现象
print('***1')
while  len(currentpath) == 0:
    print('***2')
    width = size['width']
    height = size['height']
    #currentpos = [[55,40],[55,120],[55,200],[55,280],[140,40],[140,120],[140,200],[140,280]]
    currentpos = [[40,55],[120,55],[200,55],[280,55],[40,140],[120,140],[200,140],[280,140]]
    inputs = input("请输入验证码图片")
    print('inputs = ')
    print(inputs)
    inputdata = inputs.split(' ')
    print('inputdata = ')
    print(inputdata)
    for  i  in  range(len(inputdata)):
        current = (int)(inputdata[i])-1
        ActionChains(driver).move_to_element_with_offset(code_img_element,currentpos[current][0],currentpos[current][1]).click().perform()
    #点击相应的图片的验证码位置
    driver.find_element_by_xpath('//*[@id="J-login"]').click()      
    time.sleep(3)
    #注意这边点击之后需要等待一个短暂的事件，然后才能读取相应的xpath路径
    #否则会出现页面没有响应过来找不到指定xpath路径内容的问题
    currentpath = driver.find_elements_by_xpath('//*[@id="nc_1__scale_text"]/span')
    print('currentpath = ')
    print(currentpath)

#for  i  in  range(len(posdata)):
#    ActionChains(driver).move_to_element_with_offset(code_img_element,posdata[i][0],posdata[i][1]).click().perform()
#从图片之中取出相应的验证码，并且点击验证码识别返回出来的相对偏移的坐标位置
#点击的时候报错，MoveTargetOutOfBoundsException，这里采用找到的code_img_element的相关属性值进行相对偏移
#输入用户名和密码，并登录

#接下来实现一个点击>>并向右拖动的过程

print('***3')
action = ActionChains(driver)
#实例化一个动作链的参数
currentpath = driver.find_element_by_xpath('//*[@id="nc_1__scale_text"]/span')
action.click_and_hold(currentpath).perform()
#鼠标的左键按下不放
#接下来就是通过for循环动滑块的位置，
#move_by_offset()方法:第一个参数是X轴，
#第二个参数是Y轴，单位为像素。因为是平行移动，
#所以Y设置为0，X每次移动两2个像素。
#time.sleep(3)
action.move_by_offset(500, 0).perform() #平行移动鼠标
time.sleep(0.1)
action.release()
time.sleep(1)
#按回车键
time.sleep(1)
#driver.switch_to_alert().accept()
driver.find_element_by_xpath('//*[@class="dzp-confirm"]/div[2]/div[3]/a').click()
#!!!点击对应的确定按钮


page_text = driver.page_source
#获取浏览器当前网页的数据
with  open('page_text.html','w',encoding='utf-8')  as  file_obj:
    file_obj.write(page_text)

driver.quit()
