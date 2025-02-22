from proj.bot.parse.parse import ashan, lenta, pyatyorochka, metro, magnit, okei, semishagof, perekryostok, dixy


stores = [
    {
        "name": "Магнит",
        "func": magnit,
        "items": {
            "hleb": 53363,
            "moloko": 18061,
            "maslo": 17637,
            "krupa": 16533,
            "makarony": 44595,
            "aitsa": 4854,
            "sosiski": 4869,
            "syr": 4851,
            "myaso": 4857
        }
    },
    {
        "name": "Пятёрочка",
        "func": pyatyorochka,
        "items": {
            "hleb": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C10433/products?mode=delivery&limit=499&order_by=price_asc",
            "moloko": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C2444/products?mode=delivery&limit=499&order_by=price_asc",
            "maslo": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C2443/products?mode=delivery&limit=499&order_by=price_asc",
            "krupa": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C9813/products?mode=delivery&limit=499&order_by=price_asc",
            "makarony": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C9818/products?mode=delivery&limit=499&order_by=price_asc",
            "aitsa": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C2449/products?mode=delivery&limit=499&order_by=price_asc",
            "sosiski": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C9771/products?mode=delivery&limit=499&order_by=price_asc",
            "syr": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C9729/products?mode=delivery&limit=499&order_by=price_asc",
            "myaso": "https://5d.5ka.ru/api/catalog/v1/stores/Y232/categories/73C2421/products?mode=delivery&limit=499&order_by=price_asc"
        }
    },
    # {
    #     "name": "Семишагофф",
    #     "func": semishagof,
    #     "items": {
    #         "hleb" : "https://semishagoff.org/catalog/hlebobulochnye-ideliya/hleb-baton-lavash/",
    #         "moloko": "https://semishagoff.org/catalog/molochnaya-produkciya/moloko-slivki/",
    #         "maslo": "https://semishagoff.org/catalog/syr-maslo-yayca/slivochnoe-maslo-margarin/",
    #         "krupa": "https://semishagoff.org/catalog/bakaleya-1/krupy-i-makaronnye-izdeliya/?",
    #         "makarony": "https://semishagoff.org/catalog/bakaleya-1/krupy-i-makaronnye-izdeliya/?",
    #         "aitsa": "https://semishagoff.org/catalog/syr-maslo-yayca/yayca/",
    #         "sosiski": "https://semishagoff.org/catalog/myasnaya-gastronomiya/",
    #         "syr": "https://semishagoff.org/catalog/syr-maslo-yayca/syry/",
    #         "myaso": "https://semishagoff.org/catalog/myaso/"
    #     }
    # },
    {
        "name": "Ашан",
        "func": ashan,
        "items": {
            "hleb" : "hlebnaya-vypechka",
            "moloko": "moloko",
            "maslo": "maslo_slivochnoe",
            "krupa": "krupy_1",
            "makarony": "makaronnye_izdeliya",
            "aitsa": "yayco_kurinoe",
            "sosiski": "sosiski_sardelki_shpikachki",
            "syr": "tverdye_i_polutverdye",
            "myaso": "govyadina_telyatina_1"
        }
    },
    {
        "name": "Метро",
        "func": metro,
        "items": {
            "hleb" : "https://online.metro-cc.ru/category/hleb-vypechka-torty/hleb-lavash-lepeshki?order=price_asc",
            "moloko": "https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/moloko?order=price_asc",
            "maslo": "https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/slivochnoe-maslo-i-margarin?order=price_asc",
            "krupa": "https://online.metro-cc.ru/category/bakaleya/krupy-bobovye?order=price_asc",
            "makarony": "https://online.metro-cc.ru/category/bakaleya/makaronnye-izdeliya?order=price_asc",
            "aitsa": "https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/yayca?order=price_asc",
            "sosiski": "https://online.metro-cc.ru/category/myasnye/sosiski-sardelki-shpikachki?order=price_asc",
            "syr": "https://online.metro-cc.ru/category/molochnye-prodkuty-syry-i-yayca/syry/tverdye-i-vyderzhannye?order=price_asc",
            "myaso": "https://online.metro-cc.ru/category/myasnye/myaso/govyadina?order=price_asc"
        }
    },
    {
        "name": "Окей",
        "func": okei,
        "items": {
            "hleb" : "16596",
            "moloko": "16110",
            "maslo": "16113",
            "krupa": "15064",
            "makarony": "15065",
            "aitsa": "16104",
            "sosiski": "16556",
            "syr": "16114",
            "myaso": "69069"
        }
    },
   # {
   #     "name": "Перекрёсток",
   #     "func": perekryostok,
   #     "items": {
   #         "hleb" : "https://www.perekrestok.ru/cat/c/243/hleb?orderBy=price&orderDirection=asc",
   #         "moloko": "https://www.perekrestok.ru/cat/c/114/moloko?orderBy=price&orderDirection=asc",
   #         "maslo": "https://www.perekrestok.ru/cat/c/121/maslo?orderBy=price&orderDirection=asc",
   #         "krupa": "https://www.perekrestok.ru/cat/c/107/krupy?orderBy=price&orderDirection=asc",
   #         "makarony": "https://www.perekrestok.ru/cat/c/105/makarony?orderBy=price&orderDirection=asc",
   #         "aitsa": "https://www.perekrestok.ru/cat/c/123/ajca?orderBy=price&orderDirection=asc",
   #         "sosiski": "https://www.perekrestok.ru/cat/c/134/sosiski?orderBy=price&orderDirection=asc",
   #         "syr": "https://www.perekrestok.ru/cat/c/122/syr?orderBy=price&orderDirection=asc",
   #         "myaso": "https://www.perekrestok.ru/cat/c/142/govadina?orderBy=price&orderDirection=asc"
   #        }
   # },
    {
        "name": "Лента",
        "func": lenta,
        "items": {
            "hleb" : 807,
            "moloko": 128,
            "maslo": 438,
            "krupa": 27,
            "makarony": 31,
            "aitsa": 135,
            "sosiski": 777,
            "syr": 2975,
            "myaso": 418
        }
    },
    {
        "name": "Дикси",
        "func": dixy,
        "items": {
            "hleb" : "765",
            "moloko": "11",
            "maslo": "118",
            "krupa": "115",
            "makarony": "114",
            "aitsa": "18",
            "sosiski": "59",
            "syr": "30",
            "myaso": "47"
        }
    }
]