import requests
from lxml import etree
import os
import re
from tqdm import tqdm
if __name__ == "__main__":
    photo_index = 1
    for index in tqdm(range(1,2601)):
        try:
            url = 'https://desk.3gbizhi.com/deskMV/'+str(index)+'.html'
            headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
            }
            response = requests.get(url=url,headers=headers)
            #手动设定响应数据的编码格式
            # response.encoding = 'utf-8'
            #给响应数据设置'utf-8'乱码现象仍然存在
            page_text = response.text
            results = '<div id="showimg">.*?<a href="https://pic.(.*?)".*?</div>'
            img_src_list = re.findall(results,page_text,re.S)
            result = "https://pic."+img_src_list[0]
            img_data = requests.get(url=result,headers=headers).content
            with open('/home/xiaoguzai/图片/学习资料/学习资料1/照片'+str(photo_index)+'.jpg','wb') as fp:
            #wb表示以二进制写方式打开，只能写文件
                fp.write(img_data)
            photo_index = photo_index+1
        except:
            continue
