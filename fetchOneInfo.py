from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import pandas as pd

# Initialize the web driver (make sure the GeckoDriver or ChromeDriver is in your PATH)
driver = webdriver.Firefox()  # or webdriver.Chrome() for Chrome

# Load the CSV file into a DataFrame
df = pd.read_csv('table3.csv')

indexValofCSV = 0

def iterateURL():
    global indexValofCSV  # Access the global variable
    while indexValofCSV < len(df):
        val = df.iloc[indexValofCSV, 1]
        indexValofCSV += 1
        yield val

# Using the generator to get values
url_gen = iterateURL()
print(type(url_gen))

# Iterate over the generator to get the values and visit URLs
for url in url_gen:
    complete_url = f"https://www.ncbi.nlm.nih.gov/nuccore/{url}"
    print(f"Generated URL: {complete_url}")

    def fetchTitle(urladres):
        urladresi = urladres
        print(f"Visiting URL: {urladresi}")
        try:
            # Open the search page
            driver.get(urladresi)

            # Wait for the results to load
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'genbank')))

            # Fetch results
            results = driver.find_elements(By.CLASS_NAME, 'genbank')
            content = ' '.join([result.text for result in results])

            # Regex pattern to capture any text between TITLE and JOURNAL
            pattern = r"TITLE\s+([\s\S]+?)\s+JOURNAL"
            match = re.search(pattern, content)

            # Return extracted value if found
            if match:
                return match.group(1)
            else:
                return "No match found"
        except Exception as e:
            print(f"Error occurred: {e}")
            return "Error"
        finally:
            time.sleep(3)  # Adjust time as necessary to avoid being too aggressive

    # Fetch the title for the generated URL
    title = fetchTitle(complete_url)
    idx = df.index[df.iloc[:, 1] == url].tolist()[0]
    df.at[idx , 'Articles'] = title # Update the third column
    print(type(title))

# Save the updated DataFrame back to CSV
df.to_csv('table3.csv', index=False)
print("Completed updating table3.csv")

# Close the browser
driver.quit()
