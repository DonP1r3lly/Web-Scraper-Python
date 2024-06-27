# BASIC WEB SCRAPER
# June 2024
# GitHub (DonP1r3lly)

# test1: try execute the program and you will get a normal response
# test2: try execute with url: https://www.hackthissite.org/robots.tx   will fail with response.status_code
# test3: try execute with url: https://www.hackthissit.org  will fail with except

import requests
from bs4 import BeautifulSoup

try:
    
    url = 'https://www.hackthissite.org'
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        paragraphs = soup.find_all('p')

        for para in paragraphs:
            print(para.text)
    else:
        print(f"Error accessing the page: {response.status_code}")

except Exception as e:  
    print(f"An unexpected error occurred: {e}")