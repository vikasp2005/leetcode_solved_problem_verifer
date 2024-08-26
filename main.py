from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import pandas as pd
from datetime import date
import function




# Initialize the WebDriver with headless options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless=new')  # Use the new headless mode
chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36')

# Initialize the WebDriver
service = Service()
driver = webdriver.Chrome(service=service,options=chrome_options)



data=pd.read_excel(input("Enter the excel sheet file path:"))


today_column_name = f"No of problems solved as on {date.today()}"

for index, row in data.iterrows():
    if pd.notna(row['LEETCODE USER ID']):
        value=function.findcount(row['LEETCODE USER ID'],driver)
        print(value)
        if value!=None:
            data.at[index,today_column_name] = int(value)
        else:
            data.at[index,today_column_name] = "Value not found"
    else:
        data.at[index,today_column_name] = "URL not entered"

print(data)
data.to_excel("sample.xlsx",index=False)




