##### imports #####
from random import randint
from re import I
from time import sleep
from urllib.parse import SplitResult
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


browser = webdriver.Chrome('/Users/farin/Documents/Dokumente/Business/Farin Marscholl/Projekte/scripts/iconscout-account-liker/chromedriver')

##### config #####

securetimer = randint(1,3)

##### retrieve section #####

# get data from txt file 
def retrieveData():
    # open txt file, read data and store it into an array
    with open('accounts.txt') as f:
        accounts = f.readlines()

    # return the array to use it in different functions
    return accounts


def accountAmount():
    # get accounts array with retrieveData function
    accounts = retrieveData()
    # count accounts
    x = len(accounts)

    # return the number of accounts in the array
    return x



##### iconscout section #####

def splitDetails(number):
    # get accounts array with retrieveData function
    accounts = retrieveData()
    # split username from password, return to use in different functions
    user, passwd = accounts[number].split(':')
    return(user, passwd)

def loginAccount(passedUser, passedPasswd):
    # open iconscout
    browser.get('https://iconscout.com')
    sleep(5)
    # login section
    loginbutton = browser.find_element_by_xpath('//*[@id="__layout"]/div/div[2]/div[1]/header/nav/ul/li[6]/button')
    loginbutton.click()
    sleep(securetimer)
    username = browser.find_element_by_name('email')
    username.send_keys(passedUser)
    sleep(securetimer)
    password = browser.find_element_by_name('password')
    password.send_keys(passedPasswd)
    sleep(5)

def like():
    # get links from collection.txt
    with open('collection.txt') as c:
        collection = c.readlines()
        
        m = 0
        n = len(collection)
        # while m < n like the picture until number of collection is reached
        while m < n:
            browser.get(collection[m])
            sleep(5)
            element_to_hover_over = browser.find_element_by_xpath('//*[@id="modalItemPreview___BV_modal_body_"]/div/main/div[2]/div[4]/div/button')
            hover = ActionChains(browser).move_to_element(element_to_hover_over)
            hover.perform()
            element_to_hover_over.click()
            sleep(5)
            m = m + 1

def logout():
    # logout section
    browser.get('https://iconscout.com')
    sleep(5)
    profile = browser.find_element_by_id('ddUserOptions__BV_toggle_')
    profile.click()
    sleep(securetimer)
    loginbutton = browser.find_element_by_xpath()
    loginbutton.click()
    sleep(5)



##### Loop Setcion #####

def AccountLoop():
    x = accountAmount()
    i = 0;
    # like pictures while i < x
    while i < x:
        splitDetails(i)
        user, passwd = splitDetails(i)
        loginAccount(user, passwd)
        like()
        logout()
        i = i + 1


def onStart():
    AccountLoop()
    
onStart()