sira1 = []
sira2 = []
sira3 = []
sira4 = []
sira5 = []
sira6 = []
sira7 = []
sira8 = []
sira9 = []
sira10 = []
sira11 = []
sira12 = []
sira13 = []
sira14 = []
sira15 = []
sira16 = []
sira17 = []
sira18 = []
sira19 = []
sira20 = []
for k in range(0,20):
    sira1.append('-')
    sira2.append('-')
    sira3.append('-')
    sira4.append('-')
    sira5.append('-')
    sira6.append('-')
    sira7.append('-')
    sira8.append('-')
    sira9.append('-')
    sira10.append('-')
    sira11.append('-')
    sira12.append('-')
    sira13.append('-')
    sira14.append('-')
    sira15.append('-')
    sira16.append('-')
    sira17.append('-')
    sira18.append('-')
    sira19.append('-')
    sira20.append('-')
koltuk=[sira1,sira2,sira3,sira4,sira5,sira6,sira7,sira8,sira9,sira10,
        sira11,sira12,sira13,sira14,sira15,sira16,sira17,sira18,sira19,
        sira20]

toplam_bos_koltuk=[100,100,100,100] #her kategoride başlangıçta 100'er boş koltuk bulunuyor.
bos_koltuk=[[0,5],[0,4,0,15],[10,5],[10,4,10,15]] #her kategorinin rezerve edeceği koltukların konumları.
kategori_sinirlari=[[10,15],[10,0,10,20],[20,15],[20,0,20,20]] #döngülerde kullanmadım. yalnızca sınırları görmek için.
kategori_sinirlari_sol=[[10,15],[10,0],[20,15],[20,0]] #2. ve 4. kategorinin sol taraftaki koltuk sınırları. sol taraftan rezerve etmek için kullanılacak.
kategori_sinirlari_sag=[[10,15],[10,20],[20,15],[20,20]] #2. ve 4. kategorinin sağ taraftaki koltuk sınırları. sağ taraftan rezerve etmek için kullanılacak.
kategori_baslangici=[[0,5],[0,4,0,15],[10,5],[10,4,10,15]] #bos_koltuk değişkeninin ilk haliyle aynı. boş koltuk her seferinde değişeceği için gerekli.
kategori_baslangici_sol=[[0,5],[0,4],[10,5],[10,4]]
kategori_baslangici_sag=[[0,5],[0,15],[10,5],[10,15]]
ciro=0
sag=0

with open('indirim.txt') as s:
    text=s.readlines()
    maksimum_bilet=int(text[0].replace("\n","").split('-')[1])
    b_fiyat=int(text[1].replace("\n","").split('-')[1])
    i_fiyat=int(text[2].replace("\n","").split('-')[1])
    u_fiyat=int(text[3].replace("\n","").split('-')[1])
    d_fiyat=int(text[4].replace("\n","").split('-')[1])
    b_indirim1 = int(text[5].replace("\n", "").split('-')[3])
    b_indirim2 = int(text[6].replace("\n", "").split('-')[3])
    b_indirim3 = int(text[7].replace("\n", "").split('-')[3])
    i_indirim1 = int(text[8].replace("\n", "").split('-')[3])
    i_indirim2 = int(text[9].replace("\n", "").split('-')[3])
    i_indirim3 = int(text[10].replace("\n", "").split('-')[3])
    u_indirim1 = int(text[11].replace("\n", "").split('-')[3])  #15
    u_indirim2 = int(text[12].replace("\n", "").split('-')[3])  #20
    u_indirim3 = int(text[13].replace("\n", "").split('-')[3])  #35
    d_indirim1 = int(text[14].replace("\n", "").split('-')[3])  # 5
    d_indirim2 = int(text[15].replace("\n", "").split('-')[3])  #10
    d_indirim3 = int(text[16].replace("\n", "").split('-')[3])  #15


def menu():
    while True:
        print(16*"*" + "\n*** ANA MENÜ ***\n" + 16*"*" + "\n" +
              "1. Rezervasyon\n2. Salonu Yazdır\n3. Yeni Etkinlik\n"
              "4. Toplam Ciro\n0. Çıkış\n" + 16*"*")
        secim=input("Seçiminiz?")
        if secim=="1":
            rezervasyon()
        elif secim=="2":
            salonuyazdir()
        elif secim=="3":
            yenietkinlik()
        elif secim=="4":
            print("Toplam Ciro:",ciro)
        elif secim=="0":
            break
        else:
            print("0-4 arası bir değer girin.")


def rezervasyon():
    global sag
    global ciro
    kategori=int(input("Kategori(1-4)?"))
    while kategori<1 or kategori>4: #1-4 arası dışında kategori seçilememesi için.
        kategori=int(input("Kategori(1-4)?")) #1-4 arası dışında kategori seçilmeye çalışılırsa soru tekrar soruluyor.
    biletadet=int(input("Bilet Adedi?"))
    satilan_bilet=biletadet
    while biletadet<1 or biletadet>maksimum_bilet:
        biletadet=int(input("Bilet Adedi?")) #uygun olmayan bilet sayısı girilirse soru tekrar soruluyor.

    if toplam_bos_koltuk[kategori-1] >= biletadet: #satın alınmak istenen adette bilet kalıp kalmadığı kontrol ediliyor.
        print("Rezerve Edilen Koltuklar(Sıra-Koltuk): ",end="")

        #kategori 1 ve 3 algoriması.
        if kategori==1 or kategori==3:
            for i in range(bos_koltuk[kategori-1][0],kategori_sinirlari_sol[kategori-1][0]):
                for j in range(bos_koltuk[kategori-1][1],kategori_sinirlari_sol[kategori-1][1]): #sütunu belirliyor. örneğin 1. kategori için 5-15 arası dönecek.
                    if biletadet<1:
                        bos_koltuk[kategori-1][1]=j #rezervasyon istenen koltuk kalmayınca sonraki rezervasyon için boş koltuklar tutuluyor.
                        bos_koltuk[kategori-1][0]=i
                        break
                    elif j==kategori_sinirlari_sol[kategori-1][1]-1: #kategorideki sıra dolunca:
                        bos_koltuk[kategori-1][1]=kategori_baslangici[kategori-1][1] #sütun, bir aşağıdaki sırada başa dönüyor.
                        bos_koltuk[kategori-1][0]=i+1 #sıra bir aşağıya kayıyor.
                    koltuk[i][j]='*'
                    print(i+1,"-",j+1,"  ",end="") #rezerve edilen sıra-koltuk.
                    biletadet-=1
                    toplam_bos_koltuk[kategori-1]-=1 #rezervasyon yapılan kategorideki toplam boş koltuk azaltılıyor.
                if biletadet<1:
                    break

        #kategori 2 ve 4 algoritması.
        elif kategori==2 or kategori==4:
            for i in range(bos_koltuk[kategori-1][0],kategori_sinirlari_sol[kategori-1][0]): #0,10
                for j in reversed(range(kategori_sinirlari_sol[kategori-1][1],bos_koltuk[kategori-1][1]+1)): #0,5
                    if sag==1:
                        break
                    if biletadet<1:
                        bos_koltuk[kategori-1][1]=j
                        bos_koltuk[kategori-1][0]=i
                        break
                    elif j==kategori_sinirlari_sol[kategori-1][1]: #sola doğru satın almada koltuk bitince sağa geçmek için.
                        bos_koltuk[kategori-1][1]=kategori_baslangici_sag[kategori-1][1] #satırda soldaki koltuk bitti. bos_koltuk değişkeni sağdaki yere eşitleniyor.
                        sag=1 #rezervasyon işlemi sağa doğru yapılıyor demektir.
                    koltuk[i][j]='*'
                    print(i+1,"-",j+1,"  ",end="") #sıra-koltuk.
                    biletadet-=1
                    toplam_bos_koltuk[kategori-1]-=1
                if sag==1: #sağa doğru rezervasyon yapılıyorsa.
                    for j in range(bos_koltuk[kategori-1][1],kategori_sinirlari_sag[kategori-1][1]):
                        if biletadet<1: #rezerve edilecek bilet kalmadı. kalınan yer işaretleniyor.
                            bos_koltuk[kategori-1][1]=j
                            bos_koltuk[kategori-1][0]=i
                            break
                        elif j==kategori_sinirlari_sag[kategori-1][1]-1:
                            bos_koltuk[kategori-1][1]=kategori_baslangici_sol[kategori-1][1]
                            bos_koltuk[kategori-1][0]=i+1
                            sag=0 #bir sonraki işlem sola doğru olacak.
                        koltuk[i][j]='*'
                        print(i+1,"-",j+1,"  ",end="") #sıra-koltuk
                        biletadet-=1
                        toplam_bos_koltuk[kategori-1]-=1
                if biletadet<1:
                    break

        print("\nBilet Adedi:", satilan_bilet)
        if kategori==1:
            print("Toplam Tutar:",b_fiyat*satilan_bilet)
            if satilan_bilet>=5 and satilan_bilet<=10:
                print("Yapılan İndirim:",(int(text[5].replace("\n","").split('-')[3]))/100*b_fiyat*satilan_bilet)
                print("Net Tutar:",(b_fiyat-(b_fiyat*(int(text[5].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (b_fiyat - (b_fiyat * (int(text[5].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=11 and satilan_bilet<=20:
                print("Yapılan İndirim:",(int(text[6].replace("\n","").split('-')[3]))/100*b_fiyat*satilan_bilet)
                print("Net Tutar:",(b_fiyat-(b_fiyat*(int(text[6].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (b_fiyat - (b_fiyat * (int(text[6].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=21 and satilan_bilet<=maksimum_bilet:
                print("Yapılan İndirim:",
                      (int(text[7].replace("\n", "").split('-')[3])) / 100 * b_fiyat * satilan_bilet)
                print("Net Tutar:",
                      (b_fiyat - (b_fiyat * (int(text[7].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet)
                ciro += (b_fiyat - (b_fiyat * (int(text[7].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            else:
                print("Yapılan İndirim:",0)
                print("Net Tutar:",b_fiyat*satilan_bilet)
                ciro+=b_fiyat*satilan_bilet
        if kategori==2:
            print("Toplam Tutar:",i_fiyat*satilan_bilet)
            if satilan_bilet>=5 and satilan_bilet<=10:
                print("Yapılan İndirim:",(int(text[8].replace("\n","").split('-')[3]))/100*i_fiyat*satilan_bilet)
                print("Net Tutar:",(i_fiyat-(i_fiyat*(int(text[8].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (i_fiyat - (i_fiyat * (int(text[8].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=11 and satilan_bilet<=20:
                print("Yapılan İndirim:",(int(text[9].replace("\n","").split('-')[3]))/100*i_fiyat*satilan_bilet)
                print("Net Tutar:",(i_fiyat-(i_fiyat*(int(text[9].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (i_fiyat - (i_fiyat * (int(text[9].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=21 and satilan_bilet<=maksimum_bilet:
                print("Yapılan İndirim:",
                      (int(text[10].replace("\n", "").split('-')[3])) / 100 * i_fiyat * satilan_bilet)
                print("Net Tutar:",
                      (i_fiyat - (i_fiyat * (int(text[10].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet)
                ciro += (i_fiyat - (i_fiyat * (int(text[10].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            else:
                print("Yapılan İndirim:",0)
                print("Net Tutar:",i_fiyat*satilan_bilet)
                ciro+=i_fiyat*satilan_bilet
        if kategori==3:
            print("Toplam Tutar:",u_fiyat*satilan_bilet)
            if satilan_bilet>=5 and satilan_bilet<=15:
                print("Yapılan İndirim:",(int(text[11].replace("\n","").split('-')[3]))/100*u_fiyat*satilan_bilet)
                print("Net Tutar:",(u_fiyat-(u_fiyat*(int(text[11].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (u_fiyat - (u_fiyat * (int(text[11].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=16 and satilan_bilet<=25:
                print("Yapılan İndirim:",(int(text[12].replace("\n","").split('-')[3]))/100*u_fiyat*satilan_bilet)
                print("Net Tutar:",(u_fiyat-(u_fiyat*(int(text[12].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (u_fiyat - (u_fiyat * (int(text[12].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=26 and satilan_bilet<=maksimum_bilet:
                print("Yapılan İndirim:",
                      (int(text[13].replace("\n", "").split('-')[3])) / 100 * u_fiyat * satilan_bilet)
                print("Net Tutar:",
                      (u_fiyat - (u_fiyat * (int(text[13].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet)
                ciro += (u_fiyat - (u_fiyat * (int(text[13].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            else:
                print("Yapılan İndirim:",0)
                print("Net Tutar:",u_fiyat*satilan_bilet)
                ciro+=u_fiyat*satilan_bilet
        if kategori==4:
            print("Toplam Tutar:",d_fiyat*satilan_bilet)
            if satilan_bilet>=5 and satilan_bilet<=10:
                print("Yapılan İndirim:",(int(text[14].replace("\n","").split('-')[3]))/100*d_fiyat*satilan_bilet)
                print("Net Tutar:",(d_fiyat-(d_fiyat*(int(text[14].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (d_fiyat - (d_fiyat * (int(text[14].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=11 and satilan_bilet<=20:
                print("Yapılan İndirim:",(int(text[15].replace("\n","").split('-')[3]))/100*d_fiyat*satilan_bilet)
                print("Net Tutar:",(d_fiyat-(d_fiyat*(int(text[15].replace("\n","").split('-')[3])/100)))*satilan_bilet)
                ciro += (d_fiyat - (d_fiyat * (int(text[15].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            elif satilan_bilet>=21 and satilan_bilet<=maksimum_bilet:
                print("Yapılan İndirim:",
                      (int(text[16].replace("\n", "").split('-')[3])) / 100 * d_fiyat * satilan_bilet)
                print("Net Tutar:",
                      (d_fiyat - (d_fiyat * (int(text[16].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet)
                ciro += (d_fiyat - (d_fiyat * (int(text[16].replace("\n", "").split('-')[3]) / 100))) * satilan_bilet
            else:
                print("Yapılan İndirim:",0)
                print("Net Tutar:",d_fiyat*satilan_bilet)
                ciro+=d_fiyat*satilan_bilet
    else:
        print("Yeterli Sayıda Koltuk Yok.") #alınmak istenen bilet sayısı kalan bilet sayısından fazlaysa.


def salonuyazdir():
    for a in range(0,20):
        for b in range(0,20):
            print(koltuk[a][b],end="")
        print("")


def yenietkinlik():
    global ciro
    global toplam_bos_koltuk
    global bos_koltuk
    for s in range(0,20):
        for d in range(0,20):
            koltuk[s][d]='-'
    #değişkenler sıfırlanmalı.
    toplam_bos_koltuk=[100,100,100,100]
    bos_koltuk=[[0,5],[0,4,0,15],[10,5],[10,4,10,15]]
    ciro=0


menu()
