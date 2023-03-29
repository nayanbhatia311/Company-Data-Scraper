from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pprint import pprint
from selenium.common.exceptions import NoSuchElementException
import time
import pandas as pd
from datetime import date
from selenium.webdriver.common.by import By

all_comp=[]

def company_data(company_name):
    comp={}
    driver = webdriver.Chrome()
    driver.get(f"https://www.google.com/search?q={company_name} moneycontrol")
    driver.find_element(By.CLASS_NAME, "iUh30").click() #click on the first google search result
    title=company_name
    registered_office=driver.find_element(By.XPATH,'//*[@id="company_info"]/ul/li[1]').text #registered office
    registras=driver.find_element(By.XPATH,'//*[@id="company_info"]/ul/li[2]').text # registras  
    nse=""
    date=""
    bse=""
    try:  
        nse=driver.find_element(By.ID,'nsespotval').get_attribute('value') #  nse
        date=driver.find_element(By.CLASS_NAME,'nseasondate').text
        bse=driver.find_element(By.ID,'bsespotval').get_attribute('value')
    except NoSuchElementException:
        print(f"{company_name} not found")
    finally:
        comp["company_name"]=company_name
        comp["title"]=title
        comp["registered_office"]=registered_office.split("\n")
        comp["registras"]=registras.split("\n")
        comp["nse"]=nse
        comp["date"]=date
        comp["bse"]=bse
        print(comp) 
        all_comp.append(comp)
        
        driver.close()

def read_file(path="company_name_set.txt"):
    
    f=open(path,"r")
    list_shares=f.readlines()
    list_shares=list(map(lambda x: x.strip('\n '),list_shares))
    print(list_shares)    
    return list_shares
    f.close()
shares=read_file()

for share in shares:
    try:
        company_data(share)
    except Exception as e:
        print(e)


# pprint(all_comp)
df=pd.DataFrame(all_comp)
df.to_csv(f"{date.today()}.csv")
