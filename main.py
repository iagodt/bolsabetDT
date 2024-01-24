import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from chatbot import enviarMensagem, formatarMensagem

from surebet import backtoback


chromeOptions = Options()
chromeOptions.add_argument("--window-size=1920x1080")
chromeOptions.add_argument("--headless")
clear = lambda: os.system('cls')


driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=chromeOptions)
driver.get("https://bolsadeaposta.com/exchange/inplay/1")

time.sleep(20)

iframe = driver.find_element(By.XPATH,'/html/body/main-app-root/app-root/ewl-main/app-ewl-integration/div/iframe')
driver.switch_to.frame(iframe)

script = '''
{
    var c = document.querySelectorAll('div[data-is-inplay="true"]')
    var returnObject = []
    
    c.forEach(element => {
        let teamsNames 
        element.querySelectorAll('.biab_market-title-team-names').forEach(name =>{
            teamsNames = name.childNodes
        })
        let gameuri = element.getAttribute('data-event-id')
        let Odds = element.querySelectorAll('.betContent')
        let team1 = teamsNames[0].outerText
        let x = 'x'
        let team2 = teamsNames[1].outerText
        let odd1 = Odds[0].outerText
        let empate = Odds[2].outerText
        let odd2 = Odds[4].outerText
        let output = {
            team1,odd1,
            x,empate,
            team2,odd2,
            gameuri
        }
        returnObject.push(output)
    });
        return returnObject;
    }
'''
while True:
    clear()

    print('coletando odds')
    try:
        inPlay = driver.execute_script(script)
    except:
        inPlay = []
    for i in inPlay:
        msgodds = ''
        odd1 = i['odd1'].partition('\n')[0]
        empate = i['empate'].partition('\n')[0]
        odd2 = i['odd2'].partition('\n')[0]
        partida =f"{i['team1']} {i['x']} {i['team2']}"
        url = f'https://bolsadeaposta.com/exchange/sport/1/event/{i['gameuri']}'
        msgodds+=backtoback([odd1,empate,odd2],'MoneyLine (BACK)')
        
        
        if msgodds != '':
            msgformat = []
            msgformat.append(f'Surebet Bolsa x Bolsa AO VIVO\n\n')
            msgformat.append(f'🟢Partida: {partida}\n\n')
            msgformat.append(msgodds)
            msgformat.append(f'\nlink do jogo ⬇️⬇️⬇️\n\n{url}\n')
            enviarMensagem(formatarMensagem(msgformat))

        
        
    
