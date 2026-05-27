import json

def yangi_film_qoshish(nomi, janri, cheklov, daqida):
    try:
        with open("kinoteatr_baza.json", "r") as fayl:
            baza = json.load(fayl)
    except:
        baza = {"filmlar_ro_yxati": {}, "seanslar_va_zallar": {}, "sotilgan_chiptalar": []}

    ruxsat_etilganglar = frozenset({"0+", "6+", "12+", "16+", "18+"})
    if cheklov not in ruxsat_etilganglar:
        return False

    baza["filmlar_ro_yxati"][nomi] = {
        "janr": janri,
        "yosh_cheklovi": cheklov,
        "davomiyligi_daqiqa": daqida
    }
    
    yangi_seans = f"{nomi}"
    baza["seanslar_va_zallar"][yangi_seans] = {
        "vaqt_turi": "Kechki",
        "zal_xaritasi": [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ],
        "joy_turlari": {
            "1-qator": "Oddiy",
            "2-qator": "Oddiy",
            "3-qator": "VIP"
        }
    }

    with open("kinoteatr_baza.json", "w") as fayl:
        json.dump(baza, fayl, indent=2)
    return True