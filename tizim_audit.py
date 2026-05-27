import json


FAYL = "kinoteatr_baza.json"
def json_ochish():
    try:
        with open(FAYL) as f:
            return json.load(f)
    except:
        return {"filmlar_ro'yxati":{},"seanslar_va_zallar":{}, "sotilgan_chiptalar": {}}
def xarid_dekoratori(funksiya):
    def wrapper(kino_nomi, kassa_tushumi):
        natija = funksiya(kino_nomi,kassa_tushumi)
        with open("kassa_jurnali.txt" "a") as f:
            f.write("")
        return natija
    return wrapper
