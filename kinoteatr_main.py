from tizim_audit import json_ochish
from seanslar_boshqaruvi import yangi_film_qoshish
def menyu_korsatish():
    print("1. Mavjud filmlar va seanslarni ko'rish")
    print("2. Seans dagi bo'sh joylarni ko'rish (Zal xaritasi)")
    print("3. Chipta sotib olish (Joy band qilish)")
    print("4. Yangi film qo'shish (Adminlar uchun)")
    print("5. Tizimdan chiqish")
    
admin_parol = "admin2026"
def asosiy_dastur_sikli():
    while True:
        menyu_korsatish()
        tanlov = input("Tanlang: ")
        try:
            tanlov = int(tanlov)
            match tanlov:
                case 1:
                    kinolar = json_ochish()
                    for kino, info in kinolar['filmlar_royxati'].items():
                        print(f"Nomi: {kino} \n Janr: {info['janr']} \n Yosh cheklovi: {info['yosh_cheklovi']} \n Davomiyligi: {info['davomiyligi_daqiqa']}")
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    urunish = 3
                    while urunish > 0:
                        parol = input("Parolni kiriting: ")
                        if parol == admin_parol:
                            urunish = 3
                            kino_nomi = input("Kino nomini kiriting: ")
                            kino_janri = input("Kino janrni kititing: ")
                            kino_yosh_cheklovi = input("Yosh cheklovini kiriting: ")
                            kino_daqiqa = int(input("Davomiyligini kiriting (Daqiqda): "))
                            if kino_daqiqa < 0:
                                print("Daqiqa xato kiritildi")
                                break
                            if yangi_film_qoshish(kino_nomi,kino_janri, kino_yosh_cheklovi,kino_daqiqa):
                                print("Kino qoshildi")
                            else:
                                print("Kino malumoti xato kiritildi")
                            break
                        else:
                            urunish -= 1
                            print("Parol xato")
                        
                case 5:
                    print("Dastur toxtadi")
                    break
        except:
            print("Faqat raqam kiriting")