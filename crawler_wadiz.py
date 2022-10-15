import multiprocessing
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from datetime import datetime


start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

data = pd.read_csv("/Users/shockingjmh/Dev/git/crawler/wadiz_title_url_1.csv")
data2 = data['url']
one = data2.values.tolist()

from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

for i in range(1) :    
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(executable_path="/Users/shockingjmh/opt/anaconda3/envs/py10/bin/chromedriver") # 다운받은 크롬드라이버 위치
    #driver.get("https://www.wadiz.kr/web/wreward/main?keyword=&endYn=ALL&order=recommend") #크롤링 대상 페이지
    #driver.maximize_window()
    
import requests
import time
from multiprocessing import Pool, pool

#wadiz_body=[]
#wadiz_title=[]
#wadiz_category=[]
#wadiz_url=[]

def mul(url) : 
    #for url in urls :
    driver.get(url)
    time.sleep(0.4)
    wadiz_body=""
    wadiz_title=""
    wadiz_category=""
    wadiz_url=""

    #본문내용
    body = driver.find_elements_by_xpath(f'//*[@id="introdetails"]/div')
    for value in body:
        wadiz_body += value.text
    
    
    #제목
    title = driver.find_element_by_xpath(f'//*[@id="container"]/div[3]/h2/a')
    wadiz_title = title.text
    
    #카테고리
    category = driver.find_element_by_xpath(f'//*[@id="container"]/div[3]/p')
    wadiz_category = category.text
    
    wadiz_url = driver.current_url
    
    return [str(wadiz_title), str(wadiz_category), str(wadiz_url), str(wadiz_body)]

wadiz_list = []

import os

if __name__ == '__main__':
    cpu_core = os.cpu_count()
    print("cpu core : " + str(cpu_core))
    
    pool = Pool(processes=cpu_core) #32 process use
    wadiz_list.append(pool.map(mul, one))
    pool.close()
    pool.join()
    driver.close()

import pandas as pd
import numpy as np

df1 = pd.DataFrame(data=sum(wadiz_list,[]), columns=['title', 'category', 'url', 'body'])
df1.to_csv("wadiz_"+str(datetime.now().strftime('%Y%m%d%H%M%S'))+".csv",mode='w',encoding='utf-8-sig')

end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print("start time : " + str(start_time))
print("end time : " + str(end_time))

