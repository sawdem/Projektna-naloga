import re
import csv


def izlusci_podatke_trap_in_spell():
    sez = []
    vzorec = re.compile(
        r"<b>(?P<ime>.+?)</b></a>\s*<br>\s*(?P<sifra>\d+)\s*</td>\s*<td>(?P<efekt>.+?)</td>",
        re.DOTALL
    )
    for t in range(1, 7):
        if t <= 6:
            tip = "spell"
            if t == 1:
                podtip = "normal"
            elif t == 2:
                podtip = "continuous"
            elif t == 3:
                podtip = "equip"
            elif t == 4:
                podtip = "field"
            elif t == 5:
                podtip = "quick-play"
            elif t == 6:
                podtip = "ritual"
        else:
            tip = "trap"
            if t == 7:
                podtip = "normal"
            elif t == 8:
                podtip = "continuous"
            elif t == 9:
                podtip = "counter"

        with open(f"{t}.html", "r", encoding="utf-8") as dat:
            text = dat.read()
            for najdba in vzorec.finditer(text):
                slovar = {
                    "tip": podtip + " " + tip,
                    "ime": najdba.group("ime"),
                    "sifra": najdba.group("sifra"),
                    "efekt": najdba.group("efekt"),
                }
                sez.append(slovar)
        return sez


def spell_and_trap_to_csv(karte):
    with open("karte.csv", "w") as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["sifra", "ime", "tip", "efekt"])
        for karta in karte:
            if karta["efekt"][0] == "\"":
                pisatelj.writerow([karta["sifra"], karta["ime"], karta["tip"],
                                   karta["efekt"][1:len(karta["efekt"]) - 1]])
            else:
                pisatelj.writerow([karta["sifra"], karta["ime"],
                                   karta["tip"], karta["efekt"]])


def izlusci_podatke_monster():
    sez = []
    vzorec = re.compile(r"<b>(?P<ime>.*?)</b></a>\s*?<br>(?P<sifra>\d+)\s*?</td>\s*?<td>(?P<tipi>.+?)</td>\s*?<td>(?P<tipi2>.*?)</td>\s*?<td.*?>(?P<level>[A-Z-]*\d*)</td>\s*?<td.*?>(?P<ATK>\d*?)</td>\s*?<td.*?>(?P<DEF>\d*?)</td>\s*?<td>(?P<efekt>.*?)</td>", re.DOTALL)
    vzorec2 = re.compile(r"<h1 class=\"title\" style=\"margin-top: 0\">YuGiOh (?P<atribut>[A-Z]+?) Monsters</h1>")
    for t in range(10, 17):
        with open(f"{t}.html", "r", encoding="utf-8") as dat:
            text = dat.read()
            for najdba in vzorec.finditer(text):
                if najdba.group("sifra") in ["73146473", "81759748", "40227329", "04271596", "12338068",
                                             "48948935", "30086349", "90884403", "53134520", "14212201",
                                             "17663375", "76184692", "26842483", "12652643", "62873545",
                                             "14506878", "31038159", "85800949", "64025981", "45500495",
                                             "12927849", "20474741", "84650463", "76902476", "17238333",
                                             "82670878"]:
# nestandardno zapisani na spletni strani
                    continue
                atribut = vzorec2.findall(text)[0]
                slovar = {
                    "atribut": atribut,
                    "ime": najdba.group("ime"),
                    "sifra": najdba.group("sifra"),
                    "efekt": najdba.group("efekt"),
                    "ATK": najdba.group("ATK"),
                    "DEF": najdba.group("DEF"),
                    "level": najdba.group("level"),
                }
                for element in najdba.group("tipi").split("/"):
                    tipi_niz = element + ","
                    tipi_niz += najdba.group("tipi2")
                    slovar["tipi"] = tipi_niz
                    ločitev = najdba.group("efekt").split("<br>")
                    if len(ločitev) == 2:
                        slovar["efekt"] = ločitev[1]
                        slovar["summon condition"] = ločitev[0]
                    else:
                        slovar["summon condition"] = ""
                sez.append(slovar)
    return sez

def monster_to_csv(karte):
    with open("monsters.csv", "w", encoding='utf-8') as dat:
        pisatelj = csv.writer(dat)
        pisatelj.writerow(["sifra", "ime", "tipi",   "efekt", "ATK", "DEF", "level", "atribut", "summon condition"])
        for karta in karte:
            if "Pendulum" not in karta["efekt"]:
                pisatelj.writerow([karta["sifra"], karta["ime"], karta["tipi"],
                                   karta["efekt"], karta["ATK"], karta["DEF"],
                                   karta["level"], karta["atribut"], karta["summon condition"]])
