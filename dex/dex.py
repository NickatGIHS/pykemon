# ==============================
# | PYKEMON: COMPLETE THE 'DEX |
# ------------------------------
# |       by NickatGIHS        |
# ==============================

# Files are located (in relation to this):
#
# Unobtainable: unobt-dual.csv
# Game-specific: game-specif\\(#).csv
# Mythical/Event: ..\\myth.csv
# All Pokemon: ..\\pokemon.csv

from tkinter import * # This uses Tkinter to create popup windows

funob = open("unobt-dual.csv")
fmyth = open("..\\myth.csv")
fpoke = open("..\\pokemon.csv")
games = {
    "1":["red","blue","yellow"],
    "2":["gold","silver","crystal"],
    "3":["ruby","sapphire","emerald"],
    "3r":["fire","leaf"],
    "4":["diamond","pearl","platinum"],
    "4r":["heart","soul"],
    "5":["black","white"],
    "5r":["black2","white2"],
    "6":["x","y"],
    "6r":["omega","alpha"],
    "7":["sun","moon"],
    "7r":["ultrasun","ultramoon"],
    "7r2":["pikachu","eevee"]
    } # A dict of which games are in which csv files
consoles = {
    "1":["gb","gbc","gba","3ds"],
    "2":["gbc","gba","3ds"], # I know that Gold & Silver are playable on the gba but Crystal isn't, ok?
    "3":["gba","ds"],
    "3r":["gba","ds"],
    "4":["ds","dsi","3ds"],
    "4r":["ds","dsi","3ds"],
    "5":["ds","dsi","3ds"],
    "5r":["ds","dsi","3ds"],
    "6":["3ds"],
    "6r":["3ds"],
    "7":["3ds"],
    "7r":["3ds"],
    "7r2":["switch"]
    } # A dict of which consoles you can play games on

cons=Tk()
gbv =IntVar()
gbcv=IntVar()
gbav=IntVar()
dsv =IntVar()
dsiv=IntVar()
tdsv=IntVar()
swiv=IntVar()
titc=Label(cons,text="Which consoles do you own?")
gbb =Checkbutton(cons,variable=gbv,text="Gameboy")
gbcb=Checkbutton(cons,variable=gbcv,text="Gameboy Color")
gbab=Checkbutton(cons,variable=gbav,text="Gameboy Advance")
dsb =Checkbutton(cons,variable=dsv,text="DS")
dsib=Checkbutton(cons,variable=dsiv,text="DSi")
tdsb=Checkbutton(cons,variable=tdsv,text="3DS/New 3DS")
swib=Checkbutton(cons,variable=swiv,text="Switch")
cloc=Button(cons,command=cons.destroy,text="Quit")
titc.pack()
gbb.pack()
gbcb.pack()
gbab.pack()
dsb.pack()
dsib.pack()
tdsb.pack()
swib.pack()
cloc.pack()
cons.mainloop()
# Testing tk variable output
print(gbv.get())
print(gbcv.get())
print(gbav.get())
print(dsv.get())
print(dsiv.get())
print(tdsv.get())
print(swiv.get())
