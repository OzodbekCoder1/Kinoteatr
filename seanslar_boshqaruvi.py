import json

def yangi_film_qoshish(nomi, janri, cheklov, daqida):
    try:
        with open("kinoteatr_baza.json", "r") as fayl:
            baza = json.load(fayl)
    except:
        baza = {"filmlar_royxati": {}, "seanslar_va_zallar": {}, "sotilgan_chiptalar": []}

    ruxsat_etilganglar = frozenset({"0+", "6+", "12+", "16+", "18+"})
    if cheklov not in ruxsat_etilganglar:
        return False

    baza["filmlar_royxati"][nomi] = {
        "janr": janri,
        "yosh_cheklovi": cheklov,
        "davomiyligi_daqiqa": daqida
    }
    vaqt_turlari = ["Ertalabki", "Kunduzgi", "Kechki"]
    vaqt = input("Vaqtini kiriting: ")
    if vaqt not in vaqt_turlari:
        return False
        
    yangi_seans = f"{nomi}"
    baza["seanslar_va_zallar"][yangi_seans] = {
        "vaqt_turi": vaqt,
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