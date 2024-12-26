from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

# Initialize the web driver (make sure the ChromeDriver is in your PATH)
driver = webdriver.Firefox()  # or webdriver.Chrome() for Chrome

def fetchTitle():
    try:
        # Open the search page
        driver.get('https://www.ncbi.nlm.nih.gov/nuccore/OQ992551.1')  # Replace with the actual URL of the search page

        # Wait for the results to load
        time.sleep(8)  # Adjust time as necessary or use WebDriverWait for better handling

        # Optionally, you may want to fetch and print the results here
        results = driver.find_elements(By.CLASS_NAME, 'genbank')  # Update the selector based on actual results
        titleVar = []
        for i in results:
            titleVar.append(i.text)
        newTitleVar = ' '.join(titleVar)

        # Regex pattern to capture any text between TITLE and JOURNAL
        patternForReg = r"TITLE\s+([\s\S]+?)\s+JOURNAL"

        findReg = re.search(patternForReg, newTitleVar)
        
        # Check if a match is found
        if findReg:
            extracted_value = findReg.group(1)
            print(f"Extracted value: {extracted_value}")
        else:
            print("No match found in the text.")

        time.sleep(3)

        # Check type of results if it is a list
        kayitListeItemIsmi = "//*[text()='{0}']".format("PQ676539.1")
        print(kayitListeItemIsmi)
        kayitAdi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, kayitListeItemIsmi))
        )
        kayitAdi.click()

    finally:
        # Close the browser
        driver.quit()

# Call the fetchTitle function to see if it works
fetchTitle()
