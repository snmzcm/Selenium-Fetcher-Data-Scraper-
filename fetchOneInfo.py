from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

# Initialize the web driver (make sure the ChromeDriver is in your PATH)
driver = webdriver.Firefox()  # or webdriver.Chrome() for Chrome
import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('table2.csv')

indexValofCSV = 0

def iterateURL():
    global indexValofCSV  # Access the global variable
    while indexValofCSV < len(df):
        val = df.iloc[indexValofCSV, 1]
        indexValofCSV += 1
        yield val

# Using the generator to print values
url_gen = iterateURL()
print(type(url_gen))

# Iterate over the generator to get the values
for url in url_gen:
    print(url)



def fetchTitle(urladres):
    urladresi = "https://www.ncbi.nlm.nih.gov/nuccore/{name}".format(name = urladres)
    print(urladresi)
    try:
        # Open the search page
        driver.get(urladresi)  # Replace with the actual URL of the search page

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
            print(extracted_value)
            df.iloc[12 - 1,2] = str(extracted_value)
            df.to_csv('table2.csv', index=False)
        else:
            print("No match found in the text.")

        time.sleep(3)

    finally:
        # Close the browser
        driver.quit()


############################333

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# Load the CSV file into a DataFrame
df = pd.read_csv('table2.csv')

indexValofCSV = 0

def iterateURL():
    """Generator function to read URLs from a DataFrame and yield them one by one."""
    global indexValofCSV  # Access the global variable
    while indexValofCSV < len(df):
        val = df.iloc[indexValofCSV, 1]
        indexValofCSV += 1
        yield val

def visit_urls(url_gen):
    """Function to visit each URL using Selenium."""
    # Set up Firefox options for headless mode (optional)
    firefox_options = Options()
    firefox_options.add_argument("--headless")  # Enable headless mode

    # Create a new instance of the Firefox driver with the headless options
    driver = webdriver.Firefox(options=firefox_options)

    try:
        for url in url_gen:
            fetchTitle(url)

    finally:
        # Close the browser
        driver.quit()

# Create a URL generator
url_gen = iterateURL()

# Visit each URL using the generator
visit_urls(url_gen)



