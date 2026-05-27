import json


FAYL = "kinoteatr_baza.json"
def json_ochish():
    try:
        with open(FAYL) as f:
            return json.load(f)
    except:
        return {"filmlar_ro'yxati":{},"seanslar_va_zallar":{}, "sotilgan_chiptalar": []}
def xarid_dekoratori(funksiya):
    def wrapper(*args, **kwargs):
        natija = funksiya(*args,**kwargs)
        with open("kassa_jurnali.txt", "a") as f:
            f.write(f"Joy xatid qilindi \n")
        return natija
    return wrapper
