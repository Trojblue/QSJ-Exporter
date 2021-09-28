import time

from actions import *
#!/usr/bin/python
from selenium import webdriver
from PIL import Image
from io import BytesIO
from pathlib import Path



def full_screenshot_with_scroll(driver:webdriver.Chrome, save_path:Path):
    """
    Ref --> https://stackoverflow.com/questions/17688595/finding-the-maximum-scroll-position-of-a-page
    remove -> https://stackoverflow.com/questions/53373625/remove-an-element-in-a-container-using-selenium
    main gist -> https://gist.github.com/fabtho/13e4a2e7cfbfde671b8fa81bbe9359fb
    """

    save_path = save_path.with_suffix(".png") if not save_path.match("*.png") else save_path
    img_li = []  # to store image fragment
    offset = 0  # where to start

    do_preprocess(driver)

    # get height
    max_iframe_height = driver.find_element_by_tag_name('html').rect['height']
    page_height = driver.execute_script("return Math.max(" "document.documentElement.clientHeight, window.innerHeight);")

    count = 0

    # looping from top to bottom, append to img list
    # todo: 长图接出来不是整的
    while offset < max_iframe_height:

        # Scroll to height
        driver.execute_script(f"window.scrollTo(0, {offset});")

        img = Image.open(BytesIO((driver.get_screenshot_as_png())))
        try:
            img.save(str(count) + ".png", "PNG")
        except Exception:
            print("")
        img_li.append(img)
        offset += page_height
        count += 1

    # In case it is not a perfect fit, the last image contains extra at the top.
    # Crop the screenshot at the top of last image.
    extra_height = offset - max_iframe_height
    if extra_height > 0 and len(img_li) > 1:
        pixel_ratio = driver.execute_script("return window.devicePixelRatio;")
        extra_height *= pixel_ratio
        last_image = img_li[-1]
        width, page_height = last_image.size
        box = (0, extra_height, width, page_height)
        img_li[-1] = last_image.crop(box)

    # Stitch image into one
    # Set up the full screen frame
    img_frame_height = sum([img_frag.size[1] for img_frag in img_li])
    img_frame = Image.new("RGB", (img_li[0].size[0], img_frame_height))
    offset = 0
    for img_frag in img_li:
        img_frame.paste(img_frag, (0, offset))
        offset += img_frag.size[1]
    img_frame.save(save_path)


def start_session():
    """主程序, 之后webdriver始终用这个
    """
    url = "https://www.acgdmzy.com/read/9087/8"
    driver = get_webdriver()
    driver.get(url)
    driver.execute_script('localStorage.setItem("token", "%s")'% my_token)
    driver.refresh()
    time.sleep(1)


    driver.get(url)
    time.sleep(10)
    save_path = Path('./screenshot_qing.png')
    full_screenshot_with_scroll(driver, save_path)


def test_get_header():
    url = "https://www.acgdmzy.com/home"
    driver = get_webdriver()
    driver.get(url)
    # todo: 用onload
    time.sleep(5)
    header = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[1]/header")

    driver.execute_script(
        "return document.getElementsByClassName('white--text v-sheet theme--light v-toolbar v-app-bar v-app-bar--clipped v-app-bar--fixed primary')[0].remove();")

    driver.find_element_by_xpath("/html/body/cloudflare-app/flashcard-header/flashcard-close").click()


    driver.execute_script(
        "return document.getElementsByClassName('v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--default primary')[0].remove();")

    "v-btn v-btn--is-elevated v-btn--fab v-btn--has-bg v-btn--round theme--light v-size--default primary"



    print("D")

if __name__ == '__main__':
    # refresh_cookie_qing(my_mail, my_pass)
    # test_get_header()
    start_session()
    # driver = get_webdriver()
    # driver.get("https://www.liaoxuefeng.com/wiki/1016959663602400/1017609424203904")
    # save_path = Path('./screenshot.png')
    # full_screenshot_with_scroll(driver, save_path)