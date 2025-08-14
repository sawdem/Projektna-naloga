# Projektna naloga

Avtor: Gašper Počivavšek \
Leto: 2025 \
Fakulteta: Fakulteta za matematiko in fiziko \
Predmet: Uvod v programiranje 


## Uvod
V projektni nalogi sem iz [spletne strani](https://www.yugiohcardguide.com/) pobral podatke o različnih yugioh 
kartah in jih tudi vizualno predstavil. Karte imajo različne značilnosti, ki sem jih na različne načine primerjal 
med sabo.
<figure style="float: right "> 
<img src="https://assetsio.gnwcdn.com/yu-gi-oh-card-types-spell-monster-trap.png?width=1200&height=900&fit=crop&quality=100&format=png&enable=upscale&auto=webp" alt="slika kart" width="400 px" height="auto">
<figcaption align="center">Na sliki so po vrsti spell, monster in trap karta.</figcaption>
</figure>

## Navodila za uporabo
Za zagon programa je potrebno pognati le datoteko [main](main.py) katera nato kliče ustrezne funkcije definirane
v drugih datotekah ([filtriranje](filtriranje.py) in [pobiranje](pobiranje_podatkov.py)). V mapi htmlji se shrani
html koda strani iz katerih se podatki filtrirajo. V datoteki [monsters](monsters.csv) in [spell_trap](spell_trap.csv) 
se shranita tabeli z imeni, šiframi in ostalimi podatki o kartah. V datoteki [prikaz](prikaz.ipynb) so podatki iz tabel 
še vizualno prikazani. Za ogled vizualno predstavljenih rezultatov odprite [to datoteko](prikaz.ipynb).

## Viri
- [gradiva s predavanj](https://github.com/tilenmarc/uvod-v-programiranje)
- gradiva iz vaj
- [chat GPT](https://chatgpt.com/)(večkrat med 1.6.2025 in 10.9.2025)
- [stack overflow](https://stackoverflow.com/questions)(večkrat med 1.6.2025 in 10.9.2025)
- [https://www.yugiohcardguide.com/ ](https://www.yugiohcardguide.com/)(16.6.2025)
- [slika](https://www.google.com/imgres?q=yugioh%20card&imgurl=https%3A%2F%2Fassetsio.gnwcdn.com%2Fyu-gi-oh-card-types-spell-monster-trap.png%3Fwidth%3D1200%26height%3D900%26fit%3Dcrop%26quality%3D100%26format%3Dpng%26enable%3Dupscale%26auto%3Dwebp&imgrefurl=https%3A%2F%2Fwww.dicebreaker.com%2Fgames%2Fyu-gi-oh-tcg%2Fhow-to%2Fyu-gi-oh-card-types-explained&docid=cSa34zPT3zorLM&tbnid=VCdpFFHBXi0z3M&vet=12ahUKEwjm9Ze1k4uPAxVnJBAIHUhuJk0QM3oECBgQAA..i&w=1200&h=900&hcb=2&ved=2ahUKEwjm9Ze1k4uPAxVnJBAIHUhuJk0QM3oECBgQAA)