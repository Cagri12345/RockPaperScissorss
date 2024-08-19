import random    ## Bilgisayarın rastgele seçim yapabilmesi için random modülünü dahil ediyoruz.

def tas_kagit_makas_Cagri_Tugrul_Keser():

    #Oyunun kuralları
    print("Taş, Kağıt, Makas Oyununa Hoş Geldiniz")
    print("**************************************")
    print("Kurallarımız şu şekildedir: ")
    print("Taş makası yener,makas kağıdı yener,kağıt ise taşı yener")
    print("Oyunumuz iki turdan oluşmaktadır")
    print("Oyunu kazanabilirsin,berabere kalabilirsin ve kaybedebilirsin")
    print("Oyunumuzun sonunda yeniden oynayıp oynamak istemediğiniz sorulacak")
    print("Oyundan çıkmak için 'e' tuşuna basabilirsin")


    # Seçenekler listesini tanımlıyoruz
    secenekler = ["taş","kağıt","makas"]


    # Oyuncu ve bilgisayar galibiyet sayılarını ve oyun sayısını başlatıyoruz
    oyuncu_galibiyet = 0
    bilgisayar_galibet = 0
    oyun_sayisi = 0


    # Oyunun sonsuz döngüsü
    while True:
        oyun_sayisi += 1      # Her yeni oyunda oyun sayısını artırıyoruz
        oyuncu_tur_galibiyet = 0    # Oyuncunun tur galibiyet sayısını sıfırlıyoruz
        bilgisayar_tur_galibet = 0    # Bilgisayarın tur galibiyet sayısını sıfırlıyoruz
        tur_sayisi = 0     # Tur sayısını sıfırlıyoruz


        # Bir oyun 2 tur galibiyetine kadar devam eder
        while oyuncu_tur_galibiyet < 2 and bilgisayar_tur_galibet < 2:
            print("Tur başlıyor başarılar ...")
            tur_sayisi += 1     # Tur sayısını artırıyoruz
            if tur_sayisi == 0:    # Eğer tur sayısı 0 olursa döngüye devam eder
                continue
            else:
                print(f"{tur_sayisi}. Tur")     # Tur numarasını ekrana yazdırıyoruz


            # Oyuncudan bir seçim yapmasını istiyoruz
            oyuncu_secimi = input("Seç bakalım:").lower()


            # Oyuncu 'e' tuşuna basarsa oyundan çıkılır
            if oyuncu_secimi == "e":
                print("Yapma be usta bari 1 el ataydık")
                break


            # Eğer oyuncu geçerli bir seçim yapmazsa hata mesajı verilir ve aynı tur tekrar edilir
            if oyuncu_secimi not in secenekler:
                print("Hatalı işlem yaptınız.Şöyle bir şeyler deneyebilirsin : taş , kağıt , makas")
                tur_sayisi -= 1     # Hatalı seçim yapıldığında tur sayısını geri alıyoruz
                continue


            # Bilgisayar rastgele bir seçim yapar
            bilgisayar_secimi = random.choice(secenekler)
            print(f"Bilgisayarın seçimi: {bilgisayar_secimi}")


            #Eğer oyuncu ve bilgisayarın seçimi aynı ise beraber
            if oyuncu_secimi == bilgisayar_secimi:
                print("Berabere")

            #Oyuncu kazanırsa
            elif (oyuncu_secimi == "taş" and bilgisayar_secimi == "makas") or \
                    (oyuncu_secimi == "kağıt" and bilgisayar_secimi == "taş") or \
                    (oyuncu_secimi == "makas" and bilgisayar_secimi == "kağıt"):
                print("Bu turu kazandın")
                oyuncu_tur_galibiyet += 1    #Oyuncunun tur galibiyet sayısını arttırıyoruz

            #Bilgisayar kazanırsa
            else:
                print("Bu turu bilgisayar aldı")
                bilgisayar_tur_galibet += 1     #Bilgisayarın tur galibiyet sayısını arttırıyoruz


        #Oyuncu 2 tur kazandığında
        if oyuncu_tur_galibiyet == 2:
            print(f"Tebrikler.{oyun_sayisi}. Oyununun kazanı sensin ")
            oyuncu_galibiyet += 1      # Oyuncunun oyun galibiyet sayısını artırıyoruz


        # Eğer oyuncu oyundan çıkarsa
        elif oyuncu_tur_galibiyet == 0 and bilgisayar_tur_galibet == 0:
            print(f"{tur_sayisi}. Turdan çıkma işleminiz başarıyla gerçekleşti")


        # Bilgisayar 2 tur kazandığında
        else:
            print(f"{oyun_sayisi}. Oyunu bilgisayar kazandı")
            bilgisayar_galibet += 1      # Bilgisayarın oyun galibiyet sayısını artırıyoruz


        # Oyuncuya oyunu tekrar oynamak isteyip istemediğini soruyoruz
        oyuncu_soru= input("Oyunu tekrar oynamak ister misin?: (Evet ise 'a' , Hayır ise 's'): ").lower()


        # Eğer oyuncu 'a' demezse oyun sona erdirilir
        if oyuncu_soru != "a":
            print("Oyundan çıkılıyor....")
            break


        # Bilgisayar rastgele bir karar verir, eğer 'a' değilse oyun sona erdirilir
        bilgisayar_soru = random.choice(("a","s"))
        if bilgisayar_soru != "a":
            print("Bilgisayar oynamak istemiyor")
            break


    #Oyunun kazananı belirlenir
    print("Oyun sona erdi")
    print("Şimdi kazanana bakalım...")
    if oyuncu_galibiyet > bilgisayar_galibet:
        print("Tabi ki de sen olacaktın")    # Oyuncunun kazandığı durum

    elif bilgisayar_galibet > oyuncu_galibiyet:
        print("İnanamıyorum gerçekten.Bilgisayar nasıl kazanır!")   #Bilgisayarın kazandığı durum
    else:
        print("Oyun berabere bitti")     # Oyun berabere biterse


    # Toplam skor ekrana yazdırılır
    print("Total skor şu şekilde: ")
    print(f"Bilgisayar: {bilgisayar_galibet}",f"Sen: {oyuncu_galibiyet}")

#Oyunu başlatıyoruz
tas_kagit_makas_Cagri_Tugrul_Keser()




