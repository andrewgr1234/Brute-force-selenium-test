from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
browser = webdriver.Chrome()

browser.get("https://typing-speed-test.aoeu.eu/")
def input_to_element(input):
    element = browser.find_element(By.XPATH, "//*[@id='input']")
    element.send_keys(input)


words_list = browser.find_element(By.XPATH, '//*[@id="words"]')

# create a list of the words list
words = words_list.find_elements(By.TAG_NAME, "span")

# type to the input bar elemnt.text with a space
for word in words:
    input_to_element(input=word.text + " ")

time.sleep(100)