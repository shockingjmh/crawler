import pandas as pd
from pandas import Series,DataFrame
import numpy as np
from datetime import datetime

start_stage = 8000
end_stage = 9000

#wadiz_title_url.csv   total
# 1001
data = pd.read_csv("/Users/shockingjmh/Dev/git/crawler/wadiz_title_url.csv")
data2 = data.iloc[start_stage:end_stage]['url']
#data2 = data['url']
one = data2.values.tolist()

from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

for i in range(1) :    
    chrome_options = Options()
    chrome_options.add_argument('--proxy-server=socks5://127.0.0.1:9150')
    prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
    chrome_options.add_experimental_option('prefs', prefs)

    driver = webdriver.Chrome(executable_path="/Users/shockingjmh/opt/anaconda3/envs/py8/bin/chromedriver") # 다운받은 크롬드라이버 위치
    
import time
import random
from multiprocessing import Pool, pool

def mul(url) : 
    driver.get(url)
    
    wadiz_body=""
    wadiz_title=""
    wadiz_category=""
    wadiz_achievement_rate=""
    wadiz_total_amount=""
    wadiz_total_supporter=""
    wadiz_url=""

    try:
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
        
    #    achievement_rate = driver.find_element_by_xpath(f'//*[@id="container"]/div[6]/div/div[1]/div[1]/div[1]/div[1]/p[3]')
    #    wadiz_achievement_rate = achievement_rate.text
        
    #    total_amount = driver.find_element_by_xpath(f'//*[@id="container"]/div[6]/div/div[1]/div[1]/div[1]/div[1]/p[4]')
    #    wadiz_total_amount = total_amount.text
        
    #    total_supporter = driver.find_element_by_xpath(f'//*[@id="container"]/div[6]/div/div[1]/div[1]/div[1]/div[1]/p[5]')
    #    wadiz_total_supporter = total_supporter.text

        achievement_rate = driver.find_element_by_class_name("achievement-rate")
        wadiz_achievement_rate = achievement_rate.text
        
        total_amount = driver.find_element_by_class_name("total-amount")
        wadiz_total_amount = total_amount.text
        
        total_supporter = driver.find_element_by_class_name("total-supporter")
        wadiz_total_supporter = total_supporter.text
        
        wadiz_url = url
        
        step = int(url[url.rindex('_')+1:])
        
        if (step % 100) == 0 : 
            time.sleep(600)
        elif (step % 50) == 0 : 
            time.sleep(300)
        elif (step % 10) == 0 : 
            time.sleep(60)
        elif (step % 5) == 0 : 
            time.sleep(30)            
        else :
            time.sleep(random.randint(1, 5) * 2)
        
    except:
        print("exception! : " + wadiz_url)
    
    return [str(wadiz_title), str(wadiz_category), str(wadiz_url), str(wadiz_achievement_rate), str(wadiz_total_amount), str(wadiz_total_supporter), str(wadiz_body)]

wadiz_list = []

import os
import pandas as pd
import numpy as np

if __name__ == '__main__':
    cpu_core = os.cpu_count()
    print("cpu core : " + str(cpu_core))
    
    pool = Pool(processes=cpu_core) #32 process use
    wadiz_list.append(pool.map(mul, one))
    pool.close()
    pool.join()
    driver.quit()
    
    df1 = pd.DataFrame(data=sum(wadiz_list,[]), columns=['title', 'category', 'url', 'achievement_rate', 'total_amount', 'total_supporter', 'body'])
    #df1.to_csv("wadiz_result_final"+str(datetime.now().strftime('%Y%m%d%H%M%S'))+".csv",mode='w',encoding='utf-8-sig')
    df1.to_csv("wadiz_result_final_"+str(start_stage)+"_"+str(end_stage)+"_"+str(datetime.now().strftime('%Y%m%d%H%M%S'))+".csv",mode='w',encoding='utf-8-sig')
    #df1.to_csv("wadiz_result_final_"+str(end_stage)+"_"+str(datetime.now().strftime('%Y%m%d%H%M%S'))+".csv",mode='w',encoding='utf-8-sig')


