# -*- coding: UTF-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select


import time
import random
import os

class Bawangcan:

    driver = None
    phone = ""
    pw = ""

    def __init__(self, phone, pw):
        self.init_chrome()
        self.phone = phone
        self.pw = pw

    def init_chrome_headless(self):
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def init_chrome(self):
        self.driver = webdriver.Chrome()

    def login_with_cookie(self, cookies):
        self.driver.get('http://s.dianping.com/event/shanghai')
        self.wait_a_while()

        self.driver.delete_all_cookies()
        for cookie in cookies:
            self.driver.add_cookie(cookie)
        self.driver.refresh()

    def login(self):
        self.driver.get("https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2Fshanghai")
        iframe = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "iframe"))
        )
        self.driver.switch_to.frame(iframe)

        noQRLogin = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CLASS_NAME, "icon-pc"))
        )
        noQRLogin.click()
        pwLogin = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "tab-account"))
        )
        pwLogin.click()

        phoneInput = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "account-textbox"))
        )
        phoneInput.send_keys(self.phone)

        pwInput = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "password-textbox"))
        )
        pwInput.send_keys(self.pw)
        time.sleep(1)
        loginBtn = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.ID, "login-button-account"))
        )
        loginBtn.click()
        loginBtn.click()
        loginBtn.click()

        try:
            cap_img = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "img,.captcha"))
            )
            print "get the captcha code picture"
            self.driver.get_screenshot_as_file("./bawangcan.png")
            print "stored the screenshot of captcha"
            # wait to input the captcha code and login
            while True:
                try:
                    self.driver.switch_to.window(self.driver.current_window_handle)
                    afterLogin = WebDriverWait(self.driver, 10).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "cate-container"))
                    )
                    break
                except TimeoutException:
                    print "10s past no login"
                    continue
        except TimeoutException:
            print "no need to input captcha code"

    def sign_for_category(self, category_id, location):
        # count total
        js = 'window.open("http://s.dianping.com/event/' + location + '");'
        self.driver.execute_script(js)
        self.driver.switch_to.window(self.driver.window_handles[-1])

        category_tag = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.container-title.tabs [data-type="' + category_id + '"]'))
        )
        category_tag.click()
        print "clicked"


        loadMoreFlag = True
        while loadMoreFlag:
            try:
                loadMoreIcon = WebDriverWait(self.driver, 1).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, ".load-more.show"))
                )
                loadMoreIcon.click()
                time.sleep(0.5)
            except TimeoutException:
                loadMoreFlag = False
                print "finish load more."

        fishes = self.driver.find_elements_by_css_selector(".activity-lists-wraper li a")
        print "BaWangCan list size is " + str(len(fishes))

        signedNumber = 0
        basePage = self.driver.current_window_handle

        # open each page to sign
        for fish in fishes:
            self.driver.switch_to.window(basePage)
            fish.click()
            self.driver.switch_to.window(self.driver.window_handles[-1])
            urlName = self.driver.current_url
            print "url = " + urlName

            self.wait_a_while()
            self.sign_for_each()
            self.driver.close()
        self.driver.close()

    def sign_for_each(self):
        # get title
        title = ""
        try:
            titleEle = self.driver.find_element_by_css_selector('#J_activityTitle')
            title = "[" + titleEle.text + "]"
            print "title = " + title
        except NoSuchElementException:
            print "cannot get page title"
            title = "unknown"
        # click 我要报名 button
        try:
            signBtn = self.driver.find_element_by_css_selector("[title=我要报名]")
            signBtn.click()
            print "clicked the OK button"
            time.sleep(0.5)
        except NoSuchElementException:
            print "already signed for " + title
            return False
        # select all the dropdown list
        self.wait_a_small_while()
        try:
            selectors = self.driver.find_elements_by_css_selector("#J_applyInfo select")
            print "select size " + str(len(selectors))
            for select in selectors:
                s = Select(select)
                s.select_by_index(1)
        except NoSuchElementException:
            print "no need to select"

        # press ok button
        self.wait_a_small_while()
        try:
            okBtn = self.driver.find_element_by_css_selector(".pop-main .medi-btn")
            okBtn.click()
            time.sleep(1)
            successBtn = self.driver.find_element_by_css_selector(".p-msg-succ")
            print "successfully signed for " + title
        except NoSuchElementException:
            print "there are sign limits for " + title
            return False

    def wait_a_while(self):
        time.sleep(random.randint(2, 8))

    def wait_a_small_while(self):
        time.sleep(random.randint(1, 3))
