from bs4 import BeautifulSoup
import requests
import time

import random
import time
 
 
delay_choices = [1, 5, 7, 6, 3, 4.5]  #延遲的秒數
delay = random.choice(delay_choices)  #隨機選取秒數


def getsoup():
    url = 'https://www.zeczec.com/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    r = requests.get(url,headers=headers)
    sp = BeautifulSoup(r.text,'lxml')
    return sp

def getPagenum():
    sp = getsoup()
    pagenum = sp.select('.container > .container > .text-center.mb-16 > .button-group.mt-4 > .button.button-s')
    pagenum = int(pagenum[5].text)+1
    return pagenum

def getinfo(url_href):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}
    zec_data={}
    zec_data_list = []  
    r = requests.get(url_href,headers=headers)
    sp = BeautifulSoup(r.text, 'lxml')
    data = sp.find('div', class_='w-full px-4 lg:w-3/10')
    data_url = (sp.find(rel="canonical")["href"])
    zec_data["projects_url"]=data_url
    zec_data["projects"] = data.find(class_="block").text
    zec_data["proposer"] = (data.find(class_="flex items-center").a).text
    zec_data["spec"] = data.find(class_="text-sm text-neutral-600 my-4 leading-relaxed").text
    zec_data["current_account"] = data.find("div",class_="text-2xl font-bold js-sum-raised whitespace-nowrap leading-relaxed").text
    zec_data["proposer_amount"] = data.find("span",class_="js-backers-count").text
    zec_data["group_period"] = data.find(class_="mb-2 text-xs leading-relaxed").text.strip('\n時程')# .strip('  ')=>remove (optional):字符或一組字符，需要從字符串中刪除
    
    zec_data_list.append(zec_data)
    time.sleep(6)

    print(zec_data_list)

def getall(time_sleep):
    pagenum = getPagenum()
    sp = getsoup()
    datas = sp.select('.container > .container > .flex.gutter3-l > .w-full > .text-black > .block')
    # url_list = []
    for pagenum in range(1,pagenum):
        for i in datas:
            href = i.get('href')
            url_href = 'https://www.zeczec.com'+ str(href)
            getinfo(url_href)
            # time.sleep(delay)  #延遲
  
    print("結束")       



    


if __name__ == '__main__':
    getall(time_sleep=6)