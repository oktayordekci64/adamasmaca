#encoding:utf-8
import time
import random
from os import system
system('clear')
print("----------- Adam Asmaca Oyunu ------------\n")
print("                    O  ")
print("                   /|\ ")
print("                   / \ ")
      
print("""
               KATEGORİLER

                1. Eşya
                2. Meslek
                3. Şehir

""")

seçim=input("Seçiminiz : ")
print("")
print("Kelimeniz Hazirlaniyor ...\n")
time.sleep(2)
esya_kelimeler=['ARABA','KALEM','DEFTER','MAKAS',]
meslek_kelimeler=['ŞOFÖR','DOKTOR','MANAV','BAKKAL']
şehir_kelimeler=['UŞAK','ORDU','ANKARA','TRABZON','HATAY']
hak=4
if (seçim=="1"):
    esya_değer=random.choice(esya_kelimeler)
    print("")
    print("Kelimemiz",len(esya_değer)," harften oluşan bir EŞYA !")
    print("\nKalan Hak = 4")
    görsel=[]
    for i in range(len(esya_değer)):
        görsel.append(" _")
    for i in görsel:
        print(i,end="")
    harfler=list(esya_değer)
    while (" _" in görsel):
        print("")
        harf=input("\nHarf Gir :")
        time.sleep(1)
        print("")
        new_harf=harf.upper()
        sira=[]
        for index,h in enumerate(harfler):
            if (h==new_harf):
                sira.append(index)
        
        if len(sira)==1:
            görsel[sira[0]]=new_harf
            for i in görsel:
                print(i,end="")
        elif len(sira)==2:
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            for i in görsel:
                print(i,end="")
        elif (len(sira)==3):
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            görsel[sira[2]]=new_harf
            for i in görsel:
                print(i,end="")
        else:
            hak-=1
            print("Kalan Hak : ",hak)
            if (hak==3):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                   /|\ ")

            elif(hak==2):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                    | ")
            elif(hak==1):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
            elif(hak==0):
                print("\nHakkiniz Kalmadi :(")
                print("\nCevap : ",esya_değer,"\n")
                break

if (seçim=="2"):
    meslek_değer=random.choice(meslek_kelimeler)
    print("")
    print("Kelimemiz",len(meslek_değer)," harften oluşan bir MESLEK !        (4 Hakkiniz Var) ")
    görsel=[]
    for i in range(len(meslek_değer)):
        görsel.append(" _")
    for i in görsel:
        print(i,end="")
    
    harfler=list(meslek_değer)
    while (" _" in görsel):
        print("")
        harf=input("\nHarf Gir :")
        time.sleep(1)
        print("")
        new_harf=harf.upper()
        sira=[]
        for index,h in enumerate(harfler):
            if (h==new_harf):
                sira.append(index)
        
        if len(sira)==1:
            görsel[sira[0]]=new_harf
            for i in görsel:
                print(i,end="")
        elif len(sira)==2:
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            for i in görsel:
                print(i,end="")
        elif (len(sira)==3):
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            görsel[sira[2]]=new_harf
            for i in görsel:
                print(i,end="")
        else:
            hak-=1
            print("Kalan Hak : ",hak)
            if (hak==3):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                   /|\ ")
            elif(hak==2):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                    | ")
            elif(hak==1):
                for i in görsel:
                    print(i,end="")
                print("\n")
                print("                    O  ")
            elif(hak==0):
                print("\nHakkiniz Kalmadi :(")
                print("\nCevap : ",meslek_değer,"\n")
                break
if (seçim=="3"):
    sehir_değer=random.choice(şehir_kelimeler)
    print("")
    print("Kelimemiz",len(sehir_değer)," harften oluşan bir ŞEHİR !        (4 Hakkiniz Var) ")
    görsel=[]
    for i in range(len(sehir_değer)):
        görsel.append(" _")
    for i in görsel:
        print(i,end="")
    
    harfler=list(sehir_değer)
    while (" _" in görsel):
        print("")
        harf=input("\nHarf Gir :")
        time.sleep(1)
        print("")
        new_harf=harf.upper()
        sira=[]
        for index,h in enumerate(harfler):
            if (h==new_harf):
                sira.append(index)
        
        if len(sira)==1:
            görsel[sira[0]]=new_harf
            for i in görsel:
                print(i,end="")
        elif len(sira)==2:
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            for i in görsel:
                print(i,end="")
        elif (len(sira)==3):
            görsel[sira[0]]=new_harf
            görsel[sira[1]]=new_harf
            görsel[sira[2]]=new_harf
            for i in görsel:
                print(i,end="")
        else:
            hak-=1
            print("Kalan Hak : ",hak)
            if (hak==3):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                   /|\ ")
            elif(hak==2):
                for i in görsel:
                    print(i,end="")
                print("")
                print("                    O  ")
                print("                    | ")
            elif(hak==1):
                for i in görsel:
                    print(i,end="")
                print("\n")
                print("                    O  ")
            elif(hak==0):
                print("\nHakkiniz Kalmadi :(")
                print("\nCevap : ",sehir_değer,"\n")
                break


                
            
            
            




       

        


    
    

    
   
    




    meslek_değer=random.choice(meslek_kelimeler)
    şehir_değer=random.choice(şehir_kelimeler)
