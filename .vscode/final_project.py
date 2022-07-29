import random as rnd

rehber = {}

def kisi_Ekle(isim,numara):
    global rehber

    if not isim in rehber.keys():
        rehber[isim] = numara 
        print('Yeni kişi eklendi.')
    else:
        print('Bu kişi mevcut.') 

def kisi_sil(isim):
    global rehber
    try:
        del rehber[isim]
        print('Kişi silindi.')
    except KeyError:
        print('Kişi bulunamadı.')

def random_kisi_sec():
    isim = rnd.choice(list(rehber.keys()))
    return (isim,rehber[isim])

kisi_Ekle('Bekir',1489)
kisi_Ekle('Melisa',300321)
kisi_Ekle('Bora',77)
kisi_Ekle('Yaren',3435)

print(rehber)
print(random_kisi_sec())
#print(kisi_sil('Yaren'))
