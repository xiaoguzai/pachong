from selenium import webdriver
from time import sleep
r"""
如果定位的标签位于iframe标签中，则必须使用swith_to.frame(id)
动作链(拖动)：from  selenium.webdriver  import  ActionChains
    实例化一个动作链对象：action = ActionChains(bro)
    click_and_hold(div)：长按点击操作
    move_by_offset(x,y)：
    perform()：让动作链立即执行
    action.release()：释放动作链对象
"""


#导入动作链对应的类
from selenium.webdriver import ActionChains
bro = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver')

bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')

#如果定位的标签是存在于iframe标签之中的则必须通过如下操作在进行标签定位
bro.switch_to.frame('iframeResult')#切换浏览器标签定位的作用域
#下面想要定义的id = 'draggable'包含在一个iframe的标签当中
#iframe下面为定义的一个子页面

#如果定位的标签是存在于iframe标签之中的则必须通过如下操作再进行标签定位
div = bro.find_element_by_id('draggable')
#返回一个想要拖动的div

#动作链
action = ActionChains(bro)
#实例一个动作链参数，必须将浏览器作为参数
#点击长按指定的标签
action.click_and_hold(div)

for i in range(5):
    #perform()立即执行动作链操作
    #move_by_offset(x,y):x水平方向 y竖直方向
    action.move_by_offset(17,0).perform()
    #每次向右拖动了17个像素，perform代表立即执行
    sleep(0.5)

#释放动作链
action.release()

bro.quit()
