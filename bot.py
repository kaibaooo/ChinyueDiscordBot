import discord
import asyncio
import requests
from bs4 import BeautifulSoup
from chinyue import gpuSearch, cpuSearch, pubgSearch, advance_pubg
client = discord.Client()
prefix = "%"
ninja = ['\👉\👈','\🙏','\🤲','\💪\💪','\🤟','\😏']

print('Scraping Data for usage...')
#Pre scraping
url_gpu = 'https://www.futuremark.com/hardware/gpu'
url_cpu = 'https://www.futuremark.com/hardware/cpu'
gpu_data = requests.get(url_gpu)
cpu_data = requests.get(url_cpu)
gpu_soup = BeautifulSoup(gpu_data.text, 'html.parser')
cpu_soup = BeautifulSoup(cpu_data.text, 'html.parser')
gpu_list = gpu_soup.find_all('a', 'productnameBold')
gpu_score = gpu_soup.find_all('span', 'barScore')
cpu_list = cpu_soup.find_all('a', 'productnameBold')
cpu_score = cpu_soup.find_all('span', 'barScore')
#print(len(gpu_list))
print('Scrape Completed')
print('Logging bot...')

@client.event
async def on_ready():
    print('------')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    
@client.event
#@commands.cooldown(1, 30, commands.BucketType.server)
async def on_message(message):
    #
    # Debugging Section
    #
    
    if message.content.startswith(prefix + 'test'):
        counter = 0
        tmp = await client.send_message(message.channel, '計算訊息量中...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, '你最近傳了 {} 則訊息'.format(counter))
    elif message.content.startswith(prefix + 'sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')
    elif message.content.startswith(prefix + 'gpu'):
        tmp = await client.send_message(message.channel, "\😤")
        for step in ninja:
            await client.edit_message(tmp, step)
        gpu = message.content.split(' ', 1)[1]
        msg_data = gpuSearch(gpu, gpu_list,gpu_score)
        counter = 0
        length = len(gpu_list)
        if msg_data is None:
            await client.send_message(message.channel, "找不到")
        else:
            for results in msg_data:
                msg = "{GPU}的分數為{SCORE} 是第{RANK}/{TOTAL}名的顯卡唷".format(GPU = gpu_list[results].text,SCORE = gpu_score[results * 2].text.replace(' ', ''),RANK=results+1,TOTAL = length)
                #msg = gpu_list[results].text + "的分數為" + gpu_score[results * 2].text.replace(' ', '') + " 是第" + results + "/" + str(length) + "名唷"
                #await client.send_message(message.channel, msg)
                await client.send_message(tmp, msg)
                counter += 1
                if counter >= 5:
                    await client.send_message(message.channel, "因為太多了 只幫你列出前五名唷")
                    break
    elif message.content.startswith(prefix + 'cpu'):
        tmp = await client.send_message(message.channel, "\😤")
        for step in ninja:
            await client.edit_message(tmp, step)
        cpu = message.content.split(' ', 1)[1]
        msg_data = gpuSearch(cpu, cpu_list, cpu_score)
        counter = 0
        length = len(cpu_list)
        if msg_data is None:
            await client.send_message(message.channel, "找不到")
        else:
            for results in msg_data:
                msg = "{CPU}的分數為{SCORE} 是第{RANK}/{TOTAL}名的處理器唷".format(CPU = cpu_list[results].text,SCORE = cpu_score[results * 2].text.replace(' ', ''),RANK=results+1,TOTAL = length)
                #msg = gpu_list[results].text + "的分數為" + gpu_score[results * 2].text.replace(' ', '') + " 是第" + results + "/" + str(length) + "名唷"
                #await client.send_message(message.channel, msg)
                await client.send_message(message.channel, msg)
                counter += 1
                if counter >= 5:
                    await client.send_message(message.channel, "因為太多了 只幫你列出前五名唷")
                    break
    elif message.content.startswith(prefix + 'pubg'):
        if message.content.count(' ') == 1:
            location = "as"
            player = message.content.split(' ', 1)[1]
        else:
            location = message.content.split(' ', 2)[1].lower()
            player = message.content.split(' ', 2)[2]
        id = pubgSearch(player, location)
        if id is not None:
            await client.send_message(message.channel, "```ml\n" + id + "```")
        else:
            await client.send_message(message.channel, "這應該是四級包喔=ˇ=")
    elif message.content.startswith(prefix + '地震'):
        await client.send_message(message.channel, "02/04 22:13	規模5.5	深度10.0	花蓮縣政府北偏東方 23.6 公里\🤟")
        #msg = '\nPlayer:林建鈞\nServer:NA\n在近20場遊戲中 平均擊殺:8.56 平均傷害:427 平均存活時間21:43\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\n'
        #ml = '```ml{MSG}```'.format(MSG=msg)
        #advance_pubg()
        #await client.send_message(message.channel, ml)
    elif message.content.startswith(prefix + 'debug'):
        #msg = '\nPlayer:林建鈞\nServer:NA\n在近20場遊戲中 平均擊殺:8.56 平均傷害:427 平均存活時間21:43\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\nSolo:#1234\n  KD:0.5\n  Avg. Damage:58\n'
        #ml = '```ml{MSG}```'.format(MSG=msg)
        advance_pubg()
        #await client.send_message(message.channel, ml)




client.run('BOT_TOKEN')
