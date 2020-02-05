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
import csv # And csv files to store large amounts of info.
games = {
    "2r":["gold (Virtual)","silver (Virtual)","crystal (Virtual)"],
    "1r":["red (Virtual)","blue (Virtual)","yellow (Virtual)"],
#    "8":["sword","shield"],
    "7r2":["pikachu","eevee"],
    "7r":["ultra sun","ultra moon"],
    "7":["sun","moon"],
    "6r":["omega","alpha"],
    "6":["x","y"],
    "5r":["black 2","white 2"],
    "5":["black","white"],
    "4r":["heart","soul"],
    "4":["diamond","pearl","platinum"],
    "3r":["fire","leaf"],
    "3":["ruby","sapphire","emerald"],
    "2":["gold","silver","crystal"],
    "1":["red","blue","yellow"],
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

#genh=Tk()
#th=Label(genh,text="Which Gen 8 games do you own?")
#swox=IntVar()
#shix=IntVar()
#swob=Checkbutton(genh,variable=sunx,text="Pokémon Sword")
#shib=Checkbutton(genh,variable=moox,text="Pokémon Shield")
#nh=Label(genh,text="You can't have any Gen 8 games")
#qh=Button(genh,command=genh.destroy,text="Done")
#if swiv.get() == 1:
#    th.pack()
#    swob.pack()
#    shib.pack()
#else:
#    nh.pack()
#qh.pack()
#genh.mainloop()
genhave = []
if redx.get() == 1:
    genhave.append(["1","R"])
if blux.get() == 1:
    genhave.append(["1","B"])
if yelx.get() == 1:
    genhave.append(["1","Y"])
if redvc.get() == 1:
    genhave.append(["1r","R"])
if bluvc.get() == 1:
    genhave.append(["1r","B"])
if yelvc.get() == 1:
    genhave.append(["1r","Y"])
##
if golx.get() == 1:
    genhave.append(["2","G"])
if silx.get() == 1:
    genhave.append(["2","S"])
if cryx.get() == 1:
    genhave.append(["2","C"])
if golvc.get() == 1:
    genhave.append(["2","GV"])
if silvc.get() == 1:
    genhave.append(["2","SV"])
if cryvc.get() == 1:
    genhave.append(["2","CV"])
##
if rubx.get() == 1:
    genhave.append(["3","R"])
if sapx.get() == 1:
    genhave.append(["3","S"])
if emex.get() == 1:
    genhave.append(["3","E"])
#
if firx.get() == 1:
    genhave.append(["3r","FR"])
if leax.get() == 1:
    genhave.append(["3r","LG"])
##
if diax.get() == 1:
    genhave.append(["4","D"])
if peax.get() == 1:
    genhave.append(["4","P"])
if plax.get() == 1:
    genhave.append(["4","Pt"])
#
if heax.get() == 1:
    genhave.append(["4r","HG"])
if soux.get() == 1:
    genhave.append(["4r","SS"])
##
if blax.get() == 1:
    genhave.append(["5","B"])
if whix.get() == 1:
    genhave.append(["5","W"])
#
if blbx.get() == 1:
    genhave.append(["5r","B2"])
if whbx.get() == 1:
    genhave.append(["5r","W2"])
##
if xx.get() == 1:
    genhave.append(["6","X"])
if yx.get() == 1:
    genhave.append(["6","Y"])
#
if omex.get() == 1:
    genhave.append(["6r","OR"])
if alpx.get() == 1:
    genhave.append(["6r","AS"])
##
if sunx.get() == 1:
    genhave.append(["7","S"])
if moox.get() == 1:
    genhave.append(["7","M"])
#
if usux.get() == 1:
    genhave.append(["7r","US"])
if umox.get() == 1:
    genhave.append(["7r","UM"])
#
if pikx.get() == 1:
    genhave.append(["7r2","P"])
if eevx.get() == 1:
    genhave.append(["7r2","E"])
##
#if swox.get() == 1:
#    genhave.append(["8","Sw"])
#if shix.get() == 1:
#    genhave.append(["8","Sh"])

whichgen = Tk()
genvar = IntVar()
Label(whichgen,text="Up to which generation?").pack()
Radiobutton(whichgen,variable=genvar,text="Gen 1",value=0).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 2",value=1).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 3",value=2).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 4",value=3).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 5",value=4).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 6",value=5).pack()
Radiobutton(whichgen,variable=genvar,text="Gen 7",value=6).pack()
#Radiobutton(whichgen,variable=genvar,text="Gen 8",value=7).pack()
Button(whichgen,command=whichgen.destroy,text="Done").pack()
whichgen.mainloop()
genvar.set(genvar.get()+1) # This makes it the generation's actual number, for conveniance.

eventify = Tk()
eventlol = IntVar()
Label(eventify,text="Don't count...")
Radiobutton(eventify,variable=eventlol,text="Mythicals & legendaries",value=0).pack()
Radiobutton(eventify,variable=eventlol,text="Mythicals",value=1).pack()
Radiobutton(eventify,variable=eventlol,text="Event-only mythicals",value=2).pack()
eventify.mainloop()
#STILLL NOT DONEE
pokeup = []
pokenot = []
pokeval = []
for thing in genhave:
    with open(("game-specif\\"+thing[0]+".csv"),newline="") as f:
        for row in csv.reader(f):
            if thing[1] in row:
                pokeval.append(row[0])
with open("..\\pokemon.csv") as pk:
    for row in csv.reader(pk):
        if row[13] != "Gen":
            if int(row[13])<=genvar.get():
                pokeup.append(row[6])
with open("..\\myth.csv") as mythics:
    for row in csv.reader(mythics):
        if eventlol
pokeval = list(set(pokeval))
pokeup = list(set(pokeup))
pokeval.remove("PKMN")
pokehave=[value for value in list(set(list(set(pokenot)-set(pokeup))+pokeval)) if value in pokeup]
def buy(listy):
    if sorted(pokeup) == sorted(pokehave):
        if len(listy) == 1:
            return [True, "You need to buy Pokémon "+listy[0]]
        elif len(listy) == 0:
            return [True, "You don't need to buy any Pokémon games"]
        else:
            var = ""
            for yay in listy:
                var += yay
                var += "and Pokémon "
            var=var[:-12]
            return [True, "You need to buy Pokémon "+var]
    else:
        return [False,"this shouldn't display"]
for gener, gamm in games:
    if buy([])[0] == True:
        print("yup") # Placeholder
    for thing in genhave:
        if thing[0] == gener:
            
