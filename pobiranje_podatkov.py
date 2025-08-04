import requests
import time
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    # 'Accept-Encoding': 'gzip, deflate, br',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-User': '?1',
}


def pobiranje_podatkov():
    seznam_urljev = [
                    "https://www.yugiohcardguide.com/spells/normal-spells.html",
                    "https://www.yugiohcardguide.com/spells/continuous-spells.html",
                    "https://www.yugiohcardguide.com/spells/equip-spells.html",
                    "https://www.yugiohcardguide.com/spells/field-spells.html",
                    "https://www.yugiohcardguide.com/spells/quick-play-spells.html",
                    "https://www.yugiohcardguide.com/spells/ritual-spells.html",
                    "https://www.yugiohcardguide.com/traps/normal-traps.html",
                    "https://www.yugiohcardguide.com/traps/continuous-traps.html",
                    "https://www.yugiohcardguide.com/traps/counter-traps.html",
                    "https://www.yugiohcardguide.com/attribute/dark.html",
                    "https://www.yugiohcardguide.com/attribute/divine.html",
                    "https://www.yugiohcardguide.com/attribute/earth.html",
                    "https://www.yugiohcardguide.com/attribute/fire.html",
                    "https://www.yugiohcardguide.com/attribute/light.html",
                    "https://www.yugiohcardguide.com/attribute/water.html",
                    "https://www.yugiohcardguide.com/attribute/wind.html"
                    ]
    t = 0
    for url in seznam_urljev:
        t += 1
        zadnji_odziv = requests.get(url, headers=headers)
        if zadnji_odziv.status_code == 200:
            time.sleep(10)
            with open(os.path.join("htmlji", f"{t}.html"), "w", encoding='utf-8') as f:
                f.write(zadnji_odziv.text)
        else:
            print("napačna koda", zadnji_odziv.status_code)
            time.sleep(10)
