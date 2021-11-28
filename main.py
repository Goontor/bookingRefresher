
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


def main():

    page = load("https://booking.kscgolf.org.hk/login")
    login(page, "claverie_pierre@hotmail.fr", "dratar1er!")
    sleep(10)
    go_to_sub_menu(page, "waitingRoom")
    sleep(5)
    while (is_in_queue(page)):
        page.refresh()
        sleep(0.21)


def load(path):

    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    global browser
    browser = webdriver.Chrome(r"C:\Users\Pierre\PycharmProjects\bookingRefresher\chrome_drivers\chromedriver.exe")
    browser.get(path)
    return browser


def login(driver: WebDriver, username: str, password: str):

    login_btm_xpath = '//*[@id="root"]/div[1]/div[2]/div/div/form/div[2]/div/button'
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH,login_btm_xpath).click()


def go_to_sub_menu(driver: WebDriver, menu):
    print("goto")
    booking_link_xpath = '//*[@id="root"]/div[1]'
    driver.get(driver.current_url+menu)


def is_in_queue(driver: WebDriver):
    result = False
    field_to_check_xpath = ""
    header = driver.find_element(By.ID,"headline")
    string_to_test = "Please refresh the page at 5:00 PM"
    print(header.get_attribute('innerHTML'))
    if  string_to_test in header.get_attribute('innerHTML'):
        print("set to false")
        result = True
    return result

if __name__ == '__main__':
    main()

