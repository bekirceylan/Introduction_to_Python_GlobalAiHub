import random
from sqlite3 import adapt

liste = {}

def kisi_Add(ad,no):
    global liste
    if not ad in liste.keys():
        liste[ad] = no
        print("Yeni kişi eklendi!")
    else: print("Zaten bu kişi ekli.")

def kisi_Del(ad):
    global liste
    try:
        del liste[ad]
        print("Kişi Silindi.")
    except KeyError:
        print("Böyle bir kişi bulunamadı.")

def isim_Update(ad,yeni_Ad):
    global liste
    if ad in liste.keys():
        if not yeni_Ad in liste.keys():
            liste[yeni_Ad] = liste[ad]
            del liste[ad]
            print("İsim Güncellendi!")
        else: print("Aynı isimde bir kullanıcı mevcut")
    else: print("Kişi Bulunamadı.")

def no_update(ad,yeni_no):
    global liste
    if ad in liste.keys():
        liste[ad] = yeni_no
        print("Numara Güncellendi.")
    else: print("Kişi Bulunamadı")

def rndm_kisi_sec():
    ad = random.choice(list(liste.keys()))
    return ad, liste[ad]

def goruntule():
    global liste
    if not len(liste) == 0:
        print("Liste:\n")
        i = 1
        for k,v in liste.items():
            print(f"{i})\n\tİsim: {k}\n\tNumara: {v}")
            i += 1
        return
    print("Rehber Boş")

def main():
    global liste
    menu = '''
     _________________________
     | 1: Kişi ekle          |
     | 2: Kişi Sil           |
     | 3: İsim Güncelle      |
     | 4: Numara Güncelle    |
     | 5: Rastgele Kişi Seç  |
     | 6: Kişileri Görüntüle |
     | q: Çıkış Yap          |
     _________________________
    '''
    print(menu)
    while True:
        secim = input("Lütfen Seçim Yapınız : ")
        print("*"*50+"\n")
        if secim == "1":
            ad = input("Yeni kişi ismi giriniz: ")
            no = input("Numarayı giriniz: ")
            kisi_Add(ad,no)
        elif secim == "2":
            ad = input("Silmek istediğiniz kişinin ismini giriniz: ")
            kisi_Del(ad)
        elif secim == "3":
            ad = input("Değiştirmek istediğiniz ismi giriniz: ")
            yeni_Ad = input("Yeni ismi giriniz: ")
            isim_Update(ad, yeni_Ad)
        elif secim == "4":
            ad = input("Numarasını değiştirmek istediğiniz kişinin ismini giriniz: ")
            yeni_no = input("Yeni numarayı giriniz: ")
            isim_Update(ad, yeni_no)
        elif secim == "5":
            ad, no = rndm_kisi_sec()
            print(f"\n\tİsim: {ad}\n\tNumara: {no}")
        elif secim == "6":
            goruntule()
        elif secim == "q":
            break
        else: print("Geçersiz seçim yaptınız. Lütfen tekrar deneyiniz.")
        print(menu)

main()
