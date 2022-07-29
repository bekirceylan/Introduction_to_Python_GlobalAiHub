from inspect import ismemberdescriptor
import numbers
from operator import truediv
from traceback import print_tb
from urllib.request import HTTPPasswordMgrWithDefaultRealm


#ad = 'Bekir'
#soyad = "Ceylan"
#yas = 22

#karsilama = 'Hoşgeldin' + ' '+ad + ' ' + soyad + ' '+str(yas) + ' '+'yaşında!'
#print(ad + ' ' + soyad + ' '+ str(yas))
#print(karsilama)
#---------------------------------------------------------------------------------------
#tam_Isim = 'Bekir Ceylan'
#ilk_Karakter =tam_Isim[4]
#print(ilk_Karakter)

#aralik = tam_Isim[2::2]  #  / Devamı notlarda.
#print(aralik)
#---------------------------------------------------------------------------------------
#iyi = True
#kotu = False
#print(type(iyi)) #bool
#print(10 > 9)
#print(10 < 9)

#print(True or False)  #true
#print(True and True)  #true
#print(True and False) #false
#---------------------------------------------------------------------------------------
a = ['beko', 3, 4.5]
b = list()

print(a)
print(b)

futbolcular = ['beckham', 'zidane', 'ronaldo', 'abidal']
futbolcular[0]  = 'beko' #ilk indisin değerini beko yaptım. beckham yerine beko değeri dönüyor.
print(futbolcular[0:3]) # 0. indisten başlar ve 3. indise kadar devam eder fakat 3. indis değerini almaz.

skorlar = [10,20,30,40,50,60]
skorlar.append(70) # skorlar dizisinin sonuna 70 değerini ekler.
print(skorlar)

skorlar.insert(0,0) #insert komutuna ilk değer olarak indisi, ikinci değer olarak atanılacak değeri giriyoruz.
print(skorlar) #eklenen değer sonrası diğer indisler bir sonraki indise kayar.

baba = [55, 65, 75]
skorlar.extend(baba) #extend 
print(skorlar)

#pop

diller = ['almanca', 'ingilizce', 'fransızca', 'ispanyolca']
diller.pop()
print(diller)  # pop komutu sonuncu indisi silmeye yarar.

diller.remove('almanca')
print(diller)  # remove ile direkt kaldırmak istediğimiz veriyi silebiliriz.


sayilar = [1,4,6,2,3,5]
    #sayilar.sort()
    #print(sayilar)
sirali_Sayilar = sorted(sayilar)
print(sirali_Sayilar)

harfler = ['z','c','f','d','h','e','g']
harfler.sort()
harfler.reverse() #tersten verileri getirir.
print(harfler)
 