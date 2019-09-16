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
tdsb=Checkbutton(cons,variable=tdsv,text="3DS/2DS")
swib=Checkbutton(cons,variable=swiv,text="Switch")
cloc=Button(cons,command=cons.destroy,text="Done")
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

#gcon= IntVar()
#print(gcon.get())
#tcab=Label(gamed,text="Do you have the appropriate \nGameboy Link Cable(s)?")
#caby=Radiobutton(gamed, text="Yes", variable=gcon, value=1)
#cabn=Radiobutton(gamed, text="No", variable=gcon, value=0)

#if gbv.get() == 1 or gbcv.get() == 1 or gbav.get() == 1:
#    tcab.pack()
#    caby.pack()
#    cabn.pack()

gena=Tk()
ta=Label(gena,text="Which Gen 1 games do you own?")
redx=IntVar()
blux=IntVar()
yelx=IntVar()
redb=Checkbutton(gena,variable=redx,text="Pokémon Red")
blub=Checkbutton(gena,variable=blux,text="Pokémon Blue")
yelb=Checkbutton(gena,variable=yelx,text="Pokémon Yellow")
redvc=IntVar()
bluvc=IntVar()
yelvc=IntVar()
redvb=Checkbutton(gena,variable=redvc,text="Pokémon Red\n(Virtual Console)")
bluvb=Checkbutton(gena,variable=bluvc,text="Pokémon Blue\n(Virtual Console)")
yelvb=Checkbutton(gena,variable=yelvc,text="Pokémon Yellow\n(Virtual Console)")
na=Label(gena,text="You can't have any Gen 1 games")
qa=Button(gena,command=gena.destroy,text="Done")
if gbv.get() == 1 or gbcv.get() == 1 or tdsv.get() == 1:
    ta.pack()
    if gbv.get() == 1 or gbcv.get() == 1: #Gen 1
        redb.pack()
        blub.pack()
        yelb.pack()
    if tdsv.get() == 1: #Gen 1 VC
        redvb.pack()
        bluvb.pack()
        yelvb.pack()
else:
    na.pack()
qa.pack()
gena.mainloop()
genb=Tk()
tb=Label(genb, text="Which Gen 2 games do you own?")
golx=IntVar()
silx=IntVar()
cryx=IntVar()
golb=Checkbutton(genb,variable=golx,text="Pokémon Gold")
silb=Checkbutton(genb,variable=silx,text="Pokémon Silver")
cryb=Checkbutton(genb,variable=cryx,text="Pokémon Crystal")
golvc=IntVar()
silvc=IntVar()
cryvc=IntVar()
golvb=Checkbutton(genb,variable=golvc,text="Pokémon Gold\n(Virtual Console)")
silvb=Checkbutton(genb,variable=silvc,text="Pokémon Silver\n(Virtual Console)")
cryvb=Checkbutton(genb,variable=cryvc,text="Pokémon Crystal\n(Virtual Console)")
nb=Label(genb,text="You can't have any Gen 2 games")
qb=Button(genb,command=genb.destroy,text="Done")
if gbv.get() == 1 or gbcv.get() == 1 or tdsv.get() == 1:
    tb.pack()
    if gbv.get() == 1 or gbcv.get() == 1: #Gen 2
        golb.pack()
        silb.pack()
        cryb.pack()
    if tdsv.get() == 1: #Gen 2 VC
        golvb.pack()
        silvb.pack()
        cryvb.pack()
else:
    nb.pack()
qb.pack()
genb.mainloop()
genc=Tk()
tc=Label(genc, text="Which Gen 3 games do you own?")
rubx=IntVar()
sapx=IntVar()
emex=IntVar()
rubb=Checkbutton(genc,variable=rubx,text="Pokémon Ruby")
sapb=Checkbutton(genc,variable=sapx,text="Pokémon Sapphire")
emeb=Checkbutton(genc,variable=emex,text="Pokémon Emerald")
firx=IntVar()
leax=IntVar()
firb=Checkbutton(genc,variable=firx,text="Pokémon FireRed")
leab=Checkbutton(genc,variable=leax,text="Pokémon LeafGreen")
nc=Label(genc,text="You can't have any Gen 3 games")
qc=Button(genc,command=genc.destroy,text="Done")
if gbav.get() == 1 or dsv.get() == 1: #Gen 3
    tc.pack()
    rubb.pack()
    sapb.pack()
    emeb.pack()
    firb.pack()
    leab.pack()
else:
    nc.pack()
qc.pack()
genc.mainloop()
gend=Tk()
td=Label(gend, text="Which Gen 4 games do you own?")
diax=IntVar()
peax=IntVar()
plax=IntVar()
diab=Checkbutton(gend,variable=diax,text="Pokémon Diamond")
peab=Checkbutton(gend,variable=peax,text="Pokémon Pearl")
plab=Checkbutton(gend,variable=plax,text="Pokémon Platinum")
heax=IntVar()
soux=IntVar()
heab=Checkbutton(gend,variable=heax,text="Pokémon HeartGold")
soub=Checkbutton(gend,variable=soux,text="Pokémon SoulSilver")
nd=Label(gend,text="You can't have any Gen 4 games")
qd=Button(gend,command=gend.destroy,text="Done")
if dsv.get() == 1 or dsiv.get() == 1 or tdsv.get() == 1:
    td.pack()
    diab.pack()
    peab.pack()
    plab.pack()
    heab.pack()
    soub.pack()
else:
    nd.pack()
qd.pack()
gend.mainloop()
gene=Tk()
te=Label(gene,text="Which Gen 5 games do you own?")
blax=IntVar()
whix=IntVar()
blab=Checkbutton(gene,variable=blax,text="Pokémon Black")
whib=Checkbutton(gene,variable=whix,text="Pokémon White")
blbx=IntVar()
whbx=IntVar()
blbb=Checkbutton(gene,variable=blbx,text="Pokémon Black 2")
whbb=Checkbutton(gene,variable=whbx,text="Pokémon White 2")
ne=Label(gene,text="You can't have any Gen 5 games")
qe=Button(gene,command=gene.destroy,text="Done")
if dsv.get() == 1 or dsiv.get() == 1 or tdsv.get() == 1:
    te.pack()
    blab.pack()
    whib.pack()
    blbb.pack()
    whbb.pack()
else:
    ne.pack()
qe.pack()
gene.mainloop()
genf=Tk()
tf=Label(genf,text="Which Gen 6 games do you own?")
xx=IntVar()
yx=IntVar()
xb=Checkbutton(genf,variable=xx,text="Pokémon X")
yb=Checkbutton(genf,variable=yx,text="Pokémon Y")
omex=IntVar()
alpx=IntVar()
omeb=Checkbutton(genf,variable=omex,text="Pokémon Omega Ruby")
alpb=Checkbutton(genf,variable=alpx,text="Pokémon Alpha Sapphire")
nf=Label(genf,text="You can't have any Gen 6 games")
qf=Button(genf,command=genf.destroy,text="Done")
if tdsv.get() == 1:
    tf.pack()
    xb.pack()
    yb.pack()
    omeb.pack()
    alpb.pack()
else:
    nf.pack()
qf.pack()
genf.mainloop()
geng=Tk()
tg=Label(geng,text="Which Gen 7 games do you own?")
sunx=IntVar()
moox=IntVar()
sunb=Checkbutton(geng,variable=sunx,text="Pokémon Sun")
moob=Checkbutton(geng,variable=moox,text="Pokémon Moon")
usux=IntVar()
umox=IntVar()
usub=Checkbutton(geng,variable=usux,text="Pokémon Ultra Sun")
umob=Checkbutton(geng,variable=umox,text="Pokémon Ultra Moon")
pikx=IntVar()
eevx=IntVar()
pikb=Checkbutton(geng,variable=pikx,text="Let's Go Pikachu")
eevb=Checkbutton(geng,variable=eevx,text="Let's Go Eevee")
ng=Label(geng,text="You can't have any Gen 7 games")
qg=Button(geng,command=geng.destroy,text="Done")
if tdsv.get() == 1 or swiv.get() == 1:
    tg.pack()
    if tdsv.get() == 1:
        sunb.pack()
        moob.pack()
        usub.pack()
        umob.pack()
    if swiv.get() == 1:
        pikb.pack()
        eevb.pack()
else:
    ng.pack()
qg.pack()
geng.mainloop()
