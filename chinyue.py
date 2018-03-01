import discord
import requests
import datetime
import time
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
    pubg_rank = pubg_soup.findAll('div','recent-matches__avg-rank')
    for ele in pubg_rank:
        data.append(ele.text.replace(' ', '').replace('\n',''))
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
    msg = "平均擊殺:{KD}\n平均傷害:{DAM}\n平均排名:{RANK}\n存活時間:{MIN} : ".format(PLAYER = name, LOC=location.upper(),KD = data[0], DAM = data[1], RANK = data[3], MIN = int(float(time)/60))
    print(name)
    if float(time)%60<10:
        timef = "0" + str(int(float(time))%60)
    else:
        timef = str(int(float(time))%60)
    #
    #GET_AVATAR
    #
    avatar_url = "https://pubgtracker.com/profile/pc/" + name + "?region=agg"
    print("avatar_url:" + avatar_url)
    avatar_page = requests.get(avatar_url, stream = True)
    avatar_soup = BeautifulSoup(avatar_page.text, 'html.parser')
    #with open("page_data.html", "w", encoding='UTF-8') as htmlfile:
    #    htmlfile.write(avatar_soup.prettify())
    avatar_data = avatar_soup.find_all('meta', {'property':'og:image'})
    for ele in avatar_data:
        print(str(ele).split('"')[1].split('"')[0])
        pic = str(ele).split('"')[1].split('"')[0]
        print("pic:" + pic)
    
    embed = discord.Embed(title="PUBG OPGG", colour=discord.Colour(0xf8e71c), url="https://pubg.op.gg/user/" + name + "?server=" + location, timestamp=datetime.datetime.utcnow())
    embed.set_thumbnail(url=pic)
    embed.set_author(name=location + "的" + name, url="https://pubg.op.gg/user/" + name + "?server=" + location, icon_url=pic)
    embed.set_footer(icon_url=pic)
    embed.add_field(name="最近20場遊戲🤔", value="```ml\n" + msg + timef + "\n```")

    return embed
def getAvatar(id):
    avatar_url = "https://pubgtracker.com/profile/pc/" + name + "?region=agg"
    page = requests.get(url_solo, stream = True)
    avatar_soup = BeautifulSoup(page.text, 'html.parser')
    avatar_data = pubg_soup.find_all('meta', {'property':"og:image"})
    for ele in pubg_data:
        print(str(ele).split('"')[1].split('"')[0])
        pic = str(ele).split('"')[1].split('"')[0]
def pubgStock(item = 'crate'):
    goods = []
    price = []
    url = "http://steamcommunity.com/market/search?appid=578080&q=" + item
    data = requests.get(url)
    data_soup = BeautifulSoup(data.text, 'html.parser')
    data_name = data_soup.find_all('span', {'class':'market_listing_item_name'})
    if len(data_name) == 0:
        embed = discord.Embed(title="PUBG Steam看盤小工具", colour=discord.Colour(0xa9cde1), timestamp=datetime.datetime.utcnow())
        embed.set_footer(text="投資理財有賺有賠，投資前應詳閱公開說明書", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name='沒有這個東西喔',value='😏')
        return embed
    for ele in data_name:
        goods.append(ele.text)
        #print(ele.text)
    data_money = data_soup.find_all('span', {'class':'normal_price'})
    for i in range(0, len(data_money)):
        if i%2 == 1:
            #print(data_money[i].text)
            price.append(data_money[i].text)
    goods, price = zip(*sorted(zip(goods, price)))
    embed = discord.Embed(title="PUBG Steam看盤小工具", colour=discord.Colour(0xa9cde1), url="http://steamcommunity.com/market/search?appid=578080&q=crate", timestamp=datetime.datetime.utcnow())
    embed.set_footer(text="投資理財有賺有賠，投資前應詳閱公開說明書", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
    for i in range(0, len(data_name)):
        embed.add_field(name=goods[i], value=price[i], inline=True)
    return embed
