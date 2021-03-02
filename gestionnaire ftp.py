import ftplib
import os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter.ttk as ttk
import os, winshell
from win32com.client import Dispatch
from tkinter import simpledialog
def short():
    name=""
    L=os.listdir()
    for ui in L:
        if "exe" in ui:
            name=ui
    namee=name.split(".")[0]
    desktop = winshell.desktop()
    path = os.path.join(desktop, namee+".lnk")
    if path not in L:
        target = os.getcwd()+"\\"+name
        wDir = os.getcwd()
        icon=target
        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(path)
        shortcut.Targetpath = target
        shortcut.WorkingDirectory = wDir
        shortcut.IconLocation = icon
        shortcut.save()
def conneect(event):
    connect()
screen=Tk()

screen.geometry("1920x1080")
screen.title("FTP Gestionnaire")
screen.bind('<Return>', conneect)

host=""
user=""
mdp=""
state="accueil"
screen['bg'] = '#b2bec3'
posx=[5,5,5,5,5,5,5,200,200,200,200,200,200,200,395,395,395,395,395,395,395,590,590,590,590,590,590,590,885,885,885,885,885,885,885,1080,1080,1080,1080,1080,1080,1080,1275,1275,1275,1275,1275,1275,1275,1470,1470,1470,1470,1470,1470,1470]
posy=[50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650,50,150,250,350,450,550,650]
L_Button=[]
dlt_lis=[]

ip_lab=Label(screen,text="IP du serveur : ",bg="#b2bec3",font=("Helvetica",20))
ip_lab.place(x=500,y=190)
L_Button.append(ip_lab)

ip_serv= Entry(screen, width=20)
ip_serv.place(x=690,y=200)
L_Button.append(ip_serv)

id_lab=Label(screen,text="Identifiant : ",bg="#b2bec3",font=("Helvetica",20))
id_lab.place(x=500,y=290)
L_Button.append(id_lab)

id_serv= Entry(screen, width=20)
id_serv.place(x=690,y=300)
L_Button.append(id_serv)

pass_lab=Label(screen,text="Mot de passe : ",bg="#b2bec3",font=("Helvetica",20))
pass_lab.place(x=500,y=390)
L_Button.append(pass_lab)

pass_serv=Entry(screen, width=20, show="*")
pass_serv.place(x=690,y=400)
L_Button.append(pass_serv)

def uploads():
    if state != "accueil":
        a = filedialog.askopenfilenames()
        if a !="":
            for ui in a:
                file=open(ui.replace("/",'\\'),"rb")
                name=ui.split("/")[-1]
                ftp.storbinary('STOR '+name,file)
                file.close()
        refresh()
def back():
    global ftp,liste,ccc,dlt_lis
    state=ftp.pwd()
    screen.title(state)
    if ccc==False:
        for ui in liste:
            ui.destroy()
        ftp.cwd("../")
        liste.clear()
        get_all_file()

    elif ccc == True:
        for ui in dlt_lis:
            if "PY_VAR" not in str(ui):
                ui.destroy()
        dlt_lis.clear()
        ccc=False
        get_all_file()


def connect():
    global host,user,mdp,ftp,backb,state
    tst=False
    host=ip_serv.get()
    user=id_serv.get()
    mdp=pass_serv.get()
    if host == "" or user == "" or mdp == "":
        messagebox.showerror(title="Imposible", message="Veullez remplir les champs vides")
    else:
        try:
            if ":" in host:
                port=int(ip_serv.get().split(':')[1])
                host=ip_serv.get().split(":")[0]
                ftp = ftplib.FTP()
                ftp.connect(host, port)
                ftp.login(user,mdp)
                tst=True
            else:
                ftp= ftplib.FTP(host,user,mdp)
                tst=True
        except Exception as e:

            tst = False
            messagebox.showerror(title=e, message=e)
        if tst == True:
            state="Connected"
            ftp.encoding = "utf-8"
            backb=Button(screen,text="<--",command=back,bg=screen['bg'])
            backb.place(x=0,y=0)
            print(host,user,mdp)
            a=ftp.nlst()
            print(a)
            for ui in L_Button:
                ui.destroy()
            L_Button.clear()
            get_all_file()
            print("connected")

pth=os.getcwd()
screen.iconbitmap(pth+'\\ftp icon.ico')
doss=PhotoImage(file=pth+"\\doss.PNG")
mp4=PhotoImage(file=pth+"\\mp4.PNG")
file=PhotoImage(file=pth+"\\file.PNG")
apk=PhotoImage(file=pth+"\\apk.PNG")
html=PhotoImage(file=pth+"\\html.PNG")
mp3=PhotoImage(file=pth+"\\mp3.PNG")
mp4=PhotoImage(file=pth+"\\mp4.PNG")
pdf=PhotoImage(file=pth+"\\pdf.PNG")
png=PhotoImage(file=pth+"\\png.PNG")
rar=PhotoImage(file=pth+"\\rar.PNG")
zip=PhotoImage(file=pth+"\\zip.PNG")
doc=PhotoImage(file=pth+"\\doc.PNG")
txt=PhotoImage(file=pth+"\\txt.PNG")
jpg=PhotoImage(file=pth+"\\jpg.PNG")
def get_all_file():
    global ftp,liste
    liste=[]
    secur=0
    ph=os.getcwd()
    if ftp.nlst()!=[]:
        for fl in ftp.nlst():
            img=file
            if "Ã" in fl:
                fl=fl.replace("Ã","É")
            if "." not in fl and "newfile" not in fl:
                img=doss
                gh=Button(screen,text=fl,image=img,compound=LEFT,bg="#b2bec3") #ttk.
                gh.place(x=posx[secur],y=posy[secur]+10)
                gh.configure(command=lambda btn=gh: click_on_folder(btn))
                liste.append(gh)
            else:
                if "mp4" in fl[-3:]:
                    img=mp4
                elif "apk" in fl[-3:]:
                    img=apk
                elif "html" in fl[-4:]:
                    img=html
                elif "mp3" in fl[-3:]:
                    img=mp3
                elif "pdf" in fl[-3:]:
                    img=pdf
                elif "png" in fl[-3:]:
                    img=png
                elif "rar" in fl[-3:]:
                    img=rar
                elif "zip" in fl[-3:]:
                    img=zip
                elif "txt" in fl[-3:]:
                    img=txt
                elif "jpg" in fl[-3:]:
                    img=jpg
                gh=Label(screen,text=fl,image=img,compound=LEFT,bg="#b2bec3")
                gh.place(x=posx[secur],y=posy[secur])
                liste.append(gh)
            secur+=1
    else:
        gh=Label(screen,text="Il n'y a rien ici..",bg=screen['bg'])
        gh.place(x=220,y=250)
        liste.append(gh)
def click_on_folder(btn):
    global ftp,liste,state
    nw=btn.cget('text')
    state=nw
    ftp.cwd(nw)
    state=ftp.pwd()
    screen.title(state)
    for ui in liste:
        ui.destroy()
    liste.clear()
    get_all_file()


ccc=False
def newdir():
    if state != "accueil":

        name = simpledialog.askstring(title="Newdir",prompt="What's the name of the folder:")
        if "." in name:
            messagebox.showerror(title="Imposible", message="Les points ne sont pas accepter.")
        elif name=="":
            messagebox.showerror(title="Imposible", message="Veuillez mettre un nom")
        else:
            ftp.mkd(name)
            refresh()
def select():
    global liste,ftp,dlt_lis,ccc,state,dlt,dl_butt
    if state != "accueil":

        ccc=True
        for ui in liste:
            ui.destroy()
        liste.clear()
        secur=0
        dlt_lis=[]
        for fl in ftp.nlst():
            img=file
            radioValue = StringVar()
            if "." not in fl and "newfile" not in fl:
                img=doss
                rd_butt=Checkbutton(screen, text=fl,variable=radioValue,image=img,onvalue="Y", offvalue="N",compound=LEFT,bg=screen['bg'])
                rd_butt.place(x=posx[secur],y=posy[secur])
                radioValue.set("N")
                dlt_lis.append(rd_butt)
                dlt_lis.append(radioValue)
            else:
                if "mp4" in fl[-3:]:
                    img=mp4
                elif "apk" in fl[-3:]:
                    img=apk
                elif "html" in fl[-4:]:
                    img=html
                elif "mp3" in fl[-3:]:
                    img=mp3
                elif "pdf" in fl[-3:]:
                    img=pdf
                elif "png" in fl[-3:]:
                    img=png
                elif "rar" in fl[-3:]:
                    img=rar
                elif "zip" in fl[-3:]:
                    img=zip
                elif "txt" in fl[-3:]:
                    img=txt
                elif "jpg" in fl[-3:]:
                    img=jpg
                rd_butt=Checkbutton(screen, text=fl,variable=radioValue,image=img,onvalue="Y", offvalue="N",compound="left",bg= screen['bg'])
                rd_butt.place(x=posx[secur],y=posy[secur])
                radioValue.set("N")
                dlt_lis.append(rd_butt)
                dlt_lis.append(radioValue)
            secur+=1
        dlt=Button(screen,text="Delete",command=dlt_butt,bg=screen['bg'])
        dlt.place(x=250,y=10)
        dlt_lis.append(dlt)
        dl_butt=Button(screen,text="Download",command=download,bg=screen['bg'])
        dl_butt.place(x=100,y=10)
        dlt_lis.append(dl_butt)
def download():
    global ftp
    if state != "acceuil":
        for i in range(0,len(dlt_lis),2):
            ui=dlt_lis[i]
            if ".!button" not in str(ui):
                if dlt_lis[i+1].get() == "Y":
                    if "." in ui.cget("text"):
                        try:
                            with open(ui.cget("text"),"wb") as f:
                                ftp.retrbinary("RETR " +ui.cget("text"),f.write)

                        except Exception as e:
                            messagebox.showerror(title=e, message=e)
    dl_butt.destroy()
    back()
def dlt_butt():
    global dlt_lis
    for i in range(0,len(dlt_lis),2):
        ui=dlt_lis[i]
        if ".!button" not in str(ui):
            if dlt_lis[i+1].get() == "Y":
                if "." in ui.cget("text") or "newfile" in ui.cget("text"):
                    try:
                        ftp.delete(ui.cget("text"))
                    except Exception as e:
                        messagebox.showerror(title=e, message=e)
                else:
                    try:
                        ftp.rmd(ui.cget("text"))
                    except Exception as e:
                        messagebox.showerror(title=e, message=e)
    dlt.destroy()
    back()
def refresh():
    if state!="acceuil":
        for ui in dlt_lis:
            if "PY_VAR" not in str(ui):
                ui.destroy()
        for ui in liste:
            ui.destroy()
        liste.clear()
        dlt_lis.clear()
        get_all_file()

def quit():
    global ftp,liste,backb,state,ip_serv,id_serv,pass_serv,dlt_lis
    state="accueil"
    ftp.close()
    for ui in liste:
        ui.destroy()
    liste.clear()
    for ui in dlt_lis:
        if "PY_VAR" not in str(ui):
            ui.destroy()
    dlt_lis.clear()
    ip_lab=Label(screen,text="IP du serveur : ",bg="#b2bec3",font=("Helvetica",20))
    ip_lab.place(x=500,y=190)
    L_Button.append(ip_lab)

    ip_serv= Entry(screen, width=20)
    ip_serv.place(x=690,y=200)
    L_Button.append(ip_serv)

    id_lab=Label(screen,text="Identifiant : ",bg="#b2bec3",font=("Helvetica",20))
    id_lab.place(x=500,y=290)
    L_Button.append(id_lab)

    id_serv= Entry(screen, width=20)
    id_serv.place(x=690,y=300)
    L_Button.append(id_serv)

    pass_lab=Label(screen,text="Mot de passe : ",bg="#b2bec3",font=("Helvetica",20))
    pass_lab.place(x=500,y=390)
    L_Button.append(pass_lab)

    pass_serv=Entry(screen, width=20, show="*")
    pass_serv.place(x=690,y=400)
    L_Button.append(pass_serv)

    submit=Button(screen,text="Connexion",command=connect)
    submit.place(x=650,y=500)
    L_Button.append(submit)
    backb.destroy()


submit=Button(screen,text="Connexion",command=connect,bg="#b2bec3")
submit.place(x=650,y=500)
L_Button.append(submit)
menubar=Menu(screen)
menuFile = Menu(menubar, tearoff=0)
menuFile.add_command(label="Import files",command=uploads)
menuFile.add_command(label="Select",command=select)
menuFile.add_command(label="New folder",command=newdir)
menuFile.add_command(label="Disconnect",command=quit)
menuFile.add_command(label="Refresh",command=refresh)
menuFile.add_command(label="Add a shortcut on desktop",command=short)
menubar.add_cascade(label="Gestion", menu=menuFile)
screen.config(menu=menubar)

screen.mainloop()
