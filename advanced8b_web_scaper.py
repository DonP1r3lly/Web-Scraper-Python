# ADVANCED WEB SCRAPER
# June 2024
# GitHub (DonP1r3lly)


# TESTED ON:  WORDPRESS Blog
# CONFIGURATION FOR THIS BLOG WAS: 
                                #titles = soup.find_all('h2', class_='entry-title')
                                #authors = soup.find_all('span', class_='author vcard')
                                #published_dates = soup.find_all('span', class_='published')
                                #paragraphs_text = get_paragraphs(post_div)


# if you want to know the configuration, go to the blog and click inspect with the browser

import requests
from bs4 import BeautifulSoup


def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            file.write(data)
    except Exception as e:
        print(f"Error writing to file: {e}")

def get_paragraphs(post):
    if post:
        paragraphs = post.find_all('p')
        paragraphs_text = "\n".join([para.text.strip() for para in paragraphs])
        return paragraphs_text
    return ""

try:
    url = input('Enter the URL: ')

    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        titles = soup.find_all('h2', class_='entry-title')
        authors = soup.find_all('span', class_='author vcard')
        published_dates = soup.find_all('span', class_='published')

        print("Titles found:")
        for title in titles:
            print(title.text.strip())

        print("\nAuthors found:")
        for author in authors:
            print(author.text.strip())

        print("\nPublished dates found:")
        for date in published_dates:
            print(date.text.strip())

        if len(titles) != len(authors) or len(titles) != len(published_dates):
            print("Mismatch between number of titles, authors, and published dates.")
        else:
            data = ""
            for i in range(len(titles)):
                post_div = titles[i].find_parent('div', class_='post')
                if post_div:
                    paragraphs_text = get_paragraphs(post_div)
                    data += f"Title: {titles[i].text.strip()}, Author: {authors[i].text.strip()}, Published: {published_dates[i].text.strip()}\n"
                    data += f"Paragraphs:\n{paragraphs_text}\n\n"

                    print(f"\nHTML around paragraph for post {i + 1}:\n")
                    for para in post_div.find_all('p'):
                        print(para.prettify())
                else:
                    data += f"Title: {titles[i].text.strip()}, Author: {authors[i].text.strip()}, Published: {published_dates[i].text.strip()}\n"
                    data += "Paragraphs: Not found\n\n"

            save_to_file(data, 'Blog_WordPress_data.txt')
            print("Data saved successfully.")
    else:
        print(f"Error accessing the page: {response.status_code}")

except Exception as e:  
    print(f"An unexpected error occurred: {e}")