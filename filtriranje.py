import re
import csv


def izlusci_podatke_trap_in_spell():
    sez = []
    vzorec = re.compile(
        r"<b>(?P<ime>.+?)</b></a>\s*<br>\s*(?P<sifra>\d+)\s*</td>\s*<td>(?P<efekt>.+?)</td>",
        re.DOTALL
    )
    for t in range(9):
        if t <= 5:
            tip = "spell"
            podtip = ["normal", "continous", "equip", "field", "quick-play", "ritual"][t]
        else:
            tip = "trap"
            podtip = ["normal", "continous", "counter"][t - 6]

        with open(f"htmlji/{t + 1}.html", "r", encoding="utf-8") as dat:
            text = dat.read()
            for najdba in vzorec.finditer(text):
                if len(najdba.group("ime")) > 200:
                    continue
                slovar = {
                    "tip": podtip + " " + tip,
                    "ime": najdba.group("ime"),
                    "sifra": najdba.group("sifra"),
                    "efekt": najdba.group("efekt"),
                }
                sez.append(slovar)
    return sez


def spell_and_trap_to_csv(karte):
    with open("spell_trap.csv", "w", encoding="utf-8") as dat:
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
    vzorec = re.compile(
        r"<b>(?P<ime>.*?)</b></a>\s*?<br>(?P<sifra>\d+)\s*?</td>"
        r"\s*?<td>(?P<tipi>.+?)</td>"
        r"\s*?<td>(?P<tipi2>.*?)</td>"
        r"\s*?<td.*?>(?P<level>[A-Z-]*\d*)</td>"
        r"\s*?<td.*?>(?P<ATK>\d*?)</td>"
        r"\s*?<td.*?>(?P<DEF>\d*?)</td>"
        r"\s*?<td>(?P<efekt>.*?)</td>",
        re.DOTALL
    )

    vzorec2 = re.compile(
        r"<h1 class=\"title\" style=\"margin-top: 0\">YuGiOh (?P<atribut>[A-Z]+?) Monsters</h1>"
    )
    for t in range(10, 17):
        with open(f"htmlji/{t}.html", "r", encoding="utf-8") as dat:
            text = dat.read()
            for najdba in vzorec.finditer(text):
                if (len(najdba.group("ime")) > 200) or (not najdba.group("sifra").isnumeric()):
                    continue
            # nestandardno zapisani na spletni strani
                atribut = vzorec2.findall(text)[0]
                slovar = {
                    "atribut": atribut,
                    "ime": najdba.group("ime"),
                    "sifra": najdba.group("sifra"),
                    "efekt": najdba.group("efekt").replace("\n", " "),
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
