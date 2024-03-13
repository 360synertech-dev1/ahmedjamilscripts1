from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import undetected_chromedriver as uc
import time
import pandas as pd
import requests
import json
import base64
from datetime import datetime
import os
import stat

# Update download_directory to /home/umair/data

# download_directory = '/home/umair/data'

# # Create the directory if it doesn't exist
# if not os.path.exists(download_directory):
#     os.makedirs(download_directory)

# # Set the permissions for the directory
# os.chmod(download_directory, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
try:
        options = uc.ChromeOptions()

        # Set the download directory in ChromeOptions

        prefs = {'download.default_directory': 'C:\data'}
        options.add_experimental_option('prefs', prefs)

        # options.add_argument('--incognito')
        #options.add_argument('--headless')

        driver = uc.Chrome(options)

        print("browse open")
        driver.maximize_window()



        url="https://app.batchdialer.com/login/"
        driver.get(url)


        login = "atompropertygroup@gmail.com"
        password= "Atom199654321!"

        wait = WebDriverWait(driver, 30)
        input_element = wait.until(expected_conditions.presence_of_element_located((By.NAME, "email")))
        input_element.clear()
        input_text = str(login)
        input_element.send_keys(input_text)


        wait = WebDriverWait(driver, 30)
        input_element = wait.until(expected_conditions.presence_of_element_located((By.NAME, "password")))
        input_element.clear()
        input_text = str(password)
        input_element.send_keys(input_text)


        checkmark_span = driver.find_element(By.CLASS_NAME, "checkmark")
        checkmark_span.click()

        login_button = driver.find_element(By.CSS_SELECTOR,"button.w-100.btn.btn-primary")
        login_button.click()
        time.sleep(5)

        print("Hallo")

except NoSuchElementException:
    print("Element not found. Cannot click.")

try:
    if driver.find_elements(By.ID, "pendo-button-c128bf2b"):
            print("Ahmed Jameel If")
            deleteableelements = driver.find_elements(
                By.ID, "pendo-button-c128bf2b"
            )
            for element in deleteableelements:
                driver.execute_script(
                    """var element = arguments[0]; element.parentNode.removeChild(element);""",
                    element,
                )
                print("Element Deleted1")
    time.sleep(5)
    # modal-backdrop show
    
    if driver.find_elements(By.ID, "pendo-base"):
            print("Ahmed Jameel If")
            deleteableelements = driver.find_elements(
                By.ID, "pendo-base"
            )
            for element in deleteableelements:
                driver.execute_script(
                    """var element = arguments[0]; element.parentNode.removeChild(element);""",
                    element,
                )
                print("Element Deleted2")
                
    
        
except NoSuchElementException:
    print("Element not found. Cannot click.")
    
try:
    if WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Ignore')]"))):
        button = driver.find_element(By.XPATH, "//button[contains(text(), 'Ignore')]")
        button.click()
        print("Button clicked successfully!")
        
except NoSuchElementException:
     print("Element not found. Cannot click.")

anchor_element = WebDriverWait(driver, 19).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@title='Reports']"))
)
anchor_element.click()

element = driver.find_element(By.CLASS_NAME,"d-flex.justify-content-center.align-items-center")
element.click() 

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[@class='btn btn-link' and text()='Today']"))
)
button.click()

button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(@class,'btn-primary') and contains(text(),'Export')]"))
)
button.click()
time.sleep(7)
button.send_keys(Keys.ENTER)
time.sleep(10)

driver.quit()
file_path = r'C:\data\recent_contacts.csv'

df = pd.read_csv(file_path)
print(df)

agent_name_out_counts = df['Agent Name'].dropna()
agent_name_out_counts_unique = agent_name_out_counts.unique()
comma_separated_names = ', '.join(agent_name_out_counts_unique)
print("names =",comma_separated_names)


print("-----------------------------------------------------------------------")
total_number_of_dials = df[df['Direction'] == 'out'].shape[0]
print("total_number_of_dials =",total_number_of_dials)

print("-----------------------------------------------------------------------")

out_df = df[df['Direction'] == 'out']
agent_name_out_counts1 = out_df['Agent Name'].value_counts()
agent_name_out_counts1.index.name = None

# Convert to dictionary
counts_dict = agent_name_out_counts1.to_dict()

# Print in the specified format
for key, value in counts_dict.items():
    print(key, value)

print("-----------------------------------------------------------------------")

out_specific_calls_df = df[(df['Direction'] == 'out') & 
                           ((df['Call Result'] == 'Not Interested') |
                            (df['Call Result'] == 'Do Not Call') |
                            (df['Call Result'] == 'Cold Lead -Selling within 5-12 Months') |
                            (df['Call Result'] == 'Nurture Lead - Selling within 3-5 Months') |
                            (df['Call Result'] == 'Investor Buyer') |
                            (df['Call Result'] == 'Warm Lead - Selling within 1-3 Months') |
                            (df['Call Result'] == 'Hot Lead -Selling within 31 Days') |
                            (df['Call Result'] == 'Realtor/Wholesaler') |
                            (df['Call Result'] == 'Retail Buyer') |
                            (df['Call Result'] == 'Call Back'))]

agent_name_out_counts = out_specific_calls_df['Agent Name'].value_counts()
counts_dict = agent_name_out_counts.to_dict()
for key, value in counts_dict.items():
    print(key, value)
    
print("-----------------------------------------------------------------------")


direction_counts_by_agent = df.groupby('Agent Name')['Call Result'].value_counts()
print(direction_counts_by_agent)
direction_counts_by_agent_dict=direction_counts_by_agent.to_dict()
print(type(direction_counts_by_agent))

print("-----------------------------------------------------------------------")



if not isinstance(direction_counts_by_agent, pd.DataFrame):
    direction_counts_by_agent = direction_counts_by_agent.unstack(fill_value=0)
formatted_data = {}

for agent_name in direction_counts_by_agent.index:
   
    agent_results = {}
    for call_result, count in direction_counts_by_agent.loc[agent_name].items():
        agent_results[call_result] = count
    formatted_data[agent_name] = agent_results

json_data = json.dumps(formatted_data, indent=2)

print(json_data)

current_date = datetime.now()
formatted_date = current_date.strftime("%m/%d/%Y")
print("Formatted date:", formatted_date)
base64_encoded_data = base64.b64encode(json_data.encode()).decode()

data = {
    "KPI Date": formatted_date,    
    "Names": comma_separated_names,
    "Total number of dials": total_number_of_dials,
    "Number of dials per agent":agent_name_out_counts1.to_dict(),
    "Number of live calls per agent": agent_name_out_counts.to_dict(),
    "Number of dial report per agent": base64_encoded_data
}

json_data = json.dumps(data, indent=2)
print(json_data)
base64_encoded_data = base64.b64encode(json_data.encode()).decode()

podio_api_url = "https://workflow-automation.podio.com/catch/yo0d3muchkd3892"
headers = {"Content-Type": "application/json"}

try:
    response = requests.post(podio_api_url, json={"data": base64_encoded_data}, headers=headers)
        
    if response.status_code == 200:
        print("Request successful!")
        print("Response content:", response.json())
    else:
        print("Request failed with status code:", response.status_code)
        print("Response content:", response.text) 

except Exception as e:
    print("An error occurred:", str(e))

os.remove(file_path)







