# TabiBERT Checkpoint Evaluation Report

Generated on: **2025/07/13 20:22:55**

Text path: **inference/inference_dataset/short_masked.json**

## Sample 1

<details>
<summary> web / tr / short / 0.15 </summary>

### Original Text

```
Çevre ve Şehircilik Bakanlığı'nın öncülük ettiği "Yeşil Şehirler Projesi" 81 ilde hayata geçiriliyor. Proje kapsamında kent merkezlerinde park alanları genişletilirken, bisiklet yolları da artırılıyor. Belediyeler vatandaşlarla birlikte ağaçlandırma çalışmaları düzenleyerek çevre bilincini artırmaya odaklanıyor. İlk etapta İstanbul, Ankara ve İzmir'de pilot uygulamalar başlatıldı. Bu şehirlerdeki hava kalitesi ölçümleri olumlu sonuçlar vermeye başladı. Proje koordinatörü Dr. Elif Yaman, "Amacımız yaşam kalitesini artırarak sürdürülebilir şehirler oluşturmak" dedi. Gelecek yıl projenin tüm Türkiye'ye yaygınlaştırılması planlanıyor.
```

### Masked Text

```
[CLS][MASK]e ve Şehircilik Bakanlığı'nın öncülük ettiği "Yeşil Şehirler Projesi" 81 ilde hayata geçiriliyor.[MASK]kapsamında kent merkezlerinde [MASK][MASK]genişletilirken, bisiklet yol[MASK]artırılıyor[MASK] Belediyeler vatandaş[MASK]ağaç[MASK]çalışmaları düzenleyerek [MASK][MASK]ini artırmaya odaklanıyor. İlk etapta İstanbul, Ankara ve İzmir'de pilot uygulamalar[MASK]ıldı. Bu şehirlerdeki hava kalitesi ölçümleri olumlu [MASK]vermeye başladı. Proje [MASK]atörü Dr[MASK] Elif Yaman, "A[MASK]ımız yaşam kalitesini artırarak sürdürülebilir şehir[MASK]mak" dedi. Gelecek yıl projenin tüm Türkiye'ye yaygınlaştırılması planlanıyor.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Çevr]e ve Şehircilik Bakanlığı'nın öncülük ettiği "Yeşil Şehirler Projesi" 81 ilde hayata geçiriliyor.[Proje]kapsamında kent merkezlerinde [yeşil][alanları]genişletilirken, bisiklet yol[ları da]artırılıyor[.] Belediyeler vatandaş[larla birlikte]ağaç[landırma]çalışmaları düzenleyerek [,][bilinc]ini artırmaya odaklanıyor. İlk etapta İstanbul, Ankara ve İzmir'de pilot uygulamalar[başlat]ıldı. Bu şehirlerdeki hava kalitesi ölçümleri olumlu [sonuçlar]vermeye başladı. Proje [Koordin]atörü Dr[.] Elif Yaman, "A[mac]ımız yaşam kalitesini artırarak sürdürülebilir şehir[ler oluştur]mak" dedi. Gelecek yıl projenin tüm Türkiye'ye yaygınlaştırılması planlanıyor.[SEP]
```


</details>

## Sample 2

<details>
<summary> web / en / short / 0.15 </summary>

### Original Text

```
Marvel Studios announced a new series coming to Disney+ in early 2025. Titled *Eclipse*, the show will focus on a previously unknown hero in the MCU. The cast includes rising star Mia Chen in the lead role. Filming is set to begin in Vancouver this August. Fans have already begun speculating about the character’s connection to the existing universe. More details will be revealed at San Diego Comic-Con.
```

### Masked Text

```
[CLS]Marvel Studios[MASK]no[MASK]ed a new series coming to Disney+ in ear[MASK] 2025.[MASK]led *Eclipse*, the show will focus on a previously un[MASK]n hero in the [MASK]U. The cast includes rising star[MASK]ia Chen in the lead role. Filming is set to begin in Vancouver this August. Fans have [MASK]ready[MASK]eg[MASK]speculating[MASK] the character’s connection to the [MASK]isting universe. M[MASK]details will be [MASK]eal[MASK] at San [MASK]ego Comic-Con.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Marvel Studios[an]no[unc]ed a new series coming to Disney+ in ear[ly] 2025.[Tit]led *Eclipse*, the show will focus on a previously un[know]n hero in the [MC]U. The cast includes rising star[Le]ia Chen in the lead role. Filming is set to begin in Vancouver this August. Fans have [al]ready[b]eg[un]speculating[about] the character’s connection to the [ex]isting universe. M[ore]details will be [rev]eal[ed] at San [di]ego Comic-Con.[SEP]
```


</details>

## Sample 3

<details>
<summary> creative / tr / short / 0.15 </summary>

### Original Text

```
Eski kütüphaneci her sabah aynı saatte gelir, sessizce raflar arasında dolaşırdı. Kimsenin fark etmediği şey, onun sadece kitapları okumadığı, aynı zamanda kitapların ona fısıldadığı sırları dinlediğiydi. Gecenin karanlığında, sayfalardaki karakterler canlanır, kütüphanenin koridorlarında yürürlerdi. Yaşlı adam bu gizli dünyayın tek tanığıydı ve bu yüzden asla emekli olmayı kabul etmemişti. Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten konuşuyor mu?" diye sordu. O gün kütüphaneci ilk kez gülümsedi ve "Dinlemeyi bilen kulaklar için her şey mümkün" dedi.
```

### Masked Text

```
[CLS]Eski kütüphaneci her[MASK] aynı saatte gelir, sessizce raflar arasında dolaşırdı. Kimsenin fark etmediği şey, onun sadece [MASK][MASK]madığı, aynı zamanda kitapların ona fısıldadığı sırları dinlediğiydi. Gecenin karan[MASK], sayfalardaki [MASK]ler canlanır, kütüphanenin koridorlarında yürürlerdi. Yaşlı adam bu gizli dünyayın tek tanığıydı ve bu yüzden asla emekli olmayı kabul etmemişti[MASK] Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten konuşuyor mu?" diye sordu. O gün kütüphaneci ilk kez[MASK]sedi ve "Dinlemeyi bilen kulaklar için her şey[MASK]" dedi[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Eski kütüphaneci her[sabah] aynı saatte gelir, sessizce raflar arasında dolaşırdı. Kimsenin fark etmediği şey, onun sadece [kitap][oku]madığı, aynı zamanda kitapların ona fısıldadığı sırları dinlediğiydi. Gecenin karan[lığında], sayfalardaki [gizem]ler canlanır, kütüphanenin koridorlarında yürürlerdi. Yaşlı adam bu gizli dünyayın tek tanığıydı ve bu yüzden asla emekli olmayı kabul etmemişti[.] Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten konuşuyor mu?" diye sordu. O gün kütüphaneci ilk kez[gülüm]sedi ve "Dinlemeyi bilen kulaklar için her şey[mümkün]" dedi[.][SEP]
```


</details>

## Sample 4

<details>
<summary> article / tr / short / 0.15 </summary>

### Original Text

```
Bu çalışmada, üniversite öğrencilerinin dijital öğrenme platformlarına yönelik tutumları ve akademik başarıları arasındaki ilişki incelenmiştir. Araştırma, 2023-2024 eğitim-öğretim yılında İstanbul'daki üç farklı üniversiteden 150 öğrenci ile yürütülmüştür. Veri toplama araçları olarak "Dijital Öğrenme Tutum Ölçeği" ve "Akademik Başarı Değerlendirme Formu" kullanılmıştır. Bulgular, dijital platformlara karşı olumlu tutum sergileyen öğrencilerin akademik başarı puanlarının anlamlı düzeyde yüksek olduğunu göstermiştir (p<0.05). Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital öğrenme tutumları arasında pozitif korelasyon tespit edilmiştir. Bu sonuçlar, eğitim kurumlarının dijital dönüşüm stratejilerini planlarken öğrenci profillerini dikkate alması gerektiğini ortaya koymaktadır.
```

### Masked Text

```
[CLS]Bu [MASK], üniversite [MASK]dijital [MASK][MASK]larına yönelik tutumları ve akademik başar[MASK]arasındaki ilişki incelenmiştir. Araştırma, 2023-202[MASK] eğitim-öğretim yılında İstanbul'[MASK]üç farklı üniversiteden 150 öğrenci ile [MASK]. Veri toplama [MASK]olarak "Dijital Öğrenme Tutum Ölçeği" ve[MASK][MASK]Başarı Değerlendirme [MASK]" kullanılmıştır. Bulgular, dijital platformlara karşı olumlu tutum sergileyen öğrencilerin akademik başarı puanlarının anlamlı düzeyde yüksek olduğunu göstermiştir (p<0.0[MASK]). Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital [MASK][MASK]ları arasında pozitif korelasyon tespit edilmiştir. Bu sonuçlar, eğitim kurumlarının [MASK][MASK] stratejilerini planlarken öğrenci profillerini dikkate [MASK]gerektiğini ortaya koymaktadır.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu [araştırmada], üniversite [öğrencilerinin]dijital [leşme][platform]larına yönelik tutumları ve akademik başar[ıları]arasındaki ilişki incelenmiştir. Araştırma, 2023-202[4] eğitim-öğretim yılında İstanbul'[daki]üç farklı üniversiteden 150 öğrenci ile [gerçekleştirilmiştir]. Veri toplama [aracı]olarak "Dijital Öğrenme Tutum Ölçeği" ve["][Akademik]Başarı Değerlendirme [Ölçeği]" kullanılmıştır. Bulgular, dijital platformlara karşı olumlu tutum sergileyen öğrencilerin akademik başarı puanlarının anlamlı düzeyde yüksek olduğunu göstermiştir (p<0.0[5]). Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital [platform][tutum]ları arasında pozitif korelasyon tespit edilmiştir. Bu sonuçlar, eğitim kurumlarının [dijital][dijital] stratejilerini planlarken öğrenci profillerini dikkate [almaları]gerektiğini ortaya koymaktadır.[SEP]
```


</details>

## Sample 5

<details>
<summary> thesis / tr / short / 0.15 </summary>

### Original Text

```
Bu araştırma, ortaokul öğrencilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır. Araştırma, İstanbul'daki bir devlet okulunda 7. sınıf öğrencileriyle yürütülmüştür. Deney grubundaki öğrencilere 8 hafta boyunca yapılandırılmış empati eğitimi uygulanmıştır. Kontrol grubuna herhangi bir müdahale yapılmamıştır. Araştırma verileri Sosyal Problem Çözme Envanteri ve Empati Ölçeği ile toplanmıştır. Bulgular, empati eğitiminin öğrencilerin sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.
```

### Masked Text

```
[CLS]Bu araştırma[MASK] ortaokul öğrencilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır. Araştırma, İstanbul[MASK]daki bir devlet okulunda 7. sınıf öğrencileriyle yürütülmüştür. Deney[MASK]öğrencilere 8 hafta boyunca yapılandırılmış empati eğitimi [MASK]. Kontrol grubuna herhangi bir müdahale yapılmamıştır. Araştırma verileri Sosyal Problem Çözme [MASK]i ve Empati Ölçeği ile [MASK]. Bulgular, empati eğitiminin öğrencilerin sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu araştırma[,] ortaokul öğrencilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır. Araştırma, İstanbul[']daki bir devlet okulunda 7. sınıf öğrencileriyle yürütülmüştür. Deney[grubundaki]öğrencilere 8 hafta boyunca yapılandırılmış empati eğitimi [uygulanmıştır]. Kontrol grubuna herhangi bir müdahale yapılmamıştır. Araştırma verileri Sosyal Problem Çözme [Envanter]i ve Empati Ölçeği ile [toplanmıştır]. Bulgular, empati eğitiminin öğrencilerin sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.[SEP]
```


</details>

## Sample 6

<details>
<summary> parliment / tr / short / 0.15 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 105’inci Birleşimini açıyorum. Toplantı yeter sayısı vardır, görüşmelere başlıyoruz. Gündeme geçmeden önce üç sayın milletvekiline gündem dışı söz vereceğim. İlk söz, Hatay ilinin tarımsal sorunları hakkında söz isteyen Hatay Milletvekili Mehmet Öztürk’e aittir. Buyurun Sayın Öztürk. Sayın Başkan, değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği çiftçilerimizi ciddi şekilde zor durumda bırakmıştır. Özellikle zeytin ve narenciye üreticileri hem ihracat sıkıntısı yaşamakta hem de girdi maliyetleri karşısında ezilmektedir. Bu nedenle Tarım Bakanlığının bölgeye özel destek programı geliştirmesi elzem hâle gelmiştir.
```

### Masked Text

```
[CLS]Türkiye Büyük Millet Meclisinin 105’inci Bir[MASK]imini açıyorum. Toplantı yeter[MASK]vardır[MASK] görüşmelere başlıyoruz[MASK] Gündeme geçmeden önce üç sayın milletvekil[MASK]gündem dışı söz vereceğim. İlk söz, Hatay[MASK]inin [MASK] sorunları hakkında söz isteyen Hatay Milletvekili Mehmet Öztürk’e aittir. Buyurun Sayın Öztürk. Sayın Başkan, değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği çift[MASK]imizi ciddi şekilde zor durumda bırakmıştır. Özellikle [MASK]tin ve narenciye üreticileri hem ihracat sıkıntısı yaşamakta hem de girdi maliyetleri [MASK][MASK]ilmektedir[MASK] Bu nedenle [MASK] Bakanlığının bölgeye özel destek programı geliştirmesi elzem hâle [MASK][MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 105’inci Bir[leş]imini açıyorum. Toplantı yeter[sayısı]vardır[,] görüşmelere başlıyoruz[.] Gündeme geçmeden önce üç sayın milletvekil[ine]gündem dışı söz vereceğim. İlk söz, Hatay[il]inin [,] sorunları hakkında söz isteyen Hatay Milletvekili Mehmet Öztürk’e aittir. Buyurun Sayın Öztürk. Sayın Başkan, değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği çift[çiler]imizi ciddi şekilde zor durumda bırakmıştır. Özellikle [zey]tin ve narenciye üreticileri hem ihracat sıkıntısı yaşamakta hem de girdi maliyetleri [][ger]ilmektedir[.] Bu nedenle [Tarım] Bakanlığının bölgeye özel destek programı geliştirmesi elzem hâle […][.][SEP]
```


</details>

## Sample 7

<details>
<summary> code / en / short / 0.15 </summary>

### Original Text

```
Design a Java class named `Book` that encapsulates book details such as `title`, `author`, and `price`. Implement proper getters and setters. Add a method to validate if the book price is within a logical range.

`java
public class Book {
    private String title;
    private String author;
    private double price;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price >= 0 && price <= 1000) {
            this.price = price;
        } else {
            throw new IllegalArgumentException("Price must be between 0 and 1000.");
        }
    }
}
`
```

### Masked Text

```
[CLS]Design a Java class named `[MASK]ok[MASK] that enc[MASK]ula[MASK] book details such as `tit[MASK]`,[MASK]author`, and `[MASK]ice`.[MASK]mplement proper get[MASK][MASK] setters[MASK] Add a [MASK]hod to validate if[MASK]book price is within a logical range.

`j[MASK]
public c[MASK] Book {
    private String tit[MASK];
   [MASK]ate [MASK]ing author;
    private double price;

   [MASK] String get[MASK][MASK]le() {
        return title;
    }

    public void setTit[MASK](String title)[MASK]        this.tit[MASK] = title;
   [MASK]    public[MASK]ing get[MASK]hor()[MASK]        [MASK]author;
[MASK] }

[MASK] public void[MASK]Author(String author) {
        this.author = author[MASK]    }

    public double getPrice() {
        return price;
   [MASK]   [MASK] v[MASK] setPrice(double price) {
        if (price[MASK]= 0[MASK]& pr[MASK][MASK]=[MASK]1000) {
            this.price = price[MASK]        }[MASK]se {
            throw[MASK] IllegalAr[MASK]umentException("Price must be between 0 and 1[MASK][MASK]0."[MASK][MASK][MASK][MASK] }
}
`[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Design a Java class named `[Bo]ok[`] that enc[aps]ula[tes] book details such as `tit[le]`,[`]author`, and `[pr]ice`.[I]mplement proper get[ters][and] setters[.] Add a [met]hod to validate if[the]book price is within a logical range.

```j[ava]
public c[lass] Book {
    private String tit[le];
   [priv]ate [Str]ing author;
    private double price;

   [public] String get[T][it]le() {
        return title;
    }

    public void setTit[le](String title)[{]        this.tit[le] = title;
   [}]    public[Str]ing get[Aut]hor()[{]        []author;
[] }

[] public void[set]Author(String author) {
        this.author = author[;]    }

    public double getPrice() {
        return price;
   [}]   [public] v[oid] setPrice(double price) {
        if (price[>]= 0[&]& pr[ice][<]=[]1000) {
            this.price = price[;]        }[el]se {
            throw[new] IllegalAr[g]umentException("Price must be between 0 and 1[0][0]0."[);][][}][] }
}
```[SEP]
```


</details>

## Sample 8

<details>
<summary> math / en / short / 0.15 </summary>

### Original Text

```
A train 180 meters long is running at a speed of 72 km/h. how much time will it take to cross a platform 120 meters long? also, find the time it takes to pass a man standing on the platform.

a) 15 sec and 9 sec, b) 18 sec and 10 sec, c) 20 sec and 9 sec, d) 12 sec and 7 sec, e) none of these

"explanation:
length of train = 180 m
length of platform = 120 m
total distance to cross platform = 180 + 120 = 300 m

speed of train in m/s = (72 × 1000) / 3600 = 20 m/s

time to cross platform = 300 / 20 = 15 seconds
time to cross a man = 180 / 20 = 9 seconds

answer: option a\ 
```

### Masked Text

```
[CLS]A train [MASK]80 met[MASK] long is running at [MASK]speed of 72 km[MASK]h. how much[MASK]will it take to[MASK]ros[MASK]platform[MASK]120 meters[MASK]? also, find[MASK]time it takes to pass a man stan[MASK] on the platform.

a) 15 sec and [MASK] sec, b) 18 sec and [MASK]0 sec,[MASK]) 20 sec and 9 sec, d) 12 sec and 7[MASK],[MASK]) none of these

[MASK][MASK]planation[MASK]length of train = 180 m
length of platform =[MASK]120 m
total distan[MASK]to cross[MASK] = 180 + 12[MASK][MASK] 300 m

[MASK]eed of train in m[MASK][MASK] = (72 × 1000) / 3600 = 20 m/s

time to cross platform = 3[MASK]0 / 20 = 15 second[MASK]time to c[MASK][MASK]man = 1[MASK]0 / 20 = 9 seconds

ans[MASK]:[MASK]tion a\ [SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]A train [1]80 met[ers] long is running at [some]speed of 72 km[/]h. how much[time]will it take to[c]ros[s a]platform[at]120 meters[long]? also, find[the]time it takes to pass a man stan[ding] on the platform.

a) 15 sec and [no] sec, b) 18 sec and [1]0 sec,[c]) 20 sec and 9 sec, d) 12 sec and 7[sec],[e]) none of these

[][ex]planation[]length of train = 180 m
length of platform =[]120 m
total distan[ce]to cross[platform] = 180 + 12[0][=] 300 m

[sp]eed of train in m[/][s] = (72 × 1000) / 3600 = 20 m/s

time to cross platform = 3[0]0 / 20 = 15 second[s]time to c[ros][s]man = 1[8]0 / 20 = 9 seconds

ans[wer]:[op]tion a\ [SEP]
```


</details>

## Sample 9

<details>
<summary> web / tr / short / 0.3 </summary>

### Original Text

```
Çevre ve Şehircilik Bakanlığı'nın öncülük ettiği "Yeşil Şehirler Projesi" 81 ilde hayata geçiriliyor. Proje kapsamında kent merkezlerinde park alanları genişletilirken, bisiklet yolları da artırılıyor. Belediyeler vatandaşlarla birlikte ağaçlandırma çalışmaları düzenleyerek çevre bilincini artırmaya odaklanıyor. İlk etapta İstanbul, Ankara ve İzmir'de pilot uygulamalar başlatıldı. Bu şehirlerdeki hava kalitesi ölçümleri olumlu sonuçlar vermeye başladı. Proje koordinatörü Dr. Elif Yaman, "Amacımız yaşam kalitesini artırarak sürdürülebilir şehirler oluşturmak" dedi. Gelecek yıl projenin tüm Türkiye'ye yaygınlaştırılması planlanıyor.
```

### Masked Text

```
[CLS][MASK][MASK][MASK]Bakanlığı'[MASK]öncülük ettiği "Yeşil Şehirler Projesi" 81[MASK]hayata geçiriliyor. Proje kapsamında kent merkezlerinde park alanları [MASK]ilirken[MASK] bisiklet[MASK]ları da artır[MASK]. Belediyeler vatandaşlarla birlikte ağaçlandırma [MASK][MASK]çevre bilinc[MASK]maya odaklanıyor. İlk etapta İstanbul,[MASK]a ve İzmir'[MASK]pilot[MASK][MASK] başlatıldı. Bu [MASK]lerdeki hava kalitesi ölçümleri [MASK]sonuçlar [MASK]meye başladı. Proje koordinatörü Dr. Elif[MASK]aman, "[MASK]mac[MASK] yaşam kalitesini artırarak [MASK] şehir[MASK]mak"[MASK]. Gelecek yıl projenin tüm[MASK]'ye yaygınlaştırılması planlanıyor.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Çevr][e ve][Şehircilik]Bakanlığı'[nın]öncülük ettiği "Yeşil Şehirler Projesi" 81[ilde]hayata geçiriliyor. Proje kapsamında kent merkezlerinde park alanları [genişlet]ilirken[,] bisiklet[yol]ları da artır[ılıyor]. Belediyeler vatandaşlarla birlikte ağaçlandırma [larla][yaparak]çevre bilinc[ini artır]maya odaklanıyor. İlk etapta İstanbul,[Ankar]a ve İzmir'[de]pilot[uygulama][ler] başlatıldı. Bu [gün]lerdeki hava kalitesi ölçümleri [de]sonuçlar [ver]meye başladı. Proje koordinatörü Dr. Elif[Y]aman, "[A]mac[ımız] yaşam kalitesini artırarak [,] şehir[ler oluştur]mak"[dedi]. Gelecek yıl projenin tüm[Türkiye]'ye yaygınlaştırılması planlanıyor.[SEP]
```


</details>

## Sample 10

<details>
<summary> web / en / short / 0.3 </summary>

### Original Text

```
Marvel Studios announced a new series coming to Disney+ in early 2025. Titled *Eclipse*, the show will focus on a previously unknown hero in the MCU. The cast includes rising star Mia Chen in the lead role. Filming is set to begin in Vancouver this August. Fans have already begun speculating about the character’s connection to the existing universe. More details will be revealed at San Diego Comic-Con.
```

### Masked Text

```
[CLS]Marvel Studios[MASK]nounced a new series coming to Dis[MASK][MASK] in [MASK]ly 2[MASK]25. Tit[MASK] *Eclip[MASK][MASK] the show will focus[MASK]a previously un[MASK][MASK]hero [MASK][MASK]U[MASK][MASK][MASK] inclu[MASK][MASK]ing s[MASK] Mia [MASK]en in the lead role. Film[MASK] is set to begin [MASK]Vancouv[MASK]this August. Fans have [MASK]read[MASK] b[MASK]un speculat[MASK] about the [MASK][MASK][MASK]s[MASK]nection [MASK]existing universe.[MASK]ore details will be revealed at[MASK][MASK][MASK]ego[MASK]ic-Con[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Marvel Studios[an]nounced a new series coming to Dis[ney][for] in [formal]ly 2[0]25. Tit[led] *Eclip[se][*,] the show will focus[on]a previously un[know][n]hero [,][A]U[.][,][,] inclu[ding][Amaz]ing s[tar] Mia [w]en in the lead role. Film[ing] is set to begin [*]Vancouv[er]this August. Fans have [al]read[y] b[eg]un speculat[ing] about the [#][film][']s[con]nection [s in the]existing universe.[M]ore details will be revealed at[#][an][Di]ego[Com]ic-Con[.][SEP]
```


</details>

## Sample 11

<details>
<summary> creative / tr / short / 0.3 </summary>

### Original Text

```
Eski kütüphaneci her sabah aynı saatte gelir, sessizce raflar arasında dolaşırdı. Kimsenin fark etmediği şey, onun sadece kitapları okumadığı, aynı zamanda kitapların ona fısıldadığı sırları dinlediğiydi. Gecenin karanlığında, sayfalardaki karakterler canlanır, kütüphanenin koridorlarında yürürlerdi. Yaşlı adam bu gizli dünyayın tek tanığıydı ve bu yüzden asla emekli olmayı kabul etmemişti. Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten konuşuyor mu?" diye sordu. O gün kütüphaneci ilk kez gülümsedi ve "Dinlemeyi bilen kulaklar için her şey mümkün" dedi.
```

### Masked Text

```
[CLS][MASK]kütüphaneci her sabah aynı saatte [MASK][MASK] sessizce raf[MASK]dolaşırdı. Kimsenin fark etmediği [MASK], onun sadece kitapları [MASK][MASK], aynı zamanda [MASK]ona fısıldadığı sırları dinled[MASK]iydi. Gecenin karan[MASK],[MASK]lardaki karakterler [MASK]lanır, kütüphan[MASK]koridorlarında yürür[MASK].[MASK][MASK] bu gizli dünyayın tek tan[MASK]ıydı ve bu yüzden asla emekli olmayı kabul etmemişti. Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten [MASK] mu?" diye sordu. O gün kütüphan[MASK]ilk kez gülümsedi ve "[MASK]lemeyi [MASK]kulaklar için her şey mümkün[MASK][MASK][MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][bir]kütüphaneci her sabah aynı saatte [,][,] sessizce raf[lar arasında]dolaşırdı. Kimsenin fark etmediği [şey], onun sadece kitapları [,][değil], aynı zamanda [kitapların]ona fısıldadığı sırları dinled[iğ]iydi. Gecenin karan[lığında],[kitap]lardaki karakterler [sak]lanır, kütüphan[enin]koridorlarında yürür[lerdi].[O][,] bu gizli dünyayın tek tan[ığ]ıydı ve bu yüzden asla emekli olmayı kabul etmemişti. Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten [okuyor] mu?" diye sordu. O gün kütüphan[eci]ilk kez gülümsedi ve "[Din]lemeyi [seven]kulaklar için her şey mümkün["][dedi][.][SEP]
```


</details>

## Sample 12

<details>
<summary> article / tr / short / 0.3 </summary>

### Original Text

```
Bu çalışmada, üniversite öğrencilerinin dijital öğrenme platformlarına yönelik tutumları ve akademik başarıları arasındaki ilişki incelenmiştir. Araştırma, 2023-2024 eğitim-öğretim yılında İstanbul'daki üç farklı üniversiteden 150 öğrenci ile yürütülmüştür. Veri toplama araçları olarak "Dijital Öğrenme Tutum Ölçeği" ve "Akademik Başarı Değerlendirme Formu" kullanılmıştır. Bulgular, dijital platformlara karşı olumlu tutum sergileyen öğrencilerin akademik başarı puanlarının anlamlı düzeyde yüksek olduğunu göstermiştir (p<0.05). Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital öğrenme tutumları arasında pozitif korelasyon tespit edilmiştir. Bu sonuçlar, eğitim kurumlarının dijital dönüşüm stratejilerini planlarken öğrenci profillerini dikkate alması gerektiğini ortaya koymaktadır.
```

### Masked Text

```
[CLS]Bu [MASK][MASK] üniversite [MASK]dijital öğrenme platformlarına yönelik tutum[MASK]akademik başarıları [MASK][MASK]. Araştırma,[MASK]2[MASK]23[MASK]2[MASK]24 eğitim-öğretim yılında İstanbul'daki [MASK]üniversiteden 150 öğrenci ile yürütülmüştür[MASK] Veri toplama araçları [MASK] "Dijital Öğrenme Tutum Ölçeği" ve "Akademik Başarı Değerlendirme Formu[MASK] kullanılmıştır. Bulgular[MASK] dijital platformlara karşı olumlu [MASK]eyen [MASK]akademik başarı puanlarının anlamlı düzeyde yüksek [MASK][MASK]p<0.0[MASK][MASK] Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital öğrenme [MASK]ları arasında pozitif[MASK]tespit edilmiştir. Bu sonuçlar[MASK] eğitim kurumlarının dijital dönüşüm stratejilerini planlarken öğrenci profil[MASK]dikkate alması gerektiğini ortaya koymaktadır.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu [,][,] üniversite [öğrencilerinin]dijital öğrenme platformlarına yönelik tutum[ları ve]akademik başarıları ["][incelenmiştir]. Araştırma,[]2[0]23[-]2[0]24 eğitim-öğretim yılında İstanbul'daki [üç farklı]üniversiteden 150 öğrenci ile yürütülmüştür[.] Veri toplama araçları [,] "Dijital Öğrenme Tutum Ölçeği" ve "Akademik Başarı Değerlendirme Formu["] kullanılmıştır. Bulgular[,] dijital platformlara karşı olumlu [tutum sergil]eyen [öğrencilerin]akademik başarı puanlarının anlamlı düzeyde yüksek [olduğunu göstermiştir][(]p<0.0[5][).] Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital öğrenme [yönelik tutum]ları arasında pozitif[ilişki]tespit edilmiştir. Bu sonuçlar[,] eğitim kurumlarının dijital dönüşüm stratejilerini planlarken öğrenci profil[ini]dikkate alması gerektiğini ortaya koymaktadır.[SEP]
```


</details>

## Sample 13

<details>
<summary> thesis / tr / short / 0.3 </summary>

### Original Text

```
Bu araştırma, ortaokul öğrencilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır. Araştırma, İstanbul'daki bir devlet okulunda 7. sınıf öğrencileriyle yürütülmüştür. Deney grubundaki öğrencilere 8 hafta boyunca yapılandırılmış empati eğitimi uygulanmıştır. Kontrol grubuna herhangi bir müdahale yapılmamıştır. Araştırma verileri Sosyal Problem Çözme Envanteri ve Empati Ölçeği ile toplanmıştır. Bulgular, empati eğitiminin öğrencilerin sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.
```

### Masked Text

```
[CLS][MASK][MASK],[MASK][MASK]ilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır[MASK] Araştırma,[MASK]'daki bir devlet okulunda [MASK]. sınıf öğrenc[MASK][MASK][MASK] Deney grubundaki öğrencilere [MASK] hafta boyunca yapılandırılmış[MASK]i [MASK]uygulanmıştır[MASK] Kontrol grubuna herhangi bir müdahale yapılmamıştır[MASK] Araştırma verileri Sosyal Problem Çöz[MASK]Envanteri ve [MASK]pati Ölçeği [MASK]toplanmıştır.[MASK], empati eğitiminin [MASK]sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Bu][çalışma],[ortaokul][sınıf öğrenc]ilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır[.] Araştırma,[Ankara]'daki bir devlet okulunda [8]. sınıf öğrenc[ileri ile][gerçekleştirilmiştir][.] Deney grubundaki öğrencilere [6] hafta boyunca yapılandırılmış[empat]i [eğitimi]uygulanmıştır[.] Kontrol grubuna herhangi bir müdahale yapılmamıştır[.] Araştırma verileri Sosyal Problem Çöz[me]Envanteri ve [Em]pati Ölçeği [ile]toplanmıştır.[Sonuçlar], empati eğitiminin [öğrencilerin]sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.[SEP]
```


</details>

## Sample 14

<details>
<summary> parliment / tr / short / 0.3 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 105’inci Birleşimini açıyorum. Toplantı yeter sayısı vardır, görüşmelere başlıyoruz. Gündeme geçmeden önce üç sayın milletvekiline gündem dışı söz vereceğim. İlk söz, Hatay ilinin tarımsal sorunları hakkında söz isteyen Hatay Milletvekili Mehmet Öztürk’e aittir. Buyurun Sayın Öztürk. Sayın Başkan, değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği çiftçilerimizi ciddi şekilde zor durumda bırakmıştır. Özellikle zeytin ve narenciye üreticileri hem ihracat sıkıntısı yaşamakta hem de girdi maliyetleri karşısında ezilmektedir. Bu nedenle Tarım Bakanlığının bölgeye özel destek programı geliştirmesi elzem hâle gelmiştir.
```

### Masked Text

```
[CLS]Türkiye Büyük Millet Meclisinin 10[MASK]’[MASK]Birleş[MASK]açıyorum. Toplantı yeter[MASK]vardır[MASK][MASK][MASK]başlıyoruz. Gündeme geçmeden önce üç sayın milletvekil[MASK]gündem dışı [MASK]eceğim[MASK] İlk [MASK][MASK][MASK] ilinin tarımsal sorunları hakkında söz isteyen [MASK][MASK]Mehmet Öztürk’e aittir. Buyur[MASK]Öztürk. Sayın Başkan[MASK] değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği [MASK]çilerimizi ciddi şekilde zor durumda bırakmıştır.[MASK]zeytin ve [MASK]enciye üreticileri hem ihracat[MASK]yaşa[MASK]hem de [MASK]maliyetleri karşısında ezilmektedir. Bu nedenle Tarım Bakanlığının bölgeye özel [MASK]programı geliştir[MASK]elzem hâle [MASK].[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 10[6]’[nci]Birleş[imini]açıyorum. Toplantı yeter[sayısı]vardır[,][görüş][melere]başlıyoruz. Gündeme geçmeden önce üç sayın milletvekil[ine]gündem dışı [söz ver]eceğim[.] İlk [ki][,][Hatay] ilinin tarımsal sorunları hakkında söz isteyen [Hatay][Milletvekili]Mehmet Öztürk’e aittir. Buyur[un Sayın]Öztürk. Sayın Başkan[,] değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği [çift]çilerimizi ciddi şekilde zor durumda bırakmıştır.[Özellikle]zeytin ve [nar]enciye üreticileri hem ihracat[sorunu]yaşa[makta]hem de [girdi]maliyetleri karşısında ezilmektedir. Bu nedenle Tarım Bakanlığının bölgeye özel [mücadele]programı geliştir[mesi]elzem hâle [gelmiştir].[SEP]
```


</details>

## Sample 15

<details>
<summary> code / en / short / 0.3 </summary>

### Original Text

```
Design a Java class named `Book` that encapsulates book details such as `title`, `author`, and `price`. Implement proper getters and setters. Add a method to validate if the book price is within a logical range.

`java
public class Book {
    private String title;
    private String author;
    private double price;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price >= 0 && price <= 1000) {
            this.price = price;
        } else {
            throw new IllegalArgumentException("Price must be between 0 and 1000.");
        }
    }
}
`
```

### Masked Text

```
[CLS]Design a [MASK]ava class named `Book`[MASK] encapsulates book [MASK][MASK][MASK] such as `title`, `[MASK]hor`,[MASK] `price[MASK]. Implement proper getters and setters. Ad[MASK][MASK]method to validate if the book pr[MASK][MASK] within a logical range[MASK]`java[MASK][MASK] class Book[MASK]    private [MASK]ing title;
   [MASK]ate String[MASK]hor[MASK]    private double pr[MASK];

[MASK] public[MASK]ing[MASK]Title() {
        [MASK][MASK]le;
   [MASK][MASK] public[MASK][MASK][MASK]Title([MASK]ing[MASK]le)[MASK]        this[MASK]tit[MASK] =[MASK]le[MASK][MASK] }

   [MASK][MASK]ing getAuthor()[MASK]        [MASK]author;
    }

    public[MASK]oid setAut[MASK](String author)[MASK][MASK] this.author[MASK] aut[MASK];
    }

    public double [MASK]Price() {
[MASK][MASK]price;
   [MASK]   [MASK] v[MASK] setPric[MASK](do[MASK]pr[MASK]) {
[MASK]if ([MASK][MASK] >= 0 && price <= 1[MASK][MASK][MASK])[MASK]            this.pr[MASK][MASK][MASK]ice;
       [MASK] else {
            th[MASK] new IllegalArgument[MASK]cep[MASK]("Price [MASK]st be bet[MASK]0[MASK]1000.");
        }
    }
}
`[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Design a [J]ava class named `Book`[that] encapsulates book [s][paramet][ers] such as `title`, `[aut]hor`,[and] `price[`]. Implement proper getters and setters. Ad[d][a]method to validate if the book pr[ice][is] within a logical range[.]```java[][public] class Book[{]    private [Str]ing title;
   [priv]ate String[aut]hor[;]    private double pr[ice];

[] public[Str]ing[get]Title() {
        [return][tit]le;
   [}][] public[v][oid][set]Title([Str]ing[tit]le)[{]        this[.]tit[le] =[tit]le[;][] }

   [public][Str]ing getAuthor()[{]        [return]author;
    }

    public[v]oid setAut[hor](String author)[{][] this.author[=] aut[hor];
    }

    public double [get]Price() {
[retur][n]price;
   [}]   [public] v[oid] setPric[e](do[uble]pr[ice]) {
[]if ([pr][ice] >= 0 && price <= 1[0][0][0])[{]            this.pr[ice][=][pr]ice;
       [}] else {
            th[row] new IllegalArgument[Ex]cep[tion]("Price [mu]st be bet[ween]0[and]1000.");
        }
    }
}
```[SEP]
```


</details>

## Sample 16

<details>
<summary> math / en / short / 0.3 </summary>

### Original Text

```
A train 180 meters long is running at a speed of 72 km/h. how much time will it take to cross a platform 120 meters long? also, find the time it takes to pass a man standing on the platform.

a) 15 sec and 9 sec, b) 18 sec and 10 sec, c) 20 sec and 9 sec, d) 12 sec and 7 sec, e) none of these

"explanation:
length of train = 180 m
length of platform = 120 m
total distance to cross platform = 180 + 120 = 300 m

speed of train in m/s = (72 × 1000) / 3600 = 20 m/s

time to cross platform = 300 / 20 = 15 seconds
time to cross a man = 180 / 20 = 9 seconds

answer: option a\ 
```

### Masked Text

```
[CLS]A train 180 meters long[MASK] running at [MASK][MASK]eed of 72[MASK][MASK]h. how much[MASK]will[MASK] take to cros[MASK]platform[MASK]1[MASK][MASK][MASK]ers long[MASK] also, find the time it[MASK]es[MASK][MASK][MASK]man standing on the platform.

a[MASK] 1[MASK] sec and [MASK] sec, b) 18 sec and [MASK]0[MASK][MASK] c)[MASK]2[MASK][MASK] and 9 sec,[MASK])[MASK]12 sec and [MASK] sec, e) n[MASK]of thes[MASK]

"ex[MASK][MASK]:
length[MASK] train = 1[MASK]0 m[MASK]length of platform =[MASK][MASK]20[MASK]
total distance [MASK] cross platform =[MASK]180 + [MASK]20 = 300 m

speed of tra[MASK]in m/[MASK] =[MASK]72 × 1[MASK]00)[MASK] [MASK]6[MASK][MASK] =[MASK]2[MASK] m/s[MASK]time to cross platform[MASK][MASK]300 /[MASK]20 =[MASK]15 seconds
time [MASK][MASK][MASK][MASK]man =[MASK]180[MASK] [MASK]0 = 9 second[MASK]

ans[MASK]: option a\ [SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]A train 180 meters long[is] running at [some][sp]eed of 72[km][/]h. how much[time]will[it] take to cros[s a]platform[(]1[2][0][met]ers long[?] also, find the time it[tak]es[for][a][wo]man standing on the platform.

a[)] 1[5] sec and [no] sec, b) 18 sec and [1]0[sec][,] c)[]2[0][sec] and 9 sec,[d])[]12 sec and [x] sec, e) n[one]of thes[e]

"ex[plan][ation]:
length[of] train = 1[8]0 m[]length of platform =[][1]20[m]
total distance [=] cross platform =[]180 + [1]20 = 300 m

speed of tra[in]in m/[s] =[(]72 × 1[0]00)[/] []6[0][0] =[]2[0] m/s[]time to cross platform[=][]300 /[]20 =[]15 seconds
time [=][c][ing][wo]man =[]180[/] []0 = 9 second[s]

ans[wer]: option a\ [SEP]
```


</details>

## Sample 17

<details>
<summary> web / tr / short / 0.45 </summary>

### Original Text

```
Çevre ve Şehircilik Bakanlığı'nın öncülük ettiği "Yeşil Şehirler Projesi" 81 ilde hayata geçiriliyor. Proje kapsamında kent merkezlerinde park alanları genişletilirken, bisiklet yolları da artırılıyor. Belediyeler vatandaşlarla birlikte ağaçlandırma çalışmaları düzenleyerek çevre bilincini artırmaya odaklanıyor. İlk etapta İstanbul, Ankara ve İzmir'de pilot uygulamalar başlatıldı. Bu şehirlerdeki hava kalitesi ölçümleri olumlu sonuçlar vermeye başladı. Proje koordinatörü Dr. Elif Yaman, "Amacımız yaşam kalitesini artırarak sürdürülebilir şehirler oluşturmak" dedi. Gelecek yıl projenin tüm Türkiye'ye yaygınlaştırılması planlanıyor.
```

### Masked Text

```
[CLS][MASK]e ve Şehircilik [MASK]'nın [MASK]ettiği[MASK][MASK] Şehirler Projesi" 81[MASK][MASK]iliyor. Proje [MASK]kent merkezlerinde park [MASK]genişletilirken, bisiklet[MASK]ları da [MASK]ılıyor.[MASK][MASK]vatandaşlarla birlikte ağaç[MASK]çalışmaları [MASK]çevre [MASK][MASK]maya odaklanıyor[MASK] İlk [MASK]İstanbul, Ankar[MASK][MASK]'de [MASK][MASK][MASK][MASK]ıldı. Bu [MASK]lerdeki [MASK]kalitesi ölçümleri olumlu sonuçlar vermeye başladı.[MASK]koordinatör[MASK] Dr[MASK] Elif Yaman,[MASK]Amacımız[MASK] kalitesini [MASK][MASK][MASK]ler oluşturmak[MASK] dedi. Gelecek yıl[MASK][MASK] Türkiye'[MASK]yaygınlaştırılması planlanıyor[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Çevr]e ve Şehircilik [Bakanlığı]'nın [öncülük]ettiği["][Yeşil] Şehirler Projesi" 81[ilde][hayata geçir]iliyor. Proje [kapsamında]kent merkezlerinde park [lar]genişletilirken, bisiklet[park]ları da [artır]ılıyor.[Belediy][ler ve]vatandaşlarla birlikte ağaç[landırma]çalışmaları ["]çevre [][oluştur]maya odaklanıyor[.] İlk [önce]İstanbul, Ankar[a ve][İzmir]'de [,][pilot][ler][başlat]ıldı. Bu [şehir]lerdeki [çevre]kalitesi ölçümleri olumlu sonuçlar vermeye başladı.[Proje]koordinatör[ü] Dr[.] Elif Yaman,["]Amacımız[yaşam] kalitesini [artır][artıran][şehir]ler oluşturmak["] dedi. Gelecek yıl[projenin][tüm] Türkiye'[ye]yaygınlaştırılması planlanıyor[.][SEP]
```


</details>

## Sample 18

<details>
<summary> web / en / short / 0.45 </summary>

### Original Text

```
Marvel Studios announced a new series coming to Disney+ in early 2025. Titled *Eclipse*, the show will focus on a previously unknown hero in the MCU. The cast includes rising star Mia Chen in the lead role. Filming is set to begin in Vancouver this August. Fans have already begun speculating about the character’s connection to the existing universe. More details will be revealed at San Diego Comic-Con.
```

### Masked Text

```
[CLS]Marvel Stu[MASK]os announc[MASK]new[MASK][MASK] coming to Disney+ in early [MASK]025[MASK] Tit[MASK] *Eclipse*, the [MASK]ow will[MASK]oc[MASK] on [MASK]pr[MASK][MASK][MASK][MASK]known her[MASK][MASK]MCU.[MASK]cast inclu[MASK][MASK]ing s[MASK][MASK][MASK][MASK]en in the le[MASK] rol[MASK]. Filming[MASK][MASK] to b[MASK][MASK]in Vanco[MASK]er [MASK] August. F[MASK] have al[MASK]y begun spec[MASK]ing about[MASK]character[MASK]s[MASK][MASK]tion to the [MASK][MASK][MASK][MASK]iver[MASK]. More [MASK][MASK]s will be [MASK]ealed[MASK] S[MASK]Di[MASK] Comic-[MASK].[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Marvel Stu[di]os announc[ed a]new[ser][show] coming to Disney+ in early [2]025[.] Tit[led] *Eclipse*, the [sh]ow will[f]oc[us] on [to the]pr[evi][ous][well][-]known her[o][from the]MCU.[The]cast inclu[des][act]ing s[tar][and][and][e]en in the le[ad] rol[e]. Filming[is][set] to b[eg][in]in Vanco[uv]er [,] August. F[ans] have al[read]y begun spec[ulat]ing about[the]character[’]s[re][nec]tion to the [*][com][al][un]iver[se]. More [ev][ail]s will be [rev]ealed[at] S[an]Di[ego] Comic-[Con].[SEP]
```


</details>

## Sample 19

<details>
<summary> creative / tr / short / 0.45 </summary>

### Original Text

```
Eski kütüphaneci her sabah aynı saatte gelir, sessizce raflar arasında dolaşırdı. Kimsenin fark etmediği şey, onun sadece kitapları okumadığı, aynı zamanda kitapların ona fısıldadığı sırları dinlediğiydi. Gecenin karanlığında, sayfalardaki karakterler canlanır, kütüphanenin koridorlarında yürürlerdi. Yaşlı adam bu gizli dünyayın tek tanığıydı ve bu yüzden asla emekli olmayı kabul etmemişti. Bir gün genç bir kız ona yaklaştı ve "Kitaplar gerçekten konuşuyor mu?" diye sordu. O gün kütüphaneci ilk kez gülümsedi ve "Dinlemeyi bilen kulaklar için her şey mümkün" dedi.
```

### Masked Text

```
[CLS]Eski kütüphaneci [MASK] sabah aynı saatte gelir,[MASK][MASK]raflar arasında dolaşırdı. Kimsenin fark [MASK]şey, onun sadece [MASK]oku[MASK][MASK] aynı zamanda [MASK][MASK]fısılda[MASK][MASK][MASK]dinled[MASK]iydi[MASK] Gecenin karanlığında, sayfa[MASK]karakter[MASK]canlanır[MASK][MASK]enin koridor[MASK]yürür[MASK][MASK][MASK]adam bu gizli [MASK]yayın tek [MASK]ığıydı ve bu yüzden asla emekli [MASK]kabul etm[MASK]işti. Bir gün genç bir kız[MASK]yaklaş[MASK]ve "[MASK]lar gerçekten konuşuyor mu?"[MASK][MASK] O gün kütüphaneci ilk kez gülüm[MASK][MASK][MASK] "Dinlemeyi [MASK][MASK][MASK][MASK][MASK]" dedi[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Eski kütüphaneci [,] sabah aynı saatte gelir,[kütüphan][boyunca]raflar arasında dolaşırdı. Kimsenin fark [etmediği]şey, onun sadece ["]oku[madığı][,] aynı zamanda [,]["]fısılda[yan]["][da]dinled[iğ]iydi[.] Gecenin karanlığında, sayfa[lardaki]karakter[ler]canlanır[,][kütüphan]enin koridor[larında]yürür[dü][.][Yaşlı]adam bu gizli [-]yayın tek [bir tan]ığıydı ve bu yüzden asla emekli []kabul etm[em]işti. Bir gün genç bir kız[ona]yaklaş[tı]ve "[Kitap]lar gerçekten konuşuyor mu?"[diye sordu][.] O gün kütüphaneci ilk kez gülüm[sey][edi][ve] "Dinlemeyi [,][oku][mayı][öğren][seviyorum]" dedi[.][SEP]
```


</details>

## Sample 20

<details>
<summary> article / tr / short / 0.45 </summary>

### Original Text

```
Bu çalışmada, üniversite öğrencilerinin dijital öğrenme platformlarına yönelik tutumları ve akademik başarıları arasındaki ilişki incelenmiştir. Araştırma, 2023-2024 eğitim-öğretim yılında İstanbul'daki üç farklı üniversiteden 150 öğrenci ile yürütülmüştür. Veri toplama araçları olarak "Dijital Öğrenme Tutum Ölçeği" ve "Akademik Başarı Değerlendirme Formu" kullanılmıştır. Bulgular, dijital platformlara karşı olumlu tutum sergileyen öğrencilerin akademik başarı puanlarının anlamlı düzeyde yüksek olduğunu göstermiştir (p<0.05). Ayrıca, öğrencilerin yaş ve teknoloji kullanım deneyimi ile dijital öğrenme tutumları arasında pozitif korelasyon tespit edilmiştir. Bu sonuçlar, eğitim kurumlarının dijital dönüşüm stratejilerini planlarken öğrenci profillerini dikkate alması gerektiğini ortaya koymaktadır.
```

### Masked Text

```
[CLS]Bu [MASK],[MASK]öğrencilerinin [MASK]öğrenme [MASK][MASK]tutumları ve akademik başarıları arasındaki ilişki incelenmiştir. Araştırma, 2[MASK][MASK][MASK]-[MASK]024 eğitim-[MASK] yılında İstanbul[MASK][MASK]üç farklı üniversit[MASK]1[MASK][MASK] öğrenci ile [MASK]. Veri toplama araçları olarak "Dijital Öğrenme Tutum Ölçeği" ve "[MASK]Başarı Değerlendirme Formu[MASK] kullanılmıştır.[MASK], dijital platformlara karşı [MASK][MASK][MASK]öğrencilerin akademik başarı puanlarının [MASK][MASK][MASK] (p<0[MASK][MASK][MASK]). Ayrıca, öğrencilerin yaş ve [MASK][MASK] deneyimi ile [MASK][MASK][MASK]ları arasında [MASK][MASK]tespit edilmiştir. Bu sonuçlar, eğitim[MASK]dijital dönüşüm[MASK]ilerini planlarken öğrenci profil[MASK][MASK]alması gerektiğini ortaya koymaktadır.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu [çalışmada],[üniversite]öğrencilerinin ["]öğrenme ["][ye yönelik]tutumları ve akademik başarıları arasındaki ilişki incelenmiştir. Araştırma, 2[0][2][3]-[2]024 eğitim-[öğretim] yılında İstanbul['][daki]üç farklı üniversit[eden]1[0][0] öğrenci ile [gerçekleştirilmiştir]. Veri toplama araçları olarak "Dijital Öğrenme Tutum Ölçeği" ve "[Akademik]Başarı Değerlendirme Formu["] kullanılmıştır.[Araştırma sonucunda], dijital platformlara karşı [olumlu tutum][olumlu tutum][yüksek olan]öğrencilerin akademik başarı puanlarının [anlamlı düzeyde][daha yüksek][olduğunu göstermiştir] (p<0[.][0][5]). Ayrıca, öğrencilerin yaş ve [dijital][dijital] deneyimi ile ["][öğrenme][tutum]ları arasında [istatistiksel olarak anlamlı][anlamlı bir ilişki]tespit edilmiştir. Bu sonuçlar, eğitim[kurumlarının]dijital dönüşüm[stratej]ilerini planlarken öğrenci profil[ini][dikkate]alması gerektiğini ortaya koymaktadır.[SEP]
```


</details>

## Sample 21

<details>
<summary> thesis / tr / short / 0.45 </summary>

### Original Text

```
Bu araştırma, ortaokul öğrencilerinde empati eğitiminin sosyal problem çözme becerilerine etkisini incelemeyi amaçlamaktadır. Araştırma, İstanbul'daki bir devlet okulunda 7. sınıf öğrencileriyle yürütülmüştür. Deney grubundaki öğrencilere 8 hafta boyunca yapılandırılmış empati eğitimi uygulanmıştır. Kontrol grubuna herhangi bir müdahale yapılmamıştır. Araştırma verileri Sosyal Problem Çözme Envanteri ve Empati Ölçeği ile toplanmıştır. Bulgular, empati eğitiminin öğrencilerin sosyal problem çözme becerilerinde anlamlı bir artış sağladığını göstermektedir.
```

### Masked Text

```
[CLS][MASK]araştırma[MASK] ortaokul[MASK]ilerinde empati [MASK]sosyal[MASK]me becerilerine etkisini [MASK]amaçlamaktadır[MASK] Araştırma[MASK] İstanbul'daki bir [MASK]okulunda [MASK]. sınıf öğrencileriyle yürütülmüştür[MASK] Deney[MASK]öğrencilere 8 hafta boyunca [MASK] empati eğitimi [MASK][MASK] Kontrol[MASK][MASK][MASK]yapılmamıştır. Araştırma verileri [MASK][MASK][MASK]me [MASK][MASK]Empati Ölçeği ile [MASK][MASK] Bulgular, empat[MASK]eğitiminin öğrencilerin [MASK] problem çözme becerilerinde [MASK][MASK] sağladığını göstermektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Bu]araştırma[,] ortaokul[öğrenc]ilerinde empati [eğitiminin]sosyal[problem çöz]me becerilerine etkisini [incelemeyi]amaçlamaktadır[.] Araştırma[,] İstanbul'daki bir [ilköğretim]okulunda [8]. sınıf öğrencileriyle yürütülmüştür[.] Deney[grubundaki]öğrencilere 8 hafta boyunca [,] empati eğitimi [verilmiştir][.] Kontrol[grubuna][ise][eğitim]yapılmamıştır. Araştırma verileri [,][Sosyal][Görüş]me [-][nin]Empati Ölçeği ile [toplanmıştır][.] Bulgular, empat[i]eğitiminin öğrencilerin [sosyal] problem çözme becerilerinde [olumlu][artış] sağladığını göstermektedir.[SEP]
```


</details>

## Sample 22

<details>
<summary> parliment / tr / short / 0.45 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 105’inci Birleşimini açıyorum. Toplantı yeter sayısı vardır, görüşmelere başlıyoruz. Gündeme geçmeden önce üç sayın milletvekiline gündem dışı söz vereceğim. İlk söz, Hatay ilinin tarımsal sorunları hakkında söz isteyen Hatay Milletvekili Mehmet Öztürk’e aittir. Buyurun Sayın Öztürk. Sayın Başkan, değerli milletvekilleri; Hatay’da yaşanan kuraklık ve destekleme politikalarının yetersizliği çiftçilerimizi ciddi şekilde zor durumda bırakmıştır. Özellikle zeytin ve narenciye üreticileri hem ihracat sıkıntısı yaşamakta hem de girdi maliyetleri karşısında ezilmektedir. Bu nedenle Tarım Bakanlığının bölgeye özel destek programı geliştirmesi elzem hâle gelmiştir.
```

### Masked Text

```
[CLS][MASK]Büyük Millet Meclisinin 10[MASK][MASK]inci Bir[MASK]imini [MASK]ıyorum.[MASK]lantı yeter[MASK]vardır[MASK][MASK]melere [MASK][MASK].[MASK]deme [MASK]üç[MASK]ın milletvekiline [MASK] dışı [MASK][MASK][MASK][MASK]söz[MASK] Hatay[MASK]inin [MASK][MASK][MASK][MASK][MASK]Hatay[MASK]Mehmet[MASK][MASK]e aittir.[MASK]un Sayın Öztürk. Sayın Başkan,[MASK][MASK] Hatay’da yaşanan kurak[MASK]destekleme politikalarının yetersizliği çiftçilerimizi [MASK]zor durumda bırakmıştır[MASK][MASK]zeytin ve narenc[MASK]üreticileri [MASK][MASK] sıkıntısı yaşa[MASK]hem de [MASK][MASK][MASK]ez[MASK].[MASK][MASK] Bakan[MASK]bölgeye özel destek programı geliştirmesi [MASK] hâle gelmiştir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin 10[1][’]inci Bir[leş]imini [aç]ıyorum.[Top]lantı yeter[sayısı]vardır[.][Görüş]melere [][devam edeceğiz].[Gün]deme [(]üç[say]ın milletvekiline [)] dışı [][][.][İlk]söz[,] Hatay[il]inin [][.][.][.][adına]Hatay[Milletvekili]Mehmet[Öztürk][’]e aittir.[Buyur]un Sayın Öztürk. Sayın Başkan,[değerli milletvekilleri][;] Hatay’da yaşanan kurak[lık ve]destekleme politikalarının yetersizliği çiftçilerimizi []zor durumda bırakmıştır[.][Özellikle]zeytin ve narenc[iye]üreticileri [,][geçim] sıkıntısı yaşa[makta]hem de [][bu][altında]ez[ilmektedir].[Bu nedenle][Tarım] Bakan[lığının]bölgeye özel destek programı geliştirmesi [elzem] hâle gelmiştir.[SEP]
```


</details>

## Sample 23

<details>
<summary> code / en / short / 0.45 </summary>

### Original Text

```
Design a Java class named `Book` that encapsulates book details such as `title`, `author`, and `price`. Implement proper getters and setters. Add a method to validate if the book price is within a logical range.

`java
public class Book {
    private String title;
    private String author;
    private double price;

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        if (price >= 0 && price <= 1000) {
            this.price = price;
        } else {
            throw new IllegalArgumentException("Price must be between 0 and 1000.");
        }
    }
}
`
```

### Masked Text

```
[CLS]Design a Java [MASK] named[MASK]Bo[MASK][MASK] that enc[MASK]ulates bo[MASK]details such as `title`[MASK] `[MASK]hor`, and[MASK]pr[MASK][MASK]. Imp[MASK][MASK][MASK]get[MASK][MASK][MASK]ters.[MASK][MASK][MASK][MASK][MASK] to validate if the [MASK]ok [MASK][MASK]is with[MASK][MASK][MASK]range[MASK][MASK][MASK][MASK]
public[MASK][MASK][MASK][MASK][MASK][MASK] private String tit[MASK][MASK]    priv[MASK][MASK]ing[MASK][MASK];
    private double pr[MASK];

    public String getTit[MASK]()[MASK]        [MASK]title;
    }

    public[MASK]oid[MASK]Title[MASK]Str[MASK] title) {
        this.tit[MASK][MASK][MASK]le;
[MASK] }

    public Str[MASK] getAuthor()[MASK]        [MASK]aut[MASK][MASK][MASK][MASK][MASK] public void setAuthor(String[MASK]hor)[MASK]        this.author = author;
    }

   [MASK] double [MASK]Price()[MASK]        [MASK][MASK]ice;
    }

[MASK][MASK] void[MASK]Pric[MASK]([MASK][MASK][MASK]ice)[MASK]        if ([MASK]ice >=[MASK]0 &&[MASK]ice <= 1000[MASK] {
            this.price =[MASK][MASK][MASK][MASK] }[MASK][MASK][MASK][MASK] throw[MASK] IllegalArgumentEx[MASK][MASK]("Pr[MASK]must be [MASK]ween 0 and 1[MASK]00."[MASK]        }
[MASK] }
[MASK]`[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Design a Java [program] named[`]Bo[ok][`] that enc[aps]ulates bo[ok]details such as `title`[,] `[aut]hor`, and[`]pr[ice][`]. Imp[lement][the][tar]get[s and][char][ac]ters.[It][is][a][met][hod] to validate if the [`]ok [`][function]is with[in a][cer][tain]range[.][```][j][ava]
public[c][lass][Bo][ok][{][] private String tit[le][;]    priv[ate][Str]ing[aut][hor];
    private double pr[ice];

    public String getTit[le]()[{]        [return]title;
    }

    public[v]oid[set]Title[(]Str[ing] title) {
        this.tit[le][=][tit]le;
[] }

    public Str[ing] getAuthor()[{]        []aut[hor][;][][}][] public void setAuthor(String[aut]hor)[{]        this.author = author;
    }

   [] double [get]Price()[{]        [][pr]ice;
    }

[;][public] void[set]Pric[e]([do][uble][pr]ice)[{]        if ([pr]ice >=[]0 &&[pr]ice <= 1000[)] {
            this.price =[pr][ice][;][] }[el][se][{][] throw[new] IllegalArgumentEx[cep][tion]("Pr[ice]must be [bet]ween 0 and 1[0]00."[);]        }
[] }
[;]```[SEP]
```


</details>

## Sample 24

<details>
<summary> math / en / short / 0.45 </summary>

### Original Text

```
A train 180 meters long is running at a speed of 72 km/h. how much time will it take to cross a platform 120 meters long? also, find the time it takes to pass a man standing on the platform.

a) 15 sec and 9 sec, b) 18 sec and 10 sec, c) 20 sec and 9 sec, d) 12 sec and 7 sec, e) none of these

"explanation:
length of train = 180 m
length of platform = 120 m
total distance to cross platform = 180 + 120 = 300 m

speed of train in m/s = (72 × 1000) / 3600 = 20 m/s

time to cross platform = 300 / 20 = 15 seconds
time to cross a man = 180 / 20 = 9 seconds

answer: option a\ 
```

### Masked Text

```
[CLS]A tra[MASK]180[MASK]ers[MASK] is[MASK]un[MASK] at a speed of 72 km/h.[MASK] much[MASK][MASK][MASK] take to c[MASK]s a [MASK][MASK]1[MASK][MASK] meters long[MASK][MASK][MASK] find the time it tak[MASK] to pass a [MASK][MASK]ding[MASK][MASK].

a)[MASK][MASK][MASK] sec and 9 sec[MASK][MASK])[MASK][MASK]8 sec and 10 sec[MASK] c) 20[MASK] and 9 sec[MASK] d[MASK] 1[MASK] sec and [MASK] sec,[MASK][MASK][MASK]one of[MASK][MASK][MASK]

[MASK]ex[MASK]ation:
len[MASK][MASK][MASK]in = 18[MASK][MASK]
len[MASK] of platform[MASK] [MASK]2[MASK][MASK][MASK]total[MASK]istance to cross platform =[MASK][MASK][MASK]0[MASK] 1[MASK][MASK] =[MASK]3[MASK]0[MASK][MASK]sp[MASK] of tra[MASK]in m/s = (72[MASK] [MASK][MASK]00) / [MASK]6[MASK]0 = [MASK]0[MASK]/[MASK]

[MASK]to c[MASK] platform =[MASK]300 /[MASK]2[MASK] = 15 second[MASK][MASK]to cross a man =[MASK]180 / 2[MASK] = 9[MASK]onds

[MASK]wer:[MASK]tion a\ [SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]A tra[in]180[met]ers[long] is[r]un[ning] at a speed of 72 km/h.[How] much[time][it][it] take to c[ros]s a [way][a]1[8][0] meters long[tra][in][,] find the time it tak[es] to pass a [ir][inclu]ding[a][man].

a)[][1][5] sec and 9 sec[,][b])[][1]8 sec and 10 sec[,] c) 20[sec] and 9 sec[,] d[)] 1[5] sec and [9] sec,[e][sol][N]one of[these][ans][tion]

[er]ex[plan]ation:
len[gth][of][tra]in = 18[0][m]
len[gth] of platform[=] []2[0][m][]total[d]istance to cross platform =[][1][8]0[+] 1[8][0] =[]3[0]0[m][]sp[eed] of tra[in]in m/s = (72[*] [][3]00) / []6[0]0 = []0[km]/[s]

[time]to c[ross] platform =[]300 /[]2[0] = 15 second[s][time]to cross a man =[]180 / 2[0] = 9[sec]onds

[ans]wer:[op]tion a\ [SEP]
```


</details>

