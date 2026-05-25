import re

def promo_kod_tekshiruv(kod: str) -> bool:
    return bool(kod_tekshirish = re.search(r'^[A-Z]+_{1}[0-9]+$',kod))

def mijoz_yoshini_tekshir(bemor_yoshi: int, film_cheklovi: str) -> bool:
    return bemor_yoshi >= film_cheklovi["yosh_cheklovi"]

