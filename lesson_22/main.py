from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait



driver = Chrome("./chromedriver")
driver.get("https://www.w3schools.com")
# maximize window size up to screen size on device
wait = WebDriverWait(driver, 15)
driver.maximize_window()
element: WebElement = driver.find_element(By.XPATH, "//a[contains(text(), 'Next')]")
# sleep(1)
# element.click()
# click on search icon
search_button: WebElement = driver.find_element(By.XPATH, "//a[@title='Search W3Schools']")
search_button.click()
search_bar: WebElement = driver.find_element(By.XPATH, "//input[@id='gsc-i-id1']")
search_bar.send_keys("Hello WOrld=)")
sleep(3)
search_bar.clear()
sleep(3)

#save button screenshot in binary mod into the png container
with open("next_button.png", "wb") as file:
    file.write(element.screenshot_as_png)

driver.save_screenshot("./screenshot.png")

print(driver.current_url)
driver.quit()
