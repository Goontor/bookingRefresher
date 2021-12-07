import configparser
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from time import sleep


def main():
    config = configparser.ConfigParser()
    config.sections()
    config.read("conf/conf.ini")
    url=config['Website']['path']


    page = load(config)
    login(page, config)
    sleep(2)
    go_to_sub_menu(page, "waitingRoom")
    sleep(5)
    while (is_in_queue(page)):
        page.refresh()
        sleep(0.38)


def load(config):
    path = config['Website']['path']
    remote_server = config['Remote']['server']


    global browser
    chrome_options = Options()
    chrome_options = webdriver.ChromeOptions()

    ### To use local chrome browser
    #driver_path = config['ChromeDriver']['driver_path']
    #chrome_options.add_experimental_option("detach", True)
    #browser = webdriver.Chrome(driver_path)
    ###

    ### To use a remote selenium container
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("detach", True)
    browser = webdriver.Remote(command_executor=remote_server,options=chrome_options)
    ###

    browser.get(path)
    return browser


def login(driver: WebDriver, config):

    username = config['Website']['username']
    password = config['Website']['password']
    login_btn_xpath = '//*[@id="root"]/div[1]/div[2]/div/div/form/div[2]/div/button'
    popup_ok_btn_xpath = '/html/body/div[2]/div[3]/div/div[3]/button[2]'
    driver.find_element(By.ID, "username").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.XPATH,login_btn_xpath).click()
    sleep(2)
    popup_btn = driver.find_element(By.XPATH,popup_ok_btn_xpath)
    if popup_btn:
        popup_btn.click()

def go_to_sub_menu(driver: WebDriver, menu):
    print("goto")
    booking_link_xpath = '//*[@id="root"]/div[1]/div[4]/div/div/div[2]/div[2]/h3'
    driver.get(driver.current_url+menu)


def is_in_queue(driver: WebDriver):
    result = False
    field_to_check_xpath = ""
    header = driver.find_element(By.ID,"headline")
    string_to_test = "Please refresh the page at"
    print(header.get_attribute('innerHTML'))
    if  string_to_test in header.get_attribute('innerHTML'):
        print("set to false")
        result = True
    return result

if __name__ == '__main__':
    main()

