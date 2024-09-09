"""
                    ********MÜKEMMEL SAYI**********

num = int(input("Lütfen bir sayı giriniz:"))
toplam = 0
liste = list(range(1,num+1))
liste1=list()
for i in liste:
    if num % i == 0:
        liste1.append(i)

liste1.pop()
for x in liste1:
    toplam+=x
print(toplam)
if toplam == num:
    print("{} sayısı mükemmel sayıdır.".format(num))
else:
    print("{} sayısı mükemmel sayı değilidr.".format(num))

"""


"""
            ********ARMSTRONG SAYI********
            
num = list(input("Lütfen bir sayı giriniz:"))
toplam = 0
for i in num:
    i = int(i)
    result = i ** 4
    toplam+=result
string_num = ''.join(map(str,num))
int_num = int(string_num)
if toplam == int_num:
    print(toplam)
    print("sayı Armstrong sayıdır.")
else:
    print(toplam)
    print("sayı Armstrong değildir!")

"""
"""
    *****ÇARPIM TABLOSU******
    
liste1 = list(range(1,11))
liste2 = list(range(1,11))
for i in liste1:
    for j in liste2:
        print("{} x {} = {}".format(i,j,i*j))
    print("*****************")

"""
"""
        ******TOPLAM BULMA*****
        
toplam = 0
while True:

    num = int(input("Lütfen bir sayı giriniz:"))
    toplam += num
    press = input("Çıkmak istiyor musunuz?(E/H)")
    if press == "E":
        break
    else:
        continue

print("Toplam:",toplam)

"""

"""
    ********CONTINUE KULLANIMI*******
    
liste = list(range(1,100))

for i in liste:
    if i % 3 != 0:
        continue
    else:
        print(i)

"""

"""
        ********LİST COMPRESHENİON(KOŞULLU DURUM)*******
        
liste = [x for x in range(1,101) if x % 2 == 0]
print(liste)

"""

"""
        *********ASAL SAYI MI*********
        
def asal_mi(sayi):
    if sayi ==1:
        return False
    elif sayi ==2:
        return True
    else:
        for i in range(2,sayi):
            if sayi % i ==0:
                return False
            return True

while True:
    sayi = input("Sayı:")
    if sayi == "q":
        break
    else:
        sayi = int(sayi)
        if asal_mi(sayi):
            print("Sayı asaldır")
        else:
            print("Asal değildir.")


"""

"""
        ************GİRİLEN SAYININ OKUNUŞUNU YAZMA************
        
onlar = ["On", "Yirmi", "Otuz", "Kırk", "Elli", "Altmış", "Yetmiş", "Seksen", "Doksan"]
birler = ["", "Bir", "İki", "Üç", "Dört", "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]

def sayiOkuma(sayi):
    sayi_str = str(sayi)

    if len(sayi_str) != 2 or not sayi_str.isdigit():
        return "Lütfen iki basamaklı bir sayı giriniz."

    on_index = int(sayi_str[0]) - 1
    bir_index = int(sayi_str[1])

    on = onlar[on_index]
    bir = birler[bir_index]

    return f"Sayı: {on} {bir}"

num = int(input("Lütfen okunacak sayıyı giriniz: "))
print(sayiOkuma(num))

"""

"""
        ********KARIŞIK NESNE TABANLI PROGRAMLAMA ÖRNEKLERİ*******
        
class Dog():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def bilgileri_Göster(self):
        print("Bilgiler Gösteriliyor..\n")
        print("Name:{}\nAge:{}".format(self.name,self.age))
    def bark(self):
        print("Woof!")
dog1 =Dog("Puppy",4)
dog1.bilgileri_Göster()
dog1.bark()

class Student():
    def __init__(self,name,age,grade):
        self.name = name
        self.age = age
        self.grade = grade
    def bilgileri_Göster(self):
        print("Bilgiler Gösteriliyor..\n")
        print("Name:{}\nAge:{}\nGrade:{}".format(self.name,self.age,self.grade))
    def is_passing(self):
        if self.grade > 50:
            print("Geçer Not")
            return True
        else:
            print("Başarısız Not")
            return False

student1 = Student("Alp",24,51)
student2 = Student("Berrin",23,49)

student1.bilgileri_Göster()
student1.is_passing()

student2.bilgileri_Göster()
student2.is_passing()

class Book():
    def __init__(self,name,author,id):
        self.name = name
        self.author = author
        self.id = id

    def show_info(self):
        print(f"İsim:{self.name}\nYazar:{self.author}\nİd:{self.id}")

class Library():
    def __init__(self):
        self.books_list = []
    def add_book(self,book):
        print(f"{book.name} ekleniyor..")
        self.books_list.append(book)
    def remove_book(self,id):
        for book in self.books_list:
            if book.id == id:
                print(f"{book.name} kaldırılıyor")
                self.books_list.remove(book)
                return

        print("Veri tabanında böyle bir kitap yok")
    def show_list(self):
        if not self.books_list:
            print("Kütüphanede kitap yok")
        else:
            for book in self.books_list:
                print(book.show_info())


book1 = Book("Kürt Mantolu Madonna","Alperen",1)
book2 = Book("Maze Runner","Alex",2)


library = Library()
library.add_book(book1)
library.add_book(book2)
library.remove_book(2)

library.show_list()



import time as tm

class Computer():
    def __init__(self,ram = 8,screencard_list = ["NVDIA_RTX","AMD","NVDIA_GTX"],memory = 256,screeencard = "AMD"):
        self.ram = ram
        self.screencard_list = screencard_list
        self.memory = memory
        self.screencard = screeencard
    def __str__(self):
        return "*****Bilgisayar Bilgileri****\nRam Boyutu:{}\nHafıza Miktarı:{}\nEkran Kart:{}\n".format(self.ram,self.memory,self.screencard)
    def upgrade_ram(self,amount_ram):
        print("Ram yükseltiliyor...")
        tm.sleep(1)
        if self.ram != 32:
            self.ram += amount_ram
        else:
            print("Maksimum ram miktarına ulaşıldı!!!")
    def decrease_memory(self,amount_memory):
        print("Hafıza azaltılıyor...")
        tm.sleep(1)
        if self.memory != 128:
            self.memory-=amount_memory
        else:
            print("Minimum hafızaya ulaşıldı!!")
    def change_screencard(self):
        secim = input("Lütfen değiştirilicek kartı seçiniz:\n {}".format(self.screencard_list))
        if secim == self.screencard_list[0]:
            print("Ekran kartı değiştiriliyor...")
            tm.sleep(1)
            self.screencard = self.screencard_list[0]
        elif secim == self.screencard_list[1]:
            print("Ekran kartı değiştiriliyor...")
            tm.sleep(1)
            self.screencard = self.screencard_list[1]
        elif secim == self.screencard_list[2]:
            print("Ekran kartı değiştiriliyor...")
            tm.sleep(1)
            self.screencard = self.screencard_list[2]
        else:
            print("Lütfen uygun bir kart seçiniz!")

computer = Computer()
print("Dükkana hoş geldin dayım yapacağın işlemi seç bakalım:\n")
while True:
    islem = int(input("1.Bilgisayar bilgilerini göster\n2.Ram ekle\n3.Hafıza düşür\n4.Ekran kartı değiştir.\n"))
    if islem == 1:
        print(computer)
    elif islem == 2:
        computer.upgrade_ram(8)
    elif islem == 3:
        computer.decrease_memory(64)
    elif islem == 4:
        computer.change_screencard()
    else:
        print("Yine beklerizz!")
        break
        

        
import math

class Shape:
    def __init__(self):
        self.area = 0
        self.perimeter = 0

    def calculate_area(self):
        pass

    def calculate_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self):
        super().__init__()
        self.radius = int(input("Dairenin yarıçapını giriniz:"))

    def calculate_area(self):
        self.area = math.pi * (self.radius ** 2)
        return self.area

    def calculate_perimeter(self):
        self.perimeter = 2 * math.pi * self.radius
        return self.perimeter

class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self.short_edge = int(input("Lütfen kısa kenarı giriniz:"))
        self.long_edge = int(input("Lütfen uzun kenarı giriniz:"))

    def calculate_area(self):
        self.area = self.short_edge * self.long_edge
        return self.area

    def calculate_perimeter(self):
        self.perimeter = 2 * (self.short_edge + self.long_edge)
        return self.perimeter

# Test
circle1 = Circle()
print(f"Dairenin Alanı: {circle1.calculate_area()}")
print(f"Dairenin Çevresi: {circle1.calculate_perimeter()}")

rectangle1 = Rectangle()
print(f"Dikdörtgenin Alanı: {rectangle1.calculate_area()}")
print(f"Dikdörtgenin Çevresi: {rectangle1.calculate_perimeter()}")


"""



"""
        *******KUMANDA SINIFI OLUŞTURMA*********

import random
import time

class Kumanda():
    def __init__(self,tv_durum = "Kapalı",tv_ses = 0,kanal_listesi=["Trt"],kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
    def sesi_azalt_artir(self):
        while True:
            karakter = input("Azaltmak için '<' Artırmak İçin '>' Çıkış için 'q' ya basın")

            if karakter == "<":
                if self.tv_ses != 0:
                    print("Ses azaltılıyor...")
                    time.sleep(1)
                    self.tv_ses -=1
                    print("Yeni Ses Düzeyi:{}".format(self.tv_ses))
                else:
                    print("Ses Düzeyiniz sıfır!")
            elif karakter == ">":
                if self.tv_ses != 31:
                    print("Ses arttırılıyor...")
                    time.sleep(1)
                    self.tv_ses +=1
                    print("Yeni Ses Düzeyi:{}".format(self.tv_ses))
                else:
                    print("Ses düzeyiniz full!!")

            else:
                print("Ses güncellendi")
                break
    def tv_kapat(self):
        print("Tv kapatılıyor...")
        time.sleep(1)
        self.tv_durum = "Kapalı"
    def tv_ac(self):
        print("Tv açılıyor...")
        time.sleep(1)
        self.tv_durum = "Açık"
    def __str__(self):
        return f"TV Durum:{self.tv_durum}\nSes Düzeyi:{self.tv_ses}\nKanal Listesi:{self.kanal_listesi}\nŞu anki kanal:{self.kanal}"
    def rastgele_kanal(self):
        rastgele_index = random.randint(0,len(self.kanal_listesi) -1)
        self.kanal = self.kanal_listesi[rastgele_index]
        print("Şu anki kanal:{}".format(self.kanal))
    def kanal_ekle(self,kanal):
        print(f"{kanal} ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal)
kumanda = Kumanda()
print("***TV Uygulaması***\n\nİşlemler:\n1.Tv aç\n2.Tv kapat\n3.Tv Bilgi Göster\n4.Kanal Ekle\n5.Rastgele kanal seç\n6.Ses Ayarı")
while True:
    islem = int(input("İşlemi seçiniz:"))
    if islem == 1:
        kumanda.tv_ac()
    elif islem == 2:
        kumanda.tv_kapat()
    elif islem == 3:
        print(kumanda)
    elif islem == 4:
        kanallar = input("Eklemek istediğiniz kanalları ',' ile ayırarak giriniz:")
        eklenecek_kanallar = kanallar.split(",")
        for i in eklenecek_kanallar:
            kumanda.kanal_ekle(i)
        time.sleep(1)
        print("Kanallar başarılı bir şekilde eklendi ")
    elif islem ==5:
        kumanda.rastgele_kanal()
    elif islem == 6:
        kumanda.sesi_azalt_artir()
    else:
        print("Geçersiz işlem")

"""

"""
    *********VERİLEN LİSTEDE SADECE SAYILARI EKRANA BASAN PROGRAM********
    
num_list = list(range(1, 10))
num_list_str = [str(i) for i in num_list]

try:
    liste = ["345", "sadas", "324a", "14", "kemal"]
    for a in liste:
        for b in a:
            if b in num_list_str:
                print(f"{b} Sayı")
except Exception as e:
    print(f"Hata: {e}")

"""



"""
 
        *********ASAL SAYI BULMA(2)********
        
prime_list = [2, 3]
start_index = 4

def bolen_bulma(num):
    liste1 = list(range(2, num))
    bolen_list = list()
    for i in liste1:
        if num % i == 0:
            bolen_list.append(i)
    return bolen_list

while len(prime_list) < 7:
    bolen = bolen_bulma(start_index)
    if not bolen:
        prime_list.append(start_index)
    start_index += 1

print(prime_list[:])

"""


"""
    *********MAP() FONKSİYONU ÖRNEK(DİKDÖRTGEN ALAN HESAPLAMA)**********

liste = [(3, 4), (10, 3), (5, 6), (1, 9)]
list1 = list()

for i in liste:
    i = list(i)
    list1.append(i)

def alan_hesapla(variable):
    a,b = variable
    return a * b


result = list(map(alan_hesapla,list1))
print(result)


#result = [a * b for a,b in list1]
#print(result)

"""

"""
        **********FİLTER() FONKSİYONU ÖRNEK(ÜÇGEN Mİ?)*********
        
demet = [(3,4,5),(6,8,10),(3,10,7)]
list1 = list()
for i in demet:
    i = list(i)
    list1.append(i)
#print(list1)
def is_triangle(liste):
    a,b,c = liste
    if abs(b-c) < a < b + c and abs(a-c) < b < a + c and abs(a-b) < c < a + b:
        return True
    else:
        return False
result = list(filter(is_triangle,list1))
print(result)

"""

"""
        ********REDUCE() FONKSİYONU ÖRNEK(ÇİFT SAYILARIN TOPLAMI)********
        
from functools import reduce

liste = [1,2,3,4,5,6,7,8,9,10]
cift_number = list(filter(lambda x : x % 2 ==0,liste))

def toplam(a,b):
    return a + b
result = reduce(toplam,cift_number)
print(result)

"""

"""

        *******ZİP() FONKSİYONU ÖRNEK(İSİM-SOYİSİM BİRLEŞTİRME)********
        
names = ["Kerim","Tarık","Ezgi","Kemal","İlkay","Şükran","Merve"]
surnames = ["Yılmaz","Öztürk","Dağdeviren","Atatürk","Dikmen","Kaya","Polat"]

for i,j in zip(names,surnames):
    print(i,j)

"""


"""
    *******İLK 10 SAYININ KARELERİNİN TOPLAMI - İLK 10 SAYININ TOPLAMININ KARESİ*******

num1 = list(range(1,11))

def find_total(num_list):
    total = 0
    for i in num_list:
        total +=i
    total = total ** 2
    return total
def find_total2(num_list):
    total = 0
    for j in num_list:
        j = j ** 2
        total += j
    return total
result = find_total(num1) - find_total2(num1)
print(result)

"""

"""
    *******VERİLEN LİSTEDE EN BÜYÜK İKİ DEĞERİ BULUP ÇIKARTMA********

from functools import reduce

num_list = ["73167176531330624919225119674426574742355349194934", "96983520312774506326239578318016984801869478851843"]
num = []
max_list = []

# Sayıları birleştirip tek listeye dönüştürme
for a in num_list:
    num.extend(list(a))

def find_max(x, y):
    return x if x > y else y

def find_and_remove(resulti, num1):
    while resulti in num1:
        print(f"{resulti} listeden kaldırılıyor..")
        num1.remove(resulti)
    return num1

# İlk en büyük sayıyı bulma ve çıkarma
result = str(reduce(find_max, num))
max_list.append(result)
num = find_and_remove(result, num)

# İkinci en büyük sayıyı bulma ve çıkarma
result2 = str(reduce(find_max, num))
max_list.append(result2)
num = find_and_remove(result2, num)

print("Max List:", max_list)
print("Remaining Num List:", num)

"""

"""

        *********DECORATOR FONKSİYONU ÖRNEK**********
        
def extra(func): #func = find_average
    def wrapper(numbers): #Decorator fonksiyonu  , numbers = [1,2,345,66,79,8]
        totalofevennumbers = 0 #çift sayıların toplamı
        numberofevennumbers = 0 #çift sayıların adedi
        totalofoddnumbers = 0 #tek sayıların toplamı
        numberofoddnumbers = 0 #tek sayıların adedi

        for num in numbers:
            if num % 2 == 0:
                totalofevennumbers += num
                numberofevennumbers +=1
            else:
                totalofoddnumbers += num
                numberofoddnumbers +=1

        print("Tek sayıların ortalaması: " , totalofoddnumbers / numberofoddnumbers)
        print("Çift sayıların ortalaması: " , totalofevennumbers / numberofevennumbers)

        func(numbers)  #find_average(numbers)
    return wrapper #decorator fonksiyonu bitti

@extra #decorator fonskiyonu çağrıldı
def find_average(numbers):
    total = 0
    for num in numbers:
        total+=num
    print("Ortalama :", total / len(numbers))

find_average([1,2,345,66,79,8]) #numbers = [1,2,345,66,79,8]

"""

"""
        *********DECORATOR FONKSİYON ÖRNEK(2)**********
        
prime_list = [2, 3]
start_index = 4
def is_perfect(func): #func = is_prime
    def wrapper(*args, **kwargs):  #args,kwargs = start_index
        number_list = func(*args, **kwargs) #number_list = prime_list
        for number in number_list:
            if number < 2:
                continue
            divider_list = [i for i in range(1, number) if number % i == 0]
            total = sum(divider_list) #divider_listteki elemanları toplar
            if total == number:
                print(f"{number} is a perfect number")
            else:
                print(f"{number} is not a perfect number")
        return number_list
    return wrapper

def find_divider(number):
    number_list = list(range(2, number))
    divider_list = []
    for i in number_list:
        if number % i == 0:
            divider_list.append(i)
    return divider_list

@is_perfect
def is_prime(start_index):
    global prime_list
    number_list = list(range(start_index, 101))
    for i in number_list:
        if not find_divider(i):
            prime_list.append(i)
    return prime_list

print(is_prime(start_index))

"""

"""

        ******BİR DİZİDE HANGİ ELEMANDAN KAÇ TANE VAR(FREKANS)******
        
def find_frequance(dizi):
    frequance = {}

    for eleman in dizi:
        if eleman in frequance:
            frequance[eleman] += 1
        else:
            frequance[eleman] = 1
    return frequance

liste = [1,1,1,2,3,3,4,4,4,4,4]
print(find_frequance(liste))


"""

"""

                    ***********ŞİFRE BULMA ALGORİTMASI(DECORATER KULLANILDI!)***********
                
alphabet_list = ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r", "s", "ş", "t", "u", "ü", "v", "y", "z"]
number_list = ["0","1","2","3","4","5","6","7","8","9"]
password = "alperen123"

def find_frequance(func): #func = find_passwrd
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs) #result, find_passwrd fonksiyonunun sonucunu döndürür(true_psswrd_list)
        frequance = {}
        for char in result:
            frequance[char] = frequance.get(char, 0) + 1 #karakter sözlükte yoksa değeri 0 atar ve + 1 ile 1(0 + 1) yapar.Eğer varsa değeri 1 arttırarak 1 yapar ve + 1 ile 2(1+1) atar
        return frequance
    return wrapper

@find_frequance
def find_passwrd():
    true_psswrd_list = []
    for char in alphabet_list:
        if char in password:
            true_psswrd_list.append(char)
    for number in number_list:
        if number in password:
            true_psswrd_list.append(number)
    return true_psswrd_list

print(find_passwrd())

"""


"""
        *********MATRİKS OLUŞTURMA**********
        
import random

matrix = []

for i in range(10):
    row = [] #Her satır için boş bir liste
    for j in range(10):
        rand_number = random.randint(0,9)
        row.append(rand_number) #her sütuna 0 ekleme
    matrix.append(row) #oluşturulan satırları matrixe ekleme
    
for row in matrix:
    #print(row[0])
    print(row)

"""

"""
             ***********BİR DİZİDEKİ EN KÜÇÜK VE EN BÜYÜK SAYIYI BULAN ALGORİTMA**********
                
from functools import reduce

def find_max(x, y):
    return x if x > y else y

def find_min(x, y):
    return x if x < y else y

user_list = input("Sayı Dizisi Giriniz (boşlukla ayırın): ").split()

int_user_list = [int(eleman) for eleman in user_list]

result_max = reduce(find_max, int_user_list)
result_min = reduce(find_min, int_user_list)

print("Dizideki en büyük sayı:", result_max)
print("Dizideki en küçük sayı:", result_min)

"""


"""

        ******VERİLEN METİNDE TEKRAR EDİLEN HARFLERİ BULMA*******
        
def find_againchar(liste):
    char_list = []
    for i in liste:
        if liste.count(i) > 1 and i not in char_list:
            char_list.append(i)
        else:
            pass
    print(f"Dizideki tekrar eden harfler:{char_list}")


user_list = list(input("Lütfen bir cümle giriniz:"))
find_againchar(user_list)

"""



"""

            *******BELİRLİ BİR LİSTEDE EN UZUN ZİNCİRİ HESAPLAMA*******

from functools import reduce
def func(num):
    sayac = 1
    while num > 1:
        if num % 2 != 0:
            sayac +=1
            num = (num * 3) + 1
        else:
            sayac+=1
            num = num / 2

    return sayac

def maks(x,y):
    if x > y:
        return x
    else:
        return y



chain_dict = {}
for number in range(1,101):
     result = func(number)
     chain_dict[number] = result

#print(chain_dict)
biggest_chain = reduce(maks,chain_dict.values())

target_value = biggest_chain

biggest_key = [key for key,value in chain_dict.items() if value == target_value]
print(biggest_key," = ",biggest_chain ,"adımda")

"""

"""

        *******BELİRLİ BİR LİSTEDE EN UZUN ZİNCİRİ HESAPLAMA(KISA HALİ)*******
            
def func(num):
    sayac = 1
    while num > 1:
        if num % 2 != 0:
            num = (num * 3) + 1
        else:
            num = num / 2
        sayac += 1
    return sayac

# 1'den 100'e kadar olan sayılar için adım sayısı hesaplaması
chain_dict = {number: func(number) for number in range(1, 101)}

# En uzun zinciri bulma
biggest_key = max(chain_dict, key=chain_dict.get)
biggest_chain = chain_dict[biggest_key]

print(biggest_key, "=", biggest_chain, "adımda")

"""



"""
        *******TXT DOSYASINI DÜZENLEME*********

# Dosya adını ve içeriğini ayarlayın
input_filename = "names.txt"
output_filename = "updatednames.txt"

# Dosyayı oku
with open(input_filename,"r") as file:
    data = file.read()

# Çift tırnakları ve ekstra boşlukları temizle
data = data.replace('"','').replace(' ','')

# Veriyi virgüllerle ayır
data = data.replace(',',',')


# Düzenlenmiş veriyi yeni bir dosyaya yaz
with open(output_filename,"w") as file:
    file.write(data)

print(f'Dosya "{output_filename}" olarak kaydedildi.')

"""


"""

            ********NAMESCORE HESAPLAYAN ALGORİTMA********
            
            
import string

alphabet =list(string.ascii_uppercase)
alphabet_dic = {}

num = 0
for i in alphabet:
    alphabet_dic[i] = num
    num+=1


with open("updatednames.txt","r",encoding="utf-8") as file:
    for i in file:
        voc_list = i.split(",")
    sorted_list = sorted(voc_list)

print(alphabet_dic)
print(sorted_list)



total = 0
for a in sorted_list:
    for b in a:
        value = alphabet_dic[b]
        total+=value
    print(f"{a} nın scoru {total}")
    total = 0

"""



"""

             ********NAMESCORE HESAPLAYAN ALGORİTMA(İLERİ SEVİYE)********
             
             
import string

# Alfabeyi ve sırasını oluştur
alphabet = list(string.ascii_uppercase)
alphabet_dic = {letter: index for index, letter in enumerate(alphabet)}

# Dosyayı oku ve isimleri listele
with open("updatednames.txt", "r", encoding="utf-8") as file:
    voc_list = file.read().strip().split(",")  # Tüm satırı oku ve virgüllerle ayır

# İsimleri alfabetik sıraya göre sırala
sorted_list = sorted(voc_list)

# Sıralanmış isimlerin ve skorlarının hesaplanması
for name in sorted_list:
    total = 0
    for char in name:
        if char in alphabet_dic:  # Harf dışı karakterler için kontrol ekle
            value = alphabet_dic[char]
            total += value
    print(f"{name} nın skoru {total}")

"""


"""
        
        ***********SADECE 2,3 VE 5 ASAL ÇARPANLARINA AİT SAYILAR(UGLY NUMBERS)***********
        
def has_only_2_3_5_prime_factors(n):
    # Sayıyı 2, 3 ve 5'e bölebileceğimiz kadar bölüyoruz.
    for p in [2, 3, 5]:
        while n % p == 0:
            n //= p
    # Eğer sonuç 1 ise, sayı sadece 2, 3 ve 5 çarpanlarına sahiptir.
    return n == 1

# 1'den 100'e kadar olan sayılar arasında sadece 2, 3 ve 5 asal çarpanlarına sahip olanları bulalım
result = [i for i in range(1, 101) if has_only_2_3_5_prime_factors(i)]

print(result)

"""





"""

            ********GİRİLEN STRİNG KELİMENİN BÜYÜK/KÜÇÜK KONTROLÜ********
            
            
import string

# Küçük ve büyük harflerin listelerini oluşturuyoruz
lower_alph = string.ascii_lowercase
upper_alph = string.ascii_uppercase


def all_upper(voc):
    
    #Kelimenin tamamının büyük harf olup olmadığını kontrol eder.
    
    if voc.isupper():
        print("The word is all upper case.")
        return True
    else:
        print("Wrong type!")
        return False

def first_upper(voc):

    #Kelimenin ilk harfinin büyük, diğerlerinin küçük olup olmadığını kontrol eder.
    
    if voc[0].isupper() and voc[1:].islower():
        print("The word starts with an upper case letter and the rest are lower case.")
        return True
    else:
        print("Wrong type!")
        return False


def all_lower(voc):
    
    #Kelimenin tamamının küçük harf olup olmadığını kontrol eder.
    
    if voc.islower():
        print("The word is all lower case.")
        return True
    else:
        print("Wrong type!")
        return False


while True:
    # Kullanıcıdan girdi alıyoruz ve uygun fonksiyonu çağırıyoruz
    user_input1 = input("Please enter a word in all capitals:")
    all_upper(user_input1)

    user_input2 = input("Please enter a word with the first letter in capitals:")
    first_upper(user_input2)

    user_input3 = input("Please enter a word in all lower case: ")
    all_lower(user_input3)


"""

"""
                    ********İNPUTA GÖRE LİSTEDE VERİ KOPYALAMA******

try:

    numberofcopy = int(input("Please tell me how many times the letter A should be copied:"))


    def copy_paste(number):

        copyoflist= ["A"]
        empty_list = []

        for i in range(numberofcopy):
            empty_list.insert(i,copyoflist[0])

        return empty_list


    print(copy_paste(numberofcopy))


except ValueError:
    print("Please enter a number!")


"""


"""
                        *********BİR TELEFON NUMARASININ HARF KOMBİNASYONLARI ALGORİTMA******
                        

import string

lower_alph = list(string.ascii_lowercase)

# 2'den 9'a kadar olan sayılar ve harfler arasındaki ilişkiyi tanımlayan bir sözlük oluşturuyoruz.
digit_to_letters = {}

i = 0
for number in range(2, 10):
    if number == 7 or number == 9:
        digit_to_letters[number] = lower_alph[i:(i + 4)]
        i += 4
    else:
        digit_to_letters[number] = lower_alph[i:(i + 3)]
        i += 3

# Kullanıcıdan giriş alınıyor
user_input = int(input("Please enter a number:"))

if user_input in range(2, 10):
    print(digit_to_letters[user_input])
elif 10 <= user_input < 100:  # 2 haneli sayı kontrolü
    onlar_basamagi = user_input // 10
    birler_basamagi = user_input % 10

    if onlar_basamagi in digit_to_letters and birler_basamagi in digit_to_letters:
        for x in digit_to_letters[onlar_basamagi]:
            for y in digit_to_letters[birler_basamagi]:
                print(x + y)  # Kombinasyonları birleştirerek yazdırıyoruz
    else:
        print("Invalid digits entered.")
else:
    print("Please enter a valid number between 2 and 99.")


"""



"""
                                    *********DÖNÜŞTÜRME SONRASI METNİN RAKAMLARINI TOPLAMA*********

import string

# Alfabenin küçük harflerini ve karşılık gelen sayılarını bir sözlükte tutuyoruz.
lower_alph = list(string.ascii_lowercase)
lower_alph_dict = {lower_alph[i]: i + 1 for i in range(len(lower_alph))}

# Kullanıcıdan giriş alıyoruz
user_input_text = input("Lütfen harf metni giriniz:").lower()  # Girdiği harfleri küçük harfe çeviriyoruz.
user_input_repeat = int(input("Lütfen dönüşüm miktarını giriniz:"))

# Harflerin karşılık gelen sayısal değerlerini birleştiriyoruz.
empty_string = "".join([str(lower_alph_dict[i]) for i in user_input_text if i in lower_alph_dict])

# Toplamı hesaplamak için tekrar döngüsü
total = 0
for _ in range(user_input_repeat):
    total = sum(int(i) for i in empty_string)  # Mevcut toplamı alıyoruz.
    empty_string = str(total)  # Toplamı string olarak tekrar atıyoruz.

# Sonucu ekrana basıyoruz
print(f"Sonuç: {total}")

"""



"""
            ********DİZİDE BULUNAN BAĞLANTILI LİSTEDEN DÜĞÜMLERİ SİL*******
            
            
def updateList(nums,head):
    temp_head = head.copy()
    for i in temp_head:
        if i in nums:
            head.remove(i)
    return head

nums = [5]
head = [1,2,3,4]

print(updateList(nums,head))

"""


"""
                    *******LINKED LIST IN BINARY TREE******

class ListNode(object): #head
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TreeNode(object): #root
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head ,root):

        def helper(list_node,tree_node):
            if not list_node:
                return True
            if not tree_node or list_node.val != tree_node.val:
                return False
            return (
                helper(list_node.next,tree_node.left) or
                helper(list_node.next,tree_node.right)
            )
        if helper(head,root):
            return True
        if not root:
            return False
        return (
            self.isSubPath(head,root.left) or
            self.isSubPath(head,root.right)
        )

"""































































































































































































































































































































































































































