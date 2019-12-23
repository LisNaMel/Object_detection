import os
import urllib.request as ulib
from bs4 import BeautifulSoup as Soup

import ast
from selenium import webdriver

driverPath = r"C:\Users\maket\chromedriver_win32\chromedriver.exe"

driver = webdriver.Chrome(driverPath)

# URL = 'https://www.google.com/search?q=goal+football&rlz=1C1SQJL_enTH879TH879&source=lnms&tbm=isch&sa=X&ved=2ahUKEwjE' \
#       '2Z-p6MPmAhX0IbcAHXvXAHQQ_AUoAXoECA4QAw&biw=958&bih=927'
# directory = 'SoccerNet'
# URL ='https://www.google.com/search?q=soccer&rlz=1C1SQJL_enTH879TH879&source=lnms&tbm=isch&sa=X&ved=2ahUKEwj6y5-83' \
#      '8rmAhUYdCsKHVdwBoMQ_AUoAXoECBIQAw&biw=1280&bih=578#imgrc=_'
# directory = 'Soccer'
URL = 'https://www.google.com/search?q=robotics+football+world+cup&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiZyK' \
      '-Y7srmAhWF6nMBHRCVDsEQ_AUoAXoECAsQAw&biw=1280&bih=578'
directory = 'Soccer_imgs'
def getURLs(URL):

    driver.get(URL)
    c = input()
    page = driver.page_source
    soup = Soup(page, 'lxml')
    desiredURLs = soup.findAll('div', {'class':'rg_meta notranslate'})
    ourURLs =[]

    for url in desiredURLs:
        txtURL = url.text
        txtURL = ast.literal_eval(txtURL)['ou']

        ourURLs.append(txtURL)
    return ourURLs


def save_images(URLs, directory):

    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, url in enumerate(URLs):
        savePath = os.path.join(directory, '{:05}.jpg'.format(i))

        try:
            ulib.urlretrieve(url, savePath)
        except:
            print('failed with', url)

URLs = getURLs(URL)
save_images(URLs,directory)

