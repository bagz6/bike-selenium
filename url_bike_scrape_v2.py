from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd



# roadbikes = []
# trekkingbikes = []
# fitnessbikes = []
# crossbikes = []
# childrenbikes = []
# cyclocrossgravel = []
# bmxdirtbikes = []
# working url extractor
#        url = f'https://www.bike24.com/cycling/bikes/bmx-dirt-bikes?menu=1000,173,2159&page={x}'######change
#        url = f'https://www.bike24.com/road-bikes.html?menu=1000,173,157&page={x}'
rd_links_price = []

for x in range(1,5): #######remember to change the pagination
    roadbikes_url = []
    roadbikes_price = []
    url = f'https://www.bike24.com/road-bikes.html?menu=1000,173,157&page={x}'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(url)
    time.sleep(5)
    driver.find_element(by=By.XPATH, value='//*[@id="modal-root"]/div/div[2]/div[2]/div/div[1]/button[3]').click() #to click the agreement of using cookie    
    time.sleep(10)
    blinks = driver.find_elements(by=By.XPATH, value='.//div[@class="product-tile-list__column col-6 col-md-6 col-lg-4"]/div/a')
    prices = driver.find_elements(by=By.XPATH, value='.//div[@class="product-tile__price product-tile__price--has-delivery"]/div/div/p')

    for blink in blinks:
        href = blink.get_attribute('href')
        roadbikes_url.append(href)

    for price in prices:
        value = price.text
        roadbikes_price.append(value)

    for y in range (len(roadbikes_url)):
        ccat = {
            'url'   : roadbikes_url[y],
            'price' : roadbikes_price[y]
        }
        rd_links_price.append(ccat)

    driver.quit()
    print('the number of url is', len(roadbikes_url))######change
#     print('the number of url is', len(roadbikes))
#     print('the number of url is', len(trekkingbikes))
#     print('the number of url is', len(fitnessbikes))
#     print('the number of url is', len(childrenbikes))
#     print('the number of url is', len(cyclocrossgravel))
#     print('the number of url is', len(bmxdirtbikes))

    df = pd.DataFrame(data = rd_links_price)######change
    print(df)

# df.to_csv(r'D:\revou\mountain_bikes_url.csv', index=False)######change
df.to_csv(r'D:\revou\road_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\trekking_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\fitness_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\cross_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\children_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\cyclocrossgravel_bikes_url.csv', index=False)
# df.to_csv(r'D:\revou\bmxdirt_bikes_url.csv', index=False)

