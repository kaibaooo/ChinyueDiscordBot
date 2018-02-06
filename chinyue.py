import discord
import requests
from bs4 import BeautifulSoup

def gpuSearch(vga,gpu_list, gpu_score):
    count = 0
    index = []
    for row in gpu_list:
        if row.text.lower().find(vga.lower()) != -1:
            index.append(count)
            count += 1
        else:
            count += 1
    if len(index) > 0:
        for results in index:
            print(gpu_list[results].text, "的分數為", gpu_score[results * 2].text.replace(' ', ''))
            return index
    else:
        print("Not Found")
        return None
    del index[:]
def cpuSearch(cpu,cpu_list, cpu_score):
    count = 0
    index = []
    for row in cpu_list:
        if row.text.lower().find(cpu.lower()) != -1:
            index.append(count)
            count += 1
        else:
            count += 1
    if len(index) > 0:
        for results in index:
            print(cpu_list[results].text, "的分數為", cpu_score[results * 2].text.replace(' ', ''))
    else:
        print("Not Found")
        return None
    del index[:]
def pubgSearch(player, location = "as"):
    url = "https://pubg.op.gg/user/" + player + "?server=" + location
    page = requests.get(url)
    pubg_soup = BeautifulSoup(page.text, 'html.parser')
    pubg_data = pubg_soup.find_all('div', 'recent-matches__stat-value')
    data = []
    for ele in pubg_data:
        data.append(ele.text)
    pubg_time = pubg_soup.findAll('div',{'data-survive-time': True})
    pubg_name = pubg_soup.findAll('div',{'data-user_nickname': True})
    time = None
    for ele in pubg_name:
        name = ele['data-user_nickname']
        if name is not None:
            break
    for ele in pubg_time:
        time = ele['data-survive-time']
        if time is not None:
            break
    print(data)
    print(time)
    if len(data) == 0:
        return None
    msg = "Player:{PLAYER}\nServer:{LOC}\n在最近20場遊戲\n  平均擊殺:{KD}\n  平均傷害:{DAM}\n  平均存活時間:{MIN} : ".format(PLAYER = name, LOC=location.upper(),KD = data[0], DAM = data[1], MIN = int(float(time)/60))
    
    if float(time)%60<10:
        timef = "0" + str(int(float(time))%60)
    else:
        timef = str(int(float(time))%60)
        #print(msg,int(float(time))%60)
    return (msg + timef)
def advance_pubg(player = 'Eeec', location = 'as'):
    solo = []
    duo = []
    squad = []
    url = "https://pubg.op.gg/user/" + player + "?server=" + location
    page = requests.get(url)
    pubg_soup = BeautifulSoup(page.text, 'html.parser')
    solo_data = pubg_soup.findAll('div', {'class':'ranked-stats__rank'})
    print(pubg_soup)
    print(solo_data)
    for ele in solo_data:
        print(ele.text)