# Web-Scraper-Python  BASIC/ ADVANCED/ PRO/ MASTER
In this repository we will explore how to extracts sizable amounts of data from websites
*Python required

# 1. Basic
- libraries: pip install requests, pip install beautifulsoup4
- test with: https://www.hackthissite.org


# 2. Advanced
- The program has been designed to be tested on a Wordpress Blog.
- Data is saved in a .txt file. (new function)
- Data collected: titles, authors, published_dates and paragraphs
- Paragrahps (new function)
- Don't forget to modify the file according to the page you choose:
- titles = soup.find_all('h2', class_='entry-title')
- authors = soup.find_all('span', class_='author vcard')
- published_dates = soup.find_all('span', class_='published')
- paragraphs_text = get_paragraphs(post_div)
                              

# 3. Pro 
- The project will continue in the future. POST 30/06/24
- The reason is that another larger project is being prepared.

# 4. Master
- The project will continue in the future. POST 30/06/24
- The reason is that another larger project is being prepared.




# LICENSE:
This software is free to distribute, modify and use with the condition that credit is provided to the creator (@DonP1r3lly) and is not for commercial use.

# DISCLAIMER:
This program is used for educational and ethical purposes only. I take no responsibility for any damages caused from using this program. By downloading and using this software, you agree that you take full responsibility 
