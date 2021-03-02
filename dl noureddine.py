from tkinter import *
from tkinter import messagebox
import time
import requests
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
from win10toast import ToastNotifier
root = Tk()
root.geometry("1080x1920")
bg="#8E8CD8"
root['bg']="#8E8CD8"







def launch():
    url=pr.get()
    num=deux.get()
    if url =="" or num =="":
        messagebox.showinfo(title="Nombre non valide", message="Veuillez saisir une valeur correcte")
    else:
        get_la_video(url,int(num))



options = Options()
options.add_argument('--headless')


site="https://11anim.com/opp-931-vostfr"
def get_la_video(site,nbr):
    for i in range(nbr):
        dri = webdriver.Firefox(options=options)
        dri.get(site)
        root.update_idletasks()
        dri.find_element_by_class_name("playButton").click()
        if len(dri.window_handles) == 2:
            dri.switch_to_window(dri.window_handles[1])
            dri.close()
            dri.switch_to_window(dri.window_handles[0])
        root.update_idletasks()
        time.sleep(5)
        soup=BeautifulSoup(dri.page_source,"html.parser")
        div=soup.findAll("iframe")[1]["src"]
        div="https:"+div
        ui="https://fr.savefrom.net/10-comment-t%C3%A9l%C3%A9charger-vid%C3%A9os-sur-dailymotion.html"
        dri.get(ui)
        time.sleep(3)
        root.update_idletasks()
        inpu=dri.find_element_by_tag_name("input")
        inpu.send_keys(div)
        inpu.submit()
        time.sleep(5)
        soup=BeautifulSoup(dri.page_source,"html.parser")
        a=dri.find_elements_by_tag_name("a")
        good_link=a[9].get_attribute("href")
        dri.quit()
        print(good_link)
        bn=site.split("-")
        bn=str(int(bn[-2])+1)
        mname=site.split("/")[-1].split("-")[0]
        dl(good_link,bn,mname)
        if nbr!=1:
            site=Next(site)

def Next(site):
    bn=site.split("-")
    bn[-2]=str(int(bn[-2])+1)
    site='-'.join(bn)
    return site

def dl(url,n,mname):
    chunk_size = 1024
    filename="Episode "+n+".mp4"
    r = requests.get(url, stream = True)

    ui = int(r.headers['content-length'])
    total_size=ui*0.00000095367432
    with open(filename, 'wb') as f:
        for data in r.iter_content(chunk_size = chunk_size):
            f.write(data)

    toaster = ToastNotifier()
    toaster.show_toast("Episode Téléchargé",
                    "L'épisode " +n +" de "+mname+"  est téléchagé",
                    icon_path=None,
                    duration=10)

pr=Entry(root,width="45")
pr.place(x=250,y=350)
Label(root,text="Url de téléchargement",bg=bg,font=('Helvetica', 20)).place(x=250,y=300)
deux=Entry(root,width="40")
deux.place(x=600,y=350)
Label(root,text="Nombre d'épisode",bg=bg,font=('Helvetica', 20)).place(x=600,y=300)
Button(root,text="Télécharger",bg=bg,font=('Helvetica', 13),command=launch).place(x=525,y=400)
root.focus_force()
# root.resizable(False,False)
root.title("Download 11anime")
root.mainloop()


