# TabiBERT Checkpoint Evaluation Report

Generated on: **2025/06/08 07:47:46**

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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce [yıllık]bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[la] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [ont]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek ["]özgünlüğü["]iz[olarak]muhafaza edilmektedir. Artan [an]ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [,] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[tit]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[ha]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[tit]iz[likle]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[ha]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[ha]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[tit]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce [yıllık]bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[tit]iz[likle]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[ha]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye'nin zengin kültürel mirası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır. Kapadokya'[nın]eşsiz kaya oluşum[ları]arasına gizlenmiş yer[altı]şehirleri, binlerce []bir tarihe ev sahipliği yapar. Hierapolis-Pamukkale'nin antik termal havuzları ise yüzyıllardır insanları büyülemeye devam eder.[İstanbul]'un tarihi yarımadası, Bizans ve Osmanlı medeniyetlerinin izlerini taşıyarak Ayasofya, Sultan Ahmet Camii ve Top[kapı][Sarayı]gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbeklitepe'nin keşfi de [arke]oloji dünyasında çığ[ır] açmış ve tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]mirasın korunması adına sürekli çalışmalar yürütmekte; restorasyonlar uluslararası standartlara uygun şekilde gerçekleştirilerek [,]özgünlüğü[ha]iz[bir şekilde]muhafaza edilmektedir. Artan []ziyaretçi sayıları, hem bu miras[a olan]ilginin göstergesi olmakta hem de [turizm] gelirlerine ciddi katkı sağlamaktadır. Tüm bu unsurlar, Türkiye[']nin kültürel [kim]liğini [,][turizmi]açısından güçlü bir caz[ibe]merkezi [haline getir]meye devam etmektedir.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[t]after [the]customer shar[ing] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ect] the pastry[to] become a social media sensation. The [oc]roissants are [one]made each morning and[s]hap[ed] chocolate dough for the [e]ars and[so]il. Customers are lining up as early as 6 a.m. to secure [-]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[the]bakery has s[ince]received interest from[their] blogs in Japan [,] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [-]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[es] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are []made each morning and[s]hap[ed] chocolate dough for the [at]ars and[so]il. Customers are lining up as early as 6 a.m. to secure [-]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[their] blogs in Japan [,] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [-]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed] chocolate dough for the [e]ars and[o]il. Customers are lining up as early as 6 a.m. to secure [a]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[its] blogs in Japan [&] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [‘]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed with] chocolate dough for the [j]ars and[so]il. Customers are lining up as early as 6 a.m. to secure [-]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[its] blogs in Japan [e and] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [‘]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are ["]made each morning and[s]hap[ed] chocolate dough for the [es]ars and[bas]il. Customers are lining up as early as 6 a.m. to secure [a]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[its] blogs in Japan [&] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [-]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed with] chocolate dough for the [j]ars and[o]il. Customers are lining up as early as 6 a.m. to secure [a]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[her] blogs in Japan [and] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [s]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed] chocolate dough for the [b]ars and[o]il. Customers are lining up as early as 6 a.m. to secure [a]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[her] blogs in Japan [,] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [-]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed] chocolate dough for the [e]ars and[o]il. Customers are lining up as early as 6 a.m. to secure [the]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[many] blogs in Japan [,] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [s]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed with] chocolate dough for the [b]ars and[o]il. Customers are lining up as early as 6 a.m. to secure [-]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[many] blogs in Japan [.] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [-]mile, it’s worth the effort."[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]A small bakery in Portland has gone vir[al]after [some]customer shar[ed] photos of their cat-shaped croissants. The bak[ery], called 'Whisker & Dough[',] reported a 30[0]% increase in orders within 48 hours. Owner Jasmine [,] said she nev[er]exp[ected] the pastry[to] become a social media sensation. The [C]roissants are [-]made each morning and[s]hap[ed with] chocolate dough for the [at]ars and[ma]il. Customers are lining up as early as 6 a.m. to secure [ing the]batch. Online pre-orders are now booked two we[eks] in advance. Local news covered the story,[and the]bakery has s[ince]received interest from[her] blogs in Japan [,] Fran[ce]. Kim is plan[ning] to r[ele]ase a dog-shaped version next month. "We’[re]just having fun," she says. "If it makes people [s]mile, it’s worth the effort."[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [zamanın]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [da]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][çi]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [-]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][tüm] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği ["]mekanik bir iş değil,[sıradan]insanların kayıp[olduğu][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [zamanın]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][sanki]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [-]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği ["]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][sanki]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [-]mekanik bir iş değil,[sıradan]insanların kayıp[zaman][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][inden]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][fakat] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geçmişin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][her seferinde]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [dala]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][ondan]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][lerini]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][ondan]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][-] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise []belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][inden]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][ondan]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][-] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Şehrin en eski sokağında yaşayan saatçi, zamanla tuhaf[bir]ilişki kurmuştu. Her sabah dükkânını açarken, duvarlardaki saatlerin tik-takları ona farklı hikâyeler anlatırdı. Bazıları geçmişten gelen hüzünlü melodilerdi, bazıları ise [geleceğin]belirsizliğini fısıldayan endişeli ritimlerdi. Yıllar geçtikçe, saatçi bu sesleri ayırt etmeyi öğrenmişti. Müşteriler gelir, saatlerini tamir[ettir]irler, ama asla saatçinin içinde yaşadığı bu [-]sız[lığı][fark]etmezlerdi.[Bir gün]garip bir müşteri girdi dükkâna; elinde kırık bir cep saati vardı.["]Bu saati tamir edebilir misiniz[?"] diye sordu, ama saatçi hemen anladı [-]sıradan bir tamirci işi değildi. Saat durmuş gibiydi,[ama][inden]çok farklı bir zamanda tiklaklıyordu[.] Saatçi eline aldığında, aniden çocukluk anılarını gördü - kendi geçmişine [ait]unutulmuş anları. Müşteri [,][ona] "Bazı saatler sadece zamanı [,][geçmiş] zamanı yaşatır" dedi. Saatçi o gün anladı ki mesleği [,]mekanik bir iş değil,[sıradan]insanların kayıp[an][larını]bulma sanatıydı. Akşam dükkânı kapatırken,[tüm] saatlerin aynı anda çalmaya başladığını duydu - bu,[yeni bir]zamanın başlang[ıcının]müjdesiydi[.][SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye'[de]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [dur]. Son [uncu]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Araştırmada][yeşil]alan oranları, toplu [-]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ["]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [on]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Ayrıca][yeşil]alan oranları, toplu [ma]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük [şehir][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [dur]. Son [on]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kentsel][eşil]alan oranları, toplu [ca]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [on]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kentsel][yeşil]alan oranları, toplu [laştırma]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ["]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [uncu]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kir][yeşil]alan oranları, toplu [ca]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ["]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [uncu]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kentsel][yeşil]alan oranları, toplu [ca]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un ["]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [uncu]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Ç][yeşil]alan oranları, toplu [ca]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][hedef]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [dur]. Son [uncu]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kır][eşil]alan oranları, toplu [-]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][hedef]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [yirmi]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kır][yeşil]alan oranları, toplu [-]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][öncelik]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye'[deki]büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli bu araştırmanın temel konusunu [oluşturmaktadır]. Son [yirmi]yılda hızla büyüyen Türk şehirlerinde[,] çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır. Bu çalışma, İstanbul, Ankara,[İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir. Araştırma yöntem olarak karma yaklaşım benimsenmiş, hem[nic]el hem de nitel veriler toplanmıştır[.] Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre aktivistleri ile derinlemesine [görüşmeler]yapılmıştır.[Kır][eşil]alan oranları, toplu [-]kullanım düzeyleri ve geri dönüşüm programlarının etkinliği değerlendirilmiştir. Bulgular, İzmir[']in sürdürülebilir planlama konusunda en başarılı metropol olduğunu, İstanbul'un [ise]en büyük ["][ol]masına rağmen uygulamada zorluklar yaşadığını göstermiştir. Ankar[a ve]Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir. Çalışma sonucunda, sürdürülebilir kentsel planlama için yerel yönetimlerin kapasitelerinin artırılması gerektiği önerilmiştir. Ayrıca, vatandaş katılımının teşvik edilmesi ve çok sektörlü işbirliğinin geliştirilmesi [önemli][çözüm]ler olarak değerlendirilmiştir. Bu araştırmanın bulguları[,] Türkiye'deki [kentsel]planlama politikalarının yeniden değerlendirilmesi için önemli veriler sunmaktadır. Gelecek araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[hastalarında][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da bir]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[Hb]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[ve C]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [çı]ları için yol gösterici olabilir. Araştırmanın önerileri[,][engelli]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[hasta][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da bir]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[-]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[/]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermektedir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [lı]ları için yol gösterici olabilir. Araştırmanın önerileri[,][gelecekte]hasta [lar üzerinde]daha [kapsamlı]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da bir]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermektedir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [lı]ları için yol gösterici olabilir. Araştırmanın önerileri[,][bu]hasta [lar üzerinde]daha [ve]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da bir]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermektedir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [çalışan]ları için yol gösterici olabilir. Araştırmanın önerileri[,][diğer]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da bir]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [çalışan]ları için yol gösterici olabilir. Araştırmanın önerileri[,][kanser]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [süre ile]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [çı]ları için yol gösterici olabilir. Araştırmanın önerileri[,][bu]hasta [larla]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [süreyle]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [uygulama]ları için yol gösterici olabilir. Araştırmanın önerileri[,][diğer]hasta [larla]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da ve]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [arttır]acak sağlık [grup]ları için yol gösterici olabilir. Araştırmanın önerileri[,][bu]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [da ve]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [değerlendirilmiştir]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [arttır]acak sağlık [çalışma]ları için yol gösterici olabilir. Araştırmanın önerileri[,][bu]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip 2 diyabet[li][bireylerde]egzersizin glisemik kontrol üzerindeki etkisi incelenmiştir. Araştırma, Ankara Üniversitesi Tıp Fakültesi [En]dokrinoloji Polikliniği'[nde]yürütülmüş ve 50 gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele şekilde egzersiz ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta [süreyle]haftada 3 gün aerobik egzersiz programı uygulanmıştır. Kontrol grubuna yalnızca standart medikal tedavi devam ettirilmiştir[.] Veriler, HbA[1]c düzeyleri ve Egzersiz Tutum Ölçeği kullanılarak [toplanmıştır]. Uygulama öncesi ve sonrası ölçümler karşılaştırılmıştır. Egzersiz[grubunda]HbA[1]c düzeyinde istatistiksel olarak anlamlı bir düşüş gözlenmiştir (p<0.05). Ayrıca,[her iki]gruptaki bireylerin egzersize yönelik tutumlarının da olumlu yönde değiştiği belirlenmiştir[.] Çalışma, fiziksel aktivitenin diyabet yönetiminde etkili bir destekleyici unsur[olduğunu göstermiştir]. Bulgular, bireylerin yaşam kalitesini [artır]acak sağlık [uygulama]ları için yol gösterici olabilir. Araştırmanın önerileri[,][diğer]hasta [lar üzerinde]daha [uzun süreli]takip çalışmaları yapılmasını içermektedir.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [-]söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [.][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [,] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve []Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][gerekmektedir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [(]söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [aittir][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [”], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [doktor] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][önemlidir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı []söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [aittir][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [hastalar] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][bilinmektedir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [ilk]söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [dır][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [hastalar] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][kabul edilemez]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [ilk]söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [dır][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [doktor] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][gerekmektedir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [haykır]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [ilk]söz, Erzurum[’]da yaşanan sağlık hizmetleri [][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [dır][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [doktor] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][doğru değildir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı []söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [dır][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [hastalar] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][bilinmektedir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı [“]söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [dır][Buyur][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [ambulans] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][önemlidir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı []söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya [aittir][.][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde []sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [lar] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve [Araştırma]Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][önemlidir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[luların]yaşadığı bu sorunların görmezden [gelin]memesi []buradan bir kez daha [hatırlat]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin 112[’]nci Birleşimini aç[ıyorum]. Toplantı yeter sayısı vardır,[gündeme]geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce gündem dışı konuşmalar için üç sayın milletvekiline söz vereceğim. Gündem dışı []söz, Erzurum[’]da yaşanan sağlık hizmetleri [”][hakkında][söz] isteyen Erzurum Milletvekili Ayşe Kaya’ya […][Buyur][Buyur]un Sayın Kaya. Sayın Başkan, değerli milletvekilleri; Erzurum ili ve [“]sağlık hizmetlerine [’], özellikle [,] bölgelerde [önemli bir]sorun hâline gelmiştir. Pek çok köyümüzde haftalarca [hastalar] gelmemekte, mevcut sağlık ocakları ise personel yetersizliği [nedeniyle]çalışamamaktadır. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir. Erzurum Eğitim ve []Hastanesi’[nin]kapasitesi her geçen gün yetersiz kalmakta, hastalar sevk edilmek zorunda kalmaktadır[.] Ayrıca ambulans sayısının artırılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık Bakanlığının, Doğu Anadolu Bölgesi’ne özel teşviklerle doktorları yönlendir[mesi][gerekmektedir]. Sayın milletvekilleri;[sağlık]sadece büyük şehirlerin değil, tüm yurttaşlarımızın hakkıdır. Bu nedenle,[bütç]ede kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum[halkının]yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum. Hepinizi saygıyla selamlıyorum.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[new] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [uth] to-do
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
[//] todos.push(newTodo);
    res.status(20[0][).]json(newT[od]o);
});

// Mark a to-do as[comp]leted
app.patch('/todos/:id', (req, res) => {
    const id =[par]seInt(re[q].params.id);
    const todo[=] todos.[f]ind(t => t.id === id);
    if (!todo) {
        [return]res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[,] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[:] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[ning]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[for] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [way] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[,] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[from] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[for] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [way] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[,] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[:] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

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
][;]// GET[for] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [way] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[//] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[with] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

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

// POST a [way] to-do
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
[//] todos.push(newTodo);
    res.status(20[0][).]json(newT[od]o);
});

// Mark a to-do as[comp]leted
app.patch('/todos/:id', (req, res) => {
    const id =[par]seInt(re[q].params.id);
    const todo[=] todos.[f]ind(t => t.id === id);
    if (!todo) {
        [return]res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[//] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[:] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[from] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [way] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[at] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[for] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [way] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[);] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[at] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[from] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [gent] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[);] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[at] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[from] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [gent] to-do
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
[//] todos.push(newTodo);
    res.status(20[0][).]json(newT[od]o);
});

// Mark a to-do as[comp]leted
app.patch('/todos/:id', (req, res) => {
    const id =[par]seInt(re[q].params.id);
    const todo[=] todos.[f]ind(t => t.id === id);
    if (!todo) {
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[;] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[:] http[://]localhost:${port}`);
});
```[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

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

// In-memory[to]-do list[]let todos =[[][{]   [{] id:[][1],[tas]k: 'Lear[n]Node.js', completed: false },
   [{] id: 2, task: 'Build an API', completed: false }
][;]// GET[from] to[-]dos
app.get('/todos', (req, res) => {
    [res].json[(]todos);
[}]);

// POST a [gent] to-do
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
        []res.status(404).j[son]([{] error: 'To[-]do not found' });
    }
[//] todo.[comp]leted[=] true;
    res.json(tod[o]);
});

app.[l]isten(port, () =>[{]    console.log(`Server running[at] http[://]localhost:${port}`);
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[there]are [,][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][6] ×[]5
1[0][=] 2 ×[]3²

lcm = 2 × 3²[+] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[.][re]quired number = 90 + [len] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rup]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[Step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][6] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[+] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[][re]quired number = 90 + [x] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[r]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][6] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[*] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[the][re]quired number = 90 + [x] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are ['][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][2] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[We]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][3] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [ability][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[×] 2 × 3
[²] = 3²
[]5[=][][2] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [x] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[=] 2 × 3
[²] = 3²
[]5[=][][9] ×[]5
1[8][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [a][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[=] 2 × 3
[²] = 3²
[]5[=][][3] ×[]5
1[5][=] 2 ×[]3²

lcm = 2 × 3²[*] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[rec]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are [,][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[=] 2 × 3
[²] = 3²
[]5[=][][9] ×[]5
1[5][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[r]t [ans]wer is 95 → option e"[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]F[ind] the least number [,] when divided by 6, 9,[]15, and 18 le[av]es a remaind[er]5 in each case.

a) 3[6]5[,] b) 185, c) 173, d) 365,[e]) none of these

"explanation:
[we]are ['][to] find the least number that leaves a remainder of 5 when divided by[]6, 9, 15, and 18.[This] means the number [s are]5 more than a common multiple of those numbers.

[step] 1: find the lcm of 6, 9, 15,[and]1[8].

prime factorizations[:]6[=] 2 × 3
[²] = 3²
[]5[=][][6] ×[]5
1[5][=] 2 ×[]3²

lcm = 2 × 3²[×] 5 = 90[]step 2:[ad]d the re[ma]inder 5 to the lcm[of the][re]quired number = 90 + [5] = 95

check:
95 ÷ 6 = 15 re[ma]inder 5
9[5] ÷[]9 = 10 remainder 5
95 ÷ 15 = 6[re]mainder 5
95 ÷ 18 =[]5 re[ma]inder 5

answer: none of the listed options match; cor[r]t [ans]wer is 95 → option e"[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Napol][is]'[nin][uzanan][süs] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[larda][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan [an]ziyaretçi sayıları,[bu][bu]mirasa olan [ın bir]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [,]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[E][ama]'[nın][uzanan][ülü] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sında][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[,] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[larda][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan [an]ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [de][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini []turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[E][ara]'[nın][eşsiz][süs] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara uygun][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Nem][ara]'[nın][muhteşem][kum] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara uygun][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Ayasof][fes]'[nın][eşsiz][ülü] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara uygun][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[ülkemizin][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkıda bulunmaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Nev][ara]'[nın][eşsiz][doğal] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[İz][ama]'[daki][eşsiz][termal] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sında][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][tarihi]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Nev][ara]'[in][devasa][süs] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sı][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[ıyla] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[halkın][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Gala][tepe]'[nın][eşsiz][ülü] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sında][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye[']nin zengin kültürel[mir]ası, UNESCO tarafından dünya çapında tanınmakta ve korunmaktadır[.] Kapadokya'[nın]eşsiz[kaya]oluşumları arasına gizlen[miş][yer]altı şehirleri,[binlerce]yıllık bir tarihe ev sahipliği yapar[.] H[ier]apolis-[Per][ama]'[nın][eşsiz][ülü] havuzları ise yüzyıllardır[insanları]büyül[emeye]devam eder[.] İstanbul['][un][tarihi]yarımada[sında][,][Bizans] ve Osmanlı medeniyetlerinin [izlerini]taşıyarak Ayasofya, Sultan Ahmet Cami[i ve]Top[kapı]Sarayı gibi yapılar[her yıl] milyonlarca ziyaretçiyi ağırlar. Göbek[lit]epe'nin keşfi de arkeoloji dünyasında çığır açmış ve tarihe bakış[ımızı]kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,] bu mirasın korunması adına sürekli çalışmalar yürütmekte;[restor]asyon[lar]uluslararası standart[lara][uygun olarak]gerçekleştirilerek eserlerin özgünlüğü titizlikle muhafaza edilmektedir. Artan []ziyaretçi sayıları,[bu][bu]mirasa olan [ilginin]göstergesi olmakta [,][turizm] gelirlerine [][katkı sağlamaktadır][.] Tüm bu unsurlar, Türkiye'nin kültürel zenginliğini [dünya]turizmi açısından güçlü bir cazibe merkezi haline getirmeye devam etmektedir.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][A] small bakery in [to the]land has g[one]viral after [-]customer shared photos of[f][he]at-[s]haped crois[ta][s]. The [Bak]ery, cal[led] 'W[or]ker &[Ro]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[O]w[er][J]asmine Kim[,] she nev[er]expected the pas[tor] to become a social media sen[sat]ion. The [at]ro[of][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [,][and][and][and][,][and] tail. Customers[are]lining up as e[ar]ly[] [1] a.m. to secure [-]batch. Online pre[-]orders are now book[ed for] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[or][y] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [ally] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[a][cel][for]t."[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [some]customer shared photos of[their][me]at-[s]haped crois[san][es]. The [Bak]ery, cal[led] 'W[or]ker &[Co]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[O]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [at]ro[of][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [,][s][ing][and][,][and] tail. Customers[are]lining up as e[ar]ly[as] [6] a.m. to secure [-]batch. Online pre[-]orders are now book[ed for] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re […] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][A] small bakery in [to the]land has g[one]viral after [some]customer shared photos of[their][go]at-[s]haped crois[san][es]. The [a bak]ery, cal[led] 'W[or]ker &[Co]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[T]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [at]ro[ad][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [-][s][c][ed][ed][and] tail. Customers[are]lining up as e[ar]ly[as] [6] a.m. to secure [-]batch. Online pre[-]orders are now book[ed for] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re […] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][ub]t."[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [some]customer shared photos of[their][go]at-[s]haped crois[san][s]. The [a bak]ery, cal[led] 'W[his]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[T]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[ast][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [-][s][a][ed][in][ed] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ory][,] and the bakery has since received[gu]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [,] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [some]customer shared photos of[their][go]at-[s]haped crois[san][s]. The [a bak]ery, cal[led] 'W[his]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[T]w[s][J]asmine Kim[,] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[ck][produc]ts are handma[de]each morning and[s]hap[ed with] c[hoc]olate [-][s][a][-][c][and] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed for] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [,] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [-]customer shared photos of[s][ro]at-[s]haped crois[san][ts]. The [a bak]ery, cal[led] 'W[or]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[T]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[y][produc]ts are handma[de]each morning and[s]hap[ed with] c[hoc]olate [-][f][c][-][,][and] tail. Customers[are]lining up as e[ar]ly[at] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ory][,] and the bakery has since received[gu]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [...] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [some]customer shared photos of[their][go]at-[s]haped crois[san][s]. The [bak]ery, cal[led] 'W[ic]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[O]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[ck][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [-][and][c][and][f][and] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[gu]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [...] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][A] small bakery in [g]land has g[one]viral after [some]customer shared photos of[s][go]at-[s]haped crois[san][s]. The [Bak]ery, cal[led] 'W[ic]ker &[Co]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[Her]w[ner][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[ot][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [-][f][-][-][c][and] tail. Customers[are]lining up as e[ar]ly[at] [8] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ud][y] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [ally] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][A] small bakery in [to the]land has g[one]viral after [some]customer shared photos of[s][c]at-[s]haped crois[san][ts]. The [a bak]ery, cal[led] 'W[ic]ker &[Do]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[O]w[ife][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [-]ro[y][produc]ts are handma[de]each morning and[s]hap[ed with] c[hoc]olate [-][s][c][-][f][and] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[gu]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re ['] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][A] small bakery in [to the]land has g[one]viral after [some]customer shared photos of[their][go]at-[s]haped crois[san][t]. The [bak]ery, cal[led] 'W[ic]ker &[Ro]ugh',[rep]orted[a][1]0[0]%[inc]rease in orders within 4[8] hour[s].[O]w[ner][J]asmine Kim[said] she nev[er]expected the pas[sing] to become a social media sen[sat]ion. The [']ro[ck][produc]ts are handma[de]each morning and[s]hap[ed] c[hoc]olate [-][c][c][and][on][and] tail. Customers[are]lining up as e[ar]ly[as] [9] a.m. to secure [-]batch. Online pre[-]orders are now book[ed] t[wo]weeks[in][ad]van[ce]. Local new[s][co]vered the st[ore][,] and the bakery has since received[inter]est from food blog[s in]Japan and Fran[ce]. Kim is[plan]ning to release a dog-shaped ver[sion]next[mon]th. "We’re [...] hav[ing] fun[,"] she says[.] "If it makes people smile, it’s worth[the][ef][for]t."[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[sokak]lardaki saat[çinin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten [ki]hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [,][her şeyi]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [y][bu]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi [-]anladı ki bu sıradan bir [-]ci [lası]değildi. Saat durmuş gibiydi, ama aslında ["]farklı bir zamanda tik[baş]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[-] kendi geçmişine ait [olan][kayıp] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıdır][.] Akşam[saat][']nı [çalış]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir ["]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[sokak]lardaki saat[çilerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][yaşamayı]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [y][bu]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[-]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[-] kendi geçmişine ait [olan][kayıp] anları. Müşteri gülümseyerek "[Eski]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[üstü][']nı [çalış]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [şeyin]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[muştu]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [][bu]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[-][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[tak]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[,] kendi geçmişine ait [o][o] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ı][.] Akşam[üstü][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir []başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][de]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [,][bu]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[tekrar]lıyordu. Saatçi eline aldığında,[içer]iden çocukluk anılarını gördü[,] kendi geçmişine ait [en][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ı][.] Akşam[saat][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [şeyin]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[muştu]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][yaşamayı]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [,][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[tak]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[,] kendi geçmişine ait [en][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ı][.] Akşam[üstü][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [gün]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[uyordu]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][daha iyi]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [ki][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci [i]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[tekrar]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[,] kendi geçmişine ait [en][unutulmaz] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıdır][.] Akşam[saat][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [günün]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][yaşamayı]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [,][bu]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[-]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[,] kendi geçmişine ait [en][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[,][dükkân]nı [kapan]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [hayatın]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[muştu]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [fısılda]dı. Bazıları geçmişten [gelen]hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][de]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [ki][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[,][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[-]lıyordu. Saatçi eline aldığında,[an]iden çocukluk anılarını gördü[,] kendi geçmişine ait [en][tüm] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[üstü][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [şeyin]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Şehrin []sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[sokak]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten []hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][de]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [,][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[.][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[-]lıyordu. Saatçi eline aldığında,[müşter]iden çocukluk anılarını gördü[-] kendi geçmişine ait [o][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[,][dükkân]nı [kapat]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [gün]başlangıcının müjdesiydi[.][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ında]yaşayan saatçi, zamanla tuhaf bir ilişki kur[du]. Her sabah dükkânını açarken,[duvar]lardaki saat[lerin]tik-takları ona farklı hikâyeler [sunar]dı. Bazıları geçmişten [gelen]hüzünlü melod[iler]di[,] bazıları ise geleceğin belirsizliğini fısıldayan endiş[eli][ses]lerdi.[Yıllar] geçtikçe,[saat]çi bu sesleri [][de]öğrenmişti. Müşter[iler]gelir, saatlerini tamir[ettir]irler[,] ama asla saatçinin içinde [ki][o]zamansız dünyayı fark etmezlerdi. Bir gün garip[bir]müşteri girdi dükkâna[-][elinde]kırık bir cep saati vardı[.] "[Bu]saati [tamir] edebilir misiniz[?"] diye sordu[,] ama saatçi []anladı ki bu sıradan bir [saat]ci ["]değildi. Saat durmuş gibiydi, ama aslında []farklı bir zamanda tik[-]lıyordu. Saatçi eline aldığında,[içer]iden çocukluk anılarını gördü[-] kendi geçmişine ait [en][sız] anları. Müşteri gülümseyerek "[Bu]saatler sadece zamanı göstermez[,] zamanı yaşatır["] dedi. Saat[çi]o gün anladı ki [,][bu]mekanik bir iş değil[,] aslında insanların kayıp an[larını]bulma sanat[ıydı][.] Akşam[saat][dükkân]nı [yaklaş]ırken, tüm saatlerin []çalmaya başladığını duydu -[bu], yeni bir [günün]başlangıcının müjdesiydi[.][SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][özellikle]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[İzmir][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Araştırmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [planlama][sivil toplum örgüt]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][alanların]kullanım düzey[leri ve][yeşil] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [cılıkta]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [önemli]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [tecrüb]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][kent] katılımının teşvik edilmesi ve []sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [gösterilmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [cılığın]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][dünyanın]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Araştırmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [planlama][örgüt]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][değişim] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [larda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [bu konuda]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [larda]yerel yönetimlerin [tecrüb]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve []sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [önerilmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [ların]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][dünyanın]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[İzmir][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [planlama][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][,][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [da]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [,]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][paydaş] katılımının teşvik edilmesi ve [ilgili]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [kabul edilmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [çalışmalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [aktiv][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][,][arazi]kullanım düzey[leri ve][kentsel dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [önemli]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [konusunda]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [vurgulanmıştır]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [larının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[İzmir][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Araştırmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [planlama][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [önemli]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [konusunda]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [belirlenmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[İzmir][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [aktiv][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [uygulamada]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [konusunda]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [değerlendirilmektedir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [aktiv][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][,][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [uygulamada]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [görülmektedir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [işim]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [-][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [da]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [uygulamada]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [önerilmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Araştırmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [planlama][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][dönüşüm] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [şehir] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [önemli]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve []sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [önerilmiştir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye'deki büyükşehirlerde sürdürülebilir kentsel planlama uygulamalarının mevcut durumu ve gelişim potansiyeli [,][bu çalışmanın]temel konusunu oluşturmaktadır. Son yirmi yılda [,][geliş]en [büyük]şehirlerinde, çevre dostu planlama yaklaşımlarının benimsenmesi kritik bir önem kazanmıştır.[Bu çalışma], İstanbul,[Ankara][,][İzmir] ve Bursa olmak üzere dört büyükşehrin kentsel planlama politikalarını karşılaştırmalı olarak analiz etmiştir.[Çalışmada]yöntem olarak karma yaklaşım benimsenmiş, hem nicel[hem de]nitel veriler [kullanılmıştır]. Belediye yetkilileri, şehir planlamaları [uzman]ları ve çevre [aktiv][profesyonel]leri ile derinlemesine görüşmeler yapılmıştır[.][Kentsel] yeşil alan [ların][,][yeşil][arazi]kullanım düzey[leri ve][yerel yönetim] programlarının etkinliği değerlendirilmiştir. Bulgular[,] İzmir'[in]sürdürülebilir planlama [konusunda]en başarılı [aday] olduğunu, İstanbul['][un]ise en büyük potansiyele sahip olmasına rağmen [uygulamada]zorluklar yaşadığını göstermiştir. Ankara ve Bursa'nın orta düzeyde performans sergilediği, ancak gelişim alanlarının bulunduğu tespit edilmiştir[.] Çalışma sonucunda[,] sürdürülebilir kentsel planlama [lar için]yerel yönetimlerin [kapasit]elerinin artırılması gerektiği önerilmiştir. Ayrıca[,][özel sektör] katılımının teşvik edilmesi ve [çok]sektörlü işbirliğinin geliştirilmesi kritik faktörler olarak [önerilmektedir]. Bu araştırmanın bulguları, Türkiye'deki [kentsel]planlama [uygulamalarının]yeniden değerlendirilmesi için önemli veriler sunmaktadır[.][Gelecek]araştırmalarda, küçük ve orta ölçekli şehirlerin de analiz kapsamına alınması önerilmektedir.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][Bu][analiz]inde,[tip]2 diyabet[hastalarında]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Gruplar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [(]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][top]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[ve L]c düzeyleri ve [Eg]zersiz[Kontrol] Ölçeği kullanılarak toplanmıştır. Uygulama [daki]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[ve C]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [katılım][tutumlarının]olumlu yönde değiştiği [görülmüştür]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][iyabet][model]inde,[tip]2 diyabet[hastalarında]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Gruplar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [,]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[Ac]c düzeyleri ve [Eg]zersiz[Kontrol] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[Ac]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][tutumlarının]olumlu yönde değiştiği [gözlemlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde []destekleyici unsur olduğunu göstermektedir.[Bu çalışma], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [larla]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][iyabet][il]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Kontrol] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][tutumlarının]olumlu yönde değiştiği [gözlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [getir]ileri[,] benzer hasta [larla]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][çalışmanın][özel]inde,[tip]2 diyabet[hastalarında]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Tutum] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][tutumlarının]olumlu yönde değiştiği [gözlemlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu çalışma], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [yapılmasını]içermektedir[.][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][çalışmanın][model]inde,[tip]2 diyabet[hastalarında]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [lük]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Tutum] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeyinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][larının]olumlu yönde değiştiği [gözlemlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu çalışma], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][çalışmanın][model]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Davranış] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][larının]olumlu yönde değiştiği [görülmüştür]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [yapılmasını]içermektedir[.][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][çalışmanın][spektif]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Davranış] Ölçeği kullanılarak toplanmıştır. Uygulama [dan sonra]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][larının]olumlu yönde değiştiği [görülmüştür]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][.][model]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Kontrol] Ölçeği kullanılarak toplanmıştır. Uygulama [daki]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][larının]olumlu yönde değiştiği [gözlenmiştir]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Bu sonuçlar], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [yapılmasını]içermektedir[.][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][çalışmanın][il]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubunda]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Kontrol] Ölçeği kullanılarak toplanmıştır. Uygulama [daki]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][larının]olumlu yönde değiştiği [görülmüştür]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Ayrıca], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][çalışmanın][model]inde,[tip]2 diyabet[li hastalarda]düzenli egzersizin glis[emik]kontrol üzerindeki etkisi incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi En[dok]rinoloji Pol[iklin]iği[']nde yürütül[müş ve]50 gönüllü hasta katılmıştır.[Katılımcılar]rastgele şekilde [egzersiz] ve kontrol grubu olarak ikiye ayrılmıştır. Egzersiz grubuna 12 hafta süresince [haftada]3 gün [)]egzersiz programı uygulanmıştır. Kontrol[grubuna]yalnızca [,][med]ikal tedavi devam ettirilmiştir[.] Veriler[,] HbA[1]c düzeyleri ve [Eg]zersiz[Tutum] Ölçeği kullanılarak toplanmıştır. Uygulama [lar ve]ölçümler[karşılaştır]ılmıştır.[Egzersiz] grubunda HbA[1]c[düzeylerinde]istatistiksel olarak anlamlı bir düşüş[göz]lenmiştir (p<0.[0][5]). Ayrıca, bu gruptaki bireylerin egzersize [olan][tutumlarının]olumlu yönde değiştiği [görülmüştür]. Çalışma[,] fiziksel aktivitenin diyabet yönetiminde [önemli bir]destekleyici unsur olduğunu göstermektedir.[Ayrıca], bireylerin yaşam kalitesini artıracak [sağlık]politikaları için yol gösterici olabilir. Araştırmanın [öner]ileri[,] benzer hasta [lar üzerinde]daha uzun süreli takip çalışmaları [da]içermektedir[.][SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [,][bölgeye]haftalarca doktor gelmemekte[,][diğer] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [art]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[tekn]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][e]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [,][hastaneye]haftalarca doktor gelmemekte[,][diğer] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[klin]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [büyük]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][e]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][hastaneye]haftalarca doktor gelmemekte[,][diğer] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][için]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Sayın]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[bölgelerde]ciddi sorun hâline gelmiştir. Pek çok [sağlık kuruluş][evine]haftalarca doktor gelmemekte[,][şehir] sağlık [kurum]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[klin]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [bazı]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][e]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [lar],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Osman]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][eye]haftalarca doktor gelmemekte[,][diğer] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [milletvekilleri],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Ali]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[bölgelerde]ciddi sorun hâline gelmiştir. Pek çok [ilç][a]haftalarca doktor gelmemekte[,][devlet] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[klin]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][e]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin [‘]12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [lar],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][evine]haftalarca doktor gelmemekte[,][şehir] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [lar],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Hüseyin]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][a]haftalarca doktor gelmemekte[,][şehir] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [,]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [lar],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][evine]haftalarca doktor gelmemekte[,][il] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [bir]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [hatırlat]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye Büyük Millet Meclisinin []12’[nci]Bir[leş]imini açıyorum[.] Toplantı yeter sayısı vardır, gündeme geçiyoruz. Sayın [lar],[gündeme]geçmeden önce gündem dışı [konu]lar için üç say[ın]milletvekiline söz ver[eceğim]. Gündem[dışı]ilk söz, Erzurum[’]da yaşanan sağlık hizmetleri yetersizliği hakkında söz isteyen Erzurum Milletvekili [Mustafa]Kaya’ya aittir.[Buyur]un Sayın Kaya[.] Sayın Başkan,[değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmetlerine erişim[,] özellikle kırsal[kesimde]ciddi sorun hâline gelmiştir. Pek çok [ilç][a]haftalarca doktor gelmemekte[,][şehir] sağlık [çı]ları ise personel yetersizliği nedeniyle çalış[amamaktadır]. Bu durum vatandaşlarımızın temel sağlık hakkına erişimini engellemektedir[.][Erzurum][Eğitim ve]Araştırma Hastanesi’nin kapasitesi her geçen gün [azal]makta, hastalar sevk [edil]mek zorunda kalmaktadır. Ayrıca [,] sayısının [artır]ılması ve yeni aile sağlığı merkez[lerinin]kurulması gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne özel[teşv]iklerle doktor[ları]yönlendirmesi büyük önem arz etmektedir. Sayın milletvekilleri; sağlık sadece [bir]şehirlerin değil, tüm yurttaşlarımızın hakk[ıdır]. Bu nedenle,[sağlık][hizmetlerine]kaynak ayrılırken bölgesel eşitsizlikler göz önünde bulundurulmalıdır. Erzurum halkının yaşadığı bu sorunların görmezden [gelin]memesi [gerektiğini]buradan bir kez daha [uyar]ıyorum[.] Hep[inizi]saygıyla selamlıyorum.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Build a simple Node[.]js server [.] Ex[press] that[man]ages a [to]-[d]o list. Inc[lu]de middleware for logging requests[,] route [ab]ling[,][s]ett[ing and][,][other]tasks,[and] a dummy[in]-memory database. Com[mand] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[ex][p] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[log][(]ex[press].j[son]());
app.[log]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[new] next();
}[;]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[{][{] id[:] 2[,][tas]k: 'Build[a]AP[I][',] complet[ed][:] fal[se][}]];

// GET all to-dos
app.[send]('/todos',[(]req[,][res]) => {
    res[.][j]son[(]todos);
[}]);

// POST a [-][o]-do
[main].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[}][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [;][][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[{]        comp[let]ed: false
    };
    todos.push[(][(]Tod[o]);
[//]res.status(201).json([']Todo[);]}[);]// Mark a [to]-do as completed[][app][.]patch('/[t]odos/[?]id[',][(]req[,][(][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===['']);
    if (!tod[o]) {
        return res.status([2][6]4).[j][son]({ er[ror][:] '[T]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[;]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[$][]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Build a simple Node[.]js server [.] Ex[press] that[man]ages a [']-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing and][up][ing]tasks,[and] a dummy[non]-memory database. Com[bat] the logic[dir][oper]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][q] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[open][(]ex[press].j[son]());
app.[post]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[{][{] id[:] 2[,][tas]k: 'Build[the]AP[I][',] complet[ed][:] fal[se][]];

// GET all to-dos
app.[get]('/todos',[(]req[,][res]) => {
    res[=][j]son[(]todos);
[}]);

// POST a [-][to]-do
[main].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [);][][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[return]res.status(201).json([/]Todo[);]}[);]// Mark a [To]-do as completed[][app][.]patch('/[t]odos/[?]id[',][(]req[,][(][)] => {
    [var] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([2][0]4).[j][son]({ er[ror][:] '[to]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[http][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Build a simple Node[.]js server [.] Ex[press] that[man]ages a [To]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing and][-][ing]tasks,[and] a dummy[in]-memory database. Com[mit] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][q] = express[(]);
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
[main].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [);][const][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][&]Tod[o]);
[]res.status(201).json([new]Todo[);]}[);]// Mark a [To]-do as completed[][app][.]patch('/[t]odos/[?]id[',][(]req[,][(][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([2][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[:][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Build a simple Node[.]js server [.] Ex[press] that[man]ages a [o]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ings][,][other]tasks,[and] a dummy[in]-memory database. Com[mand] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][q] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[open][(]ex[press].j[son]());
app.[post]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[}] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[{][{] id[:] 2[,][tas]k: 'Build[the]AP[I][',] complet[ed][:] fal[se][}]];

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
    [);][let][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][&]Tod[o]);
[]res.status(201).json([/]Todo[);]}[);]// Mark a [-]-do as completed[][app][.]patch('/[t]odos/[?]id[',][(]req[,][res][)] => {
    [var] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([2][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [}][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[your][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Build a simple Node[.]js server [using] Ex[press] that[man]ages a [uth]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing and][,][other]tasks,[and] a dummy[in]-memory database. Com[mit] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[ap][p] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[log][(]ex[press].j[son]());
app.[post]((req,[res],[n]ext) => {
[//][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[][{] id[:] 2[,][tas]k: 'Build[the]AP[I][',] complet[ed][:] fal[se][}]];

// GET all to-dos
app.[get]('/todos',[(]req[,][res]) => {
    res[.][j]son[(]todos);
[}]);

// POST a [-][to]-do
[es].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[//][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [;][let][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[]res.status(201).json([/]Todo[);]}[);]// Mark a [-]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [var] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[your][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Build a simple Node[.]js server [,] Ex[press] that[man]ages a [uth]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing the][for][ing]tasks,[and] a dummy[in]-memory database. Com[mand] the logic[dir][oper]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][q] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[log][(]ex[press].j[son]());
app.[run]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[}] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[{][{] id[:] 2[,][tas]k: 'Build[the]AP[I][',] complet[ed][:] fal[se][}]];

// GET all to-dos
app.[get]('/todos',[(]req[,][res]) => {
    res[.][j]son[(]todos);
[}]);

// POST a [/][to]-do
[main].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [);][let][t][od]o =[{]        id: t[odos][.][len]gth + [1],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[]res.status(201).json([/]Todo[);]}[);]// Mark a [uth]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [}][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[:][]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Build a simple Node[.]js server [,] Ex[press] that[man]ages a [']-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing the][for][ing]tasks,[and] a dummy[in]-memory database. Com[pat] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][p] = express[(]);
const port = 3000;

// Mid[d]leware [,] parse [J][S]ON and log requests
app.[load][(]ex[press].j[son]());
app.[post]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
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
    [;][let][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[]res.status(201).json([/]Todo[);]}[);]// Mark a [-]-do as completed[][app][.]patch('/[t]odos/[gu]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [retur][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[:][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Build a simple Node[.]js server [,] Ex[press] that[man]ages a [-]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing the][mult][ing]tasks,[and] a dummy[in]-memory database. Com[pat] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[ap][p] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[load][(]ex[press].j[son]());
app.[post]((req,[res],[n]ext) => {
[][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
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
    [);][][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[//]res.status(201).json([/]Todo[);]}[);]// Mark a [-]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[:][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Build a simple Node[.]js server [,] Ex[press] that[man]ages a [-]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[y][,][s]tasks,[and] a dummy[in]-memory database. Com[mit] the logic[dir][ect]ly for readability.

```javascript
const express = requ[ire][(']express');
const[re][p] = express[(]);
const port = 3000;

// Mid[d]leware [,] parse [J][S]ON and log requests
app.[load][(]ex[press].j[son]());
app.[run]((req,[res],[n]ext) => {
[//][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
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
[if][if][(]![t][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [);][let][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][/]Tod[o]);
[//]res.status(201).json([/]Todo[);]}[);]// Mark a [-]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [res][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[your][://]localhost:${port}`);
[}]);
```[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Build a simple Node[.]js server [,] Ex[press] that[man]ages a [To]-[d]o list. Inc[lu]de middleware for logging requests[,] route [hand]ling[,][s]ett[ing the][,][other]tasks,[and] a dummy[in]-memory database. Com[ply] the logic[dir][oper]ly for readability.

```javascript
const express = requ[ire][(']express');
const[ap][p] = express[(]);
const port = 3000;

// Mid[d]leware [:] parse [J][S]ON and log requests
app.[load][(]ex[press].j[son]());
app.[run]((req,[res],[n]ext) => {
[//][con]sole[.][log][(][`]${[re]q[.]met[hod]} ${req.[ur]l}`);
[//] next();
}[);]// In-memory to-do list
let todos[=] [
    { id:[]1[,][tas]k:['][L]earn No[de][.]j[s]', completed[:][fal]se[}],
[{][{] id[:] 2[,][tas]k: 'Build[U]AP[I][',] complet[ed][:] fal[se][}]];

// GET all to-dos
app.[get]('/todos',[(]req[,][res]) => {
    res[=][j]son[(]todos);
[}]);

// POST a [uth][to]-do
[main].post[('][/]t[odos]', ([re]q[,] res) => {
    const { task[}] = req.[b]ody;
[][if][(]![tas][k]) {
        return res.[stat]us(400).json[(][{] error: 'Task is requir[ed]' });
    }
    [);][][t][od]o =[{]        id: t[odos][.][len]gth + [id],
        task[,]        comp[let]ed: false
    };
    todos.push[(][a]Tod[o]);
[]res.status(201).json([a]Todo[);]}[);]// Mark a [To]-do as completed[][app][.]patch('/[t]odos/[a]id[',][(]req[,][res][)] => {
    [const] id = parse[In]t(req.params.id[);]    const[t]od[o] = todos[.]find[(]t => t[.]id ===[id]);
    if (!tod[o]) {
        return res.status([4][0]4).[j][son]({ er[ror][:] '[To]-[do] not f[ound]['][}]);
    }
    todo.[comp]leted = t[rue];
    [}][.][j]son[(][t]odo);
}[);]app.listen[(]port, () => {
    console.log[(]`[Ser]ver running at[:][://]localhost:${port}`);
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][f]ind the least[c][in]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[lass].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][5][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[inter]factoriz[ation]:
[][=] 2 × 3
9 =[]3²[]1[5] =[][9] × 5
1[5] = 2 × 3[²]

l[cm] = 2[] [3]² × 5 =[]90[][=] 2[=] add the re[ma]ind[er]5 to the lcm
required[l][cm] = [][9] + 5 = [][6]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][�] �[*] 9 = 10 remainder 5
95[]� 15 = 6 remainder 5
[][�][]� 18[=] 5 remainder 5

ans[wer]: none [-]listed op[tion][to]match; correct [ans]wer is 9[0] → option [2]"[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[lass].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[0][,] and 18[,] this means the number is 5 more than [$][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][6] × 5
1[8] = 2 × 3[²]

l[cm] = 2[] [3]² × 5 =[]90[][div] 2[:] add the re[ma]ind[er]5 to the lcm
required[l][s] = [][6] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][2] �[=] 9 = 10 remainder 5
95[+]� 15 = 6 remainder 5
[][1][=]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option []"[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[cm].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [e]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][6] × 5
1[8] = 2 × 3[²]

l[cm] = 2[] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[num][ue] = [][2] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][2] �[×] 9 = 10 remainder 5
95[²]� 15 = 6 remainder 5
[][1][5]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option []"[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[lass].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we ["]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the [l]cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][2] × 5
1[5] = 2 × 3[²]

l[cm] = 2[] [3]² × 5 =[]90[][�] 2[=] add the re[ma]ind[er]5 to the lcm
required[l][ue] = [][2] + 5 = [][6]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][2] �[×] 9 = 10 remainder 5
95[+]� 15 = 6 remainder 5
[][6][5]� 18[=] 5 remainder 5

ans[wer]: none [-]listed op[tion][s]match; correct [ans]wer is 9[0] → option []"[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][F]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[ell].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we ["]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][3] × 5
1[8] = 2 × 3[²]

l[cm] = 2[0] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[l][cm] = [][5] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][5] �[×] 9 = 10 remainder 5
95[+]� 15 = 6 remainder 5
[][1][5]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option [al]"[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[ell].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [two][,][]9,[]1[5][,] and 18[.] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[cm][=] 2 × 3
9 =[]3²[]1[5] =[][2] × 5
1[8] = 2 × 3[²]

l[cm] = 2[x] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[num][s] = [][2] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][6] �[×] 9 = 10 remainder 5
95[×]� 15 = 6 remainder 5
[][6][]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option []"[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[ell].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we ["]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[][=] 2 × 3
9 =[]3²[]1[5] =[][6] × 5
1[5] = 2 × 3[²]

l[cm] = 2[] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[c][s] = [][5] + 5 = [][6]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][5] �[-] 9 = 10 remainder 5
95[²]� 15 = 6 remainder 5
[][9][5]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option [:]"[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[m].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [6][,][]9,[]1[5][,] and 18[,] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[6][=] 2 × 3
9 =[]3²[]1[5] =[][6] × 5
1[5] = 2 × 3[²]

l[cm] = 2[x] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[num][ue] = [][5] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][5] �[+] 9 = 10 remainder 5
95[+]� 15 = 6 remainder 5
[][][5]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[5] → option [:]"[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[cm].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[.] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[cm][=] 2 × 3
9 =[]3²[]1[5] =[][3] × 5
1[5] = 2 × 3[²]

l[cm] = 2[x] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[l][cm] = [][5] + 5 = [][6]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][5] �[+] 9 = 10 remainder 5
95[=]� 15 = 6 remainder 5
[][6][=]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tion][s]match; correct [ans]wer is 9[0] → option []"[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][f]ind the least[num][ber]which when divided by 6[,] 9, 15, and 18[le]av[es] a remainder 5 in [to] c[ell].

a[)] 365, b) 185, c) 173,[d]) []65, e)[n]one of these

[]ex[plan]ation:
we [are]asked to find[the][le]ast[num][ber]that leaves[a]remaind[er][of] 5 when divided by [][,][]9,[]1[5][,] and 18[.] this means the number is 5 more than ["][com]mon multiple ["][of the]num[ber].

step[]1: find the []cm[of][6],[]9[,] 15, and 18.

pr[ime]factoriz[ation]:
[cm][=] 2 × 3
9 =[]3²[]1[5] =[][6] × 5
1[5] = 2 × 3[²]

l[cm] = 2[x] [3]² × 5 =[]90[][step] 2[:] add the re[ma]ind[er]5 to the lcm
required[l][cm] = [][2] + 5 = [][5]

check:
9[0] ÷ 6 = 15 remaind[er]5
[][6] �[+] 9 = 10 remainder 5
95[+]� 15 = 6 remainder 5
[][9][0]� 18[=] 5 remainder 5

ans[wer]: none []listed op[tions][s]match; correct [ans]wer is 9[5] → option [.]"[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [bulun]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][,]['][,][birleş]miş yeraltı şehirleri,[binlerce]yıllık ["]tarihe ["][dayanmaktadır]. Hierapolis[-]Pamukkale'nin []termal havuzları ise [,][tüm] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][,][yasof][Camii]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][tarihi]miras[ın]korunması adına sürekli [,][mekte]; restor[asyon][a ve]uluslararası [laştır][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [muhafaza]edilmektedir[.]["]müze [/][yap]ıları, hem bu mirasa olan [ca][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Bu][ESCO][,] Türkiye'nin [,][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][,][,][,][geçir]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][tüm] insanları büyülemeye [gelmiştir]. İstanbul[']un [tarihi][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][nin][yasof][esi]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][mekte]; restor[asyon][ve]uluslararası [laştır][ilkelerine]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [muhafaza]edilmektedir[.][Bu]müze [][sanatç]ıları, hem bu mirasa olan [ca][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Bu][ESCO][,] Türkiye'nin [][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [devam etmektedir][.][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][']['][,][birleş]miş yeraltı şehirleri,[binlerce]yıllık ["]tarihe [][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][tüm] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][,][yasof][esi]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [,][mekte]; restor[asyon][-]uluslararası [laştır][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Bu]müze [][kaz]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Bu][ESCO][,] Türkiye'nin [][zengin]liğini dünya turizmi ['][nde]caz[ibe]merkezi haline getirmeye [devam etmektedir][.][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][,]['][,][gizlen]miş yeraltı şehirleri,[binlerce]yıllık [“]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][,][yasof][esi]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [][mekte]; restor[asyon][çalışmaları]uluslararası [][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Bu]müze [][sanatç]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Bu][ımız][,] Türkiye'nin [][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,][']['][,][gizlen]miş yeraltı şehirleri,[binlerce]yıllık ["]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][Ayasof][yasof][Camii]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][mekte]; restor[asyon][,]uluslararası [standart][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Böylece]müze [][sanatç]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Bu][ESCO][,] Türkiye'nin [,][güzel]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,]['][']['][,][kalabil]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [tarihi][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][S][yasof][esi]gibi [,][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [çığ][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][mekte]; restor[asyon][,]uluslararası [standart][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Böylece]müze [][kaz]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Amac][ESCO][,] Türkiye'nin [,][zengin]liğini dünya turizmi [için][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][,]['][,][,][gizlen]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][tüm] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[,][İstanbul][yasof][ya]gibi [,][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [,][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][çalışmaktadır]; restor[asyon][lar]uluslararası [][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [restore]edilmektedir[.][Böylece]müze [][sanatç]ıları, hem bu mirasa olan [][duyarlı]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Amac][ESCO][,] Türkiye'nin [,][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,]['][']['][,][ebil]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][Sin][yasof][Camii]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [çığ][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][makta]; restor[asyon][çalışmaları]uluslararası [][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle [muhafaza]edilmektedir[.][Ülkemizin]müze [][sanatç]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Kültür ve Turizm][ESCO][,] Türkiye'nin [kültürel][zengin]liğini dünya turizmi [için][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][']['][,][,][ebil]miş yeraltı şehirleri,[binlerce]yıllık [bir]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][,][yasof][ya]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [yeni bir][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][çalışmaktadır]; restor[asyon][çalışmaları]uluslararası [][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle []edilmektedir[.][Yapılan]müze [][sanatç]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Kültür ve Turizm][ESCO][,] Türkiye'nin [,][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [...][.][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Türkiye'nin [][kültürel] mirası[,][UN]ESCO tarafından dünya çapında [tanın]makta ve korun[maktadır].[Kap]adokya['][nın][,][']['][,][,][ebil]miş yeraltı şehirleri,[binlerce]yıllık ["]tarihe ["][sahiptir]. Hierapolis[ile]Pamukkale'nin []termal havuzları ise [,][her yıl] insanları büyülemeye [gelmiştir]. İstanbul[']un [][yarı]madası,[Bizans] ve Osmanlı ['][nın]izlerini [(]Ayasofya[,] Sultan Ahmet Cami[i ve][,][yasof][Camii]gibi [)][her yıl] milyonlarca ziyaretç[iyi]ağırlar[.] Göbeklitepe['][nin]keşfi de arkeoloji dünyasında [yeni bir][ır] aç[mış ve]tarihe bakışımızı kökten değiştirmiştir. Kültür ve Turizm Bakanlığı[,][bu]miras[ın]korunması adına sürekli [çalışmalar][makta]; restor[asyon][da]uluslararası [][malara]uygun şekilde [,][tarihi]eserlerin özgünlüğü titizlikle []edilmektedir[.][Böylece]müze [][sanatç]ıları, hem bu mirasa olan [][destek]olmakta hem de turizm gelirlerine ciddi [katkıda bulunmaktadır].[Kültür ve Turizm][ESCO][,] Türkiye'nin [,][zengin]liğini dünya turizmi ['][nin]caz[ibe]merkezi haline getirmeye [][.][SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][A][s]mall bak[ery][,][]land[s][have]one viral af[ter][the]customer[s]hared photos of their[c]at[est][-][lat]ed[In][ro]issants[.] The bakery[is] cal[led] '[W][uc]ker & Dough',[con][mit]ted a [$][1][0]% increase in [stan]ders with[][1]8[0][day]s.[O]wner J[as]mine Kim said[the][bak]er ['][s] the ["]try[ing to] become a [oc]ial media sen[sat]ion.[The][ect]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ors] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [they] a.[m]. to secure a batch[.][The]pre-orders are [as] booked two weeks[in][ad]van[ce][.] Loc[al][']s co[ver][ate]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][ese][Fran]ce. Kim [has] plan[ned][to]r[un][ive]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[,]["][’][ing] makes people s[har][e], it’s worth the [af]fort."[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][The][s]mall bak[ery][,][]land[s][g]one viral af[ter][the]customer[s]hared photos of their[e]at[-][-][mok]ed[c][ro]issants[.] The bakery[,] cal[led] '[W][uc]ker & Dough',[rep][ac]ted a [][1][0]% increase in [stan]ders with[in][1]8[mon][our]s.[O]wner J[as]mine Kim said[the][bak]er ['][s] the [at]try[has] become a [oc]ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[,][The]pre-orders are [as] booked two weeks[in][ad]van[ce][.] Loc[al][new]s co[me][the]story, and the bak[er][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ece][ive]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[,]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][a][s]mall bak[ery][in][is]land[s][g]one viral af[ter][a]customer[s]hared photos of their[f]at[-][-][bas]ed[c][ro]issants[.] The bakery[,] cal[led] '[W][ic]ker & Dough',[rep][or]ted a [+][2][0]% increase in [or]ders with[in][1]8[mon][our]s.[O]wner J[as]mine Kim said[the][ev]er [s][s] the [at]try[has] become a [']ial media sen[sat]ion.[The][mic]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[.][The]pre-orders are [as] booked two weeks[in][ad]van[ce][.] Loc[ke][’]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ning][to]r[ele][ive]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[.]["][If][food] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][a][s]mall bak[ery][was][]land[has][g]one viral af[ter][a]customer[s]hared photos of their[me]at[-][-][bas]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][ic]ker & Dough',[rep][or]ted a [-][1][0]% increase in [stan]ders with[][1]8[mon][our]s.[O]wner J[as]mine Kim said[the][bak]er [s][was] the ["]try[has] become a [soc]ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [day] a.[m]. to secure a batch[,][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][’]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[,]["][T][hat] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][The][s]mall bak[ery][was][]land[was][g]one viral af[ter][a]customer[s]hared photos of their[c]at[-][-][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[W][uc]ker & Dough',[rep][or]ted a [][1][0]% increase in [or]ders with[][1]8[mon][our]s.[O]wner J[as]mine Kim said[the][bak]er [s][s] the ["]try['] become a [soc]ial media sen[sat]ion.[The][C]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [day] a.[m]. to secure a batch[,][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[ation][’]s co[me][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ele][ive]a dog-[s]haped version next[mon]th. "We[']re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][The][s]mall bak[ery][in][Is]land[has][g]one viral af[ter][a]customer[s]hared photos of their[c]at[-][s][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][ic]ker & Dough',[rep][or]ted a [.][2][0]% increase in [or]ders with[][1]8[0][our]s.[O]wner J[as]mine Kim said[the][bak]er [ies][is] the ["]try[ing to] become a [#]ial media sen[sat]ion.[The][rep]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [day] a.[m]. to secure a batch[of][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][’]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ning][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[']re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][The][s]mall bak[ery][in][Eng]land[has][g]one viral af[ter][a]customer[s]hared photos of their[f]at[-][s][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][ic]ker & Dough',[rep][or]ted a [.][2][0]% increase in [or]ders with[][1]8[mon][lar]s.[O]wner J[as]mine Kim said[the][bak]er [ve][was] the ["]try[to] become a [soc]ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[of][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][new]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[']re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][The][s]mall bak[ery][in][is]land[has][g]one viral af[ter][a]customer[s]hared photos of their[c]at[-][-][pir]ed[r][ro]issants[.] The bakery[,] cal[led] '[W][ic]ker & Dough',[rep][or]ted a [.][2][0]% increase in [stan]ders with[in][1]8[mon][th]s.[O]wner J[as]mine Kim said[the][bak]er [y][is] the ["]try[to] become a [mas]ial media sen[sat]ion.[The][C]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[.][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][’]s co[mes][ed the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][The][s]mall bak[ery][in][Eng]land[has][been]one viral af[ter][a]customer[s]hared photos of their[f]at[-][s][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][ic]ker & Dough',[rep][or]ted a [.][2][0]% increase in [stan]ders with[][1]8[h][our]s.[O]wner J[as]mine Kim said[the][bak]er [y][is] the ["]try[to] become a [Soc]ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[.][The]pre-orders are [,] booked two weeks[in][ad]van[ce][.] Loc[al][new]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ning][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[']re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][The][s]mall bak[ery][in][Eng]land[has][g]one viral af[ter][a]customer[s]hared photos of their[f]at[-][s][hap]ed[c][ro]issants[.] The bakery[,] cal[led] '[Ch][uc]ker & Dough',[rep][or]ted a [.][2][0]% increase in [or]ders with[in][1]8[h][our]s.[O]wner J[as]mine Kim said[the][bak]er [s][is] the ["]try[to] become a [Soc]ial media sen[sat]ion.[The][c]ro[is]sants[are]hand[ma]de each[mor]ning and[s]haped with choc[ola][te]do[ugh] for the ears and tail[.] Cust[om]ers[are]lining up[as] early as [of] a.[m]. to secure a batch[of][The]pre-orders are [as] booked two weeks[in][ad]van[ce][.] Loc[al][new]s co[mes][the]story, and the bak[ery][has] since r[eceiv]ed interest from food blogs in Jap[an][and][Fran]ce. Kim [has] plan[ned][to]r[ele][ase]a dog-[s]haped version next[mon]th. "We[’]re [ally] having fun[,"] she says[.]["][If][it] makes people s[mil][e], it’s worth the [ef]fort."[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Şehrin [-]sokağ[ın][geçen]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[on]lardaki ["][roman]tik-tak[tik][-]farklı ["][ları]anlatır[dı].[İç][lerinden]gelen hüz[ünlü] mel[od]iler[le],[bazıları]ise geleceğin [,][olduğunu]fısıldayan endişeli ["]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [denbire]girdi dükkân[a][,] elinde kırık bir [,] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][zorunda]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [anahtarı]aldığında[,] an[ılarını][,][an]ılarını gördü -[kendi]geçmişine [-]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [-]sadece mekan[keş]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][çi][saat][larını][yaklaş]ırken[,] tüm[saat]lerin aynı anda [laş]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Şehrin []sokağ[ının][birinde]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[sokak]lardaki ["][roman]tik-tak["][çok]farklı ["][zamanları]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin ["][larını]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [isi]girdi dükkân[a][,] elinde kırık bir [saat] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][zamanı]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [gözlerini]aldığında[,] an[iden][,][an]ılarını gördü -[kendi]geçmişine [gelen]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[a gir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][saat][saat][ını][yaklaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Şehrin []sokağ[ın][dolaşan]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[sokak]lardaki ["][roman]tik-tak["][-]farklı ["][sesleri]anlatır[dı].[Bir yan][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [-][larını]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [isi]girdi dükkân[a][,] elinde kırık bir [,] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][zamanı][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [saati]aldığında[,] an[ı][kalan][an]ılarını gördü -[kendi]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][,][saat][ini][yaklaş]ırken[,] tüm[ses]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ında][birinde]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[insan]lardaki ["][tak]tik-tak[tik][-]farklı ["][sesleri]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [iç][ini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [isi]girdi dükkân[a][,] elinde kırık bir [kol] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [yerini]aldığında[,] an[ıların][tüm][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][çi][saat][ini][yaklaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ında][birinde]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[sokak]lardaki [,][tak]tik-tak[tik][-]farklı ["][şeyleri]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [-][ini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [i]girdi dükkân[a][,] elinde kırık bir [,] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][zaman][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [yerini]aldığında[,] an[ılarının][tüm][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][çi][saat][ini][yaklaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ında][birinde]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[sokak]lardaki [,][tak]tik-tak[tik][-]farklı ["][şeyler]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [,][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][,][onlar] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [i]girdi dükkân[a][,] elinde kırık bir [duvar] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][çünkü]tamir[etmek][mümkün]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [eline]aldığında[,] an[ıların][tüm][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][kendine][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [ların]ıydı.[Saat][,][saat][ini][dolaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Şehrin []sokağ[ının][başındaki]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[duvar]lardaki [,][roman]tik-tak[tik][-]farklı ["][zamanları]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazen]ise geleceğin [,][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][ama][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [i]girdi dükkân[a][,] elinde kırık bir [,] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [saati]aldığında[,] an[ıların][tüm][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [ların]ıydı.[Saat][,][,][ini][dolaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Şehrin []sokağ[ının][birinde]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[duvar]lardaki [,][tak]tik-tak["][çok]farklı ["][ları]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [,][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][ama][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [isi]girdi dükkân[a][,] elinde kırık bir [saat] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [şaşır]dı [.][saati]tamir[etmek][zamanı]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [saati]aldığında[,] an[ıların][,][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [malar]ıydı.[Saat][,][,][ini][yaklaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Şehrin []sokağ[ının][başındaki]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[insan]lardaki [,][tak]tik-tak["][lerden]farklı ["][şeyler]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [,][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][ama][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [gün]girdi dükkân[a][,] elinde kırık bir [saat] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [çal]dı [.][Aslında]tamir[etmek][zorunda]değildi.[Saat][bir][saat] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [saati]aldığında[,] an[ıların][geçmişin][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [ların]ıydı.[Saat][saat][saat][ini][çalış]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Şehrin [bir]sokağ[ında][başındaki]saat[çi], zamanla[tuhaf] bir ilişki kurmuştu. Her sabah dükkânını aç[tığında],[duvar]lardaki ["][roman]tik-tak["][çok]farklı ["][şeyleri]anlatır[dı].[Biri][geçmişten]gelen hüz[ünlü] mel[od]iler[di],[bazıları]ise geleceğin [,][lerini]fısıldayan endişeli [ses]lerdi[.] Yıllar geç[tik][çe], saatçi bu sesleri ayırt etmeyi [öğren]mişti. Müşteriler gelir, saatlerini tamir ettirirler[di][ama][,] saatçinin içinde yaşadığı bu zamansız dünyayı fark etmez[lerdi].[Bir gün]garip bir [gün]girdi dükkân[a][,] elinde kırık bir [saat] saati vardı[.] "Bu saati tamir edebilir misiniz[?"] diye sordu[,] ama saatçi hemen [inan]dı [.][saati]tamir[etmek][mümkün]değildi.[Saat][bir][geçmiş] gibiydi,[ama]aslında çok farklı bir zamanda tiklak[ti].[Saat]çi [saati]aldığında[,] an[ıların][tüm][an]ılarını gördü -[zamanın]geçmişine [ait]unutulmuş anları.[Saat][çi][,]["]Bazı saatler sadece zamanı göstermez, zamanı yaşatır" dedi. Saatçi o gün anladı ki [,]sadece mekan[ik bir]iş değil,[aynı zamanda]insanların kayıp anlarını bulma [ların]ıydı.[Saat][çi][saat][ini][yaklaş]ırken[,] tüm[saat]lerin aynı anda [çal]maya başladığını duydu - bu, yeni bir zamanın başlangıcının müjdesiydi.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][Türkiye]'[de]büyükşehirlerde [,] kentsel [yönetim]uygulamalarının [,][ve]gelişim potansiyeli ["]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu ['][politikaların]benimsen[mesi]kritik bir [gerçektir].[Araştırma][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bütüncül bir]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[lerin][çevre][sorun]ları ve çevre [-][yerel yönetim][konularında]derinlemesine görüşmeler [sağlanmıştır].[Kentsel][eşil]alan oranları,[]taşıma [cılığın][büyüklük]leri ve ["][y]etkinliği ["][açısından][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[lerinden biridir][.] İstanbul['][un][,][bir]potansiyele sahip ol[sa da]uygulamada zorluklar [yarat][.][.] Ankar[a ve]Bursa['][da]orta düzeyde [,][olan],[kentsel][planlama]alanlarının [,][incelenmiştir][.][Araştırmanın]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [,][etkinliğinin]artırılması [,][][ların][artırılması], vatandaş katılımının teşvik [i ve]çok sektörlü işbirliğinin ["]kritik ["][]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[de]kentsel planlama politikalarının ["]değerlendirilmesi için ["][yeterli][niteliğindedir].[Ayrıca]araştırmalarda,[ilk]ve orta [-][öncelik]lerin de [,] kapsamına alınması [,][.][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][değişim ve]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [][politikaların]benimsen[mesi]kritik bir [hale gelmiştir].[Bu araştırma][,][İstanbul][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehrin]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bu]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [/][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kır][eşil]alan oranları,[toplu]taşıma [cılık][büyüklük]leri ve [/][y]etkinliği [,][bakımından][İstanbul], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[lerden biridir][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [bulun][İstanbul][,] Ankar[a ve]Bursa['][da]orta düzeyde [,][kentsel],[kentsel][planlama]alanlarının [,][][.][değerlendirilmesi]sonucunda[,][sürdürülebilir] kentsel [planlama]için yerel yönetimlerin [][etkinliğinin]artırılması [,][][güçlendir][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][yol gösterici][olacaktır].[Gelecek]araştırmalarda,[büyük]ve orta [daki][büyükşehir]lerin de [,] kapsamına alınması [önerilmektedir][.][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][değişim ve]gelişim potansiyeli []araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [,][politikaların]benimsen[mesi]kritik bir [dir].[Bu][,][,][,][Ankara][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][nitel]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [,][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kentsel][eşil]alan oranları,[toplu]taşıma [cılığının][büyüklük]leri ve [/][y]etkinliği [,][açısından][İstanbul], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[şehir][.] İstanbul['][un][ise][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][görülmüştür][.] Ankar[a ve]Bursa['][da]orta düzeyde [,][büyük],[sosyal ve][kentsel]alanlarının [,][incelenmiştir][.][Araştırmanın]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [][kapasitesinin]artırılması [,][yerel yönetim][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][][niteliğindedir].[Gelecek]araştırmalarda,[büyük]ve orta [doğu][büyükşehir]lerin de [,] kapsamına alınması [,][.][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [yönetim]uygulamalarının [,][değişim ve]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [,][politikaların]benimsen[mesi]kritik bir [önem taşımaktadır].[Bu][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bütüncül bir]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Metr][eşil]alan oranları,[toplu]taşıma [cılığının][büyüklük]leri ve [/][]etkinliği ["][açısından][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğunu][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][İzmir][.] Ankar[a ve]Bursa['][da]orta düzeyde [,][kentsel],[kültürel ve][kırsal]alanlarının [,][][.][incelenmesi]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [,][etkinliğinin]artırılması [,][yerel yönetim][bilincinin][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının ["]değerlendirilmesi için [,][yol gösterici][olacaktır].[Gelecek]araştırmalarda,[küçük]ve orta [doğu][büyükşehir]lerin de [,] kapsamına alınması [önerilmektedir][.][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [yönetim]uygulamalarının [,][değişim ve]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [,][politikaların]benimsen[mesi]kritik bir [önem taşımaktadır].[Bu çalışma][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bütüncül bir]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[plan][planlama][uzman]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Y][eşil]alan oranları,[toplu]taşıma [,][maliyet]leri ve [/][ulaşım]etkinliği [,][][ılmış], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][İzmir][.] Ankar[a ve]Bursa['][nın]orta düzeyde [,][kentsel],[sosyal ve][yerleşim]alanlarının [,][incelenmiştir][.][Çalışma]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [,][kapasitesinin]artırılması [,][kamu][elerin][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][önemli bir][olacaktır].[Gelecek]araştırmalarda,[küçük]ve orta [doğu][büyükşehir]lerin de [,] kapsamına alınması [,][.][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][değişim ve]gelişim potansiyeli [Bu]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [bir][politikaların]benimsen[mesi]kritik bir [hale gelmiştir].[Bu araştırma][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bütüncül bir]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[plan][planlama][uzman]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kentsel][eşil]alan oranları,[toplu]taşıma [,][büyüklük]leri ve ["][y]etkinliği ["][analiz][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[şehir][.] İstanbul['][un][ise][önemli bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][vurgulanmıştır][.] Ankar[a ve]Bursa['][nın]orta düzeyde [,][kentsel],[sosyal ve][kırsal]alanlarının [,][incelenmiştir][.][Araştırma]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [,][kapasitesinin]artırılması [,][kamu][bilincinin][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının [yeniden]değerlendirilmesi için [,][][olacaktır].[Gelecek]araştırmalarda,[büyük]ve orta [ölçekli][büyükşehir]lerin de [analiz] kapsamına alınması [önerilmektedir][.][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][ekonomik]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [][politikaların]benimsen[mesi]kritik bir [önem kazanmıştır].[Bu çalışma][,][İstanbul][,][Ankara][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][nitel]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kır][eşil]alan oranları,[]taşıma [,][büyüklük]leri ve [][ulaşım]etkinliği ["][karşılaştır][arak], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][,] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [barındır][İzmir][.] Ankar[a ve]Bursa['][nın]orta düzeyde [,][kentsel],[kentsel][yeşil]alanlarının [][incelenmiştir][.][Çalışma]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [][etkinliğinin]artırılması [,][katılım][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][önemli bir][olacaktır].[Gelecek]araştırmalarda,[küçük]ve orta [-][büyükşehir]lerin de [,] kapsamına alınması [][.][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [yönetim]uygulamalarının [,][gelecekteki]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [planlama][politikaların]benimsen[mesi]kritik bir [].[Bu çalışma][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][nitel]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [-][uzman][leri ile]derinlemesine görüşmeler [sağlanmıştır].[Kır][eşil]alan oranları,[]taşıma [,][potansiyel]leri ve ["][ulaşım]etkinliği ["][açısından][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [olduğu][İzmir][.] Ankar[a ve]Bursa['][da]orta düzeyde [,][kentsel],[çevre ve][gelişme]alanlarının [][değerlendirilmiştir][.][Araştırmanın]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [][kapasitesinin]artırılması [,][katılım][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][][olacaktır].[Gelecek]araştırmalarda,[küçük]ve orta [ölçekli][büyükşehir]lerin de [,] kapsamına alınması [,][.][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [gelişme]uygulamalarının [,][ve]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [bir][politikaların]benimsen[mesi]kritik bir [önem taşımaktadır].[Bu][,][,][,][Ankara][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][bütüncül bir]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [-][yönetic][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kentsel][eşil]alan oranları,[]taşıma [,][büyüklük]leri ve ["][ulaşım]etkinliği ["][açısından][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [barındır][İzmir][.] Ankar[a ve]Bursa['][nın]orta düzeyde [,][kentsel],[kentsel][kentsel]alanlarının [][incelenmiştir][.][Araştırmanın]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [,][kapasitesinin]artırılması [,][katılımcı][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][][olacaktır].[Gelecek]araştırmalarda,[büyük]ve orta [ölçekli][büyükşehir]lerin de [,] kapsamına alınması [önerilmektedir][.][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][Türkiye]'[deki]büyükşehirlerde [,] kentsel [planlama]uygulamalarının [,][gelecekteki]gelişim potansiyeli [,]araştırmanın temel konusunu oluşturmaktadır[.] Son yirmi [yılda]hızla büyüyen Türk şehirlerinde,[çevre]dostu [][yaklaşımın]benimsen[mesi]kritik bir [].[Bu][,][,][,][İstanbul][,] İzmir ve Bursa olmak üzere dört büyük[şehirde]kentsel planlama politikalarını karşılaştırmalı olarak [analiz] etmiştir. Araştırma [,][nitel]yaklaşım benimsen[miş], hem nicel hem de [nitel]veriler [kullanılmıştır][.] Belediye yetkilileri, şehir[planlama][planlama][uzman]ları ve çevre [-][uzman][ları ile]derinlemesine görüşmeler [sağlanmıştır].[Kent][eşil]alan oranları,[]taşıma [][büyüklük]leri ve ["][ulaşım]etkinliği ["][açısından][değerlendirildiğinde], İzmir['][in]sürdürülebilir planlama konusunda en başarılı metropol[olduğu][.] İstanbul['][un][,][bir]potansiyele sahip ol[masına rağmen]uygulamada zorluklar [barındır][İzmir][,] Ankar[a ve]Bursa['][nın]orta düzeyde [,][kentsel],[sosyal ve][etki]alanlarının [][incelenmiştir][.][Çalışma]sonucunda[,][sürdürülebilir] kentsel [gelişme]için yerel yönetimlerin [][etkinliğinin]artırılması [,][katılımcı][ların][artırılması], vatandaş katılımının teşvik [inin ve]çok sektörlü işbirliğinin ["]kritik ["][olduğu]değerlendirilmiştir. Bu araştırmanın bulguları,[Türkiye]'[deki]kentsel planlama politikalarının []değerlendirilmesi için [,][önemli][olacaktır].[Gelecek]araştırmalarda,[büyük]ve orta [-][büyükşehir]lerin de [,] kapsamına alınması [][.][SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [2] diyabet hastalarında [,][egzer]sizin glisemik [)][üzerine olan][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [][3] gönüllü hasta [lardan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu ["][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [da bir]haftada [,] gün [de bir][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[süre]devam ettirilmiştir.[Ver]iler[,][P][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Elde edilen veriler][grup][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [)][bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][Ancak][,][her iki]gruptaki bireylerin egzer[size][yönelik tutum][tutumlarının]olumlu yönde [olduğu]belirlenmiştir. Çalışma, fiziksel aktivitenin ["][sağlık][leyici ve]destekleyici ["][olduğunu göstermiştir][.] Bulgular,[bu][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [önermektedir].[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine olan][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][5] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [)][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [delik][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[İki][öncesi ve sonrası][veriler] karşılaştırılmıştır[.] Egzersiz grubunda [,][glis][1][c] düzeyinde [,][anlamlı]düşüş göz[lenmiş] (p<[0].[0][5][).][Sonuç olarak][,][her iki]gruptaki bireylerin egzer[size][yönelik tutum][tutumlarının]olumlu yönde [olduğu]belirlenmiştir. Çalışma, fiziksel aktivitenin ["][diyabet][ucu ve]destekleyici ["][olduğunu göstermiştir][.] Bulgular,[bireylerin][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [sağlayabilir].[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][üzerine etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [)][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [da bir]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[İki][öncesi ve sonrası][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [,][anlamlı]düşüş göz[lenmiş] (p<[0].[0][5][).][Ayrıca][).][her iki]gruptaki bireylerin egzer[sizin][uyum][tutumlarının]olumlu yönde [değiştiği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][sağlık][sistemini]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[toplumda][kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [sağlık]gruplarında daha uzun süreli takip [lerin]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [/][][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [)][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Kontrol][öncesi ve sonrası][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [,][anlamlı]düşüş göz[lenmiştir] (p<[0].[0][5][).][Sonuç olarak][,][her iki]gruptaki bireylerin egzer[sizin][motivasyon][larının]olumlu yönde [etkilediği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][sağlık][açısından]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[bireylerin][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [ler]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][etkileri]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [)][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Egzersiz] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[İki][öncesi ve sonrası][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [,][anlamlı]düşüş göz[lenmiştir] (p<[0].[0][5][).][Ayrıca][,][her iki]gruptaki bireylerin egzer[size][yönelik tutum][larının]olumlu yönde [arttığı]belirlenmiştir. Çalışma, fiziksel aktivitenin ["][sağlık][sağlığı]destekleyici ["][olduğunu göstermiştir][.] Bulgular,[bireylerin][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [ler]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [%][5] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu [)][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Egzersiz] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[İki][ve][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][1][1][c] düzeyinde [istatistiksel olarak][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][).][).][her iki]gruptaki bireylerin egzer[size][ilişkin][larının]olumlu yönde [arttığı]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][diyabet][sağlığı]destekleyici ["][olduğunu göstermiştir][.] Bulgular,[bireylerin][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [%][8] gönüllü hasta [lardan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu ["][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [de bir][egzersiz] programı uygulanmıştır.[Egzersiz] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[İki][iki][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [,][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][Sonuç olarak][,][her iki]gruptaki bireylerin egzer[size][yönelik tutum][larının]olumlu yönde [değiştiği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][diyabet][için]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[egzersiz][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [ler]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele ["][egzersiz] ve kontrol grubu ["][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [da bir]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Grup][grup][iki grup] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [,][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][).][).][her iki]gruptaki bireylerin egzer[size][yönelik][larının]olumlu yönde [geliştiği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][diyabet][sağlığını]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[bu][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [ler]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][insülin][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][5] gönüllü hasta [lardan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu ["][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [da bir]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Egzersiz] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Grup][öncesi ve sonrası][iki grup] karşılaştırılmıştır[.] Egzersiz grubunda [,][][1][c] düzeyinde [anlamlı][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][).][).][her iki]gruptaki bireylerin egzer[size][yönelik][larının]olumlu yönde [değiştiği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][diyabet][sağlığını]destekleyici [olduğunu][olduğunu göstermektedir][.] Bulgular,[egzersiz][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [içermektedir].[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Bu yüksek lisans tezinde, tip [II] diyabet hastalarında [,][egzer]sizin glisemik [-][üzerine][etkisi]incelenmiştir. Araştırma[,] Ankara Üniversitesi Tıp Fakültesi Endokrinoloji Pol[iklin]iği'nde yürütülmüş ve [1][0] gönüllü hasta [dan oluşmaktadır]. Katılımcılar rastgele [(][egzersiz] ve kontrol grubu ['][olarak]ayrılmıştır[.] Egzersiz[grubuna]1[2] hafta [/]haftada [,] gün [lük][egzersiz] programı uygulanmıştır.[Kontrol] grubuna yalnızca [,] medikal[tedavi]devam ettirilmiştir.[Ver]iler[,][Hb][-]1c düzeyleri ve [Eg]zersiz Tutum Ölçeği kullanılarak toplanmıştır.[Grup][öncesi ve sonrası][gruplar] karşılaştırılmıştır[.] Egzersiz grubunda [,][Hb][1][c] düzeyinde [istatistiksel olarak][anlamlı bir]düşüş göz[lenmiştir] (p<[0].[0][5][).][).][).][her iki]gruptaki bireylerin egzer[size][ilişkin][larının]olumlu yönde [değiştiği]belirlenmiştir. Çalışma, fiziksel aktivitenin [,][diyabet][sağlığını]destekleyici [olduğunu][olduğunu göstermiştir][.] Bulgular,[egzersiz][yaşam kalitesini]artıracak sağlık politikaları için yol gösterici olabilir[.] Araştırmanın önerileri, benzer [hasta]gruplarında daha uzun süreli takip [lerin]yapılmasını [içermektedir].[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [,][]2’[nci][grup][ma][ısını]açıyorum. Toplantı yeter sayısı [.][dolayısıyla] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][ilk]konuşma[mak üzere]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [ler],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [,] Milletvekili [,][Sayın][’][ya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[inin][yetersizliği],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[sağlık][hastan][ise]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Eğitim ve Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayısının]artır[ılması ve][,][,][sağlık][sağlık hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [,][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [,][,] tüm yurttaşlarımızın hakkıdır.[Bu nedenle],[kalit]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][.][.][olursa olsun]bu sorunların görmezden gelin[mesi][gerektiğini]buradan bir kez daha [uyar]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [,][]2’[nci][birleş][toplant][ısını]açıyorum. Toplantı yeter sayısı [.][dolayısıyla] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][ben]konuşma[cı]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetleri]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [,][Mehmet][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[inin][yetersizliği],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[sağlık][larımız][ları]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Şehir][une]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayısının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [değil][değil] tüm yurttaşlarımızın hakkıdır.[Ancak],[yör]ede kaynak [larımız][yaşanan]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][.][yaşanan]bu sorunların görmezden gelin[memesi][de]buradan bir kez daha [uyar]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [,][]2’[nci][olağan][toplant][ısını]açıyorum. Toplantı yeter sayısı [vardır][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][bazı]konuşma[cı]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [,][Sayın][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[inin][erişim],[özellikle]kırsal bölgelerde [önemli bir][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[sağlık][larımız][ları]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[yurttaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Şehir][Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [değil][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][yaşanan]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][.][yaşanan]bu sorunların görmezden gelin[memesi][bir kez daha]buradan bir kez daha [uyar]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][]2’[nci][birleş][birleş][unu]açıyorum. Toplantı yeter sayısı [vardır][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][gelecek]konuşma[larla ilgili]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [,][Sayın][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[inin][yetersizliği],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][uzman]doktor[yetiş]memekte, mevcut[sağlık][larımız][ları]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Devlet][Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [değil][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][,][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [uyar]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][]2’[nci][birleş][um][ısını]açıyorum. Toplantı yeter sayısı [vardır][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][ben]konuşma[larla ilgili]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [,][Sayın][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[i][erişim],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeni]doktor[yetiş]memekte, mevcut[doktor][larımız][da]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Eğitim ve Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][sağlık][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][mesi]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [,][dolayısıyla] tüm yurttaşlarımızın hakkıdır.[Ancak],[yör]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][.][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [,][6]2’[nci][Genel Kurul][toplant][ısını]açıyorum. Toplantı yeter sayısı [olmadığından][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][değerli]konuşma[lar için]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [Sayın][Kaya][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[lerindeki][yetersizliği],[özellikle]kırsal bölgelerde [bir][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[sağlık][larımız][ise]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Eğitim ve Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [sadece]büyük şehirlerin [değil][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][.][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][0]2’[nci][birleş][um][imini]açıyorum. Toplantı yeter sayısı [var][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][ilk]konuşma[lar için]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [,] Milletvekili [,][Kaya][’][ya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[lerine][erişim],[özellikle]kırsal bölgelerde [,][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[doktor][lar][lar da]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [gönder][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [,][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][,][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [,][]2’[nci][birleş][um][imini]açıyorum. Toplantı yeter sayısı [var][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][dışı]konuşma[lar için]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [Erzurum] Milletvekili [Sayın][Kaya][’][ya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[lerine][erişim],[özellikle]kırsal bölgelerde [bir][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[doktor][larımız][ise]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayısının]artır[ılması ve][,][,][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [gönder][mesi]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [sadece]büyük şehirlerin [değil][,] tüm yurttaşlarımızın hakkıdır.[Ancak],[yör]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ularak][,][,][.][,]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][]2’[nci][birleş][lant][imini]açıyorum. Toplantı yeter sayısı [vardır][dolayısıyla] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][ilk]konuşma[lar için]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [,] Milletvekili [,][Kaya][’][ya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[lerine][yetersizliği],[özellikle]kırsal bölgelerde [bir][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][yeterli]doktor[yetiş]memekte, mevcut[sağlık][larımız][ları]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[yurttaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Bölge][Eğitim ve Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayısının]artır[ılması ve][,][sağlık][ambulans][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [gönder][ması]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [,]büyük şehirlerin [değil][değil] tüm yurttaşlarımızın hakkıdır.[Ancak],[yör]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[ul][,][,][.][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [hatırlat]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS][Türkiye]Büyük Millet Meclisinin [1][]2’[nci][birleş][um][unu]açıyorum. Toplantı yeter sayısı [.][,] gündeme geçiyoruz. Sayın milletvekilleri, gündeme geçmeden önce [,][dışı]konuşma[mak üzere]üç say[ın]milletvekil[ine]söz vereceğim[.] Gündem dışı ilk [söz],[Erzurum]’da yaşanan [sağlık hizmetlerinin]yetersizliği hakkında söz isteyen [,] Milletvekili [,][Kaya][’][aya]aittir[.] Buyurun Sayın Kaya. Sayın Başkan[,][değerli milletvekilleri]; Erzurum ili ve ilçelerinde sağlık hizmet[lerine][erişim],[özellikle]kırsal bölgelerde [bir][sorun]hâline gelmiştir[.] Pek çok [köy]ümüzde [,][uzman]doktor[yetiş]memekte, mevcut[sağlık][larımız][ları]personel yetersizliği nedeniyle çalışamamaktadır[.] Bu durum[vatandaş]larımızın temel sağlık hakkına erişimini [engellemektedir]. Erzurum[Eğitim ve][Eğitim ve Araştırma]Hastanesi’nin kapasitesi [de]yetersiz kalmakta[,] hastalar sevk edilmek zorunda kalmaktadır[.][Bu nedenle]ambulans[sayılarının]artır[ılması ve][,][sağlık][sağlık][hizmet]lerinin [artırılması]gerekmektedir. Sağlık [Bakan]lığının, Doğu Anadolu Bölgesi[’]ne [,] teşviklerle doktorları [getir][mesi]büyük önem arz etmektedir[.] Sayın milletvekilleri; sağlık [sadece]büyük şehirlerin [,][değil] tüm yurttaşlarımızın hakkıdır.[Ancak],[bütç]ede kaynak [larımız][ve]bölgesel eşitsizlik[ler]göz önünde bulundur[arak][,][,][,][yaşanan]bu sorunların görmezden gelin[memesi][gerektiğini]buradan bir kez daha [uyar]ıyorum. Hep[inizi]saygıyla selamlıyorum.[SEP]
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]Build[L][ear][n]Node[.][j]s[f][ile]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[an]for[ward][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a []my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[t][s]');
const[ex][odos] = ex[p][(][);]const[id][=] [][4]00[);]//[H][imp]le[an][:][par]se [J][S]ON[=] log requests
[App].[load](ex[press][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[;]// In-memory[new][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][new] to[]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[;]// POST a new to[-][d][o][]['][t][(']/t[od][',][(][(][q][,] res) => {
    const { task[}][=] req[.]b[egin][}]    [if] (!task)[{]        return [res].status(400).[j][ush]({ er[ror][:][']Task [s] required'[}]);
    }
[,][] newTod[o] = {
[]id:[t]odos[)][][]] +[]1,
        task,
        completed[:] fal[se]
    };
   [tas][os].[p]ush(new[T]odo);
    res.[p][=][(]2[0][}][).]json(newTod[o]);
});

//[C][reate]a [ger]-[to][-][s][comp][creat]ed
app.[c][(][('][('][('][t][']:[']', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[bit] not found['] }[);]    }
[,] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[res].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[No][-][war]ning[:]['][]loc[ation][:][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]Build[L][ear][n]Node[.][j]s[f][s]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[an]for[mem][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[j][s]');
const[ex][odos] = ex[pres][(][);]const[id][=] [][4]00[);]//[S][imp]le[-][res][en]se [J][S]ON[and] log requests
[].[open](ex[port][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[new][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][new] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][ush]({ er[ror][:][']Task [s] required'[}]);
    }
[;][const] newTod[o] = {
[]id:[t]odos[.][id][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [res][res].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][0][).]json(newTod[o]);
});

//[Mak][et]a [in]-[d][-][s][re][requir]ed
app.[add][('][('][('][('][-][o]:[1]', ([re][q][,] res) => {
    const id[=][par]seIn[fo][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[do] not found['] }[);]    }
[;] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[app].[l]isten[(]port,[port][)] =>[{][]con[sole].log(`[Er][valid][war]ning[s][port][]loc[ated]['][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]Build[a][lear][n]Node[.][j]s[f][ile]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[an]for[bu][PI][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][press]');
const[ex][odos] = ex[ec][(][(]const[re][,] [][4]00[);]//[S][imp]le[']['][U]se [J][S]ON[for] log requests
['].[get](ex[press][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[new][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][.][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [_].status(400).[j][us]({ er[ror][:][']Task [s] required'[}]);
    }
[;][const] newTod[o] = {
[]id:[t]odos[.][][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [][res].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][}][).]json(newTod[o]);
});

//[G][et]a [']-[d][to][-][c][let]ed
app.[set][('][('][/][-][-][s]:[1]', ([re][q][,] res) => {
    const id[=][par]seIn[fo][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[app].[l]isten[(]port,[port][)] =>[{][]con[sole].log(`[No][R][run]ning[:][port][]loc[ated][:][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]Build[a][lear][n]Node[.][j]s[f][ackage]using Express that man[ages] a to-d[o]list[.] Include [s a][tab]le[an]for[ward][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][press]');
const[ex][odos] = ex[press][(][);]const[stat][us] [][4]00[);]//[Do][imp]le['][//][U]se [J][S]ON[for] log requests
[].[open](ex[press][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[to][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[ET][P] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][us]({ er[ror][:][']Task [:] required'[}]);
    }
[;][const] newTod[o] = {
[]id:[t]odos[.][id][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][odos].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][}][).]json(newTod[o]);
});

//[C][-]a [que]-[to][-][is][c][us]ed
app.[add][('][('][('][/][-][']:[']', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[App].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[No][R][un]ning[:][this][]loc[ated][host][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]Build[a][J][ava]Node[.][j]s[f][ile]using Express that man[ages] a to-d[o]list[.] Include [s][c]le[an]for[re][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a []my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][p] = requ[ire]('[ex][press]');
const[ex][p] = ex[press][(][);]const[re][=] [][4]00[);]//[H][imp]le[-][re][par]se [J][S]ON[for] log requests
[].[get](ex[press][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[to][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][son]({ er[ror][:][']Task [s] required'[}]);
    }
[;][const] newTod[o] = {
[]id:[t]odos[.][id][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][odos].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][0][).]json(newTod[o]);
});

//[U][-]a [ger]-[to][-][-][-][requir]ed
app.[add][('][('][('][-][-][de]:[1]', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[=][id]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[;] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[app].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[No][ror][un]ning[:][from][]loc[ation][:][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]Build[a][lear][n]Node[.][j]s[f][ule]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[ase]for[ward][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][ample]');
const[ex][p] = ex[p][(][(]const[port][=] [][4]00[);]//[H][imp]le[:][r][U]se [J][S]ON[for] log requests
[].[log](ex[pr][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[to][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][son]({ er[ror][:][']Task [ing] required'[}]);
    }
[,][const] newTod[o] = {
[]id:[t]odos[.][id][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][res].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][res][.]json(newTod[o]);
});

//[U][gr]a [que]-[to][-][-][re][requir]ed
app.[post][('][('][/][-][-][o]:[']', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[].[l]isten[(]port,[port][)] =>[{][]con[sole].log(`[Er][r][un]ning[:][port][]loc[ated][port][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]Build[a][la][ava]Node[.][j]s[f][ule]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[-]for[-][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][press]');
const[ex][p] = ex[port][(][);]const[re][=] [][4]00[;]//[S][imp]le[-][to][U]se [J][S]ON[for] log requests
[].[send](ex[ample][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[for][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][son]({ er[ror][:][']Task [s] required'[}]);
    }
[);][const] newTod[o] = {
[]id:[t]odos[.][id][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][odos].[p]ush(new[T]odo);
    res.[stat][us][(]2[);][res][).]json(newTod[o]);
});

//[U][et]a [ger]-[for][-][-][re][requir]ed
app.[post][('][('][/][-][-][de]:[']', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[param]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [retur][.]json[(][t][od]o[);]});

[].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[Er][are][un]ning[:][from][]loc[ation][port][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]Build[a][C][ava]Node[.][j]s[p][ackage]using Express that man[ages] a to-d[o]list[.] Include [s a][hand]le[an]for[-][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][press]');
const[ex][p] = ex[port][(][);]const[res][us] [][4]00[);]//[H][imp]le[-][r][U]se [J][S]ON[for] log requests
[].[get](ex[pr][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[to][-][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [_].status(400).[j][ect]({ er[ror][:][']Task [s] required'[}]);
    }
[,][const] newTod[o] = {
[]id:[t]odos[.][id][]] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][res].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][res][.]json(newTod[o]);
});

//[U][et]a [gram]-[for][-][is][re][requir]ed
app.[add][('][('][('][-][-][s]:[']', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[param]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[;] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[Er][ror][un]ning[:][port][]loc[ation][port][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]Build[a][app][n]Node[.][j]s[f][ule]using Express that man[ages] a to-d[o]list[.] Include [s a][c]le[ase]for[send][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][app] = requ[ire]('[ex][press]');
const[ex][q] = ex[port][(][);]const[re][=] [][4]00[;]//[Do][imp]le[:][r][U]se [J][S]ON[for] log requests
[].[get](ex[port][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[to][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[ET][all] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][app][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [$].status(400).[j][ch]({ er[ror][:][']Task [s] required'[}]);
    }
[;][const] newTod[o] = {
[]id:[t]odos[.][id][]] +[]1,
        task,
        completed[:] fal[se]
    };
   [t][odos].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][0][).]json(newTod[o]);
});

//[U][et]a [ger]-[d][-][is][re][requir]ed
app.[get][('][('][('][-][-][o]:[get]', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[param]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[=][id]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [res][.]json[(][t][od]o[);]});

[res].[l]isten[(]port,[res][)] =>[{][]con[sole].log(`[No][o][run]ning[:][from][]loc[ation][port][:][$]{port}`);
}[);][```][SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]Build[a][app][n]Node[.][j]s[f][ackage]using Express that man[ages] a to-d[o]list[.] Include [s a][tab]le[an]for[log][ing][re]quests, route handling for gett[ing and] posting tasks[,][and] a [.]my in-memory da[tab]ase[.] Comment the logic clearly[for] readability[.]```j[av][as]cript
[][const][App] = requ[ire]('[ex][press]');
const[ex][p] = ex[press][(][);]const[port][us] [][4]00[;]//[H][imp]le[-][res][U]se [J][S]ON[for] log requests
[].[get](ex[port][.]json());
app.use([(][re]q[,] res[,] next)[=>] {
    [con]sole[.][log](`${[re]q.method}[$]{req[.][ur]l[}]`);
    next();
}[);]// In-memory[new][t][od]o []
[const] todos[=] [
    { id:[]1, task:[']Learn No[de][.]js', completed[:] fal[se] },
    { id[:] 2, task: 'Build an API[',][comp][let][ed]: false[}][}][;][//] G[et][new] to[-]dos
[][.]get('/t[odos]', ([re]q[,] res) =>[{]    res[.][j]son([t]odos);
}[);]// POST a new to[-][dos][][][.][get][(']/t[odos][',][(][re][q][,] res) => {
    const { task[}][=] req[.]b[ody][;]    [if] (!task)[{]        return [res].status(400).[j][ch]({ er[ror][:][']Task [s] required'[}]);
    }
[);][] newTod[o] = {
[]id:[t]odos[.][][id] +[]1,
        task,
        completed[:] fal[se]
    };
   [n][res].[p]ush(new[T]odo);
    res.[stat][us][(]2[0][}][).]json(newTod[o]);
});

//[U][et]a [ger]-[to][-][-][comp][requir]ed
app.[load][('][('][('][/][-][dos]:[1]', ([re][q][,] res) => {
    const id[=][par]seIn[t][(]req.[j]s.[id]);
    const[t][od]o =[t]odos[.][f]ind([t] => t[.]id ==[][1]);
    if (![t][od]o) {
        return res.status(40[0]).j[son]({[er][ror][:] 'To-[dos] not found['] }[);]    }
[,] todo[.]completed = true;
    [}][.]json[(][t][od]o[);]});

[}].[l]isten[(]port,[(][)] =>[{][]con[sole].log(`[I][r][run]ning[for][port][]loc[al][port][:][$]{port}`);
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

#### Checkpoint: ep0-ba4000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][pro]vided[by] 6, 9,[][1]5, and 18[.][ad][has] a remaind[er]5 in [to] case[:]a) 365, b) 18[3][,][c]) 173,[d][)] 365[][][)] none [][w][rit]e

"explanation:
we ['][ne]ed to find[the][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [,] when [,][][3][,][]6,[][9],[]1[5], and []8. this means the [num]ber [s][is] more than a common [inc]iple [.][the]num[ber][is][is] 1[.] find the l[eft] of [6], [6], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[=][][][1]
[]5[] [9] × [][1]18[=][][=][=][]3²

lcm[=] 2[0][][6][=][][]5[=][]90

[+] 2: add the rema[ind]er [,] to the l[eft]
[of the][x]ed number[=][]90 +[][6] = 95

check[1]9[0] �[*] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [][][]5 ÷ 1[8] =[][5] remainder 5
95[]� []8 = 5[re]ma[ind][er]5

[][2]: n[one]of the [L]isted option[s]mat[ch];[cor]rect answer is [-]["] → option [2]"[SEP]
```

#### Checkpoint: ep0-ba8000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][pro]vided[by] 6, 9,[][1]5, and 18[,][ad][find] a remaind[er]5 in [to] case[(]a) 365, b) 18[0][,][c]) 173,[d][)] 365[,][e][)] none [][ans][hav]e

"explanation:
we ['][ne]ed to find[a][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [,] when [ever][][0][is][]6,[][9],[]1[0], and [1]8. this means the [num]ber [s][is] more than a common [mult]iple [.][the]num[ber][is][=] 1[:] find the l[eft] of [x], [9], 1[0][,][and][1]8.

pr[ime]factorizations:
6[×] 2 ×[]3
9[0][][][3]
[]5[] [9] × [][]18[=][][][][]3²

lcm[=] 2[0][][][0][][]5[=][]90

[=] 2: add the rema[ind]er [set] to the l[eft]
[of the][bin]ed number[:][]90 +[][6] = 95

check[:]9[0] �[+] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [][][]5 ÷ 1[8] =[][8] remainder 5
95[+]� [1]8 = 5[re]ma[ind][er]5

[][2]: n[one]of the [or]isted option[s]mat[ter];[cor]rect answer is [:][] → option []"[SEP]
```

#### Checkpoint: ep0-ba12000-rank0.pt

```
[CLS]F[ind] the [le]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[.][ad][find] a remaind[er]5 in [to] case[(]a) 365, b) 18[0][,][c]) 173,[d][)] 365[,][e][)] none [.][sol][rit]e

"explanation:
we ['][ne]ed to find[the][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [and] when [(][][)][,][]6,[][9],[]1[5], and [1]8. this means the [num]ber [s][is] more than a common [mult]iple [.][the]num[ber][is][=] 1[to] find the l[cm] of [x], [5], 1[8][,][and][1]8.

pr[ime]factorizations:
6[×] 2 ×[]3
9[0][][][]
[]5[] [9] × [][]18[=][][][][]3²

lcm[=] 2[0][][1][0][][]5[=][]90

[=] 2: add the rema[ind]er [set] to the l[eft]
[of the][enter]ed number[:][]90 +[][2] = 95

check[:]9[0] �[×] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [][][9]5 ÷ 1[8] =[][5] remainder 5
95[+]� [1]8 = 5[re]ma[ind][er]5

[][not]: n[one]of the [ex]isted option[s]mat[ch];[cor]rect answer is [:][] → option [.]"[SEP]
```

#### Checkpoint: ep0-ba16000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[.][F][find] a remaind[er]5 in [to] case[(]a) 365, b) 18[5][,][c]) 173,[d][)] 365[,][e][)] none [,][][hav]e

"explanation:
we ['][ne]ed to find[a][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][][)][,][]6,[][9],[]1[5], and [1]8. this means the [num]ber [s][is] more than a common [mult]iple [.][the]num[ber][is][is] 1[,] find the l[eft] of [x], [5], 1[,][,][and][1]8.

pr[ime]factorizations:
6[×] 2 ×[]3
9[0][][][]
[]5[] [5] × [][]18[=][][][1][]3²

lcm[=] 2[0][][1][0][][]5[=][]90

[/] 2: add the rema[ind]er [set] to the l[eft]
[of the][enter]ed number[=][]90 +[][2] = 95

check[]9[0] �[=] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [=][][9]5 ÷ 1[8] =[][8] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][not]: n[one]of the [ex]isted option[s]mat[ter];[cor]rect answer is [:][] → option []"[SEP]
```

#### Checkpoint: ep0-ba20000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[.][ad][d] a remaind[er]5 in [to] case[(]a) 365, b) 18[5][,][c]) 173,[d][)] 365[,][e][)] none [,][][hav]e

"explanation:
we ['][ne]ed to find[a][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][l][)][,][]6,[][9],[]1[5], and [1]8. this means the [num]ber [bel][is] more than a common [mult]iple [.][the]num[ber][is][is] 1[,] find the l[cm] of [6], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[×] 2 ×[]3
9[0][][][]
[]5[] [9] × [][]18[=][][][][]3²

lcm[=] 2[0][][1][=][][]5[=][]90

[+] 2: add the rema[ind]er [ess] to the l[eft]
[of the][requir]ed number[.][]90 +[][2] = 95

check[:]9[0] �[×] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [1][][9]5 ÷ 1[8] =[][5] remainder 5
95[+]� [1]8 = 5[re]ma[ind][er]5

[][not]: n[one]of the [ass]isted option[s]mat[ter];[cor]rect answer is [:][] → option [al]"[SEP]
```

#### Checkpoint: ep1-ba24000-rank0.pt

```
[CLS]F[ind] the [le]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[,][tak][ives] a remaind[er]5 in [to] case[(]a) 365, b) 18[0][,][c]) 173,[d][)] 365[,][e][)] none [][][plan]e

"explanation:
we [][ne]ed to find[the][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][t][)][is][]6,[][9],[]1[5], and [1]8. this means the [num]ber [is][is] more than a common [mult]iple [.][the]num[ber][2][is] 1[,] find the l[eft] of [6], [5], 1[5][,][and][1]8.

pr[ime]factorizations:
6[×] 2 ×[]3
9[0][][][]
[]5[] [9] × [][]18[=][][][1][]3²

lcm[=] 2[][][1][=][][]5[=][]90

[/] 2: add the rema[ind]er [set] to the l[eft]
[of the][iv]ed number[:][]90 +[][2] = 95

check[:]9[0] �[×] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [][][9]5 ÷ 1[8] =[][8] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][sum]: n[one]of the [ex]isted option[s]mat[ch];[cor]rect answer is [:][] → option []"[SEP]
```

#### Checkpoint: ep1-ba28000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[.][g][ind] a remaind[er]5 in [this] case[]a) 365, b) 18[5][,][c]) 173,[d][)] 365[,][e][)] none [][][her]e

"explanation:
we ['][ne]ed to find[a][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][it][)][,][]6,[][9],[]1[5], and []8. this means the [num]ber [bel][is] more than a common [mult]iple [.][the]num[ber][1][is] 1[,] find the l[eft] of [6], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[0][][][1]
[]5[] [9] × [][]18[=][][][1][]3²

lcm[=] 2[][][1][=][][]5[=][]90

[-] 2: add the rema[ind]er [*] to the l[eft]
[of the][enter]ed number[=][]90 +[][2] = 95

check[:]9[0] �[�] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [=][][9]5 ÷ 1[8] =[][8] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][box]: n[one]of the [ex]isted option[s]mat[ch];[cor]rect answer is [:][] → option [:]"[SEP]
```

#### Checkpoint: ep1-ba32000-rank0.pt

```
[CLS]F[ind] the [L]ast[num]ber which[is][di]vided[by] 6, 9,[][9]5, and 18[,][which][ind] a remaind[er]5 in [to] case[(]a) 365, b) 18[5][,][c]) 173,[d][)] 365[,][e][)] none [,][ex][her]e

"explanation:
we ['][ne]ed to find[the][le][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][it][,][,][]6,[][9],[]1[5], and [1]8. this means the [num]ber [�][is] more than a common [mult]iple [.][the]num[ber][is][is] 1[,] find the l[eft] of [6], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[5][][][1]
[6]5[] [9] × [][]18[=][][][1][]3²

lcm[=] 2[][][1][0][][]5[=][]90

[=] 2: add the rema[ind]er [1] to the l[eft]
[of the][iv]ed number[:][]90 +[][2] = 95

check[:]9[0] �[+] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [=][][9]5 ÷ 1[8] =[][5] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][e]: n[one]of the [ex]isted option[s]mat[ch];[cor]rect answer is [:][] → option [:]"[SEP]
```

#### Checkpoint: ep1-ba36000-rank0.pt

```
[CLS]F[ind] the [le]ast[num]ber which[is][di]vided[by] 6, 9,[][1]5, and 18[.][inclu][ind] a remaind[er]5 in [this] case[]a) 365, b) 18[5][,][c]) 173,[d][)] 365[][e][)] none [,][ex][gre]e

"explanation:
we ['][ne]ed to find[the][le][ast] num[ber]that[le]aves a re[ma]ind[er]of [5] when [ever][t][is][,][]6,[][9],[]1[5], and [1]8. this means the [num]ber [�][is] more than a common [mult]iple [.][the]num[ber][2][is] 1[:] find the l[cm] of [both], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[=][][][]
[]5[] [5] × [][]18[=][][2][=][]3²

lcm[=] 2[][][1][=][][]5[=][]90

[=] 2: add the rema[ind]er [set] to the l[eft]
[of the][iv]ed number[=][]90 +[][2] = 95

check[:]9[0] �[+] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [=][][9]5 ÷ 1[8] =[][8] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][test]: n[one]of the [ex]isted option[s]mat[ch];[cor]rect answer is [:][] → option [:]"[SEP]
```

#### Checkpoint: ep1-ba40000-rank0.pt

```
[CLS]F[ind] the [le]ast[num]ber which[is][di]vided[by] 6, 9,[][9]5, and 18[,][tak][has] a remaind[er]5 in [this] case[]a) 365, b) 18[5][,][c]) 173,[d][)] 365[,][e][)] none [][][gre]e

"explanation:
we ['][ne]ed to find[the][l][ast] num[ber]that[le]aves a re[ma]ind[er]of [,] when [ever][it][is][is][]6,[][9],[]1[5], and [1]8. this means the [num]ber [bel][no] more than a common [mult]iple [.][The]num[ber][is][is] 1[,] find the l[cm] of [6], [9], 1[5][,][and][1]8.

pr[ime]factorizations:
6[=] 2 ×[]3
9[5][][][]
[9]5[] [5] × [][]18[=][][][1][]3²

lcm[=] 2[][][3][=][][]5[=][]90

[+] 2: add the rema[ind]er [*] to the l[eft]
[of the][iv]ed number[.][]90 +[][2] = 95

check[:]9[0] �[+] 6 = 1[0] re[ma][ind]er 5[]95[�][�][]9 =[][1]0[re]ma[ind]er [][][9]5 ÷ 1[8] =[][5] remainder 5
95[+]� []8 = 5[re]ma[ind][er]5

[][e]: n[one]of the [l]isted option[s]mat[ch];[cor]rect answer is [:][one] → option [.]"[SEP]
```


</details>

