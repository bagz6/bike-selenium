from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import pandas as pd
import csv

data  = pd.read_csv('d:/revou/road_bikes_url.csv')
rd_catalog   = {}

for i in range(0, len(data)):
    roadbikes = []
    rb_column     = []
    rb_value      = []
    rb_price      = []
    driver = webdriver.Chrome(ChromeDriverManager().install())
    datas  = data['url'][i]
    
    print('Data Scraper Progress :' , i+1, 'of', len(data))
    print('Ongoing Scraping on URL :' , datas)
    driver.get(datas)
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='.//*[@id="modal-root"]/div/div[2]/div[2]/div/div[1]/button[3]').click()
    time.sleep(5)
    driver.execute_script("window.scrollTo(0,900)")
    time.sleep(6)
    driver.find_element(by=By.XPATH, value='.//*[@id="productDetail"]/div[2]/div[1]/div[1]/ul/li[2]/label').click()
    
    titles = driver.find_elements(by=By.XPATH, value='.//table[@class="product-detail-data-sheet__table"]/tbody/tr/td[1]')
    descs  = driver.find_elements(by=By.XPATH, value='.//table[@class="product-detail-data-sheet__table"]/tbody/tr/td[2]')
    
    for title in titles:
        title = title.text.split(':')[0]
        rb_column.append(title)
    for desc in descs:
        desc = desc.text
        rb_value.append(desc)
        
    for x in range(len(rb_column)):
        specs = {
            'key' : rb_column[x],
            'vals': rb_value[x],
        }
        roadbikes.append(specs)
        
    for bike in roadbikes:
        if bike['key'] in rd_catalog:
            rd_catalog[bike['key']].append(bike['vals'])
        else:
            rd_catalog[bike['key']] = [] ##buatkan suatu key-value pair yg kosong
            for j in range(0,i):
                rd_catalog[bike['key']].append(' ') ##tambahkan nilai kosong sebanyak i-1 krn bsa saja d i ke n dia baru muncul
            rd_catalog[bike['key']].append(bike['vals']) ## kemudian tambahkan value tersebut
    
    print(rd_catalog)
    driver.quit()
    
    for catalog_key, catalog_list in rd_catalog.items():
        if len(catalog_list) <= i: ##jika panjang catalog kurang dari sama dengan i, maka isikan value yg kosong agar sama panjangnya
            rd_catalog[catalog_key].append(' ')
               
    pd.set_option('display.max_rows', None)

    df = pd.DataFrame(rd_catalog)
    # df = pd.DataFrame(mtb_catalog)
    print(df)

df.to_csv(r'D:\revou\road_bikes_data.csv')


