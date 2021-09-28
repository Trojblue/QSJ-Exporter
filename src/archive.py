# def refresh_cookie_qing(mail: str, password: str):
#     """selenium获取cookie
#     """
#     add_debug("刷新cookie")
#     driver = get_webdriver()
#     driver.get(login_url)
#
#     wait_msg = input("点掉用户协议后继续")
#
#     if mail and password: # 账户密码非空
#         driver.find_element_by_xpath("//*[@id='input-55']").send_keys(mail)
#         driver.find_element_by_xpath("//*[@id='input-59']").send_keys(password)
#         # driver.find_element_by_xpath("//*[@id='main']/div/div/form/div/div[3]/div/div[4]/button").click()
#
#     wait_msg = input("等待浏览器里填写验证并登录:")
#
#
#     new_cookie = driver.get_cookies()
#
#     local_token = driver.execute_script('return localStorage.getItem("token")')
#     print(local_token)
#
#     driver.close()
#
#     write_new_cookie(new_cookie, my_mail)
#     return new_cookie


# 需要针对修改
# driver.execute_script("document.getElementsByClassName('white--text v-sheet theme--light v-toolbar v-app-bar v-app-bar--clipped v-app-bar--fixed primary')[0].innerHTML = '';")

# driver.execute_script("""
# document.evaluate("//*[@id="app"]/div/div[1]/header",document.documentElement, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null);
# """)