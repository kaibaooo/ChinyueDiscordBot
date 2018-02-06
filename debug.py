import requests
from bs4 import BeautifulSoup

player = "Eeec"
location = "as"
url = "https://pubg.op.gg/user/" + player + "?server=" + location
page = requests.get(url)
pubg_soup = BeautifulSoup(page.text, 'html.parser')
with open("page_data.txt", "w", encoding='UTF-8') as htmlfile:
	htmlfile.write(pubg_soup.prettify())
pubg_data = pubg_soup.find_all('div', 'recent-matches__stat-value')
data = []
for ele in pubg_data:
    data.append(ele.text)
pubg_time = pubg_soup.findAll('div',{'data-survive-time': True})
time = None
for ele in pubg_time:
    time = ele['data-survive-time']
    if time is not None:
        break
print(data)
print(time)
msg = "{PLAYER}在最近20場遊戲 平均擊殺:{KD} 平均傷害:{DAM} 平均存活時間:{MIN} :".format(PLAYER = player,KD = data[0], DAM = data[1], MIN = int(float(time)/60))

if float(time)%60<10:
	timef = "0" + str(int(float(time))%60)
else:
	timef = int(float(time))%60
    #print(msg,int(float(time))%60)
print(msg,timef)