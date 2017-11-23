import requests
from bs4 import BeautifulSoup


# import nytimes html document into python
url = "https://www.nytimes.com/"
r = requests.get(url)  # parses out the html of the website

soup = BeautifulSoup(r.text, 'html.parser')
headings = soup.find_all("h2", {"class": "story-heading"})

for heading in headings:
	if heading.find_all("a"):
		print(heading.a.text.strip())  # strip removes the whitespace around it if a 
	else:
		print(heading.text)
