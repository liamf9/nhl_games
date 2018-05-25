#!/usr/bin/python
from bs4 import BeautifulSoup
import requests
import re

url = 'http://naturalstattrick.com'
watch = []

try:
	request = requests.get(url)
except requests.exceptions.RequestException as e:
	##print e
	print("Possible network error.  Is internet connection enabled?")
	exit(1)

soup = BeautifulSoup(request.text, "html.parser")

games = [g for g in soup.find_all(["div"], class_="boxscore") if 'Ducks' in g.text or 'Maple Leafs' in g.text]

if(len(games) > 0):
	for g in games:
		game = str(g)
		soup = BeautifulSoup(game,"html.parser")
		watch.append(soup)

	for w in watch:
		text = w.get_text().split('\n')
		for g in text[1:-1]:
			g = filter(lambda x: not re.match(r'^\n*$', x), g)
			print(g.split(u'\xa0\xa0\xa0')[0].rstrip())
	exit(0)
else:
	print("No Games.")
	exit(1)
