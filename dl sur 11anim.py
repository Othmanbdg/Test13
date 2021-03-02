import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

options = Options()
options.add_argument('--headless')


site="https://11anim.com/opp-931-vostfr"
def get_la_video(site,nbr):
    for i in range(nbr):
        dri = webdriver.Firefox(options=options)
        dri.get(site)
        dri.find_element_by_class_name("playButton").click()
        if len(dri.window_handles) == 2:
            dri.switch_to_window(dri.window_handles[1])
            dri.close()
            dri.switch_to_window(dri.window_handles[0])
        time.sleep(5)
        soup=BeautifulSoup(dri.page_source,"html.parser")
        div=soup.findAll("iframe")[1]["src"]
        div="https:"+div
        ui="https://fr.savefrom.net/10-comment-t%C3%A9l%C3%A9charger-vid%C3%A9os-sur-dailymotion.html"
        dri.get(ui)
        time.sleep(3)
        inpu=dri.find_element_by_tag_name("input")
        inpu.send_keys(div)
        inpu.submit()
        time.sleep(5)
        soup=BeautifulSoup(dri.page_source,"html.parser")
        a=dri.find_elements_by_tag_name("a")
        good_link=a[9].get_attribute("href")
        dri.quit()
        print(good_link)
        if nbr!=1:
            site=Next(site)

def Next(site):
    bn=site.split("-")
    bn[-2]=str(int(bn[-2])+1)
    site='-'.join(bn)
    return site