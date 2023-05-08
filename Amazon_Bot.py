from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

field = ['Title', 'MRP', 'Price', 'Discount', 'Availability', 'Url']
data = []

search_term = input("Enter Your Search Term:- ")

driver = webdriver.Chrome()
driver.get('https://www.amazon.in')

driver.find_element('id','twotabsearchtextbox').send_keys(search_term)
driver.find_element('id','nav-search-submit-button').click()

products = driver.find_elements('xpath','//div[@data-component-type="s-search-result"]')

for product in products:
    product.find_element(By.TAG_NAME,'a').click()
    driver.switch_to.window(driver.window_handles[1])
    try:
        title = driver.find_element(By.ID,'productTitle').text
    except:
        title = "Not Available"
    try:
        mrp = driver.find_element(By.XPATH,'//span[@class="a-price a-text-price"]').text
    except:
        mrp="Not Available"
    try:
        price = driver.find_element(By.XPATH,'//span[@class="a-price aok-align-center reinventPricePriceToPayMargin priceToPay"]').text
    except:
        price="Not Available"
    try:
        discount = driver.find_element(By.XPATH,'//span[@class="a-size-large a-color-price savingPriceOverride aok-align-center reinventPriceSavingsPercentageMargin savingsPercentage"]').text
    except:
        discount="Not Available"
    try:
        availability = driver.find_element(By.ID,'availability').text
    except:
        availability = "Not Present"


    data.append({'Title' : title, 'MRP': mrp, 'Price': price[:len(price)-3], 'Discount':discount[1:],'Availability': availability, 'Url':driver.current_url })
    
    # print(f"Title:- {title}")
    # print(f"MRP:- {mrp}")
    # print(f"Price:- {price[:len(price)-3]}.00")
    # print(f"Discount:- {discount[1:]}")
    # print(f"Availability:- {availability}")
    # print(f"Url:- {driver.current_url}")

    driver.close()
    driver.switch_to.window(driver.window_handles[0])
df = pd.DataFrame(data)
df.to_csv("D:\WebScrapperBot/amazon.csv", header= field, encoding='utf-8', mode='w')
