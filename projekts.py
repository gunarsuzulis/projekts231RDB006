import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
marka=input("Ievadiet vēlamo marku: ")
if marka == "Mercedes":
    marka_2="Mercedes-Benz"
else:
    marka_2=marka
modelis = input("Ievadiet vēlamās markas mašīnas modeli: ")
izlaiduma_gads = str(input("Ievadiet vēlamās markas mašīnas izlaiduma gadu(no): "))
izlaiduma_gads_2 = str(input("Ievadiet vēlamās markas mašīnas izlaiduma gadu(līdz): "))

degvielas_tips = input("Ievadiet vēlamās markas mašīnas degvielas tipu: ")
if degvielas_tips=="Benzīns/gāze":
    degvielas_tips_2="Benzīns / gāze"
else:
    degvielas_tips_2=degvielas_tips
atrumkarbas_tips = input("Ievadiet vēlamās markas mašīnas ātrumkārbas tipu: ")
if atrumkarbas_tips =="Manuāla":
    atrumkarbas_tips_2="Mehāniskā"
elif atrumkarbas_tips =="Automāts":
    atrumkarbas_tips_2="Automātiskā"


virsbuves_tips = input("Ievadiet vēlamās markas mašīnas virsbūves tipu: ")
if virsbuves_tips=="Universāls":
    virsbuves_tips_2="Universalas"
elif virsbuves_tips=="Apvidus":
    virsbuves_tips_2="Visurgājējs / Krosovers"
elif virsbuves_tips=="Kupeja":
    virsbuves_tips_2="Kupeja (Coupe)"
elif virsbuves_tips=="Kabriolets":
    virsbuves_tips_2="Kabriolets / Roadster"
elif virsbuves_tips=="Pikaps":
    virsbuves_tips_2="Apvidus Pikaps"
elif virsbuves_tips=="Mikroautobuss":
    virsbuves_tips_2="Pasažieru mikroautobuss"
else:
    virsbuves_tips_2=virsbuves_tips

mainigais_1="1_"
mainigais_2="2_"
mainigais_3=mainigais_1+izlaiduma_gads
mainigais_4=mainigais_2+izlaiduma_gads_2

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)


url = "https://www.ss.com/"
driver.get(url)
# time.sleep(2)

find=driver.find_element(By.XPATH, "//button[contains(text(), 'Pieņemt un turpināt')]")
find.click()

find=driver.find_element(By.ID, "mtd_97")
find.click()
#time.sleep(1)


find = driver.find_element(By.LINK_TEXT, marka)
find.click()
#time.sleep(1)

year_form= driver.find_element(By.ID, "f_o_18_min")
select=Select(year_form)
select.select_by_visible_text(izlaiduma_gads)
#time.sleep(1)

year_to= driver.find_element(By.ID, "f_o_18_max")
select=Select(year_to)
select.select_by_visible_text(izlaiduma_gads_2)
#time.sleep(1)

# tilpums_from= driver.find_element(By.ID, "f_o_15_min")
# select=Select(tilpums_from)
# select.select_by_visible_text(c)
# time.sleep(1)

# tilpums_to= driver.find_element(By.ID, "f_o_15_max")
# select=Select(tilpums_to)
# select.select_by_visible_text(d)
# time.sleep(1)

dzinejs= driver.find_element(By.ID, "f_o_34")
select=Select(dzinejs)
select.select_by_visible_text(degvielas_tips)
#time.sleep(1)

atrumkarba= driver.find_element(By.ID, "f_o_35")
select=Select(atrumkarba)
select.select_by_visible_text(atrumkarbas_tips)
#time.sleep(1)

virsbuves= driver.find_element(By.ID, "f_o_32")
select=Select(virsbuves)
select.select_by_visible_text(virsbuves_tips)
#time.sleep(1)

modelis_1 = driver.find_element(By.XPATH, "//select[@class='filter_sel']")
select=Select(modelis_1)
select.select_by_visible_text(modelis)

input()
url_2="https://lv.m.autoplius.lt/"
driver.get(url_2)
time.sleep(2)

find=driver.find_element(By.ID, "onetrust-accept-btn-handler")
find.click()

find=driver.find_element(By.CLASS_NAME, "field-name")
find.click()
#time.sleep(1)

find=driver.find_element(By.XPATH, f"//a[@title='{marka_2}']")
find.click()
#time.sleep(1)

find=driver.find_element(By.XPATH, f"//a[@title='{modelis}']")
find.click()
#time.sleep(1)

find=driver.find_element(By.ID, "field_make_date_from")
find.click()
# time.sleep(1)

find=driver.find_element(By.XPATH, f"//a[@ID='{mainigais_3}']")
find.send_keys()
find.click()
# time.sleep(1)

find=driver.find_element(By.XPATH, f"//a[@ID='{mainigais_4}']")
find.send_keys()
find.click()


find=driver.find_element(By.XPATH, "//a[@title='Degvielas tips']")
find.click()
# #time.sleep(1)

find=driver.find_element(By.XPATH, f"//label[(text()='{degvielas_tips_2}')]")
find.click()
# #time.sleep(1)

find=driver.find_element(By.CLASS_NAME, "title")
find.click()
# #time.sleep(1)

find=driver.find_element(By.XPATH, "//a[@title='Ātrumkārbas tips']")
find.click()
# #time.sleep(1)

find=driver.find_element(By.XPATH, f"//a[(text()='{atrumkarbas_tips_2}')]")
find.click()
# #time.sleep(1)

find=driver.find_element(By.XPATH, "//a[@title='Virsbūves tips']")
find.click()
# #time.sleep(1)

find=driver.find_element(By.XPATH, f"//label[(text()='{virsbuves_tips_2}')]")
find.click()
# #time.sleep(1)

find=driver.find_element(By.CLASS_NAME, "title")
find.click()
# #time.sleep(1)

find=driver.find_element(By.CLASS_NAME, "group-search")
find.click()
# #time.sleep(1)

input()