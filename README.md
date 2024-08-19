# Taş, Kağıt, Makas Oyunu
Bu Python projesi, geleneksel "Taş, Kağıt, Makas" oyununu dijital ortamda oynayabilmenizi sağlar. Oyuncu ve bilgisayar karşı karşıya gelerek, her biri rastgele veya bilinçli bir seçim yapar. İki tur kazanan ilk oyuncu oyunun galibi olur.
## Proje Özeti
Bu proje, Python'da temel programlama becerilerini geliştirmek amacıyla tasarlanmıştır. Döngüler, koşullu ifadeler, kullanıcı girişi gibi temel programlama yapılarını içerir. Ayrıca, PEP-8 kodlama standartlarına uygun olarak yazılmıştır.
## Özellikler
- Taş, Kağıt, Makas oyunu kurallarına uygun bir şekilde çalışır.
- Oyuncu ve bilgisayar rastgele seçim yapar.
- İlk iki turu kazanan oyun galibi olur.
- Oyun sonunda toplam skorlar gösterilir.
# Proje İçeriği
- **`tas_kagit_makas_Cagri_Tugrul_Keser.py`**: Oyunun tüm mantığını içeren ana Python dosyası.
- # Kullanım

### Gereksinimler
- **Python 3.x** yüklü olmalıdır.
- Python ile birlikte gelen `random` modülü kullanılır, ek bir modül yüklemenize gerek yoktur.
## Nasıl Oynanır
Oyunu çalıştırmak için şu komutu girin:

python tas_kagit_makas_Cagri_Tugrul_Keser.py
Program başladığında, sizden bir seçim yapmanız istenecektir: "taş", "kağıt" veya "makas".

Oyun sırasında:

Beraberlik: Eğer oyuncunun ve bilgisayarın seçimi aynıysa, tur berabere biter.
Oyuncu Kazanır: Taş makası yener, kağıt taşı yener, makas kağıdı yener.
Bilgisayar Kazanır: Bilgisayarın seçimi oyuncunun seçimini yenerse, bilgisayar kazanır.
Oyun her seferinde iki tur galibiyeti gerektirir. Oyun sonunda, toplam galibiyetler ekrana yazdırılır.

Oyundan çıkmak için e tuşuna basabilirsiniz.

Oyunun bitiminde, yeniden oynamak isteyip istemediğiniz sorulacaktır. Tekrar oynamak için "a" tuşuna basın, çıkmak için "s" tuşuna basın.
