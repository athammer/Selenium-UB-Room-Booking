import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
from html.parser import HTMLParser
from lxml import etree
import re


#http://selenium-python.readthedocs.io/locating-elements.html
driver = webdriver.Chrome(
    '/home/athammer/bin/chromedriver')  # Optional argument, if not specified will search path.
driver.get(
    'https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier');

time.sleep(.5)

element = driver.find_element_by_id("Email")
element.send_keys("sdfg@sdfg.edu")
driver.find_element_by_id("gaia_loginform").submit()

time.sleep(.5)

element = driver.find_element_by_id("login")
element.send_keys("sdfg") # get rid of pass when submitting duh....
element = driver.find_element_by_id("password")
element.send_keys("sdfg")  # get rid of pass when submitting duh....
driver.find_element_by_name("f").submit()
time.sleep(2)

def run():



    email = driver.find_elements_by_class_name("zE")  # does it get first one it finds?
    for x in email:
        try:
            element = x.find_element_by_name("UB Libraries Booking Sys.")
            print(element.get_attribute('innerHTML'))
            if (element.get_attribute('innerHTML') == "UB Libraries Booking Sys."):
                x.click()
        except NoSuchElementException:
            print('not found, moving on')
        else:
            print('error')

    time.sleep(1)

    text = driver.find_element_by_class_name(("gs")).text
    url = re.search("(http:\/\/booking\.lib\.buffalo\.edu\/confirm\.php\?i=.+\|.+&c=.{10})", text)
    driver.get(url.group(0));

    time.sleep(1)

    driver.find_element_by_id("rm_confirm_link").click()
    driver.get_screenshot_as_file('/home/athammer/Pictures/confirmation.png')

    time.sleep(1)

    driver.get("https://groupme.com/signin")
    element = driver.find_element_by_id("signinUserNameInput")
    element.send_keys("sdfg")  # get rid of email when submitting duh....
    element = driver.find_element_by_id("signinPasswordInput")
    element.send_keys("sdfg")  # get rid of pass when submitting duh....
    driver.find_element_by_class_name("login").click()

    time.sleep(1)

    text = driver.find_elements_by_class_name("chat-name")
    for x in text:
        if (x.text == "bot testing"):
            x.click()

    time.sleep(.5)

    driver.find_element_by_id("filestyle-0").send_keys("/home/athammer/Pictures/confirmation.png");

    time.sleep(1)

    driver.find_element_by_class_name("send").click()
    print("email sent")
    run()

while(True):
    try:
        run()
    except NoSuchElementException:
        print('email not found most likely')
    else:
        print('email not found most likely')
