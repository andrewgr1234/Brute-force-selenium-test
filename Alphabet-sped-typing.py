from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://qwik-9v1m.onrender.com/ast")

alphabet = [chr(letter) for letter in range(ord('a'), ord('z') + 1)]

time.sleep(1)

start_time = time.time()

for letter in alphabet:
    driver.find_element_by_tag_name('body').send_keys(letter)

end_time = time.time()

time.sleep(10)
driver.quit()

elapsed_time = end_time - start_time
print(f"Test finished in {elapsed_time} seconds")
