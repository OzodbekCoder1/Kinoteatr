import json
from tizim_audit import xarid_dekoratori

def narx_belgilash(seans_vaqti, joy_turi):
    match seans_vaqti:
        case "Ertalabki":
            bazaviy = 30000.0
        case "Kunduzgi":
            bazaviy = 40000.0
        case "Kechki":
            bazaviy = 50000.0
        case _:
            bazaviy = 40000.0

    match joy_turi:
        case "VIP":
            ustama = 20000.0
        case _:
            ustama = 0.0

    return bazaviy + ustama

@xarid_dekoratori
def joy_band_qilish(film_nomi, qator, orindiq, *chipta_egasi):
    with open("kinoteatr_baza.json", "r") as fayl:
        baza = json.load(fayl)
    seans_kalit = film_nomi
    if seans_kalit not in baza["seanslar_va_zallar"]:
        return False

    seans = baza["seanslar_va_zallar"][seans_kalit]
    xarita = seans["zal_xaritasi"]

    try:
        if xarita[qator][orindiq] == 0:
            xarita[qator][orindiq] = 1
            ism = chipta_egasi[0] if len(chipta_egasi) > 0 else "Nomalum"
            
            joy_turi = seans["joy_turlari"].get(f"{qator + 1}-qator", "Oddiy")
            narx = narx_belgilash(seans["vaqt_turi"], joy_turi)
            
            yangi_chipta = {
                "chipta_id": len(baza["sotilgan_chiptalar"]) + 1,
                "film": film_nomi,
                "joy": {"qator": qator + 1, "o'rindiq": orindiq + 1},
                "sotilgan_narx": narx,
                "xaridor": ism
            }
            baza["sotilgan_chiptalar"].append(yangi_chipta)
            
            with open("kinoteatr_baza.json", "w") as f:
                json.dump(baza, f, indent=2)
            return True
        else:
            return False
    except:
        return False

def bosh_joylar_izlagich(film_nomi):
    with open("kinoteatr_baza.json", "r") as fayl:
        baza = json.load(fayl)
    if film_nomi in baza["seanslar_va_zallar"]:
        xarita = baza["seanslar_va_zallar"][film_nomi]["zal_xaritasi"]
        for q_ind, qator in enumerate(xarita):
            for o_ind, o_rindiq in enumerate(qator):
                if o_rindiq == 0:
                    yield (q_ind + 1, o_ind + 1)