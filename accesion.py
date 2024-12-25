from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

def accesion():
    driver = webdriver.Firefox()  # or webdriver.Firefox() for Firefox

    try:
        # Open the search page
        driver.get('https://www.ncbi.nlm.nih.gov/nuccore')  # Replace with the actual URL of the search page

        # Locate the input field with id 'term' and enter the search query
        search_input = driver.find_element(By.ID, 'term')
        search_input.send_keys('txid545932[Organism:exp]')  # Enter the search term

        # Locate the search button with id 'search' and click it
        search_button = driver.find_element(By.ID, 'search')
        search_button.click()  # Click the search button
        kacadetlistelenecek = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.XPATH, "//*[text()='20 per page']")) )
        kacadetlistelenecek.click()
        menu_item = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.ID, "ps100")) ) 
        menu_item.click()
        time.sleep(8)
        #Accession Listeleme
        accessionListele = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.XPATH, "//*[text()='Summary']")) )
        accessionListele.click()
        accession_item = WebDriverWait(driver, 10).until( EC.presence_of_element_located((By.ID, "accnlisttext")) ) 
        accession_item.click()
        ######################
        # Wait for the results to load
        time.sleep(8)  # Adjust time as necessary or use WebDriverWait for better handling

        # Optionally, you may want to fetch and print the results here
        resultText = WebDriverWait(driver, 30).until( EC.presence_of_element_located((By.TAG_NAME, "pre")) )
        results = resultText.text
        items = results.split('\n')
        for item in items:
            print(item)


        return items

    finally:
        # Close the browser
        driver.quit()

