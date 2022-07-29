#Operators

#print(10 > 100) # False
#print(10 < 100) # True
#print(10 == 10) # True
#print(10 != 50) # True
#print(2 > 1 and 2 > 0) # True
#print(not True) # False
#print(not False) # True

#-----------------------------------------------------------------

#yas = int(input('Yaşınızı Giriniz = '))

#if yas >= 18 :
    #print('Banka hesabı açabilirsiniz')
#else:
    #print('Banka hesabı açamazsınız')

#-----------------------------------------------------------------

#sonuc = input('Sınav notunuzu girin: ')
#if (int(sonuc) > 90):
 #print('Aldığınız not A+, tebrikler!')

#elif (int(sonuc) > 80):
 #print('Aldığınız not A')
#else:
 #print('Aldığınız not B')

#-----------------------------------------------------------------

                # Kayitli Kullanici Adi ve Sifre Girisi
#id = "bekoleytee123"
#sifre = "bekir1489"
#kullanici_Adi = input("Lütfen kullanıcı adınızı giriniz : ")
#parola = input("Lütfen Parolanızı giriniz : ")
#if (kullanici_Adi != id and parola == sifre):
 #print("Kullanıcı adınız hatalı")
#elif (kullanici_Adi == id and parola != sifre):
 #print("Parolanız hatalı")
#elif (kullanici_Adi != id and parola != sifre):
 #print("Kullanıcı adınız ve parolanız hatalıdır.")
#else:
 #print("Tebrikler, Başarıyla giriş yaptınız")

#-----------------------------------------------------------------

#maas = int(input('Maaşınızı girin : '))

#if maas < 0:
    #print('Geçersiz maaş değeri girdiniz.')
#else:
 
 #if 0 < maas <= 1000:
    #maas = maas + maas*0.15
 #elif maas <= 2000:
    #maas = maas + maas*0.10
 #elif maas <= 3000:
    #maas = maas + maas*0.05
 #else:
    #maas = maas + maas*0.025

#print("Zamlı maaşınız = ", maas)

##-----------------------------------------------------------------

#for item in [1,2,3,4,5]: # Listeler üzerinde gezilebilir
 #print (int(item)) # Verilen listedeki tüm harflerin üzerin geçer

#for i in 'Bekir':
 #print(i)

#oyuncu = { 'ilk adi' : 'Bekir',
            #'soyadi' : 'Ceylan',
            #'rol' : 'Aı Engineer'}

#for b in oyuncu.values(): #values kullanmazsak anahtar değerler gelir, kullanırsak veriler gelir.
    #print(b) 


#for key, value in oyuncu.items():
    #print(key,value) #bu şekilde hem değer başlığını hem de değerleri verir.

#for i in range(10, 0,-1): #10 dan 0'a kadar 1'er geri 
 #print(i)

#---------------------------------------------------------------------------

#liste = [2,3,4,5,6,7,8]
#print(*range(7))

#for i, j in enumerate(liste):
    #print(f"index: {i} ..... Deger: {j}")

#while
#aclik = True
#mide = 10
#while aclik < 100:
    #print('Beni Besle')
    #mide += 10

#isimler = []
#notlar = []
#dersler = []
#durum = True
#while durum:
#    isim = str(input('İsminizi giriniz = '))
#    not1 = float(input('Notunuzu giriniz = '))
#    ders = str(input('Ders adini giriniz = '))

#    isimler.append(isim)
#    notlar.append(not1)
#    dersler.append(ders)
#
#    if len(isimler) > 3:
#        durum = False
#    
#    print(isimler)
#    print(notlar)
#    print(dersler)

