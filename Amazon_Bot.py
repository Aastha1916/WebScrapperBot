# These lines import the necessary modules: 'webdriver' from Selenium for browser automation,
# 'By' for specifying the method to locate elements, and 'pandas' for data manipulation.
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

# Here, a list called field is created to define the column headers for the data.
# An empty list called data is also created to store the scraped data.
field = ['Title', 'MRP', 'Price', 'Discount', 'Availability', 'Url']
data = []

# The user is prompted to enter a search term.
search_term = input("Enter Your Search Term:- ")

# A new Chrome WebDriver instance is created. This will allow the script to control a Chrome browser.
driver = webdriver.Chrome()

# The WebDriver navigates to the specified URL, which is the Amazon India website.
driver.get('https://www.amazon.in')

# These lines locate the search input field and search button on the Amazon website,
# enter the search term provided by the user, and click the search button to initiate the search.
driver.find_element('id','twotabsearchtextbox').send_keys(search_term)
driver.find_element('id','nav-search-submit-button').click()

# Using XPath, this line finds a list of elements corresponding to search results on the Amazon page.
products = driver.find_elements('xpath','//div[@data-component-type="s-search-result"]')

# This loop iterates through the search results. For each result, it clicks on the first link (a hyperlink)
# within the result to open the product details page. It also switches the WebDriver focus to the new tab that 
# opens.
for product in products:
    product.find_element(By.TAG_NAME,'a').click()
    driver.switch_to.window(driver.window_handles[1])

    # This code attempts to find the product title element on the page and extract its text. If the element
    # is not found, it assigns "Not Available" to the title variable. Similary for mrp, selling price, discount, 
    # availability
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

    # The extracted information (title, MRP, price, discount, availability, and URL) is added to the data list 
    # as a dictionary. 
    data.append({'Title' : title, 'MRP': mrp, 'Price': price[:len(price)-3], 'Discount':discount[1:],'Availability': availability, 'Url':driver.current_url })
    
    # print(f"Title:- {title}")
    # print(f"MRP:- {mrp}")
    # print(f"Price:- {price[:len(price)-3]}.00")
    # print(f"Discount:- {discount[1:]}")
    # print(f"Availability:- {availability}")
    # print(f"Url:- {driver.current_url}")

    # The WebDriver is then closed for the current tab, and focus is switched back to the original tab.
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# After the loop ends, the collected data is converted into a pandas DataFrame. The DataFrame is then saved to 
# a CSV file named "amazon.csv" using the specified column headers (field). The file is saved in the 
# "D:\WebScrapperBot" directory with UTF-8 encoding and in "append" mode (mode='a'), which allows you to add 
# more data to the same file if the script is run multiple times.
df = pd.DataFrame(data)
df.to_csv("D:\WebScrapperBot/amazon.csv", header= field, encoding='utf-8', mode='a')
