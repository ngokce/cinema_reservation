# cinema_reservation
•	sira: koltuk düzenindeki sıraları temsil eden tek boyutlu liste. (sira1,sira2,sira3…)
•	k: her sıraya 20 adet koltuk (20 adet ‘-’) eklemek için for döngüsü içerisinde bulunuyor.
•	koltuk: koltuk düzeninin tamamını temsil eden 2 boyutlu liste. sira1, sira2 (…) listelerini içinde bulunduruyor.
•	toplam_bos_koltuk: 4 elemanlı bir dizi. her bir elemanı bir kategoride bulunan toplam boş koltuğu temsil ediyor.
•	bos_koltuk: koltuk rezerve edilirken bir sonraki rezerve edilecek boş koltuk. her rezerve işlemi sonrası güncelleniyor. her kategori için listenin içinde ayrı liste var. ilk değeri her kategorinin rezerve edilecek başlangıç değeri.
•	def menu(): ana menüyü ekrana getirecek fonksiyon.
•	secim: ana menüde yapılacak 1,2,3,4,0 seçimlerinden biri.
•	def rezervasyon(): ana menüdeki 1. seçenekteki rezervasyon işlemini yapacak fonksiyon.
•	kategori: rezervasyon işleminde sorulacak. hangi kategoride işlem yapılmak istendiğini soruyor.
•	biletadet: seçilen kategoriden kaç adet bilet satın alınmak istendiği soruluyor. rezerve işlemi yapıldıkça sayısı azalıyor.
•	maksimum_bilet: txt dosyasında belirlenecek olan, tek seferde satın alınabilecek maksimum bilet sayısı.
•	def salonuyazdir(): ana menüdeki 2. seçenek seçildiği zaman koltukları yazdıracak olan fonksiyon.
•	a: salon koltuk sırası (satır).
•	b: salon koltuk numarası (sütun).
•	def yenietkinlik(): ana menüdeki 3. seçenek seçildiğinde yapılan işlemleri sıfırlayan fonksiyon.
•	s-d: yeni etkinlik seçildiğinde koltukları boş yazdırmak için kullanılan döngüdeki satır ve sütun değişkenleri.
•	ciro: elde edilecek toplam ciro.
•	kategori_sinirlari: döngüde kullanılmadı. açıklamaya yardımcı olması için yazdığım her kategorideki koltukların sınırları.
•	kategori_sinirlari_sol: 2. ve 4. kategorinin sol tarafında rezerve işlemi yapılırken kullanılacak sınırlar için.
•	kategori_sinirlari_sag: 2. ve 4. kategorinin sağ tarafında rezerve işlemi yapılırken kullanılacak sınırlar için.
•	kategori_baslangici: her bir kategorinin rezerve edilecek ilk koltukları. bos_koltuk değişkeninin ilk haliyle aynı. bos_koltuk her rezervasyonda değişeceği için sabit kalacak değişken bu oldu.
•	kategori_baslangici_sol: koltukların rezervasyon edileceği ilk konumlar. 2 ve 4 için sol taraf.
•	kategori_baslangici_sag: koltukların rezervasyon edileceği ilk konumlar. 2 ve 4 için sağ taraf.
•	sag: 2. ve 4. kategori rezervasyonları için gerekli. rezervasyon sağa doğru yapıldığında 1’e eşit.
•	satilan_bilet: print edilecek satılan bilet sayısı.
•	b_fiyat: 1. kategori 1 bilet fiyatı
•	i_fiyat: 2. kategori 1 bilet fiyatı
•	u_fiyat: 3. kategori 1 bilet fiyatı
•	d_fiyat: 4. kategori 1 bilet fiyatı
•	b_indirim1,b_indirim2,b_indirim3: 1. kategori 1. 2. ve 3. indirim seçenekleri
•	i_indirim1,i_indirim2,i_indirim3: 2. kategori 1. 2. ve 3. indirim seçenekleri
•	u_indirim1,u_indirim2,u_indirim3: 3. kategori 1. 2. ve 3. indirim seçenekleri
•	d_indirim1,d_indirim2,d_indirim3: 4. kategori 1. 2. ve 3. indirim seçenekleri

