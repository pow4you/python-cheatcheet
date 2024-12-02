from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
import namegenerator
import names
import random
import threading

def caller():

    torexe = os.popen(r'D:\Users\Morplson\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
    profile = FirefoxProfile(r'D:\Users\Morplson\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
    profile.set_preference('network.proxy.type', 1)
    profile.set_preference('network.proxy.socks', '127.0.0.1')
    profile.set_preference('network.proxy.socks_port', 9050)
    profile.set_preference("network.proxy.socks_remote_dns", False)
    profile.update_preferences()
    driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'D:\Morplson\Documents\python-cheatcheet\selenium\geckodriver.exe')

    driver.get("https://check.torproject.org")
    time.sleep(0.33)
    #driver.get('https://strawpoll.de/8z7c8x9')
    driver.get('https://strawpoll.de/2xy1cxd')



    time.sleep(1.66)


    driver.execute_script(r"el = document.getElementById('check2'); el.scrollIntoView()")

    time.sleep(.33)
    try:
        driver.find_element_by_xpath('//*[@id="check2"]').click()
    except:
        driver.find_element_by_xpath('//*[@id="check2"]//following-sibling::label').click()

    time.sleep(.33)
    driver.execute_script(r"el = document.getElementById('votebutton'); el.scrollIntoView()")
    time.sleep(.33)
    driver.find_element_by_xpath('//*[@id="votebutton"]').click()

    time.sleep(6.66)
    driver.close()


for n in range(1):
    data = [caller for x in range(1)]
    thread_num = 4

    if len(data)>0:

        threads = []
        for i in range(len(data)):
            thread = threading.Thread(target=data[i],args=())
            threads.append(thread)

        for thread in threads:
            thread.start()

        for thread in threads:
            thread.join()