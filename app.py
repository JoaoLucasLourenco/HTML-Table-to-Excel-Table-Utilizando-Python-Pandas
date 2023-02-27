from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import selenium
import openpyxl
from time import sleep
import pandas as pd


driver = webdriver.Firefox()
driver.get('https://www.nba.com/stats/players')
player = []
team = []
point = []
rank = '1 2 3 4 5'.split()
i=0
while i<=4:
      player.insert(i,driver.find_element(By.XPATH,'//*[@id="players_traditional"]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[2]/a').text)
      team.insert(i,driver.find_element(By.XPATH,'//*[@id="players_traditional"]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[2]/span').text)
      point.insert(i,driver.find_element(By.XPATH,'//*[@id="players_traditional"]/div[1]/div/table/tbody/tr['+str(i+1)+']/td[3]').text)
      i+=1
junta_dados={
      'Players':player,
      'Team':team,
      'Points':point
}
dados = pd.DataFrame(data = junta_dados,index=rank)
print(dados)
dados.to_excel('tabel.xlsx')
driver.quit()

