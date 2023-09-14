from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import time

# Set the path for the Edge driver
path = "msedgedriver.exe"

# Create an Options instance and enable headless mode
options = Options()
options.headless = True

# Create a Service instance for the Edge driver
service = Service(path)

# Create an Edge WebDriver instance with the specified options and service
browser = webdriver.Edge(service=service, options=options)

# Perform the web scraping tasks as before
browser.get('https://www.amazon.in')
browser.maximize_window()

# get the input elements
input_search = browser.find_element(By.ID, 'twotabsearchtextbox')
search_button = browser.find_element(By.XPATH, "//input[@type='submit']")

# send the input to the web page
input_search.send_keys("Smartphones under 10000")
time.sleep(2)  # Scroll down the page to make the button visible
search_button.click()

product_class = "a-size-medium a-color-base a-text-normal"
products = []

for i in range(5):
    print("scraping page", i + 1)
    
    # Find all product elements on the current page
    page_products = browser.find_elements(By.XPATH, "//span[@class='a-size-medium a-color-base a-text-normal']")
    
    # Collect product data from each element and extend the main list
    products.extend([product.text for product in page_products])
    
    # Click the "Next" button to navigate to the next page
    next_button = browser.find_element(By.XPATH, "//a[contains(@class, 's-pagination-next') and contains(text(), 'Next')]")
    next_button.click()
    time.sleep(3)

# Print or process the collected product data
for product_data in products:
    print(">", product_data)
    
# print("length of the product:",)
# products
# Close the browser
browser.quit()
