import json
import logging
import time

from typing import List, Dict
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from selenium.common.exceptions import NoSuchElementException
from test import *
from logger import *


login_url = "https://www.acgdmzy.com/login"

# ========= CREDENTIAL =======
my_proxy = "localhost:20901"
my_token = ''       # 
# my_token = ''     # 

def get_webdriver():
    """返回设置好参数的webdriver
    """
    options = webdriver.ChromeOptions()
    options.add_argument("disable-software-rasterizer")
    options.add_argument("log-level=3")

    PROXY = my_proxy
    options.add_argument('--proxy-server=%s' % PROXY)

    driver = webdriver.Chrome(chrome_options=options)
    return driver

def do_login(driver, token):
    """
    https://blog.csdn.net/qq_42183962/article/details/118144725
    token: 轻书架登录token
    """
    driver.get(login_url)
    driver.execute_script('localStorage.setItem("token", "%s")'% token)
    driver.refresh()

def do_preprocess(driver):
    """截图前的处理, 具体见注释
    """

    # remove sticky header
    driver.execute_script(
        "return document.getElementsByClassName('white--text v-sheet "
        "theme--light v-toolbar v-app-bar v-app-bar--clipped v-app-bar--fixed primary')[0].remove();")

    # remove top padding
    driver.execute_script("document.getElementById('main').style.padding = '0px 0px 0px';")

    # remove fab
    driver.execute_script(
        "return document.getElementsByClassName('v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--default primary')[0].remove();")

    # remove card
    try:
        driver.find_element_by_xpath("/html/body/cloudflare-app/flashcard-header/flashcard-close").click()
    except NoSuchElementException:
        print("preprocess: 未找到提示卡")

    # switch to iframe
    iframe = driver.find_element_by_id("chapterFrame")
    iframe.click()
    driver.execute_script("arguments[0].focus();", iframe)
    driver.switch_to.frame(iframe)

    # try remove padding
    # driver.execute_script("document.getElementsByClassName('fr-view')[0].style.padding = '0px 12px 0px';")
    return





def write_error(prefix:str, content:str):
    """保存错误日志
    prefix: 文件名前缀
    content: 错误日志内容
    """
    my_date = prefix + datetime.today().strftime(' %Y-%m-%d %H%M %S.%f.log')
    with open(my_date, "w") as f:
        f.write(content)
    return