import re

def promo_kod_tekshiruv(kod: str) -> bool:
    return bool(kod_tekshirish = re.search(r'^[A-Z]+_{1}[0-9]+$',kod))

def mijoz_yoshini_tekshir(yosh: int, film_cheklovi: str) -> bool:
    cheklov_son = int(film_cheklovi.replace("+", ""))
    return yosh >= cheklov_son

