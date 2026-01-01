# TabiBERT Checkpoint Evaluation Report

Generated on: **2025/07/13 20:24:23**

Text path: **inference/inference_dataset/mid_masked.json**

## Sample 1

<details>
<summary> web/tr / tr / mid / 0.15 </summary>

### Original Text

```
Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'nın eşsiz kaya oluşumları arasına gizlenmiş yeraltı şehirleri, binlerce yıllık bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder. İstanbul'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Topkapı Sarayı gibi yapılarla milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı, bu mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan müze ziyaretçi sayıları, hem bu mirasa olan ilginin göstergesi olmakta hem de turizm gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini dünya turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.
```

### Masked Text

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[MASK]eşsiz kaya oluşum[MASK]arasına gizlenmiş yer[MASK]şehirleri, binlerce [MASK]bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[MASK]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[MASK][MASK]gibi yapılar[MASK] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [MASK]oloji dünyasında çığ[MASK] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[MASK][MASK]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [MASK]özgünlüğü[MASK]iz[MASK]muhafaza edilmektedir. Artan [MASK]ziyaretçi sayıları, hem bu miras[MASK]ilginin göstergesi olmakta hem de [MASK] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[MASK]nin kültürel [MASK]liğini [MASK][MASK]açısından güçlü bir caz[MASK]merkezi [MASK]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce [yıllık]bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[tit]iz[bir şekilde]muhafaza edilmektedir. Artan [yerli ve yabancı]ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```


</details>

## Sample 2

<details>
<summary> web/en / en / mid / 0.15 </summary>

### Original Text

```
A small bakery in Portland has gone viral after a customer shared photos of their cat-shaped croissants. The bakery, called 'Whisker & Dough', reported a 300% increase in orders within 48 hours. Owner Jasmine Kim said she never expected the pastry to become a social media sensation. The croissants are handmade each morning and shaped with chocolate dough for the ears and tail. Customers are lining up as early as 6 a.m. to secure a batch. Online pre-orders are now booked two weeks in advance. Local news covered the story, and the bakery has since received interest from food blogs in Japan and France. Kim is planning to release a dog-shaped version next month. "We’re just having fun," she says. "If it makes people smile, it’s worth the effort."
```

### Masked Text

```
[CLS]A small bakery in Portland has gone vir[MASK]after [MASK]customer shar[MASK] photos of their cat-shaped croissants. The bak[MASK], called 'Whisker & Dough[MASK] reported a 30[MASK]% increase in orders within 48 hours. Owner Jasmine [MASK] said she nev[MASK]exp[MASK] the pastry[MASK] become a social media sensation. The [MASK]roissants are [MASK]made each morning and[MASK]hap[MASK] chocolate dough for the [MASK]ars and[MASK]il. Customers are lining up as early as 6 a.m. to secure [MASK]batch. Online pre-orders are now booked two we[MASK] in advance. Local news covered the story,[MASK]bakery has s[MASK]received interest from[MASK] blogs in Japan [MASK] Fran[MASK]. Kim is plan[MASK] to r[MASK]ase a dog-shaped version next month. "We’[MASK]just having fun," she says. "If it makes people [MASK]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [a]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[,'] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [Kim] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[are]hap[ed with] chocolate dough for the [e]ars and[gr]il. Customers are lining up as early as 6 a.m. to secure [a]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[food] blogs in Japan [&] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [s]mile, it’s worth the effort."[SEP]
```


</details>

## Sample 3

<details>
<summary> creative / tr / mid / 0.15 </summary>

### Original Text

```
Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf bir ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise geleceğin belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir ettirirler, ama asla saatçinin içinde yaşadığı bu zamansız dünyayı fark etmezlerdi. Bir gün garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı. "Bu saati tamir edebilir misiniz?" diye sordu, ama saatçi hemen anladı ki bu sıradan bir tamirci işi değildi. Saat durmuş gibiydi, ama aslında çok farklı bir zamanda tiklaklıyordu. Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine ait unutulmuş anları. Müşteri gülümseyerek "Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği sadece mekanik bir iş değil, aslında insanların kayıp anlarını bulma sanatıydı. Akşam dükkânı kapatırken, tüm saatlerin aynı anda çalmaya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.
```

### Masked Text

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[MASK]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [MASK]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[MASK]irler, ama asla saatçinin içinde yaşadığı bu [MASK]sız[MASK][MASK]etmezlerdi.[MASK]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.[MASK]Bu saati tamir edebilir misiniz[MASK] diye sordu, ama saatçi hemen anladı [MASK]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[MASK][MASK]çok farklı bir zamanda tiklaklıyordu[MASK] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [MASK]unutulmuş anları. Müşteri [MASK][MASK] "Bazı saatler sadece zamanı [MASK][MASK] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [MASK]mekanik bir iş değil,[MASK]insanların kayıp[MASK][MASK]bulma sanatıydı. Akşam dükkânı kapatırken,[MASK] saatlerin aynı anda çalmaya başladığını duydu - bu,[MASK]zamanın başlang[MASK]müjdesiydi[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [zamanın]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu []sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][şimdi]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[aynı zamanda]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```


</details>

## Sample 4

<details>
<summary> article / tr / mid / 0.15 </summary>

### Original Text

```
Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu oluşturmaktadır. Son yirmi yılda hızla büyüyen Türk şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara, İzmir ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem nicel hem de nitel veriler toplanmıştır. Belediye yetkilileri, şehir planlamaları uzmanları ve çevre aktivistleri ile derinlemesine görüşmeler yapılmıştır. Kentsel yeşil alan oranları, toplu taşıma kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir'in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ise en büyük potansiyele sahip olmasına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak değerlendirilmiştir. Bu araştırmanın bulguları, Türkiye'deki kentsel planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.
```

### Masked Text

```
[CLS]Türkiye'[MASK]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [MASK]. Son [MASK]yılda hızla büyüyen Türk şehirlerinde[MASK] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[MASK] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[MASK]el hem de nitel veriler toplanmıştır[MASK] Belediye yetkilileri, şehir planlamaları [MASK]ları ve çevre aktivistleri ile derinlemesine [MASK]yapılmıştır.[MASK][MASK]alan oranları, toplu [MASK]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[MASK]in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [MASK]en büyük [MASK][MASK]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[MASK]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [MASK][MASK]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[MASK] Türkiye'deki [MASK]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [yirmi]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kır][eşil]alan oranları, toplu [ca]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük [ler arasında][yer al]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][hedef]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```


</details>

## Sample 5

<details>
<summary> thesis / tr / mid / 0.15 </summary>

### Original Text

```
Bu yüksek lisans tezinde, tip 2 diyabet hastalarında düzenli egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Polikliniği'nde yürütülmüş ve 50 gönüllü hasta katılmıştır. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir. Veriler, HbA1c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak toplanmıştır. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz grubunda HbA1c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca, bu gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir. Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur olduğunu göstermektedir. Bulgular, bireylerin yaşam kalitesini artıracak sağlık politikaları için yol gösterici olabilir. Araştırmanın önerileri, benzer hasta gruplarında daha uzun süreli takip çalışmaları yapılmasını içermektedir.
```

### Masked Text

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[MASK][MASK]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [MASK]dokrinoloji Polikliniği'[MASK]yürütülmüş ve 50 gönüllü hasta [MASK]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [MASK]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[MASK] Veriler, HbA[MASK]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [MASK]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[MASK]HbA[MASK]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[MASK]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[MASK] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[MASK]. Bulgular, bireylerin yaşam kalitesini [MASK]acak sağlık [MASK]ları için yol gösterici olabilir. Araştırmanın önerileri[MASK][MASK]hasta [MASK]daha [MASK]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [süresince]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [eğitim program]ları için yol gösterici olabilir. Araştırmanın önerileri[,][bu]hasta [lar üzerinde]daha [kapsamlı]takip çalışmaları yapılmasını içermektedir.[SEP]
```


</details>

## Sample 6

<details>
<summary> parliment / tr / mid / 0.15 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 112’nci Birleşimini açıyorum. Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı ilk söz, Erzurum’da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili Ayşe Kaya’ya aittir. Buyurun Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim, özellikle kırsal bölgelerde ciddi sorun hâline gelmiştir. Pek çok köyümüzde haftalarca doktor gelmemekte, mevcut sağlık ocakları ise personel yetersizliği nedeniyle çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve Araştırma Hastanesi’nin kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır. Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkezlerinin kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle, bütçede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden gelinmemesi gerektiğini buradan bir kez daha hatırlatıyorum. Hepinizi saygıyla selamlıyorum.
```

### Masked Text

```
[CLS]Türkiye Büyük Millet Meclisinin 112[MASK]nci Birleşimini aç[MASK]. Toplantı yeter sayısı vardır,[MASK]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [MASK]söz, Erzurum[MASK]da yaşanan sağlık hizmetleri [MASK][MASK][MASK] isteyen Erzurum Milletvekili Ayşe Kaya’ya [MASK][MASK][MASK]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [MASK]sağlık hizmetlerine [MASK], özellikle [MASK] bölgelerde [MASK]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [MASK] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [MASK]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [MASK]Hastanesi’[MASK]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[MASK] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[MASK]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[MASK][MASK]. Sayın milletvekilleri;[MASK]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[MASK]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[MASK]yaşadığı bu sorunların görmezden [MASK]memesi [MASK]buradan bir kez daha [MASK]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [ilk]söz, Erzurum[’]da yaşanan sağlık hizmetleri [][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [aittir][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve []sağlık hizmetlerine [erişim], özellikle [,] bölgelerde [büyük bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [doktor] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve []Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][sağlanmalıdır]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```


</details>

## Sample 7

<details>
<summary> code / en / mid / 0.15 </summary>

### Original Text

```
Build a simple Node.js server using Express that manages a to-do list. Include middleware for logging requests, route handling for getting and posting tasks, and a dummy in-memory database. Comment the logic clearly for readability.

`javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON and log requests
app.use(express.json());
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// In-memory to-do list
let todos = [
    { id: 1, task: 'Learn Node.js', completed: false },
    { id: 2, task: 'Build an API', completed: false }
];

// GET all to-dos
app.get('/todos', (req, res) => {
    res.json(todos);
});

// POST a new to-do
app.post('/todos', (req, res) => {
    const { task } = req.body;
    if (!task) {
        return res.status(400).json({ error: 'Task is required' });
    }
    const newTodo = {
        id: todos.length + 1,
        task,
        completed: false
    };
    todos.push(newTodo);
    res.status(201).json(newTodo);
});

// Mark a to-do as completed
app.patch('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const todo = todos.find(t => t.id === id);
    if (!todo) {
        return res.status(404).json({ error: 'To-do not found' });
    }
    todo.completed = true;
    res.json(todo);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
`
```

### Masked Text

```
[CLS]Build a simple Node.js[MASK]ver using Express that manages a to-do list[MASK] Include middleware for logging requests, route handling for getting and posting tasks, and a dummy in-memory[MASK]tabase. Comment the logic clear[MASK] for readability.

`javascript
const express =[MASK]quire('express');
const app = express();
const port[MASK] 3000;

// Midd[MASK]ware to parse [MASK]SON and log re[MASK]ests
app.use(express.json());
app.use((re[MASK], res, next) => {
    console[MASK]log([MASK]${req.method} ${[MASK]q.url}`);
    n[MASK]([MASK]});

// In-memory[MASK]-do list[MASK]let todos =[MASK][MASK]   [MASK] id:[MASK][MASK],[MASK]k: 'Lear[MASK]Node.js', completed: false },
   [MASK] id: 2, task: 'Build an API', completed: false }
][MASK]// GET[MASK] to[MASK]dos
app.get('/todos', (req, res) => {
    [MASK].json[MASK]todos);
[MASK]);

// POST a [MASK] to-do
app.post[MASK]/todos[MASK] (re[MASK], res) => {
[MASK]const { task[MASK] = req.body;
    if (!task) {
        return res.status[MASK]400).json({ error[MASK] 'Task is requir[MASK]' });
    }
    const[MASK]Todo = {
[MASK]id[MASK][MASK]odos.length + 1,
        tas[MASK],
        completed: false
    };
[MASK] todos.push(newTodo);
    res.status(20[MASK][MASK]json(newT[MASK]o);
});

// Mark a to-do as[MASK]leted
app.patch('/todos/:id', (req, res) => {
    const id =[MASK]seInt(re[MASK].params.id);
    const todo[MASK] todos.[MASK]ind(t => t.id === id);
    if (!todo) {
        [MASK]res.status(404).j[MASK]([MASK] error: 'To[MASK]do not found' });
    }
[MASK] todo.[MASK]leted[MASK] true;
    res.json(tod[MASK]);
});

app.[MASK]isten(port, () =>[MASK]    console.log(`Server running[MASK] http[MASK]localhost:${port}`);
});
`[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Build a simple Node.js[ser]ver using Express that manages a to-do list[.] Include middleware for logging requests, route handling for getting and posting tasks, and a dummy in-memory[da]tabase. Comment the logic clear[ly] for readability.

```javascript
const express =[re]quire('express');
const app = express();
const port[=] 3000;

// Midd[le]ware to parse [J]SON and log re[qu]ests
app.use(express.json());
app.use((re[q], res, next) => {
    console[.]log([`]${req.method} ${[re]q.url}`);
    n[ext]([);]});

// In-memory[to]-do list[]let todos =[[][[]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[all] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [new] to-do
app.post[(']/todos[',] (re[q], res) => {
[]const { task[}] = req.body;
    if (!task) {
        return res.status[(]400).json({ error[:] 'Task is requir[ed]' });
    }
    const[new]Todo = {
[]id[:][t]odos.length + 1,
        tas[k],
        completed: false
    };
[] todos.push(newTodo);
    res.status(20[0][).]json(newT[od]o);
});

// Mark a to-do as[comp]leted
app.patch('/todos/:id', (req, res) => {
    const id =[par]seInt(re[q].params.id);
    const todo[=] todos.[f]ind(t => t.id === id);
    if (!todo) {
        [return]res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[);] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[:] http[://]localhost:${port}`);
});
```[SEP]
```


</details>

## Sample 8

<details>
<summary> math / en / mid / 0.15 </summary>

### Original Text

```
Find the least number which when divided by 6, 9, 15, and 18 leaves a remainder 5 in each case.

a) 365, b) 185, c) 173, d) 365, e) none of these

"explanation:
we are asked to find the least number that leaves a remainder of 5 when divided by 6, 9, 15, and 18. this means the number is 5 more than a common multiple of those numbers.

step 1: find the lcm of 6, 9, 15, and 18.

prime factorizations:
6 = 2 × 3
9 = 3²
15 = 3 × 5
18 = 2 × 3²

lcm = 2 × 3² × 5 = 90

step 2: add the remainder 5 to the lcm
required number = 90 + 5 = 95

check:
95 ÷ 6 = 15 remainder 5
95 ÷ 9 = 10 remainder 5
95 ÷ 15 = 6 remainder 5
95 ÷ 18 = 5 remainder 5

answer: none of the listed options match; correct answer is 95 → option e"
```

### Masked Text

```
[CLS]F[MASK] the least number [MASK] when divided by 6, 9,[MASK]15, and 18 le[MASK]es a remaind[MASK]5 in each case.

a) 3[MASK]5[MASK] b) 185, c) 173, d) 365,[MASK]) none of these

"explanation:
[MASK]are [MASK][MASK] find the least number that leaves a remainder of 5 when divided by[MASK]6, 9, 15, and 18.[MASK] means the number [MASK]5 more than a common multiple of those numbers.

[MASK] 1: find the lcm of 6, 9, 15,[MASK]1[MASK].

prime factorizations[MASK]6[MASK] 2 × 3
[MASK] = 3²
[MASK]5[MASK][MASK][MASK] ×[MASK]5
1[MASK][MASK] 2 ×[MASK]3²

lcm = 2 × 3²[MASK] 5 = 90[MASK]step 2:[MASK]d the re[MASK]inder 5 to the lcm[MASK][MASK]quired number = 90 + [MASK] = 95

check:
95 ÷ 6 = 15 re[MASK]inder 5
9[MASK] ÷[MASK]9 = 10 remainder 5
95 ÷ 15 = 6[MASK]mainder 5
95 ÷ 18 =[MASK]5 re[MASK]inder 5

answer: none of the listed options match; cor[MASK]t [MASK]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]F[ind] the least number [that] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[=] 2 × 3
[²] = 3²
[]5[=][][2] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[.][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```


</details>

## Sample 9

<details>
<summary> web/tr / tr / mid / 0.3 </summary>

### Original Text

```
Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'nın eşsiz kaya oluşumları arasına gizlenmiş yeraltı şehirleri, binlerce yıllık bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder. İstanbul'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Topkapı Sarayı gibi yapılarla milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı, bu mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan müze ziyaretçi sayıları, hem bu mirasa olan ilginin göstergesi olmakta hem de turizm gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini dünya turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.
```

### Masked Text

```
[CLS]Türkiye[MASK]nin zengin kültürel[MASK]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[MASK] Kapadokya'[MASK]eşsiz[MASK]oluşumları arasına gizlen[MASK][MASK]altı şehirleri,[MASK]yıllık bir tarihe ev sahipliği yapar[MASK] H[MASK]apolis-[MASK][MASK]'[MASK][MASK][MASK] havuzları ise yüzyıllardır[MASK]büyül[MASK]devam eder[MASK] İstanbul[MASK][MASK][MASK]yarımada[MASK][MASK][MASK] ve Osmanlı medeniyetlerinin [MASK]taşıyarak Ayasofya, Sultan Ahmet Cami[MASK]Top[MASK]Sarayı gibi yapılar[MASK] milyonlarca ziyaretçiyi ağırlar. Göbek[MASK]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[MASK]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[MASK] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[MASK]asyon[MASK]uluslararası standart[MASK][MASK]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan [MASK]ziyaretçi sayıları,[MASK][MASK]mirasa olan [MASK]göstergesi olmakta [MASK][MASK] gelirlerine [MASK][MASK][MASK] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [MASK]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[E][fes]'[nın][eşsiz][termal] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilgisinin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [,]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```


</details>

## Sample 10

<details>
<summary> web/en / en / mid / 0.3 </summary>

### Original Text

```
A small bakery in Portland has gone viral after a customer shared photos of their cat-shaped croissants. The bakery, called 'Whisker & Dough', reported a 300% increase in orders within 48 hours. Owner Jasmine Kim said she never expected the pastry to become a social media sensation. The croissants are handmade each morning and shaped with chocolate dough for the ears and tail. Customers are lining up as early as 6 a.m. to secure a batch. Online pre-orders are now booked two weeks in advance. Local news covered the story, and the bakery has since received interest from food blogs in Japan and France. Kim is planning to release a dog-shaped version next month. "We’re just having fun," she says. "If it makes people smile, it’s worth the effort."
```

### Masked Text

```
[CLS][MASK] small bakery in [MASK]land has g[MASK]viral after [MASK]customer shared photos of[MASK][MASK]at-[MASK]haped crois[MASK][MASK]. The [MASK]ery, cal[MASK] 'W[MASK]ker &[MASK]ugh',[MASK]orted[MASK][MASK]0[MASK]%[MASK]rease in orders within 4[MASK] hour[MASK].[MASK]w[MASK][MASK]asmine Kim[MASK] she nev[MASK]expected the pas[MASK] to become a social media sen[MASK]ion. The [MASK]ro[MASK][MASK]ts are handma[MASK]each morning and[MASK]hap[MASK] c[MASK]olate [MASK][MASK][MASK][MASK][MASK][MASK] tail. Customers[MASK]lining up as e[MASK]ly[MASK] [MASK] a.m. to secure [MASK]batch. Online pre[MASK]orders are now book[MASK] t[MASK]weeks[MASK][MASK]van[MASK]. Local new[MASK][MASK]vered the st[MASK][MASK] and the bakery has since received[MASK]est from food blog[MASK]Japan and Fran[MASK]. Kim is[MASK]ning to release a dog-shaped ver[MASK]next[MASK]th. "We’re [MASK] hav[MASK] fun[MASK] she says[MASK] "If it makes people smile, it’s worth[MASK][MASK][MASK]t."[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][A] small bakery in [-]land has g[one]viral after [a]customer shared photos of[their][c]at-[s]haped crois[san][ts]. The [a bak]ery, cal[led] 'W[his]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[The]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [C]ro[is][san]ts are handma[de]each morning and[s]hap[ed with] c[hoc]olate [-][like][ed][ed][on][and] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [a]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ory][,] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [all] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```


</details>

## Sample 11

<details>
<summary> creative / tr / mid / 0.3 </summary>

### Original Text

```
Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf bir ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise geleceğin belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir ettirirler, ama asla saatçinin içinde yaşadığı bu zamansız dünyayı fark etmezlerdi. Bir gün garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı. "Bu saati tamir edebilir misiniz?" diye sordu, ama saatçi hemen anladı ki bu sıradan bir tamirci işi değildi. Saat durmuş gibiydi, ama aslında çok farklı bir zamanda tiklaklıyordu. Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine ait unutulmuş anları. Müşteri gülümseyerek "Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği sadece mekanik bir iş değil, aslında insanların kayıp anlarını bulma sanatıydı. Akşam dükkânı kapatırken, tüm saatlerin aynı anda çalmaya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.
```

### Masked Text

```
[CLS]Şehrin [MASK]sokağ[MASK]yaşayan saatçi, zamanla tuhaf bir ilişki kur[MASK]. Her sabah dükkânını açarken,[MASK]lardaki saat[MASK]tik-takları ona farklı hikâyeler [MASK]dı. Bazıları geçmişten [MASK]hüzünlü melod[MASK]di[MASK] bazıları ise geleceğin belirsizliğini fısıldayan endiş[MASK][MASK]lerdi.[MASK] geçtikçe,[MASK]çi bu sesleri [MASK][MASK]öğrenmişti. Müşter[MASK]gelir, saatlerini tamir[MASK]irler[MASK] ama asla saatçinin içinde [MASK][MASK]zamansız dünyayı fark etmezlerdi. Bir gün garip[MASK]müşteri girdi dükkâna[MASK][MASK]kırık bir cep saati vardı[MASK] "[MASK]saati [MASK] edebilir misiniz[MASK] diye sordu[MASK] ama saatçi [MASK]anladı ki bu sıradan bir [MASK]ci [MASK]değildi. Saat durmuş gibiydi, ama aslında [MASK]farklı bir zamanda tik[MASK]lıyordu. Saatçi eline aldığında,[MASK]iden çocukluk anılarını gördü[MASK] kendi geçmişine ait [MASK][MASK] anları. Müşteri gülümseyerek "[MASK]saatler sadece zamanı göstermez[MASK] zamanı yaşatır[MASK] dedi. Saat[MASK]o gün anladı ki [MASK][MASK]mekanik bir iş değil[MASK] aslında insanların kayıp an[MASK]bulma sanat[MASK][MASK] Akşam[MASK][MASK]nı [MASK]ırken, tüm saatlerin [MASK]çalmaya başladığını duydu -[MASK], yeni bir [MASK]başlangıcının müjdesiydi[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[muştu]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten [gelen]hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][yaşamayı]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci [-]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[tak]lıyordu. Saatçi eline aldığında,[içer]iden çocukluk anılarını gördü[,] kendi geçmişine ait [o][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[,][dükkân]nı [laş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [günün]başlangıcının müjdesiydi[.][SEP]
```


</details>

## Sample 12

<details>
<summary> article / tr / mid / 0.3 </summary>

### Original Text

```
Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu oluşturmaktadır. Son yirmi yılda hızla büyüyen Türk şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara, İzmir ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem nicel hem de nitel veriler toplanmıştır. Belediye yetkilileri, şehir planlamaları uzmanları ve çevre aktivistleri ile derinlemesine görüşmeler yapılmıştır. Kentsel yeşil alan oranları, toplu taşıma kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir'in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ise en büyük potansiyele sahip olmasına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak değerlendirilmiştir. Bu araştırmanın bulguları, Türkiye'deki kentsel planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.
```

### Masked Text

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [MASK][MASK]temel konusunu oluşturmaktadır. Son yirmi yılda [MASK][MASK]en [MASK]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[MASK], İstanbul,[MASK][MASK][MASK] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[MASK]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[MASK]nitel veriler [MASK]. Belediye yetkilileri, şehir planlamaları [MASK]ları ve çevre [MASK][MASK]leri ile derinlemesine görüşmeler yapılmıştır[MASK][MASK] yeşil alan [MASK][MASK][MASK][MASK]kullanım düzey[MASK][MASK] programlarının etkinliği değerlendirilmiştir. Bulgular[MASK] İzmir'[MASK]sürdürülebilir planlama [MASK]en başarılı [MASK] olduğunu, İstanbul[MASK][MASK]ise en büyük potansiyele sahip olmasına rağmen [MASK]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[MASK] Çalışma sonucunda[MASK] sürdürülebilir kentsel planlama [MASK]yerel yönetimlerin [MASK]elerinin artırılması gerektiği önerilmiştir. Ayrıca[MASK][MASK] katılımının teşvik edilmesi ve [MASK]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [MASK]. Bu araştırmanın bulguları, Türkiye'deki [MASK]planlama [MASK]yeniden değerlendirilmesi için önemli veriler sunmaktadır[MASK][MASK]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][büyüy]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [aktiv][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][gelişim] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [aday] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [bazı]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [belirlenmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [politikalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```


</details>

## Sample 13

<details>
<summary> thesis / tr / mid / 0.3 </summary>

### Original Text

```
Bu yüksek lisans tezinde, tip 2 diyabet hastalarında düzenli egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Polikliniği'nde yürütülmüş ve 50 gönüllü hasta katılmıştır. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir. Veriler, HbA1c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak toplanmıştır. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz grubunda HbA1c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca, bu gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir. Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur olduğunu göstermektedir. Bulgular, bireylerin yaşam kalitesini artıracak sağlık politikaları için yol gösterici olabilir. Araştırmanın önerileri, benzer hasta gruplarında daha uzun süreli takip çalışmaları yapılmasını içermektedir.
```

### Masked Text

```
[CLS][MASK][MASK]inde,[MASK]2 diyabet[MASK]düzenli egzersizin glis[MASK]kontrol üzerindeki etkisi incelenmiştir. Araştırma[MASK] Ankara Üniversitesi Tıp Fakültesi En[MASK]rinoloji Pol[MASK]iği[MASK]nde yürütül[MASK]50 gönüllü hasta katılmıştır.[MASK]rastgele şekilde [MASK] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [MASK]3 gün [MASK]egzersiz programı uygulanmıştır. Kontrol[MASK]yalnızca [MASK][MASK]ikal tedavi devam ettirilmiştir[MASK] Veriler[MASK] HbA[MASK]c düzeyleri ve [MASK]zersiz[MASK] Ölçeği kullanılarak toplanmıştır. Uygulama [MASK]ölçümler[MASK]ılmıştır.[MASK] grubunda HbA[MASK]c[MASK]istatistiksel olarak anlamlı bir düşüş[MASK]lenmiştir (p<0.[MASK][MASK]). Ayrıca, bu gruptaki bireylerin egzersize [MASK][MASK]olumlu yönde değiştiği [MASK]. Çalışma[MASK] fiziksel aktivitenin diyabet yönetiminde [MASK]destekleyici unsur olduğunu göstermektedir.[MASK], bireylerin yaşam kalitesini artıracak [MASK]politikaları için yol gösterici olabilir. Araştırmanın [MASK]ileri[MASK] benzer hasta [MASK]daha uzun süreli takip çalışmaları [MASK]içermektedir[MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Bu][tez]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Tutum] Ölçeği kullanılarak toplanmıştır. Uygulama [öncesi ve sonrası]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeyinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [ilişkin][larının]olumlu yönde değiştiği [gözlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```


</details>

## Sample 14

<details>
<summary> parliment / tr / mid / 0.3 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 112’nci Birleşimini açıyorum. Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı ilk söz, Erzurum’da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili Ayşe Kaya’ya aittir. Buyurun Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim, özellikle kırsal bölgelerde ciddi sorun hâline gelmiştir. Pek çok köyümüzde haftalarca doktor gelmemekte, mevcut sağlık ocakları ise personel yetersizliği nedeniyle çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve Araştırma Hastanesi’nin kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır. Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkezlerinin kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle, bütçede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden gelinmemesi gerektiğini buradan bir kez daha hatırlatıyorum. Hepinizi saygıyla selamlıyorum.
```

### Masked Text

```
[CLS]Türkiye Büyük Millet Meclisinin [MASK]12’[MASK]Bir[MASK]imini açıyorum[MASK] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [MASK],[MASK]geçmeden önce gündem dışı [MASK]lar için üç say[MASK]milletvekiline söz ver[MASK]. Gündem[MASK]ilk söz, Erzurum[MASK]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [MASK]Kaya’ya aittir.[MASK]un Sayın Kaya[MASK] Sayın Başkan,[MASK]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[MASK] özellikle kırsal[MASK]ciddi sorun hâline gelmiştir. Pek çok [MASK][MASK]haftalarca doktor gelmemekte[MASK][MASK] sağlık [MASK]ları ise personel yetersizliği nedeniyle çalış[MASK]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[MASK][MASK][MASK]Araştırma Hastanesi’nin kapasitesi her geçen gün [MASK]makta, hastalar sevk [MASK]mek zorunda kalmaktadır. Ayrıca [MASK] sayısının [MASK]ılması ve yeni aile sağlığı merkez[MASK]kurulması gerekmektedir. Sağlık [MASK]lığının, Doğu Anadolu Bölgesi[MASK]ne özel[MASK]iklerle doktor[MASK]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [MASK]şehirlerin değil, tüm yurttaşlarımızın hakk[MASK]. Bu nedenle,[MASK][MASK]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [MASK]memesi [MASK]buradan bir kez daha [MASK]ıyorum[MASK] Hep[MASK]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin [1]12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Ali]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][eye]haftalarca doktor gelmemekte[,][diğer] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[klin]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [belirli]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```


</details>

## Sample 15

<details>
<summary> code / en / mid / 0.3 </summary>

### Original Text

```
Build a simple Node.js server using Express that manages a to-do list. Include middleware for logging requests, route handling for getting and posting tasks, and a dummy in-memory database. Comment the logic clearly for readability.

`javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON and log requests
app.use(express.json());
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// In-memory to-do list
let todos = [
    { id: 1, task: 'Learn Node.js', completed: false },
    { id: 2, task: 'Build an API', completed: false }
];

// GET all to-dos
app.get('/todos', (req, res) => {
    res.json(todos);
});

// POST a new to-do
app.post('/todos', (req, res) => {
    const { task } = req.body;
    if (!task) {
        return res.status(400).json({ error: 'Task is required' });
    }
    const newTodo = {
        id: todos.length + 1,
        task,
        completed: false
    };
    todos.push(newTodo);
    res.status(201).json(newTodo);
});

// Mark a to-do as completed
app.patch('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const todo = todos.find(t => t.id === id);
    if (!todo) {
        return res.status(404).json({ error: 'To-do not found' });
    }
    todo.completed = true;
    res.json(todo);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
`
```

### Masked Text

```
[CLS]Build a simple Node[MASK]js server [MASK] Ex[MASK] that[MASK]ages a [MASK]-[MASK]o list. Inc[MASK]de middleware for logging requests[MASK] route [MASK]ling[MASK][MASK]ett[MASK][MASK][MASK]tasks,[MASK] a dummy[MASK]-memory database. Com[MASK] the logic[MASK][MASK]ly for readability.

`javascript
const express = requ[MASK][MASK]express');
const[MASK][MASK] = express[MASK]);
const port = 3000;

// Mid[MASK]leware [MASK] parse [MASK][MASK]ON and log requests
app.[MASK][MASK]ex[MASK].j[MASK]());
app.[MASK]((req,[MASK],[MASK]ext) => {
[MASK][MASK]sole[MASK][MASK][MASK][MASK]${[MASK]q[MASK]met[MASK]} ${req.[MASK]l}`);
[MASK] next();
}[MASK]// In-memory to-do list
let todos[MASK] [
    { id:[MASK]1[MASK][MASK]k:[MASK][MASK]earn No[MASK][MASK]j[MASK]', completed[MASK][MASK]se[MASK],
[MASK][MASK] id[MASK] 2[MASK][MASK]k: 'Build[MASK]AP[MASK][MASK] complet[MASK][MASK] fal[MASK][MASK]];

// GET all to-dos
app.[MASK]('/todos',[MASK]req[MASK][MASK]) => {
    res[MASK][MASK]son[MASK]todos);
[MASK]);

// POST a [MASK][MASK]-do
[MASK].post[MASK][MASK]t[MASK]', ([MASK]q[MASK] res) => {
    const { task[MASK] = req.[MASK]ody;
[MASK][MASK][MASK]![MASK][MASK]) {
        return res.[MASK]us(400).json[MASK][MASK] error: 'Task is requir[MASK]' });
    }
    [MASK][MASK][MASK][MASK]o =[MASK]        id: t[MASK][MASK][MASK]gth + [MASK],
        task[MASK]        comp[MASK]ed: false
    };
    todos.push[MASK][MASK]Tod[MASK]);
[MASK]res.status(201).json([MASK]Todo[MASK]}[MASK]// Mark a [MASK]-do as completed[MASK][MASK][MASK]patch('/[MASK]odos/[MASK]id[MASK][MASK]req[MASK][MASK][MASK] => {
    [MASK] id = parse[MASK]t(req.params.id[MASK]    const[MASK]od[MASK] = todos[MASK]find[MASK]t => t[MASK]id ===[MASK]);
    if (!tod[MASK]) {
        return res.status([MASK][MASK]4).[MASK][MASK]({ er[MASK][MASK] '[MASK]-[MASK] not f[MASK][MASK][MASK]);
    }
    todo.[MASK]leted = t[MASK];
    [MASK][MASK][MASK]son[MASK][MASK]odo);
}[MASK]app.listen[MASK]port, () => {
    console.log[MASK]`[MASK]ver running at[MASK][MASK]localhost:${port}`);
[MASK]);
`[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Build a simple Node[.]js server [such as] Ex[press] that[man]ages a [To]-[d]o list. Inc[lu]de middleware for logging requests[,] route [-]ling[,][s]ett[ing the][r][ing]tasks,[and] a dummy[in]-memory database. Com[ment] the logic[pr][oper]ly for readability.

```javascript
const express = requ[ire][(']express');
const[ap][p] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[log][(]ex[press].j[son]());
app.[run]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[][{] id[:] 2[,][tas]k: 'Build[the]AP[I][',] complet[ed][:] fal[se][}]];

// GET all to-dos
app.[get]('/todos',[(]req[,][res]) => {
    res[.][j]son[(]todos);
[}]);

// POST a [-][to]-do
[].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [var][let][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][new]Tod[o]);
[]res.status(201).json([new]Todo[);]}[);]// Mark a [*]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[http][://]localhost:${port}`);
[}]);
```[SEP]
```


</details>

## Sample 16

<details>
<summary> math / en / mid / 0.3 </summary>

### Original Text

```
Find the least number which when divided by 6, 9, 15, and 18 leaves a remainder 5 in each case.

a) 365, b) 185, c) 173, d) 365, e) none of these

"explanation:
we are asked to find the least number that leaves a remainder of 5 when divided by 6, 9, 15, and 18. this means the number is 5 more than a common multiple of those numbers.

step 1: find the lcm of 6, 9, 15, and 18.

prime factorizations:
6 = 2 × 3
9 = 3²
15 = 3 × 5
18 = 2 × 3²

lcm = 2 × 3² × 5 = 90

step 2: add the remainder 5 to the lcm
required number = 90 + 5 = 95

check:
95 ÷ 6 = 15 remainder 5
95 ÷ 9 = 10 remainder 5
95 ÷ 15 = 6 remainder 5
95 ÷ 18 = 5 remainder 5

answer: none of the listed options match; correct answer is 95 → option e"
```

### Masked Text

```
[CLS][MASK]ind the least[MASK][MASK]which when divided by 6[MASK] 9, 15, and 18[MASK]av[MASK] a remainder 5 in [MASK] c[MASK].

a[MASK] 365, b) 185, c) 173,[MASK]) [MASK]65, e)[MASK]one of these

[MASK]ex[MASK]ation:
we [MASK]asked to find[MASK][MASK]ast[MASK][MASK]that leaves[MASK]remaind[MASK][MASK] 5 when divided by [MASK][MASK][MASK]9,[MASK]1[MASK][MASK] and 18[MASK] this means the number is 5 more than [MASK][MASK]mon multiple [MASK][MASK]num[MASK].

step[MASK]1: find the [MASK]cm[MASK][MASK],[MASK]9[MASK] 15, and 18.

pr[MASK]factoriz[MASK]:
[MASK][MASK] 2 × 3
9 =[MASK]3²[MASK]1[MASK] =[MASK][MASK] × 5
1[MASK] = 2 × 3[MASK]

l[MASK] = 2[MASK] [MASK]² × 5 =[MASK]90[MASK][MASK] 2[MASK] add the re[MASK]ind[MASK]5 to the lcm
required[MASK][MASK] = [MASK][MASK] + 5 = [MASK][MASK]

check:
9[MASK] ÷ 6 = 15 remaind[MASK]5
[MASK][MASK] �[MASK] 9 = 10 remainder 5
95[MASK]� 15 = 6 remainder 5
[MASK][MASK][MASK]� 18[MASK] 5 remainder 5

ans[MASK]: none [MASK]listed op[MASK][MASK]match; correct [MASK]wer is 9[MASK] → option [MASK]"[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][F]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[cm].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than [(][com]mon multiple ["][of the]num[ber].

step[]1: find the [l]cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][2] × 5
1[8] = 2 × 3[²]

l[cm] = 2[x] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[num][ue] = [][5] + 5 = [][9]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][6] �[>] 9 = 10 remainder 5
95[0]� 15 = 6 remainder 5
[][6][5]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[5] → option [e]"[SEP]
```


</details>

## Sample 17

<details>
<summary> web/tr / tr / mid / 0.45 </summary>

### Original Text

```
Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'nın eşsiz kaya oluşumları arasına gizlenmiş yeraltı şehirleri, binlerce yıllık bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder. İstanbul'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Topkapı Sarayı gibi yapılarla milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı, bu mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan müze ziyaretçi sayıları, hem bu mirasa olan ilginin göstergesi olmakta hem de turizm gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini dünya turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.
```

### Masked Text

```
[CLS]Türkiye'nin [MASK][MASK] mirası[MASK][MASK]ESCO tarafından dünya çapında [MASK]makta ve korun[MASK].[MASK]adokya[MASK][MASK][MASK][MASK][MASK][MASK][MASK][MASK]miş yeraltı şehirleri,[MASK]yıllık [MASK]tarihe [MASK][MASK]. Hierapolis[MASK]Pamukkale'nin [MASK]termal havuzları ise [MASK][MASK] insanları büyülemeye [MASK]. İstanbul[MASK]un [MASK][MASK]madası,[MASK] ve Osmanlı [MASK][MASK]izlerini [MASK]Ayasofya[MASK] Sultan Ahmet Cami[MASK][MASK][MASK][MASK]gibi [MASK][MASK] milyonlarca ziyaretç[MASK]ağırlar[MASK] Göbeklitepe[MASK][MASK]keşfi de arkeoloji dünyasında [MASK][MASK] aç[MASK]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[MASK][MASK]miras[MASK]korunması adına sürekli [MASK][MASK]; restor[MASK][MASK]uluslararası [MASK][MASK]uygun şekilde [MASK][MASK]eserlerin özgünlüğü titizlikle [MASK]edilmektedir[MASK][MASK]müze [MASK][MASK]ıları, hem bu mirasa olan [MASK][MASK]olmakta hem de turizm gelirlerine ciddi [MASK].[MASK][MASK][MASK] Türkiye'nin [MASK][MASK]liğini dünya turizmi [MASK][MASK]caz[MASK]merkezi haline getirmeye [MASK][MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Türkiye'nin ["][kültür] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][,][,][,][gizlen]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe [tanıklık][sahiptir]. Hierapolis[ve]Pamukkale'nin []termal havuzları ise [,][yıllardır] insanları büyülemeye [devam etmektedir]. İstanbul[']un [tarihi][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][Sultan][kapı][Camii]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [yeni bir][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar yürüt][makta]; restor[asyon][çalışmaları]uluslararası [standart][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Yapılan]müze [][kaz]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[UN][ESCO][,] Türkiye'nin [eşsiz][zengin]liğini dünya turizmi [için][için]caz[ibe]merkezi haline getirmeye [devam etmektedir][.][SEP]
```


</details>

## Sample 18

<details>
<summary> web/en / en / mid / 0.45 </summary>

### Original Text

```
A small bakery in Portland has gone viral after a customer shared photos of their cat-shaped croissants. The bakery, called 'Whisker & Dough', reported a 300% increase in orders within 48 hours. Owner Jasmine Kim said she never expected the pastry to become a social media sensation. The croissants are handmade each morning and shaped with chocolate dough for the ears and tail. Customers are lining up as early as 6 a.m. to secure a batch. Online pre-orders are now booked two weeks in advance. Local news covered the story, and the bakery has since received interest from food blogs in Japan and France. Kim is planning to release a dog-shaped version next month. "We’re just having fun," she says. "If it makes people smile, it’s worth the effort."
```

### Masked Text

```
[CLS][MASK][MASK]mall bak[MASK][MASK][MASK]land[MASK][MASK]one viral af[MASK][MASK]customer[MASK]hared photos of their[MASK]at[MASK][MASK][MASK]ed[MASK][MASK]issants[MASK] The bakery[MASK] cal[MASK] '[MASK][MASK]ker & Dough',[MASK][MASK]ted a [MASK][MASK][MASK]% increase in [MASK]ders with[MASK][MASK]8[MASK][MASK]s.[MASK]wner J[MASK]mine Kim said[MASK][MASK]er [MASK][MASK] the [MASK]try[MASK] become a [MASK]ial media sen[MASK]ion.[MASK][MASK]ro[MASK]sants[MASK]hand[MASK]de each[MASK]ning and[MASK]haped with choc[MASK][MASK]do[MASK] for the ears and tail[MASK] Cust[MASK]ers[MASK]lining up[MASK] early as [MASK] a.[MASK]. to secure a batch[MASK][MASK]pre-orders are [MASK] booked two weeks[MASK][MASK]van[MASK][MASK] Loc[MASK][MASK]s co[MASK][MASK]story, and the bak[MASK][MASK] since r[MASK]ed interest from food blogs in Jap[MASK][MASK][MASK]ce. Kim [MASK] plan[MASK][MASK]r[MASK][MASK]a dog-[MASK]haped version next[MASK]th. "We[MASK]re [MASK] having fun[MASK] she says[MASK][MASK][MASK][MASK] makes people s[MASK][MASK], it’s worth the [MASK]fort."[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][A][s]mall bak[ery][in][Is]land[has][g]one viral af[ter][a]customer[s]hared photos of their[c]at[-][s][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][ic]ker & Dough',[rep][or]ted a [$][2][0]% increase in [or]ders with[in][1]8[h][our]s.[O]wner J[as]mine Kim said[the][ev]er [vis][ed] the ["]try[to] become a [']ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [about] a.[m]. to secure a batch[,][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][new]s co[ver][ed the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ning][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[’]re [all] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```


</details>

## Sample 19

<details>
<summary> creative / tr / mid / 0.45 </summary>

### Original Text

```
Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf bir ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise geleceğin belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir ettirirler, ama asla saatçinin içinde yaşadığı bu zamansız dünyayı fark etmezlerdi. Bir gün garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı. "Bu saati tamir edebilir misiniz?" diye sordu, ama saatçi hemen anladı ki bu sıradan bir tamirci işi değildi. Saat durmuş gibiydi, ama aslında çok farklı bir zamanda tiklaklıyordu. Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine ait unutulmuş anları. Müşteri gülümseyerek "Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği sadece mekanik bir iş değil, aslında insanların kayıp anlarını bulma sanatıydı. Akşam dükkânı kapatırken, tüm saatlerin aynı anda çalmaya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.
```

### Masked Text

```
[CLS]Şehrin [MASK]sokağ[MASK][MASK]saat[MASK], zamanla[MASK] bir ilişki kurmuştu. Her sabah dükkânını aç[MASK],[MASK]lardaki [MASK][MASK]tik-tak[MASK][MASK]farklı [MASK][MASK]anlatır[MASK].[MASK][MASK]gelen hüz[MASK] mel[MASK]iler[MASK],[MASK]ise geleceğin [MASK][MASK]fısıldayan endişeli [MASK]lerdi[MASK] Yıllar geç[MASK][MASK], saatçi bu sesleri ayırt etmeyi [MASK]mişti. Müşteriler gelir, saatlerini tamir ettirirler[MASK][MASK][MASK] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[MASK].[MASK]garip bir [MASK]girdi dükkân[MASK][MASK] elinde kırık bir [MASK] saati vardı[MASK] "Bu saati tamir edebilir misiniz[MASK] diye sordu[MASK] ama saatçi hemen [MASK]dı [MASK][MASK]tamir[MASK][MASK]değildi.[MASK][MASK][MASK] gibiydi,[MASK]aslında çok farklı bir zamanda tiklak[MASK].[MASK]çi [MASK]aldığında[MASK] an[MASK][MASK][MASK]ılarını gördü -[MASK]geçmişine [MASK]unutulmuş anları.[MASK][MASK][MASK][MASK]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [MASK]sadece mekan[MASK]iş değil,[MASK]insanların kayıp anlarını bulma [MASK]ıydı.[MASK][MASK][MASK][MASK][MASK]ırken[MASK] tüm[MASK]lerin aynı anda [MASK]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ının][yaşayan]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[duvar]lardaki [saat][zamanın]tik-tak["][çok]farklı [zaman][olduğunu]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [haber][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][ama][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [i]girdi dükkân[a][,] elinde kırık bir [duvar] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [yapama]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[tı].[Saat]çi [geri]aldığında[,] an[ı][geçmişin][an]ılarını gördü -[kendi]geçmişine [ait]unutulmuş anları.[Sonra][kendine][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [yas]ıydı.[Saat][saat][saat][ını][kapat]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```


</details>

## Sample 20

<details>
<summary> article / tr / mid / 0.45 </summary>

### Original Text

```
Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu oluşturmaktadır. Son yirmi yılda hızla büyüyen Türk şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara, İzmir ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem nicel hem de nitel veriler toplanmıştır. Belediye yetkilileri, şehir planlamaları uzmanları ve çevre aktivistleri ile derinlemesine görüşmeler yapılmıştır. Kentsel yeşil alan oranları, toplu taşıma kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir'in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ise en büyük potansiyele sahip olmasına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak değerlendirilmiştir. Bu araştırmanın bulguları, Türkiye'deki kentsel planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.
```

### Masked Text

```
[CLS][MASK]'[MASK]büyükşehirlerde [MASK] kentsel [MASK]uygulamalarının [MASK][MASK]gelişim potansiyeli [MASK]araştırmanın temel konusunu oluşturmaktadır[MASK] Son yirmi [MASK]hızla büyüyen Türk şehirlerinde,[MASK]dostu [MASK][MASK]benimsen[MASK]kritik bir [MASK].[MASK][MASK][MASK][MASK][MASK][MASK] İzmir ve Bursa olmak üzere dört büyük[MASK]kentsel planlama politikalarını karşılaştırmalı olarak [MASK] etmiştir. Araştırma [MASK][MASK]yaklaşım benimsen[MASK], hem nicel hem de [MASK]veriler [MASK][MASK] Belediye yetkilileri, şehir[MASK][MASK][MASK]ları ve çevre [MASK][MASK][MASK]derinlemesine görüşmeler [MASK].[MASK][MASK]alan oranları,[MASK]taşıma [MASK][MASK]leri ve [MASK][MASK]etkinliği [MASK][MASK][MASK], İzmir[MASK][MASK]sürdürülebilir planlama konusunda en başarılı metropol[MASK][MASK] İstanbul[MASK][MASK][MASK][MASK]potansiyele sahip ol[MASK]uygulamada zorluklar [MASK][MASK][MASK] Ankar[MASK]Bursa[MASK][MASK]orta düzeyde [MASK][MASK],[MASK][MASK]alanlarının [MASK][MASK][MASK][MASK]sonucunda[MASK][MASK] kentsel [MASK]için yerel yönetimlerin [MASK][MASK]artırılması [MASK][MASK][MASK][MASK], vatandaş katılımının teşvik [MASK]çok sektörlü işbirliğinin [MASK]kritik [MASK][MASK]değerlendirilmiştir. Bu araştırmanın bulguları,[MASK]'[MASK]kentsel planlama politikalarının [MASK]değerlendirilmesi için [MASK][MASK][MASK].[MASK]araştırmalarda,[MASK]ve orta [MASK][MASK]lerin de [MASK] kapsamına alınması [MASK][MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][ve]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [kentsel][politikaların]benimsen[mesi]kritik bir [konudur].[Araştırma][,][İstanbul][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehrin]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][karma]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[plan][planlama][cı]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kap][eşil]alan oranları,[]taşıma [][büyüklük]leri ve [kentsel][]etkinliği [,][][İstanbul], İzmir[ve][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][.] İstanbul['][un][,][yüksek]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][gözlenmiştir][.] Ankar[a ve]Bursa['][nın]orta düzeyde [.][Ancak],[kentsel][gelişme]alanlarının [][olduğu görülmüştür][.][Araştırmanın]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [][etkinliğinin]artırılması [,][yerel][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[de]kentsel planlama politikalarının []değerlendirilmesi için [,][önemli bir][önem taşımaktadır].[Gelecek]araştırmalarda,[küçük]ve orta [ölçekli][metropol]lerin de [,] kapsamına alınması [önerilmektedir][.][SEP]
```


</details>

## Sample 21

<details>
<summary> thesis / tr / mid / 0.45 </summary>

### Original Text

```
Bu yüksek lisans tezinde, tip 2 diyabet hastalarında düzenli egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Polikliniği'nde yürütülmüş ve 50 gönüllü hasta katılmıştır. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir. Veriler, HbA1c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak toplanmıştır. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz grubunda HbA1c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca, bu gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir. Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur olduğunu göstermektedir. Bulgular, bireylerin yaşam kalitesini artıracak sağlık politikaları için yol gösterici olabilir. Araştırmanın önerileri, benzer hasta gruplarında daha uzun süreli takip çalışmaları yapılmasını içermektedir.
```

### Masked Text

```
[CLS]Bu yüksek lisans tezinde, tip [MASK] diyabet hastalarında [MASK][MASK]sizin glisemik [MASK][MASK][MASK]incelenmiştir. Araştırma[MASK] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[MASK]iği'nde yürütülmüş ve [MASK][MASK] gönüllü hasta [MASK]. Katılımcılar rastgele [MASK][MASK] ve kontrol grubu [MASK][MASK]ayrılmıştır[MASK] Egzersiz[MASK]1[MASK] hafta [MASK]haftada [MASK] gün [MASK][MASK] programı uygulanmıştır.[MASK] grubuna yalnızca [MASK] medikal[MASK]devam ettirilmiştir.[MASK]iler[MASK][MASK][MASK]1c düzeyleri ve [MASK]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[MASK][MASK][MASK] karşılaştırılmıştır[MASK] Egzersiz grubunda [MASK][MASK][MASK][MASK] düzeyinde [MASK][MASK]düşüş göz[MASK] (p<[MASK].[MASK][MASK][MASK][MASK][MASK][MASK]gruptaki bireylerin egzer[MASK][MASK][MASK]olumlu yönde [MASK]belirlenmiştir. Çalışma, fiziksel aktivitenin [MASK][MASK][MASK]destekleyici [MASK][MASK][MASK] Bulgular,[MASK][MASK]artıracak sağlık politikaları için yol gösterici olabilir[MASK] Araştırmanın önerileri, benzer [MASK]gruplarında daha uzun süreli takip [MASK]yapılmasını [MASK].[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerindeki][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [olarak][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [(]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][A]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Deney ve kontrol][iki][iki grup] karşılaştırılmıştır[.] Egzersiz grubunda [Hb][Hb][1][c] düzeyinde [anlamlı][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][).][).][her iki]gruptaki bireylerin egzer[size][ilişkin][tutumlarının]olumlu yönde [etkilediği]belirlenmiştir. Çalışma, fiziksel aktivitenin [diyabet][diyabet][sağlığını]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[egzersiz][aktiviteyi]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [içermektedir].[SEP]
```


</details>

## Sample 22

<details>
<summary> parliment / tr / mid / 0.45 </summary>

### Original Text

```
Türkiye Büyük Millet Meclisinin 112’nci Birleşimini açıyorum. Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı ilk söz, Erzurum’da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili Ayşe Kaya’ya aittir. Buyurun Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim, özellikle kırsal bölgelerde ciddi sorun hâline gelmiştir. Pek çok köyümüzde haftalarca doktor gelmemekte, mevcut sağlık ocakları ise personel yetersizliği nedeniyle çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve Araştırma Hastanesi’nin kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır. Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkezlerinin kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle, bütçede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden gelinmemesi gerektiğini buradan bir kez daha hatırlatıyorum. Hepinizi saygıyla selamlıyorum.
```

### Masked Text

```
[CLS][MASK]Büyük Millet Meclisinin [MASK][MASK]2’[MASK][MASK][MASK][MASK]açıyorum. Toplantı yeter sayısı [MASK][MASK] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [MASK][MASK]konuşma[MASK]üç say[MASK]milletvekil[MASK]söz vereceğim[MASK] Gündem dışı ilk [MASK],[MASK]’da yaşanan [MASK]yetersizliği hakkında söz isteyen [MASK] Milletvekili [MASK][MASK][MASK][MASK]aittir[MASK] Buyurun Sayın Kaya. Sayın Başkan[MASK][MASK]; Erzurum ili ve ilçelerinde sağlık hizmet[MASK][MASK],[MASK]kırsal bölgelerde [MASK][MASK]hâline gelmiştir[MASK] Pek çok [MASK]ümüzde [MASK][MASK]doktor[MASK]memekte, mevcut[MASK][MASK][MASK]personel yetersizliği nedeniyle çalışamamaktadır[MASK] Bu durum[MASK]larımızın temel sağlık hakkına erişimini [MASK]. Erzurum[MASK][MASK]Hastanesi’nin kapasitesi [MASK]yetersiz kalmakta[MASK] hastalar sevk edilmek zorunda kalmaktadır[MASK][MASK]ambulans[MASK]artır[MASK][MASK][MASK][MASK][MASK]lerinin [MASK]gerekmektedir. Sağlık [MASK]lığının, Doğu Anadolu Bölgesi[MASK]ne [MASK] teşviklerle doktorları [MASK][MASK]büyük önem arz etmektedir[MASK] Sayın milletvekilleri; sağlık [MASK]büyük şehirlerin [MASK][MASK] tüm yurttaşlarımızın hakkıdır.[MASK],[MASK]ede kaynak [MASK][MASK]bölgesel eşitsizlik[MASK]göz önünde bulundur[MASK][MASK][MASK][MASK][MASK]bu sorunların görmezden gelin[MASK][MASK]buradan bir kez daha [MASK]ıyorum. Hep[MASK]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][0]2’[nci][birleş][um][imini]açıyorum. Toplantı yeter sayısı [bulun][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][dışı]konuşma[mak üzere]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [,][Kaya][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[i][erişim],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[gel]memekte, mevcut[doktor][larımız][lar da]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Bölge][Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayısının]artır[ılması ve][,][acil][sağlık][sefer]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [gönder][mesi]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [değil][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ulduğunda][,][,][,][,]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```


</details>

## Sample 23

<details>
<summary> code / en / mid / 0.45 </summary>

### Original Text

```
Build a simple Node.js server using Express that manages a to-do list. Include middleware for logging requests, route handling for getting and posting tasks, and a dummy in-memory database. Comment the logic clearly for readability.

`javascript
const express = require('express');
const app = express();
const port = 3000;

// Middleware to parse JSON and log requests
app.use(express.json());
app.use((req, res, next) => {
    console.log(`${req.method} ${req.url}`);
    next();
});

// In-memory to-do list
let todos = [
    { id: 1, task: 'Learn Node.js', completed: false },
    { id: 2, task: 'Build an API', completed: false }
];

// GET all to-dos
app.get('/todos', (req, res) => {
    res.json(todos);
});

// POST a new to-do
app.post('/todos', (req, res) => {
    const { task } = req.body;
    if (!task) {
        return res.status(400).json({ error: 'Task is required' });
    }
    const newTodo = {
        id: todos.length + 1,
        task,
        completed: false
    };
    todos.push(newTodo);
    res.status(201).json(newTodo);
});

// Mark a to-do as completed
app.patch('/todos/:id', (req, res) => {
    const id = parseInt(req.params.id);
    const todo = todos.find(t => t.id === id);
    if (!todo) {
        return res.status(404).json({ error: 'To-do not found' });
    }
    todo.completed = true;
    res.json(todo);
});

app.listen(port, () => {
    console.log(`Server running at http://localhost:${port}`);
});
`
```

### Masked Text

```
[CLS]Build[MASK][MASK][MASK]Node[MASK][MASK]s[MASK][MASK]using Express that man[MASK] a to-d[MASK]list[MASK] Include [MASK][MASK]le[MASK]for[MASK][MASK][MASK]quests, route handling for gett[MASK] posting tasks[MASK][MASK] a [MASK]my in-memory da[MASK]ase[MASK] Comment the logic clearly[MASK] readability[MASK]`j[MASK][MASK]cript
[MASK][MASK][MASK] = requ[MASK]('[MASK][MASK]');
const[MASK][MASK] = ex[MASK][MASK][MASK]const[MASK][MASK] [MASK][MASK]00[MASK]//[MASK][MASK]le[MASK][MASK][MASK]se [MASK][MASK]ON[MASK] log requests
[MASK].[MASK](ex[MASK][MASK]json());
app.use([MASK][MASK]q[MASK] res[MASK] next)[MASK] {
    [MASK]sole[MASK][MASK](`${[MASK]q.method}[MASK]{req[MASK][MASK]l[MASK]`);
    next();
}[MASK]// In-memory[MASK][MASK][MASK]o [MASK]
[MASK] todos[MASK] [
    { id:[MASK]1, task:[MASK]Learn No[MASK][MASK]js', completed[MASK] fal[MASK] },
    { id[MASK] 2, task: 'Build an API[MASK][MASK][MASK][MASK]: false[MASK][MASK][MASK][MASK] G[MASK][MASK] to[MASK]dos
[MASK][MASK]get('/t[MASK]', ([MASK]q[MASK] res) =>[MASK]    res[MASK][MASK]son([MASK]odos);
}[MASK]// POST a new to[MASK][MASK][MASK][MASK][MASK][MASK][MASK]/t[MASK][MASK][MASK][MASK][MASK][MASK] res) => {
    const { task[MASK][MASK] req[MASK]b[MASK][MASK]    [MASK] (!task)[MASK]        return [MASK].status(400).[MASK][MASK]({ er[MASK][MASK][MASK]Task [MASK] required'[MASK]);
    }
[MASK][MASK] newTod[MASK] = {
[MASK]id:[MASK]odos[MASK][MASK][MASK] +[MASK]1,
        task,
        completed[MASK] fal[MASK]
    };
   [MASK][MASK].[MASK]ush(new[MASK]odo);
    res.[MASK][MASK][MASK]2[MASK][MASK][MASK]json(newTod[MASK]);
});

//[MASK][MASK]a [MASK]-[MASK][MASK][MASK][MASK][MASK]ed
app.[MASK][MASK][MASK][MASK][MASK][MASK][MASK]:[MASK]', ([MASK][MASK][MASK] res) => {
    const id[MASK][MASK]seIn[MASK][MASK]req.[MASK]s.[MASK]);
    const[MASK][MASK]o =[MASK]odos[MASK][MASK]ind([MASK] => t[MASK]id ==[MASK][MASK]);
    if (![MASK][MASK]o) {
        return res.status(40[MASK]).j[MASK]({[MASK][MASK][MASK] 'To-[MASK] not found[MASK] }[MASK]    }
[MASK] todo[MASK]completed = true;
    [MASK][MASK]json[MASK][MASK][MASK]o[MASK]});

[MASK].[MASK]isten[MASK]port,[MASK][MASK] =>[MASK][MASK]con[MASK].log(`[MASK][MASK][MASK]ning[MASK][MASK][MASK]loc[MASK][MASK][MASK][MASK]{port}`);
}[MASK][MASK][SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]Build[a][sim][ple]Node[.][j]s[p][ule]using Express that man[ages] a to-d[o]list[.] Include [s a][hand]le[an]for[log][ging][re]quests, route handling for gett[ing and] posting tasks[,][and] a [dum]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][App] = requ[ire]('[ex][press]');
const[ex][port] = ex[press][(][);]const[stat][us] [][4]00[;]//[S][imp]le[][for][par]se [J][S]ON[and] log requests
[].[log](ex[press][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[da][-][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][]][;][//] G[ET][new] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][app][.][post][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][]    [if] (!task)[{]        return [res].status(400).[j][son]({ er[ror][:][']Task [s] required'[}]);
    }
[;][let] newTod[o] = {
[]id:[t]odos[.][id][]] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][odos].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][res][).]json(newTod[o]);
});

//[G][et]a [']-[d][to][list][comp][est]ed
app.[c][('][('][('][/][/][to]:[list]', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[param]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[=][id]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[;] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[app].[l]isten[(]port,[port][)] =>[{][]con[sole].log(`[Ex][o][run]ning[:][$][{]loc[al][port][:][$]{port}`);
}[);][```][SEP]
```


</details>

## Sample 24

<details>
<summary> math / en / mid / 0.45 </summary>

### Original Text

```
Find the least number which when divided by 6, 9, 15, and 18 leaves a remainder 5 in each case.

a) 365, b) 185, c) 173, d) 365, e) none of these

"explanation:
we are asked to find the least number that leaves a remainder of 5 when divided by 6, 9, 15, and 18. this means the number is 5 more than a common multiple of those numbers.

step 1: find the lcm of 6, 9, 15, and 18.

prime factorizations:
6 = 2 × 3
9 = 3²
15 = 3 × 5
18 = 2 × 3²

lcm = 2 × 3² × 5 = 90

step 2: add the remainder 5 to the lcm
required number = 90 + 5 = 95

check:
95 ÷ 6 = 15 remainder 5
95 ÷ 9 = 10 remainder 5
95 ÷ 15 = 6 remainder 5
95 ÷ 18 = 5 remainder 5

answer: none of the listed options match; correct answer is 95 → option e"
```

### Masked Text

```
[CLS]F[MASK] the [MASK]ast[MASK]ber which[MASK][MASK]vided[MASK] 6, 9,[MASK][MASK]5, and 18[MASK][MASK][MASK] a remaind[MASK]5 in [MASK] case[MASK]a) 365, b) 18[MASK][MASK][MASK]) 173,[MASK][MASK] 365[MASK][MASK][MASK] none [MASK][MASK][MASK]e

"explanation:
we [MASK][MASK]ed to find[MASK][MASK][MASK] num[MASK]that[MASK]aves a re[MASK]ind[MASK]of [MASK] when [MASK][MASK][MASK][MASK][MASK]6,[MASK][MASK],[MASK]1[MASK], and [MASK]8. this means the [MASK]ber [MASK][MASK] more than a common [MASK]iple [MASK][MASK]num[MASK][MASK][MASK] 1[MASK] find the l[MASK] of [MASK], [MASK], 1[MASK][MASK][MASK][MASK]8.

pr[MASK]factorizations:
6[MASK] 2 ×[MASK]3
9[MASK][MASK][MASK][MASK]
[MASK]5[MASK] [MASK] × [MASK][MASK]18[MASK][MASK][MASK][MASK][MASK]3²

lcm[MASK] 2[MASK][MASK][MASK][MASK][MASK][MASK]5[MASK][MASK]90

[MASK] 2: add the rema[MASK]er [MASK] to the l[MASK]
[MASK][MASK]ed number[MASK][MASK]90 +[MASK][MASK] = 95

check[MASK]9[MASK] �[MASK] 6 = 1[MASK] re[MASK][MASK]er 5[MASK]95[MASK][MASK][MASK]9 =[MASK][MASK]0[MASK]ma[MASK]er [MASK][MASK][MASK]5 ÷ 1[MASK] =[MASK][MASK] remainder 5
95[MASK]� [MASK]8 = 5[MASK]ma[MASK][MASK]5

[MASK][MASK]: n[MASK]of the [MASK]isted option[MASK]mat[MASK];[MASK]rect answer is [MASK][MASK] → option [MASK]"[SEP]
```

#### Checkpoint: ep0-ba5300-rank0.pt

```
[CLS]F[ind] the [le]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[and][av][es] a remaind[er]5 in [this] case[:]a) 365, b) 18[0][,][c]) 173,[d][)] 365[,][d][)] none [,][op][on]e

"explanation:
we ['][ne]ed to find[the][le][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [it][pro][vide][d][]6,[][9],[]1[5], and [1]8. this means the [num]ber [s][is] more than a common [mult]iple [.][the]num[ber][is][is] 1[.] find the l[cm] of [6], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[=][][2][×]
[]5[] [2] × [][]18[=][][2][×][]3²

lcm[=] 2[×][][3][0][][9]5[=][]90

[+] 2: add the rema[ind]er [5] to the l[eft]
[of the][x]ed number[][]90 +[][2] = 95

check[:]9[5] �[>] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [5][][9]5 ÷ 1[5] =[][5] remainder 5
95[5]� []8 = 5[re]ma[ind][er]5

[][return]: n[one]of the [l]isted option[s]mat[ch];[cor]rect answer is [n][one] → option [a]"[SEP]
```


</details>

