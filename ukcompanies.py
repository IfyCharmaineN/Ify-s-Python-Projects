'''
I created a web scraping program that collects data from a real webpage with an article that displays the highest grossing companies
in the UK.

This program should show you a database containing:
- Company name
- Ranks
- Industry
- Revenue, Profit and Assets
- Employees
- Headquaters 

You need to work with a virtual environment for python libraries.

- try python3 or python install virtualenv

Ensure all are installed: (e.g. pip install BeautifulSoup4)

- BeautifulSoup4 
- requests
- lxml
- pandas

'''
# Importing requests  
import requests 
from bs4 import BeautifulSoup #BeautifulSoup library imported for parsing and navigating HTML and XML files
import pandas as pd #Pandas library imported to manipulate data

#URL of UK Company article

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_Kingdom'

# Using a GET request to fecth data from the URL 
response = requests.get(url)

# Checking if the request was successful (i.e. status code 200)
if response.status_code == 200:
    # Parsing the HTML content of the page in text format
    soup = BeautifulSoup(response.text, 'html.parser')

    # Finding the relevant table on the page 
    table = soup.find('table')

     # Use pandas to read the HTML table into a DataFrame
    # df = pd.read_html(str(first_table))[0]
    df = pd.read_csv('ukcompanies.csv')
    # Display the DataFrame
    print(df)
else:
    print(f"Unable to retrieve the page. Status code: {response.status_code}") 

print('DataFrame has been saved to "ukcompanies.csv" ')

