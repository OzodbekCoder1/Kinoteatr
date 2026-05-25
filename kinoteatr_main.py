import tizim_audit


def menyu_korsatish():
    print("1. Mavjud filmlar va seanslarni ko'rish")
    print("2. Seans dagi bo'sh joylarni ko'rish (Zal xaritasi)")
    print("3. Chipta sotib olish (Joy band qilish)")
    print("4. Yangi film qo'shish (Adminlar uchun)")
    print("5. Tizimdan chiqish")
    

def asosiy_dastur_sikli():
    while True:
        menyu_korsatish()
        tanlov = input("Tanlang: ")
        try:
            tanlov = int(tanlov)
            match tanlov:
                case 1:
                    kinolar = tizim_audit.json_ochish()
                    for kino, info in kinolar['filmlar_royxati'].items():
                        print(f"Nomi: {kino} \n Janr: {info['janr']} \n Yosh cheklovi: {info["yosh_cheklovi"]} \n Davomiyligi: {info['davomiyligi_daqiqa']}")
                case 2:
                    pass

        except:
            print("Faqat raqam kiriting")