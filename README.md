
# WebScrapperBot

Web scraping is an automated process of gathering public data. A webpage scraper automatically extracts large amounts of public data from target websites in seconds. 
This project presents a simple yet effective web scraping program designed to extract data from the Amazon website and store it in a CSV file. 

## Features

- Chatbot to Enter search Term 
- Automatic Scratching of data
- CSV file maintenance
- Available for amazon website


## Required Libraries

```
from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

```
## Installation

- Chrome Driver for selenium
- IDE (Python based)


## Documentation

Stepwise implementation: 

- Step 1: First, we will import some required modules. 

- Step 2: The next step is to open the required website. 

- Step 3: Extracting the Products title from the webpage, to extract a specific part of the 
    page, we need its XPath, which can be accessed by right-clicking on the required element 
    and selecting Inspect in the dropdown bar
    - After clicking Inspect a window appears. From there, we have to copy the 
      elements ids to access it

    *Note: You might not always get the exact element that you want by inspecting 
    (depending on the structure of the website), so you may have to surf the HTML 
    code for a while to get the exact element you want. And now, just copy that id 
    and paste that into your code. After running all these lines of code, you will get 
    the input from the terminal which will be automatically entered into the search 
    box.* 

- Step 4: Now, the target is to get all the items present in the searched field. 
    One way is that we can copy all the XPaths or ids of all the items and we can fetch 
    all those, but that method is not suited if there are a large number of things to be 
    scrapped. So, the elegant way is to find the pattern of the XPaths of the titles 
    which will make our tasks way easier and efficient. 

- Step 5: We have used CSV files to collect our data instead of getting it on the terminal. 
    For this purpose, we have used pandas library for reading and writing CSV files 
    efficiently.



    
