# Gets news article URL from user and saves text under article's title, as a txt file


import requests
from bs4 import BeautifulSoup

# test: url = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture?intcid=inline_amp"


def get_article(x):
	r = requests.get(x)
	soup = BeautifulSoup(r.text, "html.parser")
	article_content = []
	title = soup.title.string

	for line in soup.find_all("p"):
		if line.string is not None and line.string.lower() != "advertisement":
			article_content.append(line.string)  # adds article into list
	return article_content, title


def save_article(x, t):  # saves article under text with title
	file_name = "{}.txt".format(t)
	file = open(file_name, "a")
	file.write(t + '\n\n')
	for paragraph in x:
		file.write(paragraph + '\n \n')
	file.close()


url = input("What website do you want to save? ")
text, article_title = get_article(url)  # saves article content under 'text', title under 'article_title'
save_article(text, article_title)
