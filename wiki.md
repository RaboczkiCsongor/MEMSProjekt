# Fejlesztői dokumentáció
## Vonal követő robot
#### Raboczki Csongor (Neptun kód: HFJQX4)


## Tervezési fázis: 
Tervezési fázis első lépése az volt hogy, kiválasszam a small board computert ami az egészet irányitani fogja. 
A választásom egy Raspberry Pi 3 B modell-re esett. Nemes egyszerűség miatt, mert ezt tudtam leggyorsabban beszerezni. 
Alkatrészek melyek még szükségesek voltak a projekt elkészítéséhez az két motor, egy motor vezérlő modul, egy négy darab AA elem 
 sorban való összekötésére szolgáló tartó és kettő optikai érzékelő 
mely figyelni fogja a pályaként lehelyezett vonalat. Ezeket az alkatrészeket Kínából szereztem be Aliexpressen keresztül. Lehet venni erre 
létrehozott csomagokat(úgynevezett kiteket) de mivel számomra belőle csak pár alkatrészre volt szükség egyesével szereztem be őket.
Ebböl késöbb problémáim is akadtak, hiszen nem teljesen megbízható a nagy távú csomag szállítés ebböl kifolyólag el is veszett egy csomagom. A robot vázát elöször műanyagból képzeltem el, amelyet megtervezek és egy 3D nyomtató segítségével kinyomtatok végül vastag karton lapok összeragasztásánal maradtam az egyszerübb kezelhetőség miatt.

## Felmerülő problémák: 
 -Elveszett csomag problémája: Az egyik csomagom mely tartalmazta az elem tartót elveszett az úton Magyarország fele. Ez abból okozott problémát, hogy a motor vezérlő elektronika 12V segítségével műkodik tökéletesen. Raspberry Pi kimenetein a legnagyobb feszültség 5V. De a modul képes működni csak 5V segítségével is. Így ez a probléma elhárult.
 
 -Váz problémája: Nem várt szállítási időtartamok miatt (átlagosan 2 hónap volt) megnehezítette a végleges váz megtervezését. Ennek megoldására erős karton lapokból építettem meg a kocsi alvázát és a tetejére ragasztottam falakat melyek a helyükön tartják az ott elhelyezett modulokat.
 


## Áramköri rajzok, felhasznált elemek:


## Hardver specifikációk:


## Szoftver specifikációk:


## Rendszerkövetelmények:


## Fejlesztett kódok részletezése:


## Képek a kész projektről:
