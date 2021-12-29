import time, re
from datetime import datetime
from selenium import webdriver
from urllib.request import urlopen
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
import credentials
import pandas as pd
import json, urllib.request


def driver_initialization():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(credentials.url)
    return driver


driver = driver_initialization()
cookie_button = WebDriverWait(driver, 10).until(lambda d: d.find_element_by_css_selector('.aOOlW.bIiDR'))
cookie_button.click()

time.sleep(1)

user = driver.find_element_by_css_selector('._2hvTZ.pexuQ.zyHYP').send_keys(credentials.username)  # username

password = driver.find_element_by_name('password').send_keys(credentials.password)  # password

button_login = driver.find_element_by_css_selector('.sqdOP.L3NKy.y3zKF')
button_login.click()

not_now = WebDriverWait(driver, 10).until(
    lambda d: d.find_element_by_xpath("//*[@id=\"react-root\"]/section/main/div/div"
                                      "/div/div/button"))
not_now.click()

date = datetime.today()
print(date)
posts = driver.find_elements_by_css_selector('.g47SY')[0].text
print(posts)
follower = driver.find_elements_by_css_selector('.g47SY')[1].text
print(follower)
following = driver.find_elements_by_css_selector('.g47SY')[2].text
print(following)

for i in range(int(posts)):
    post = driver.find_elements_by_css_selector('.v1Nh3.kIKUG._bz0w')[i]  # i
    link = post.find_element_by_tag_name('a')
    link.click()
    amount_likes = WebDriverWait(driver, 5).until(lambda d: d.find_element_by_xpath(
        "/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[2]/section[2]/div/div").text)
    print(re.sub('\D', '', amount_likes))
    close_button = driver.find_element_by_xpath("/html/body/div[6]/div[3]/button")
    close_button.click()

driver.close()

# data = open('data.txt', 'a')
#
# # data.write(Datum)
# #data.write("Mainka am " + Datum + "\n")
# data.write('Beiträge: ' + Beitraege + "\n")
# data.write('Follower: ' + Follower + "\n")
# data.write('abonniert: ' + abonniert + "\n")
#
# # for i in range(int(Beitraege)):
# Post = driver.find_elements_by_css_selector('.v1Nh3.kIKUG._bz0w')[0]  # i
# Link = Post.find_element_by_tag_name('a')
# Link.click()
# print("gut")
# time.sleep(1)
#
# current = driver.current_url
# driver.get("view-source:" + current)
# new_current = driver.current_url
# print(new_current)


# response = urlopen(current)
# data_json = json.loads(response.read())
# print(data_json)


#
# post_url = requests.get(current)
# data_url = post_url.text

# new_data = json.loads(text)


# Schliessen = driver.find_element_by_xpath('/html/body/div[6]/div[3]/button') #3. Button weiter 10. Button schleißen
# Schliessen.click()
# time.sleep(1)
# data.write('Likes: ' "fehlt noch" "\n")
