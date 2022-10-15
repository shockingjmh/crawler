from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/shockingjmh/opt/anaconda3/envs/py10/bin/chromedriver") # 다운받은 크롬드라이버 위치
driver.get("https://www.wadiz.kr/web/wreward/main?keyword=&endYn=ALL&order=recommend") #크롤링 대상 페이지
driver.maximize_window()
import time

from datetime import datetime

start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
num = [1,2,3,4,5]

import random

try:
    print("for start")
    for i in range(2500):
        print(str(i+1) + " process")
        button = driver.find_element_by_xpath(f'//*[@id="main-app"]/div[2]/div/div[3]/div[2]/div[2]/div/button') #더보기버튼 xpath
        
        time.sleep(random.randint(1, 5) * 0.01)
        driver.execute_script("arguments[0].click();", button) #click()으로 에러가나서 써줌
        
except Exception as e:
    print("except : " + str(e))
    button = driver.find_element_by_class_name #더보기버튼    

wadiz_title=[]
wadiz_url=[]

table = driver.find_element_by_class_name('ProjectCardList_container__3Y14k')
rows = table.find_elements_by_class_name('ProjectCardList_item__1owJa')

for index, value in enumerate(rows):
    title = value.find_element_by_class_name('CommonCard_title__1oKJY')
    wadiz_title.append(title.text)

    url_class = value.find_element_by_class_name('CommonCard_container__e_ebQ')
    url = url_class.get_attribute('href')
    
    wadiz_url.append(url)


import pandas as pd
import numpy as np
from datetime import datetime

df1 = pd.DataFrame({'title' : wadiz_title, 'url' : wadiz_url})
df1.to_csv("wadiz_title_url_"+ str(datetime.now().strftime('%Y%m%d%H%M%S')) +".csv",mode='w',encoding='utf-8-sig')

end_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

print("start time : " + str(start_time))
print("end time : " + str(end_time))

