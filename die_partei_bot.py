from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, time
import namegenerator
import names
import random

torexe = os.popen(r'D:\Users\Morplson\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe')
profile = FirefoxProfile(r'D:\Users\Morplson\Desktop\Tor Browser\Browser\TorBrowser\Data\Browser\profile.default')
profile.set_preference('network.proxy.type', 1)
profile.set_preference('network.proxy.socks', '127.0.0.1')
profile.set_preference('network.proxy.socks_port', 9050)
profile.set_preference("network.proxy.socks_remote_dns", False)
profile.update_preferences()
driver = webdriver.Firefox(firefox_profile= profile, executable_path=r'D:\Morplson\Documents\python-cheatcheet\selenium\geckodriver.exe')

driver.get("https://check.torproject.org")

#driver.get("https://instaparlament.at/?page_id=49")

mail = "{fn}.{ln}{num}@{mp}.{add}".format(
    fn=names.get_first_name().lower(),
    ln=names.get_last_name().lower(),
    num=random.randrange(0,1000)//100,
    mp=random.choice(["gmail","protonmail"]),
    add=random.choice(["com"])
    )
print(mail)

time.sleep(3.33)


driver.find_element_by_xpath('//*[@id="wpforms-57-field_2"]').send_keys(mail)

time.sleep(.33)
lol = driver.find_element_by_xpath('//*[@id="wpforms-57-field_3_2"]')
time.sleep(.33)
driver.execute_script("arguments[0].scrollIntoView(true);", lol)
lol.click()

time.sleep(1)
driver.find_element_by_xpath('//*[@id="wpforms-submit-57"]').click()

time.sleep(3.33)
driver.close()