# Felhasználói útmutató

### Pálya készítés:
A pályát ajánlott fekete szigetelő szallaggal elkészíteni. Túl szűk fordulók létrehozását kerüljük. Ha a pálya nem ér körbe, akkor 
a két végén keresztbe húzott szallaggal jelezzük a pálya végét.
### Indítás:
Figyelem: Jelen típus vezetéken működik!
Tegyük a robotot egy biztonságos helyzetbe(fontos hogy a hátsó kerekek a levegőben legyen)\
Csatlakoztassuk a robotot egy monitorhoz, egérhez és billentyűzethez. Indítsuk el a Robot.py python file-t a Python IDLE fejlesztő 
környezetben és az F5 billentyű lenyomásával indítsuk el a programot.\
Ezek után óvatosan szüntessük meg a csatlakozást a monitor, egér,billentyűzet és a Raspberry Pi között. Helyezzük a robotot a pálya egyik
végére, hogy az érzékelők a keresztben elhelyezett szallag felett legyenek (ha nem körpálya). Ha szeretnénk menjen végig a pályán akkor 
óvatosan toljuk meg a kocsit hogy az érzékelők ne a keresztben elhelyezett szallag felett legyenek.

### Kikapcsolás:

A robot addig megy amíg olyan felületet "lát" ami visszaveri az infra sugarakat. Amikor szeretnénk kikapcsolni a robotot akkor vegyük fel
és helyezzük újra az indítás elötti biztonságos pozícióba. Ekkor csatlakoztassuk vissza óvatosan a billentyűzetet, egeret és monitort majd
majd control+C billentyű kombinációval megszakíthatjuk a programot.
