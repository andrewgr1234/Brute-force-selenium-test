from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import itertools
import time

driver = webdriver.Chrome()
driver.get("https://qwik-9v1m.onrender.com/bf")
time.sleep(1)


def generate_combinations(digits, length):
    return [''.join(p) for p in itertools.product(digits, repeat=length)]


def brute_force_level(digits, length):
    input_field = driver.find_element(By.XPATH, '//*[@id="guess"]')
    submit_button = driver.find_element(By.XPATH, '//*[@id="check"]')
    for combination in generate_combinations(digits, length):
        input_field.clear()
        input_field.send_keys(combination)
        submit_button.click()
        if "correct!" in driver.find_element(By.XPATH, '//*[@id="result"]').text.lower():
            driver.find_element(By.XPATH, '//*[@id="next"]').click()
            return True
    return False


digits = '012'
length = 2
while True:

    while not brute_force_level(digits, length):
        pass
    length += 1
    try:
        result_element = WebDriverWait(driver, 1).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="result"]/h2'))
        )
        if "congratulations!" in result_element.text.lower():
            print("All levels completed!")
            break
    except:
        continue

driver.quit()
