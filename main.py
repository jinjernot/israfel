
import time
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def twitterlogin(driver, user):
    """Funcion para logearse a Twitter"""

    driver.implicitly_wait(5)
    driver.get('https://www.twitter.com/')
    sleep(3)

    tweet = driver.find_element("xpath", "//a[@href='/login']/./..").click()
    sleep(3)
    tweet = driver.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
    tweet.send_keys("username")
    tweet.send_keys(Keys.ENTER)
    sleep(3)
    tweet = driver.find_element("xpath", "/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
    tweet.send_keys("password")
    tweet.send_keys(Keys.ENTER)
    sleep(5)


def like(driver, user):
    """Funcion para dar like"""

    twitterlogin(driver, user)

    likes = driver.find_element("xpath", "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")
    likes.send_keys("from:")
    likes.send_keys(user)
    time.sleep(3)
    likes.send_keys(Keys.ENTER)
    time.sleep(5)
    darlike = driver.find_elements(By.CSS_SELECTOR, ".css-18t94o4[data-testid ='like']")
       
    for botonlike in darlike:
        time.sleep(5)
        botonlike.click()


def main():
    user = input("User name: ")
    driver = webdriver.Firefox() #Start the webbrowser
    like(driver, user)

if __name__ == "__main__":
    main()