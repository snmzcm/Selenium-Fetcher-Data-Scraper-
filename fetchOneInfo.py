from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the web driver (make sure the ChromeDriver is in your PATH)
driver = webdriver.Firefox()  # or webdriver.Firefox() for Firefox

try:
    # Open the search page
    driver.get('https://www.ncbi.nlm.nih.gov/nuccore/')  # Replace with the actual URL of the search page

    # Locate the input field with id 'term' and enter the search query
    search_input = driver.find_element(By.ID, 'term')
    search_input.send_keys('txid545932[Organism:exp]')  # Enter the search term

    # Locate the search button with id 'search' and click it
    search_button = driver.find_element(By.ID, 'search')
    search_button.click()  # Click the search button
    kacadetlistelenecek = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//*[text()='20 per page']")) )
    kacadetlistelenecek.click()
    menu_item = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "ps100")) ) 
    menu_item.click()


    # Wait for the results to load
    time.sleep(8)  # Adjust time as necessary or use WebDriverWait for better handling

    # Optionally, you may want to fetch and print the results here
    results = driver.find_elements(By.CLASS_NAME,'title')  # Updat the selector based on actual results
    time.sleep(3)
    #check Type results if is it a list
    kayitListeItemIsmi = "//*[text()='{0}']".format(results[0])
    print(kayitListeItemIsmi)
    kayitAdi = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, kayitListeItemIsmi)) )
    kayitAdi.click()
    # sayac = 1
    # for result in results:
    #     print(str(sayac) + ' ' + result.text)

    #     sayac= sayac + 1

finally:
    # Close the browser
    driver.quit()
