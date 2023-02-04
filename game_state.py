import requests
import bs4
import json



url = 'https://www.game-state.com/91.134.254.233:7777/'

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}

result = requests.get(url, headers=headers)

c = result.content

soup = bs4.BeautifulSoup(c, "html.parser")

data = soup.find(id = 'players')


for players in data:
    players = players[:-3]

dictionary = [
	{
	  	"text": "Georgian Mobile RolePlay",
	  	"min": int(players),
	  	"ping":45
	}
	    ]

json_object = json.dumps(dictionary, indent=4)

with open("online.json", "w") as outfile:
    outfile.write(json_object)



