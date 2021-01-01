#Apa Tod Mau Recode?
#Tinggal Pake aja ribet_-
import os,sys,time
from time import sleep

def load(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1./12)
os.system('clear')
sleep(1)
os.system("figlet -f small HomeTermux |lolcat")
banner = """
\033[90m==============================================
\033[1;91m Coded  \033[90m:\033[1;96mGabriel.S
\033[1;91m Youtube\033[90m:\033[1;96mGabriel id\033[90m/\033[1;96mGabrielChannel
\033[1;91m Github \033[90m:\033[1;96mhttps://github.com/menang22
\033[90m==============================================
"""
print (banner)
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mMengambil File Default Termux\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m]\033[1;96mLoading\033[90m............\033[1;97m")
sleep (2)
try:
      os.mkdir('/data/data/com.termux/files/home/.termux')
except:
      pass
print('\033[90m[\033[1;92m+\033[90m]\033[1;92mSuccess\033[1;97m')
sleep(2)
print('\n\033[90m[\033[1;91m!\033[90m] \033[1;96mMenambahkan Tombol Termux\033[1;97m')
sleep(1)
load("\033[90m[\033[1;92m•\033[90m]\033[1;96mLoading\033[90m............\033[1;97m")

key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
xmanz = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
xmanz.write(key)
xmanz.close()
sleep (2)
os.system('termux-reload-settings')
print ("\033[90m[\033[1;92m+\033[90m]\033[1;92m Success\033[1;97m")
sleep (2)
tod = input("\033[90mSubscribe To Channel Admin?\033[1;96m (y/t)\033[90m: \033[1;96m")
if tod == "y":
   print ("\033[90m[\033[1;91m!\033[90m]\033[1;96mWaiting\033[90m...\033[1;97m")
   sleep (2)
   os.system("xdg-open https://www.youtube.com/channel/UCbraGGLYSgD5Rsz29W3eorw")
   sleep (4)
   print ("\033[90m[\033[1;92m+\033[90m]\033[1;92m Thanks You Gan\033[90m:)\033[1;97m")
elif tod == "t":
     print ("\033[90m[\033[1;91m!\033[90m]\033[1;91mExit\033[1;97m")
     sleep (1)
     sys.exit()
