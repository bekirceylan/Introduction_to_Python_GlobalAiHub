#Fonksiyonlar

#def isim_yazdir():
#    print('Bekir Ceylan') 

#print(type(isim_yazdir)) #function

#def beko(): # Burası fonksiyonu tanımladığımız yer
 #print('bekom ')
#beko() # Burada fonksiyonu çağırmak için çağırıyoruz
#beko()

#--------------------------------------------------------------------------------------------------------------------------------------

#faktoriyel
#def faktoriyel(x):
#    fakt = 1
#    if (x == 0 or x == 1):
#        print(f'Faktöriyel Değeri : {fakt}')
#    else:
#        while x > 1:
#            fakt = fakt * x
#            x -= 1
#    print(f'Faktöriyel Değeri : {fakt}')

#faktoriyel(5)

#--------------------------------------------------------------------------------------------------------------------------------------

#words = ["artificial","intelligence","machine","learning","python","programming"]
#import random as rnd
#from sqlite3 import adapters
#def randomWord(words):
# index = rnd.randint(0, len(words)-1)
# return words[index]

#len(words)
#word = randomWord(words)
#print(word)

#--------------------------------------------------------------------------------------------------------------------------------------

#metodlar
#ad = input("Lütfen adınızı giriniz: ")
#print(ad.upper())

#--------------------------------------------------------------------------------------------------------------------------------------

#try-except

while True:
    sayi1 = input('Birinci Sayıyı Giriniz = ')

    if sayi1 == 'q':
     break
    
    sayi2 = input('İkinci Sayıyı Giriniz =')

    try:
        sayi1_int = int(sayi1)
        sayi2_int = int(sayi2)

        print(sayi1_int/sayi2_int)
    except (ValueError, ZeroDivisionError):
        print('Hata Aldınız')
        print('Tekrar Deneyiniz')
